<!-- Visual assets live in this repository. Public statistics and the snake refresh through GitHub Actions. -->

<p align="center">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/header.svg" alt="Krum — student developer from Stara Zagora, Bulgaria. Python, Java, web and Linux. Code for the everyday." width="100%">
</p>

<p align="center">
  <a href="#about-me">About me</a> &nbsp; / &nbsp;
  <a href="#selected-projects">Projects</a> &nbsp; / &nbsp;
  <a href="#my-toolkit">Toolkit</a> &nbsp; / &nbsp;
  <a href="#beyond-the-code">Beyond the code</a> &nbsp; / &nbsp;
  <a href="#github-activity">Activity</a> &nbsp; / &nbsp;
  <a href="#на-български">На български</a>
</p>

## About me

Hi, I'm **Krum — Krumqnkata**, a student developer from **Stara Zagora, Bulgaria**, studying at **PGKNMA “Prof. Minko Balkanski”**.

I work with **Python, Java, web technologies and Linux**. I build school platforms, desktop tools and practical services, taking projects from the interface and API through to deployment and maintenance.

> I like software that earns its place in someone's everyday life.

## Selected projects

Projects with private source code are included through descriptions of my work and public website links.

<table>
<tr>
<td colspan="2" valign="top">
<h3><a href="https://pgknma.space">PGKNMA Blog — School Digital Platform</a></h3>
<p>A school platform for articles, events, polls, profiles and notifications, with a React frontend, Django REST API and administration tools.</p>
<p><b>My contribution:</b> frontend, backend API, deployment and maintenance.</p>
<p><sub><b>React · TypeScript · Vite · Django REST Framework · MySQL</b></sub></p>
<p><b><a href="https://pgknma.space">Website</a> · Private source</b></p>
<p><a href="https://pgknma.space"><img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/pgknma-blog-homepage.png" alt="Screenshot of the PGKNMA Blog homepage, showing the navigation, school introduction and school photograph" width="100%"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://logopedkrumova.com">Daniela Krumova — Professional Website</a></h3>
<p>A Bulgarian and English website for a speech therapy practice, with a responsive layout, service information and search-engine metadata.</p>
<p><b>My contribution:</b> frontend, bilingual layouts and website presentation.</p>
<p><sub><b>HTML · CSS · JavaScript · Responsive design · SEO</b></sub></p>
<p><b><a href="https://logopedkrumova.com">Website</a> · <a href="https://logopedkrumova.com/en/">English version</a> · Private source</b></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Krumqnkata/stara-zagora-transit">Stara Zagora Transit</a></h3>
<p>An interactive city transport map with routes, stops, timetables and journey planning. Displays real GPS vehicle positions when the data feed is available.</p>
<p><sub><b>JavaScript · Python · GTFS · OpenStreetMap</b></sub></p>
<p><b><a href="https://github.com/Krumqnkata/stara-zagora-transit">Code</a> · <a href="https://github.com/Krumqnkata/stara-zagora-transit/blob/main/README.md">Guide &amp; data sources</a></b></p>
</td>
</tr>
</table>

<details>
<summary><b>Behind PGKNMA Blog — technical overview</b></summary>

<br>

The platform combines a separate **React frontend** and **Django backend**, with **MySQL for production data**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/pgknma-blog-architecture.svg" alt="Simplified architecture: React and TypeScript exchange JSON with Django REST Framework; Django accesses MySQL through its ORM and includes a Django Unfold administration panel." width="100%">
</p>

- **Interface:** React, TypeScript and Vite power the pages; TanStack Query fetches and caches server data.
- **API &amp; administration:** Django REST Framework validates requests and applies permissions. Django Unfold provides the content administration interface within the backend.
- **Data &amp; deployment:** MySQL stores production records, with SQLite available for local development. The React build and Django service are deployed with Linux and Apache.

**One request in practice:** when the news page needs fresh data, the frontend requests posts from the API. Django queries the database and returns JSON, which React uses to render the page.

**My contribution:** frontend and API development, connecting the data flow, deployment and ongoing maintenance. The source lives in separate private repositories.

[Visit PGKNMA Blog →](https://pgknma.space)

</details>

<details>
<summary><b>More projects — desktop, audio &amp; school tools</b></summary>

<br>

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Krumqnkata/python-raw-processor">RAW Studio</a></h3>
<p>A desktop RAW photo editor with automatic corrections, previews, individual edits and batch JPG/PNG export.</p>
<p><sub><b>Python · CustomTkinter · rawpy · OpenCV</b></sub></p>
<p><b><a href="https://github.com/Krumqnkata/python-raw-processor">Code</a> · <a href="https://github.com/Krumqnkata/python-raw-processor/blob/main/README.md">Guide</a> · <a href="https://github.com/Krumqnkata/python-raw-processor/actions/workflows/windows-package.yml">Windows builds</a></b></p>
<p><a href="https://github.com/Krumqnkata/python-raw-processor/actions/workflows/tests.yml"><img src="https://github.com/Krumqnkata/python-raw-processor/actions/workflows/tests.yml/badge.svg?branch=main" alt="RAW Studio Python checks"></a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Krumqnkata/bell-song-cutter">School Bell Cutter</a></h3>
<p>An audio tool that analyses songs, suggests suitable excerpts and lets the user preview, adjust and export clips for school bells.</p>
<p><sub><b>Python · librosa · FFmpeg · Audio processing</b></sub></p>
<p><b><a href="https://github.com/Krumqnkata/bell-song-cutter">Code</a> · <a href="https://github.com/Krumqnkata/bell-song-cutter/blob/main/README.md">Guide</a></b></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION">School AI</a></h3>
<p>A school information platform with QR badges, kiosk and display PWAs, an assistant and an administration panel for content and devices.</p>
<p><sub><b>Python · FastAPI · PostgreSQL · WebSocket · PWA</b></sub></p>
<p><b><a href="https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION">Code</a> · <a href="https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION/blob/main/ADMIN_GUIDE.md">Admin guide</a> · <a href="https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION/blob/main/docs/KIOSK_PWA.md">Kiosk &amp; screens</a></b></p>
<p><a href="https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION/actions/workflows/ci.yml"><img src="https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION/actions/workflows/ci.yml/badge.svg?branch=main" alt="School AI CI status"></a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Krumqnkata/Discord-Bot-Notifier">IT Club Discord Bot</a></h3>
<p>A bot and web panel for club meetings, notifications and community commands.</p>
<p><sub><b>Python · discord.py · FastAPI · SQLite</b></sub></p>
<p><b><a href="https://github.com/Krumqnkata/Discord-Bot-Notifier">Code &amp; documentation</a></b></p>
</td>
</tr>
</table>

</details>

<p align="right">
  <a href="https://github.com/Krumqnkata?tab=repositories"><b>Explore all my repositories →</b></a>
</p>

## My toolkit

<p>
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/python.svg" alt="Python" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/java.svg" alt="Java" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/typescript.svg" alt="TypeScript" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/javascript.svg" alt="JavaScript" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/php.svg" alt="PHP" height="32">
</p>

<p>
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/react.svg" alt="React" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/django.svg" alt="Django" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/fastapi.svg" alt="FastAPI" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/postgresql.svg" alt="PostgreSQL" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/mysql.svg" alt="MySQL" height="32">
</p>

<p>
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/debian.svg" alt="Debian" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/docker.svg" alt="Docker" height="32">
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/git.svg" alt="Git" height="32">
</p>

| Area | Technologies I work with |
| :--- | :--- |
| **Languages** | Python, Java, JavaScript, TypeScript, PHP |
| **Web & APIs** | React, FastAPI, Django REST Framework, HTML, CSS, WordPress |
| **Data** | PostgreSQL, MySQL, SQLite |
| **Servers & deployment** | Linux / Debian, Docker, Apache, systemd |
| **Desktop & media** | Tkinter / CustomTkinter, OpenCV, rawpy, FFmpeg |
| **Everyday tools** | Git, GitHub, VS Code |

## Beyond the code

I take part in school technology projects and IT club activities, sharing practical programming experience and working on useful tools with the school community.

<p>
  <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/arduino.svg" alt="Arduino" height="32">
</p>

I also experiment with **Arduino and RFID**, work with **3D printing**, and prepare **audio for school projects**. I enjoy the point where software meets a physical device, a printed object or something people hear and use.

## Current focus

- **PGKNMA Blog** — developing the platform and maintaining its deployment.
- **Stara Zagora Transit** — improving route discovery, timetables and vehicle data.

## GitHub activity

<p align="center">
  <a href="https://github.com/Krumqnkata?tab=repositories"><img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/generated/summary.svg" alt="Public repository statistics for Krumqnkata" width="400"></a>
  <a href="https://github.com/Krumqnkata?tab=repositories"><img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/generated/languages.svg" alt="Primary languages of original public repositories, counted by repository" width="400"></a>
</p>

<sub>Public repository data, refreshed daily. Language mix counts the primary language of original repositories and excludes forks.</sub>

### Contribution calendar

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/generated/snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/generated/snake-light.svg">
    <img src="https://raw.githubusercontent.com/Krumqnkata/Krumqnkata/main/assets/generated/snake-light.svg" alt="Animated snake following Krumqnkata's GitHub contribution calendar" width="100%">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/Krumqnkata/Krumqnkata/actions/workflows/profile-visuals.yml"><img src="https://github.com/Krumqnkata/Krumqnkata/actions/workflows/profile-visuals.yml/badge.svg" alt="Daily profile visuals refresh status"></a>
</p>

## Let's build something useful

I'm interested in educational tools, web applications and everyday automation. For an idea, feedback or collaboration around a project, open an issue in its [repository](https://github.com/Krumqnkata?tab=repositories).

## На български

<details>
<summary><b>Здравей, аз съм Крум — Крумянката. 🇧🇬</b></summary>

<br>

Ученик съм в **ПГКНМА „Проф. Минко Балкански“ в Стара Загора**. Работя с **Python, Java, уеб технологии и Linux** и създавам училищни платформи, настолни приложения и автоматизации.

Занимавам се с интерфейса, API, базите данни и разгръщането на сървъра. Харесва ми да виждам как една идея се превръща в нещо, което хората използват.

**Избрани проекти:**

- **[ПГКНМА Блог](https://pgknma.space)** — публикации, събития, анкети, профили и известия за училищната общност. Работя по React интерфейса, Django REST API и поддръжката. Кодът е частен.
- **[Сайтът на Даниела Крумова](https://logopedkrumova.com)** — професионален сайт на български и английски с адаптивен дизайн. Кодът е частен.
- **[Транспорт Стара Загора](https://github.com/Krumqnkata/stara-zagora-transit)** — карта, линии, разписания и GPS позиции при налични данни.
- **[RAW Studio](https://github.com/Krumqnkata/python-raw-processor)** — обработка на RAW снимки и групово експортиране.
- **[School Bell Cutter](https://github.com/Krumqnkata/bell-song-cutter)** — анализ на песни и подготовка на музикални звънци.
- **[School AI](https://github.com/Krumqnkata/AI-TV-COMPUTER_VISION)** — училищна информационна система с QR баджове, киоски и екрани.
- **[Ботът на ИТ клуба](https://github.com/Krumqnkata/Discord-Bot-Notifier)** — известия, сбирки и уеб панел.

**Технически поглед към ПГКНМА Блог:** React и TypeScript изграждат интерфейса, а TanStack Query управлява заявките и кеширането на данни. Django REST API обработва заявките, проверява правата за достъп и работи с MySQL чрез Django ORM. Административният панел използва Django Unfold. Работя по свързването на тези части, разгръщането им на Linux сървър с Apache и поддръжката.

**Извън кода:** участвам в училищни технологични проекти и дейностите на ИТ клуба, експериментирам с Arduino и RFID, занимавам се с 3D принтиране и подготовка на аудио.

**За мен добрата идея оживява, когато някой започне да я използва.**

</details>

---

<p align="center">
  <sub><b>Built with curiosity. Improved through practice.</b></sub><br>
  <sub>Кодът е началото. Ползата му дава смисъл.</sub>
</p>
