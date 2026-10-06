# 🟢 Phase 0 — Tutorial

[🇧🇷 Português](./README.md) · 🇺🇸 **English**

> **Duration:** 2 weeks · **Phase XP:** 150 · **Weekly goal:** 3 sessions of ≥ 30 min
> **Goal:** get the environment ready and, above all, **build the study habit**.

> ⛓️ **In the saga:** six chains bind you to the Throne. Missions M0.1–M0.6 break one each; M0.7 lights the first spark of power. Report with `/mestre missão cumprida M0.x`. The Master runs a short [oral exam](../../ROADMAP.en.md#prova-oral) before accepting each mission.

Content is deliberately light in this phase. What matters is showing up 3 times a week and logging it in [`LOG.md`](../../LOG.md).

---

## 🗒️ Missions

Tick `[x]` when done, log it in `LOG.md`, and close the matching GitHub issue.

- [x] **M0.1 · Hello, GitHub** · ⛓️ *Chain I · Ignorance* — 15 XP · 🏅 *First Commit*
  Follow GitHub's [Hello World guide](https://docs.github.com/en/get-started/start-your-journey/hello-world) to understand repository, branch, commit and pull request. No need to create another repo — understanding the concepts is enough. Then **create your first note on the website**: open the [`notes/`](./notes/) folder, click **Add file → Create new file**, name it `01-git-e-github.md`, write it and click **Commit changes**. That's it: your **first commit**.
  **Evidence:** the note `notes/01-git-e-github.md` explaining, in your own words, what a *commit* and a *branch* are.

- [x] **M0.2 · Logbook** · ⛓️ *Chain II · Silence* — 15 XP
  Now **edit** a file that already exists: open [`LOG.md`](../../LOG.md), click the ✏️ pencil and log your session in the week's table (date, minutes, what you did, mission). Commit it. From now on, every study session ends this way.
  **Evidence:** the session row in `LOG.md`.

- [x] **M0.3 · First notebook** · ⛓️ *Chain III · Blank Page* — 20 XP · 🏅 *First Notebook*
  Open [Google Colab](https://colab.research.google.com/), create a notebook, run `print("Hello, world!")` and a few sums (`2 + 2`, `10 / 3`). Save it into the repo with **File → Save a copy in GitHub**, under `tracks/00-tutorial/exercises/`.
  **Evidence:** `exercises/01-ola-mundo.ipynb`.

- [x] **M0.4 · Visual Git** · ⛓️ *Chain IV · Labyrinth* — 15 XP
  Complete the **"Introduction Sequence"** (4 levels) of [Learn Git Branching](https://learngitbranching.js.org/).
  **Evidence:** a screenshot of the final screen in `notes/` or one line in `LOG.md`.

- [x] **M0.5 · My mission and my schedule** · ⛓️ *Chain V · Lost Purpose* — 15 XP
  Rewrite the *Why* and *Constraints* sections of [`classroom/MISSION.md`](../../classroom/MISSION.md) in your own words (in Portuguese; the headings stay in English because that is the `/teach` format), and pick **3 fixed weekly slots** to study. Write them at the top of `LOG.md`.
  **Evidence:** updated `MISSION.md` and `LOG.md`.

- [x] **M0.6 · First lesson with the teacher** · ⛓️ *Chain VI · Solitude* — 0 XP (+10 from the lesson)
  Open Claude Code in this repo and run `/teach What is Machine Learning, in plain language, for someone who has never programmed`. Take the lesson's quiz.
  **Evidence:** the lesson saved in `classroom/lessons/`.

- [x] **M0.7 · First spell** · ✨ *The Spark* — 20 XP
  Feel the power before you understand it all. In a new Colab notebook, run a **pretrained** AI model that reads the sentiment of sentences in Portuguese:
  ```python
  from transformers import pipeline
  leitor = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
  leitor(["Hoje eu aprendi a fazer um commit!", "Odeio quando o código não roda."])
  ```
  Then try **10 sentences of your own** (include irony and slang) and note where the model gets it right and where it fails. You don't need to understand the code yet: in 18 months you will know how to build this from scratch.
  **Evidence:** `exercises/02-primeiro-feitico.ipynb` with your sentences and 3 lines at the end: what surprised you, where it failed, and a guess why.

**Mission total:** 100 XP (+10 from the lesson)

---

## 🐉 Boss — The Habit Guardian · 50 XP · 🪑 *The Throne of Broken Blades*

- [ ] Every mission above done.
- [ ] **2 weeks in a row** meeting the 3-session goal (check `LOG.md`).

This phase's boss is about consistency, so it cannot be [challenged](../../ROADMAP.en.md#desafiar-o-chefao) early.

Defeating the boss = **Level 1 · Apprentice** 🎉 and unlocks [Phase 1 — Python](../01-python/README.en.md).

---

## 💡 Tips for building the habit

- **Same time, same place.** The brain ties context to routine.
- **Start ridiculously small.** 30 min is the ceiling at first, not the floor.
- **Never skip twice in a row.** Missed a day? Do a 15-min minimum session the next one.
- **Always log it.** Watching `LOG.md` grow and the GitHub graph turn green is part of the reward.
