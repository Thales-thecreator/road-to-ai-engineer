# 🟢 Fase 0 — Tutorial

🇧🇷 **Português** · [🇺🇸 English](./README.en.md)

> **Duração:** 2 semanas · **XP da fase:** 150 · **Meta semanal:** 3 sessões de ≥ 30 min
> **Objetivo:** ter o ambiente pronto e, acima de tudo, **criar o hábito de estudar**.

> ⛓️ **Na saga:** seis correntes prendem você ao Trono. As missões M0.1–M0.6 quebram uma cada; a M0.7 acende a primeira faísca de poder. Relate com `/mestre missão cumprida M0.x`. O Mestre faz uma [prova oral](../../ROADMAP.md#prova-oral) curta antes de aceitar cada missão.

Nesta fase o conteúdo é leve de propósito. O que importa é aparecer 3 vezes por semana e registrar no [`LOG.md`](../../LOG.md).

---

## 🗒️ Missões

Marque `[x]` ao concluir, registre no `LOG.md` e feche a issue correspondente no GitHub.

- [x] **M0.1 · Olá, GitHub** · ⛓️ *Corrente I · Ignorância* — 15 XP · 🏅 *Primeiro Commit*
  Siga o guia [Hello World do GitHub](https://docs.github.com/pt/get-started/start-your-journey/hello-world) (em PT) para entender repositório, branch, commit e pull request. Não precisa criar outro repo: basta entender os conceitos. Depois, **crie sua primeira nota pelo site**: abra a pasta [`notes/`](./notes/), clique em **Add file → Create new file**, dê o nome `01-git-e-github.md`, escreva e clique em **Commit changes**. Pronto: esse é o seu **primeiro commit**.
  **Evidência:** a nota `notes/01-git-e-github.md` explicando, com suas palavras, o que é *commit* e o que é *branch*.

- [x] **M0.2 · Diário de bordo** · ⛓️ *Corrente II · Silêncio* — 15 XP
  Agora **edite** um arquivo que já existe: abra o [`LOG.md`](../../LOG.md), clique no lápis ✏️ e registre sua sessão na tabela da semana (data, minutos, o que fez, missão). Faça o commit. Daqui em diante, toda sessão de estudo termina assim.
  **Evidência:** a linha da sessão no `LOG.md`.

- [x] **M0.3 · Primeiro notebook** · ⛓️ *Corrente III · Página em Branco* — 20 XP · 🏅 *Primeiro Notebook*
  Abra o [Google Colab](https://colab.research.google.com/), crie um notebook, rode `print("Olá, mundo!")` e algumas contas (`2 + 2`, `10 / 3`). Salve no repo com **Arquivo → Salvar uma cópia no GitHub** dentro de `tracks/00-tutorial/exercises/`.
  **Evidência:** `exercises/01-ola-mundo.ipynb`.

- [x] **M0.4 · Git visual** · ⛓️ *Corrente IV · Labirinto* — 15 XP
  Complete a sequência **"Introdução"** (4 níveis) do [Learn Git Branching em PT](https://learngitbranching.js.org/?locale=pt_BR).
  **Evidência:** print da tela final em `notes/` ou uma linha no `LOG.md`.

- [x] **M0.5 · Minha missão e minha agenda** · ⛓️ *Corrente V · Propósito Perdido* — 15 XP
  Reescreva as seções *Why* (por quê) e *Constraints* (restrições) do [`classroom/MISSION.md`](../../classroom/MISSION.md) com suas palavras, em português (os títulos ficam em inglês porque é o formato da `/teach`), e escolha **3 horários fixos na semana** para estudar. Anote-os no topo do `LOG.md`.
  **Evidência:** `MISSION.md` e `LOG.md` atualizados.

- [x] **M0.6 · Primeira aula com o professor** · ⛓️ *Corrente VI · Solidão* — 0 XP (+10 da aula)
  Abra o Claude Code neste repo e rode `/teach O que é Machine Learning, em linguagem simples, para quem nunca programou`. Faça o quiz da aula.
  **Evidência:** a aula salva em `classroom/lessons/`.

- [x] **M0.7 · Primeiro feitiço** · ✨ *A Faísca* — 20 XP
  Sinta o poder antes de entender tudo. Num notebook novo do Colab, rode um modelo de IA **pré-treinado** que lê o sentimento de frases em português:
  ```python
  from transformers import pipeline
  leitor = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
  leitor(["Hoje eu aprendi a fazer um commit!", "Odeio quando o código não roda."])
  ```
  Depois teste **10 frases suas** (inclua ironia e gíria) e anote onde o modelo acerta e onde erra. Não precisa entender o código ainda: em 18 meses você vai saber construir isso do zero.
  **Evidência:** `exercises/02-primeiro-feitico.ipynb` com as suas frases e 3 linhas no fim: o que surpreendeu, onde errou e um palpite do porquê.

**Total de missões:** 100 XP (+10 da aula)

---

## 🐉 Chefão — O Guardião do Hábito · 50 XP · 🪑 *O Trono das Lâminas Partidas*

- [ ] Todas as missões acima concluídas.
- [ ] **2 semanas seguidas** batendo a meta de 3 sessões (confira no `LOG.md`).

Nesta fase o chefão é de constância, então não dá para [desafiá-lo](../../ROADMAP.md#desafiar-o-chefao) antes da hora.

Vencer o chefão = **Nível 1 · Aprendiz** 🎉 e desbloqueia a [Fase 1 — Python](../01-python/).

---

## 💡 Dicas para criar o hábito

- **Mesmo horário, mesmo lugar.** O cérebro associa contexto a rotina.
- **Comece ridiculamente pequeno.** 30 min é o teto no começo, não o piso.
- **Nunca pule duas vezes seguidas.** Perdeu um dia? Faça uma sessão mínima de 15 min no seguinte.
- **Registre sempre.** Ver o `LOG.md` crescer e o gráfico do GitHub ficar verde é parte da recompensa.
