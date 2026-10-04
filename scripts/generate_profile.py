#!/usr/bin/env python3
"""Generate profile SVG cards from public, user-owned repositories."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

PALETTE = {
    "Python": "#edc789", "TypeScript": "#6aa9ff", "JavaScript": "#f6d66f",
    "Java": "#ef9aa6", "PHP": "#b4a6ef", "HTML": "#f2a98d",
    "CSS": "#8fb9ed", "Other": "#8fa7c4",
}
FONT = "Arial, Helvetica, sans-serif"

def request_json(url: str, token: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-profile-visuals",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers=headers), timeout=20) as response:
                return json.load(response)
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError("GitHub API request failed: HTTP " + str(error.code)) from None
        except (URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError("GitHub API request timed out or could not connect") from None
        time.sleep(2 ** attempt)
    raise RuntimeError("GitHub API request failed")

def fetch_repositories(owner: str, token: str) -> list[dict]:
    repositories = []
    page = 1
    while True:
        query = urlencode({"type": "owner", "sort": "full_name", "per_page": 100, "page": page})
        batch = request_json("https://api.github.com/users/" + quote(owner, safe="") + "/repos?" + query, token)
        if not isinstance(batch, list):
            raise RuntimeError("GitHub returned an unexpected repository response")
        repositories.extend(batch)
        if len(batch) < 100:
            return repositories
        page += 1

def summarize(repositories: list[dict], owner: str) -> dict:
    # Fail closed: never include a private repository or one owned by another account.
    public = [
        repository for repository in repositories
        if repository.get("private") is False
        and repository.get("owner", {}).get("login", "").casefold() == owner.casefold()
    ]
    original = [repository for repository in public if repository.get("fork") is False]
    languages = Counter(
        repository["language"] for repository in original if repository.get("language")
    )
    return {
        "owner": owner,
        "public_repositories": len(public),
        "original_repositories": len(original),
        "stars": sum(int(repository.get("stargazers_count", 0)) for repository in public),
        "languages": dict(sorted(languages.items(), key=lambda pair: (-pair[1], pair[0]))),
        "updated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }

def frame(title: str, description: str, content: str) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="480" height="270" viewBox="0 0 480 270" role="img" aria-labelledby="title desc">'
        '<title id="title">' + escape(title) + '</title><desc id="desc">' + escape(description) + '</desc>'
        '<rect x="1" y="1" width="478" height="268" rx="16" fill="#101c2e" stroke="#30445e"/>'
        '<rect x="24" y="24" width="24" height="3" rx="1.5" fill="#63e6dc"/>'
        '<g font-family="' + FONT + '">' + content + '</g></svg>\n'
    )

def text(x: int, y: int, value: object, size: int = 14, color: str = "#a5b8d1", weight: str = "400") -> str:
    return '<text x="' + str(x) + '" y="' + str(y) + '" fill="' + color + '" font-size="' + str(size) + '" font-weight="' + weight + '">' + escape(str(value)) + '</text>'

def summary_svg(snapshot: dict) -> str:
    content = text(24, 58, "PUBLIC PROJECTS", 18, "#f3f7ff", "700")
    metrics = [
        (24, 102, snapshot["public_repositories"], "Public repositories", "#63e6dc"),
        (253, 102, snapshot["original_repositories"], "Original repositories", "#6aa9ff"),
        (24, 179, len(snapshot["languages"]), "Primary languages", "#edc789"),
        (253, 179, snapshot["stars"], "Repository stars", "#ef9aa6"),
    ]
    for x, y, value, label, color in metrics:
        content += text(x, y + 20, value, 37, color, "700")
        content += text(x, y + 43, label, 14)
    content += '<path d="M24 235H456" stroke="#30445e"/>'
    content += text(24, 255, "Updated " + snapshot["updated_utc"], 11)
    description = (
        str(snapshot["public_repositories"]) + " public repositories, "
        + str(snapshot["original_repositories"]) + " original repositories, "
        + str(len(snapshot["languages"])) + " primary languages and "
        + str(snapshot["stars"]) + " repository stars. Updated " + snapshot["updated_utc"]
    )
    return frame("Krumqnkata public GitHub projects", description, content)

def languages_svg(snapshot: dict) -> str:
    languages = list(snapshot["languages"].items())
    visible = languages[:5]
    if len(languages) > 5:
        visible = languages[:4] + [("Other", sum(count for _, count in languages[4:]))]
    total = sum(snapshot["languages"].values())
    content = text(24, 58, "LANGUAGE MIX", 18, "#f3f7ff", "700")
    content += text(24, 80, "Primary language · original public repositories", 12)
    for index, (language, count) in enumerate(visible):
        y = 111 + index * 24
        color = PALETTE.get(language, "#8fa7c4")
        width = round(240 * count / total) if total else 0
        content += text(24, y + 4, language, 13, "#e4edf9")
        content += '<rect x="143" y="' + str(y - 8) + '" width="240" height="10" rx="5" fill="#213249"/>'
        if width:
            content += '<rect x="143" y="' + str(y - 8) + '" width="' + str(width) + '" height="10" rx="5" fill="' + color + '"/>'
        content += text(399, y + 4, str(count) + " repos", 12)
    if not visible:
        content += text(24, 139, "No primary-language data yet.", 15)
    content += '<path d="M24 235H456" stroke="#30445e"/>'
    content += text(24, 255, "Based on repository counts · excludes forks", 11)
    description = ", ".join(language + ": " + str(count) + " repositories" for language, count in languages)
    return frame("Primary languages in original public repositories", description or "No language data", content)

def write_assets(snapshot: dict, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    files = {
        "summary.svg": summary_svg(snapshot),
        "languages.svg": languages_svg(snapshot),
        "snapshot.json": json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n",
    }
    # Fetch all data and build both SVGs before touching the previous images.
    with tempfile.TemporaryDirectory(dir=output) as staging:
        stage = Path(staging)
        for name, content in files.items():
            (stage / name).write_text(content, encoding="utf-8")
        for name in files:
            (stage / name).replace(output / name)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default=os.environ.get("PROFILE_OWNER", "Krumqnkata"))
    parser.add_argument("--input", type=Path, help="Optional repository JSON for an offline generation")
    parser.add_argument("--output", type=Path, default=Path("assets/generated"))
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", args.owner):
        parser.error("Invalid GitHub owner")
    if args.input:
        repositories = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(repositories, list):
            parser.error("Repository input must be a JSON array")
    else:
        repositories = fetch_repositories(args.owner, os.environ.get("GH_TOKEN", ""))
    snapshot = summarize(repositories, args.owner)
    write_assets(snapshot, args.output)
    print("Generated public profile cards for", args.owner)

if __name__ == "__main__":
    main()
