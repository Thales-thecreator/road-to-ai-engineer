<p align="center">
  <img src="./assets/banner.jpg" alt="Road to AI Engineer — from zero to ML, MLOps and LLMs, played as a dark-fantasy RPG" width="100%">
</p>

<p align="center">
  <a href="./README.pt-BR.md">🇧🇷 Leia em português</a> ·
  <a href="./ROADMAP.en.md">🗺️ Roadmap</a> ·
  <a href="./saga/README.en.md">📜 The Saga</a> ·
  <a href="./COMANDOS.en.md">⌨️ Commands</a> ·
  <a href="./LOG.md">📅 Study log</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/level-0%20·%20Recruit-6e7681?style=for-the-badge" alt="Level">
  <img src="https://img.shields.io/badge/XP-110%20%2F%207000-2ea043?style=for-the-badge" alt="XP">
  <img src="https://img.shields.io/badge/phase-0%20·%20Tutorial-1f6feb?style=for-the-badge" alt="Phase">
  <img src="https://img.shields.io/badge/streak-0%20weeks-f0883e?style=for-the-badge" alt="Streak">
  <a href="https://github.com/Thales-thecreator/road-to-ai-engineer/actions/workflows/qa.yml"><img src="https://github.com/Thales-thecreator/road-to-ai-engineer/actions/workflows/qa.yml/badge.svg" alt="QA"></a>
</p>

**Learning ML, MLOps and AI Engineering in public.** Every phase ends in a shipped project: its own repository, tests, real metrics and a public demo. The [projects](#-featured-projects) come first; the dark-fantasy RPG that keeps me studying is [further down](#-the-saga).

<!-- quest:start -->
> - ⚔️ **Current quest:** Boss · The Habit Guardian — The Throne
> - 📜 **Latest from the saga:** [The Spark](./saga/cenas/0007-a-faisca.en.md)
> - 🔥 **Streak:** 0 weeks · **Next level:** Apprentice (40 XP to go)
<!-- quest:end -->

## 👋 About me

_I'm Thales Gomes, learning in public to become an AI Engineer._

- 🎯 **Goal:** land my first ML / AI Engineer role
- 🌱 **Currently learning:** Git, GitHub and study habits (Phase 0)
- 📫 **Reach me:** [LinkedIn](https://www.linkedin.com/in/thales-gomes-2a6a12163/)

## 🏆 Featured projects

Each phase ends with a **boss fight**: a hands-on project published as its own repository, with tests, real metrics and a public demo.

| Project | Phase | Stack | Demo |
|---|:---:|---|:---:|
| _Coming soon — first boss unlocks in Phase 1_ | | | |

## 📜 The Saga

<p align="center">
  <a href="./saga/capitulos/00-prologo.en.md"><img src="./assets/art/00-prologo.jpg" alt="A chained exile on a throne of broken blades faces a creature of obsidian and ice" width="720"></a>
</p>

> _The sky over the Citadel of Aethelgard has held no stars for three hundred years._
>
> _"The Throne you are bound to demands a sacrifice the flesh cannot pay. It demands Focus. It demands the forging of your own intellect."_

This roadmap is played as a **grimdark narrative RPG**. Every real study mission breaks a chain, every phase boss is an Overlord, and nothing from the future is revealed before its time. Published in Portuguese and English. **[Read the prologue →](./saga/capitulos/00-prologo.en.md)**

## 🎮 Progress

<p align="center">
  <img src="./assets/circles-en.svg" alt="The Map of the Nine Circles — the player's progress through the phases" width="520">
</p>

<!-- sync:phases -->
| Phase | Track | Weeks | Status | Boss 🐉 |
|:---:|---|:---:|:---:|---|
| 0 | [Tutorial](./tracks/00-tutorial/README.en.md) — Git, Colab, habit | 2 | 🟢 In progress | The Habit Guardian |
| 1 | [Python](./tracks/01-python/README.en.md) | 10 | 🔒 | The Toolmaker |
| 2 | [Data & Math](./tracks/02-data-math/README.en.md) — pandas, SQL, stats, linear algebra | 10 | 🔒 | The Data Oracle |
| 3 | [Classical ML](./tracks/03-classical-ml/README.en.md) — dev tooling bridge, scikit-learn | 12 | 🔒 | The Kaggler |
| 4 | [Deep Learning](./tracks/04-deep-learning/README.en.md) — PyTorch, fast.ai | 10 | 🔒 | The Machine's Eye |
| 5 | [MLOps](./tracks/05-mlops/README.en.md) — Docker, FastAPI, MLflow, CI/CD | 12 | 🔒 | The Production Engineer |
| 6 | [LLMs & AI Engineering](./tracks/06-llms-ai-eng/README.en.md) — RAG, agents, evals | 12 | 🔒 | The RAG Architect |
| 7 | [Capstone & Career](./tracks/07-capstone-career/README.en.md) | 8 | 🔒 | The Capstone |
| 8 | [The Hunt](./tracks/08-the-hunt/README.en.md) — applications & interviews | open | 🔒 | The First Offer |
<!-- /sync:phases -->

The full game — missions, XP, levels, achievements and every free resource — lives in **[ROADMAP.en.md](./ROADMAP.en.md)** ([Portuguese version](./ROADMAP.md)).

## 🧰 Stack I'm learning

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?logo=postgresql&logoColor=white)

---

<details>
<summary><b>🗂️ How this repo works</b></summary>

```
├── progress.yml        # game state — single source of truth (synced by scripts/sync.py)
├── ROADMAP.md          # the game: phases, missions, XP, levels, achievements
│                       #   (every public doc has a *.en.md twin)
├── COMANDOS.md         # every command: the Master, study skills, Obsidian, scripts
├── LOG.md              # one line per study session → weekly goal & streak
├── CONTEXT.md          # glossary of the game's vocabulary
├── tracks/             # one folder per phase
│   └── NN-name/
│       ├── README.md   #   missions + boss checklist
│       ├── notes/      #   my study notes (Portuguese)
│       └── exercises/  #   code & notebooks
├── projects/           # small projects (boss projects get their own repos)
├── saga/               # the RPG: chapters, character sheet, chronicle
├── brain/              # second brain (Obsidian vault): concept notes + maps
├── classroom/          # interactive lessons generated with Claude's /teach skill
├── templates/          # note & project README templates
├── assets/             # banner, map of the nine circles, saga art
├── scripts/            # sync.py · qa.py (CI) · clean_images.py · visual generators
└── docs/adr/           # decisions about how this repo is organized
```

**Study loop:** pick the next mission → study the free resource → write a note → solve the exercises → log the session → earn XP. Stuck? Generate a short interactive lesson with `/teach`, or ask a community. Every command is in [COMANDOS.en.md](./COMANDOS.en.md).

**Rules of the game:** a weekly goal (3–4 sessions of 30+ min) instead of a fragile daily streak, XP only with evidence in the repo, and a mandatory boss project to unlock each phase. Details in [ROADMAP.en.md](./ROADMAP.en.md#regras).

</details>

<a id="play-it-yourself"></a>

<details>
<summary><b>🎲 Play it yourself</b></summary>

This roadmap is meant to be forked (it is also a **template repository**). To start your own run:

1. **Fork** this repository (and make sure your GitHub email is private — see [SECURITY](./SECURITY.md)).
2. **Reset the progress:** set everything in [`progress.yml`](./progress.yml) back to zero/`null` and run `python scripts/sync.py` (badges, dashboards, sheet and map follow). Then clear the session rows in `LOG.md`, untick the checkboxes in `tracks/`, reset `saga/cronica*.md` (keep the prologue) and delete `saga/cenas/*`.
3. **Make it yours:** rewrite `classroom/MISSION.md`, the *About me* section and the timeline to fit your life.
4. **Play:** open [Claude Code](https://claude.com/claude-code) in your fork and run `/mestre começar`. The skills in `.claude/skills/` come with the repo.

The plot pillars are the same for everyone — your choices are not. Credit this repo as described in the licenses below.

</details>

<details>
<summary><b>📄 License, credits & security</b></summary>

- **Code:** [MIT](./LICENSE) · **Roadmap & notes:** [CC BY-SA 4.0](./LICENSE-CONTENT.md) · **Saga:** [CC BY-NC-SA 4.0](./LICENSE-CONTENT.md) · details in [LICENSE-CONTENT.md](./LICENSE-CONTENT.md)
- **Credits:** icons by [Game-Icons.net](https://game-icons.net/) (CC BY 3.0) · fonts Cinzel & Cormorant Garamond (SIL OFL) · saga art AI-generated and composited for this repo
- Security & privacy rules for this public repo: [SECURITY.md](./SECURITY.md)

</details>

<details>
<summary><b>📚 Highlights of the curriculum</b></summary>

All resources are **free**. A few favourites:

[CS50P](https://cs50.harvard.edu/python/) ·
[Kaggle Learn](https://www.kaggle.com/learn) ·
[3Blue1Brown](https://www.3blue1brown.com/) ·
[Andrew Ng's ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction) ·
[fast.ai](https://course.fast.ai/) ·
[Karpathy's Zero to Hero](https://karpathy.ai/zero-to-hero.html) ·
[MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) ·
[Made With ML](https://madewithml.com/) ·
[Hugging Face LLM Course](https://huggingface.co/learn/llm-course) ·
[Anthropic Courses](https://github.com/anthropics/courses)

</details>

---

<p align="center"><i>Learning in public, one session at a time.</i> 🌱</p>
