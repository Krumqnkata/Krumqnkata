# Profile visuals

The README uses repository-owned visual assets, public repository statistics
and a contribution-calendar animation. Its project summaries also include
selected projects with private source code.

## Static artwork

`assets/header.svg` is the profile banner. The small technology badges in
`assets/` share the same navy background, type and colour accents.
The Java, PHP, Django, PostgreSQL and MySQL badges appear in the toolkit;
Arduino appears with the hardware interests.

These SVGs contain their own shapes and text, with accessible labels.
They do not depend on external images, web fonts or an image-generation service.
Edit them directly when changing the profile's wording or toolkit.

## Blog architecture diagram

`assets/pgknma-blog-architecture.svg` is a simplified application view of
PGKNMA Blog: React and TypeScript communicate with Django REST Framework,
which accesses production MySQL data through the Django ORM. Django Unfold
administration is part of the same backend. Local development may use SQLite.

The diagram summarises the frontend and backend architecture documentation.
It omits media storage, external integrations and detailed hosting routes.

## Automatic refresh

[Refresh profile visuals](https://github.com/Krumqnkata/Krumqnkata/actions/workflows/profile-visuals.yml)
runs daily, when its generator changes, or through **Run workflow**. It uses
the built-in GitHub Actions token; no personal access token is needed.

The workflow updates only `assets/generated/`. A failed API request keeps
the previously committed images available. Generated-image commits do not
trigger this workflow again.

## What the cards count

- **Public repositories:** public repositories owned by this account, including forks.
- **Original repositories:** those public repositories that are not forks.
- **Primary languages:** distinct primary languages across original public repositories.
- **Repository stars:** stars on the account's public repositories.
- **Language mix:** repository counts by primary language, excluding forks and repositories without a primary language. This is not code-byte share.

The script explicitly excludes private repositories and repositories owned
by other accounts. The snake uses GitHub's contribution calendar as published
by GitHub; repository names and details are not included in the animation.

## Local use

Python 3 with its standard library is sufficient:

```bash
python3 scripts/generate_profile.py --owner Krumqnkata
```

Set `GH_TOKEN` if authenticated API access is needed. For an offline snapshot:

```bash
python3 scripts/generate_profile.py --input public-repositories.json
```

## Animation

Generated with [Platane/snk](https://github.com/Platane/snk), pinned to a commit.
Light and dark variants are selected through a README `picture` element.
