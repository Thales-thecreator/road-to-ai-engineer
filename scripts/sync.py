"""Sincroniza o progresso do jogo a partir de progress.yml (fonte única de verdade).

Atualiza: badges e caixa de missão dos READMEs, painel e tabela de fases dos ROADMAPs,
datas das conquistas, nível/XP da ficha da saga e as classes do Mapa dos Nove Círculos.

    python scripts/sync.py           # reescreve os arquivos
    python scripts/sync.py --check   # só verifica; sai com erro se algo estiver fora de sincronia
"""
import re, sys, pathlib, urllib.parse
try:
    import yaml
except ImportError:
    sys.exit("Instale o PyYAML: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (XP mínimo, título PT, título EN, título da saga PT, título da saga EN)
LEVELS = [
    (0, "Recruta", "Recruit", "Herege Acorrentado", "Chained Heretic"),
    (150, "Aprendiz", "Apprentice", "Portador da Manopla", "Bearer of the Gauntlet"),
    (800, "Pythonista", "Pythonista", "Escriba do Verbo Proibido", "Scribe of the Forbidden Word"),
    (1600, "Explorador de Dados", "Data Explorer", "Vidente dos Números", "Seer of Numbers"),
    (2500, "Cientista de ML Júnior", "Junior ML Scientist", "Áugure Herege", "Heretic Augur"),
    (3400, "Deep Learner", "Deep Learner", "Tecelão de Sinapses", "Weaver of Synapses"),
    (4500, "MLOps Engineer", "MLOps Engineer", "Forjador de Engrenagens", "Forger of Gears"),
    (5600, "AI Engineer", "AI Engineer", "Arquiteto de Vozes", "Architect of Voices"),
    (6500, "Veterano", "Veteran", "Suserano Sem Trono", "Throneless Overlord"),
    (7000, "Lenda", "Legend", "Aquele Que Viu as Estrelas", "The One Who Saw the Stars"),
]
MAX_XP = 7000
# (nome PT, nome EN, "estudando agora" PT, EN)
PHASES = [
    ("Tutorial", "Tutorial", "Git, GitHub e hábito de estudo", "Git, GitHub and study habits"),
    ("Python", "Python", "Python (CS50P)", "Python (CS50P)"),
    ("Dados & Matemática", "Data & Math", "pandas, SQL, estatística e álgebra linear", "pandas, SQL, statistics and linear algebra"),
    ("ML Clássico", "Classical ML", "ferramentas de engenharia e scikit-learn", "engineering tools and scikit-learn"),
    ("Deep Learning", "Deep Learning", "PyTorch e fast.ai", "PyTorch and fast.ai"),
    ("MLOps", "MLOps", "Docker, FastAPI, MLflow e CI/CD", "Docker, FastAPI, MLflow and CI/CD"),
    ("LLMs & AI Engineering", "LLMs & AI Engineering", "LLMs, RAG, agentes e evals", "LLMs, RAG, agents and evals"),
    ("Capstone & Carreira", "Capstone & Career", "o projeto capstone", "the capstone project"),
    ("A Caçada", "The Hunt", "candidaturas e entrevistas", "applications and interviews"),
    ("Epílogo", "Epilogue", "a primeira vaga", "the first job"),
]

def load():
    s = yaml.safe_load((ROOT / "progress.yml").read_text(encoding="utf-8"))
    assert 0 <= s["level"] <= 9 and 0 <= s["phase"] <= 9 and 0 <= s["xp"] <= 10 ** 5, "progress.yml fora dos limites"
    assert s["xp"] >= LEVELS[s["level"]][0], f"nível {s['level']} exige {LEVELS[s['level']][0]} XP, mas xp={s['xp']}"
    return s

def badge(label, message, color):
    q = lambda t: urllib.parse.quote(str(t).replace("-", "--").replace("_", "__"), safe="").replace("%C2%B7", "·")
    return f"https://img.shields.io/badge/{q(label)}-{q(message)}-{color}?style=for-the-badge"

def next_level(s):
    lv = s["level"]
    if lv >= 9: return None, 0
    need = LEVELS[lv + 1][0] - s["xp"]
    return lv + 1, max(need, 0)

def sub_block(text, name, new):
    pat = re.compile(rf"(<!-- sync:{name} -->\n).*?(\n<!-- /sync:{name} -->)", re.S)
    assert pat.search(text), f"marcador sync:{name} ausente"
    return pat.sub(lambda m: m.group(1) + new + m.group(2), text)

def status_table(text, name, col, labels, phase, finished):
    def fix(block):
        out = []
        for line in block.split("\n"):
            m = re.match(r"^\| (\d) \|", line)
            if m:
                n = int(m.group(1)); cells = line.split("|")
                st = labels[2] if n > phase else (labels[1] if (n < phase or finished) else labels[0])
                cells[col + 1] = f" {st} "
                line = "|".join(cells)
            out.append(line)
        return "\n".join(out)
    pat = re.compile(rf"(<!-- sync:{name} -->\n)(.*?)(\n<!-- /sync:{name} -->)", re.S)
    return pat.sub(lambda m: m.group(1) + fix(m.group(2)) + m.group(3), text)

def readme(text, s, lang):
    lv, xp, ph = s["level"], s["xp"], s["phase"]
    L = LEVELS[lv]; nxt, need = next_level(s)
    pt = lang == "pt"
    phase_name = PHASES[ph][0 if pt else 1]
    # badges
    specs = [("Nível" if pt else "Level", "nível" if pt else "level", f"{lv} · {L[1] if pt else L[2]}", "6e7681"),
             ("XP", "XP", f"{xp} / {MAX_XP}", "2ea043"),
             ("Fase" if pt else "Phase", "fase" if pt else "phase", f"{ph} · {phase_name}", "1f6feb"),
             ("Streak", "streak", f"{s['streak']['current']} {'semanas' if pt else 'weeks'}", "f0883e")]
    for alt, label, msg, color in specs:
        text, n = re.subn(rf'<img src="https://img\.shields\.io/badge/[^"]*" alt="{alt}">',
                          f'<img src="{badge(label, msg, color)}" alt="{alt}">', text)
        assert n == 1, f"badge {alt} não encontrado"
    # caixa de missão
    q = s["quest"]["pt" if pt else "en"]
    if q is None:
        q = "o jogo ainda não começou — a primeira corrente espera." if pt else "the game has not started yet — the first chain awaits."
    sl = s["saga_latest"]["pt" if pt else "en"]
    if nxt is None:
        lvl_txt = "nível máximo" if pt else "max level"
    elif need == 0:
        lvl_txt = (f"{LEVELS[nxt][1]} (XP pronto — falta o chefão)" if pt else f"{LEVELS[nxt][2]} (XP ready — boss pending)")
    else:
        lvl_txt = (f"{LEVELS[nxt][1]} (faltam {need} XP)" if pt else f"{LEVELS[nxt][2]} ({need} XP to go)")
    wk = f"{s['streak']['current']} {'semanas' if pt else 'weeks'}"
    box = (f"> - ⚔️ **Missão atual:** {q}\n> - 📜 **Último da saga:** [{sl['title']}](./{sl['path']})\n> - 🔥 **Streak:** {wk} · **Próximo nível:** {lvl_txt}"
           if pt else
           f"> - ⚔️ **Current quest:** {q}\n> - 📜 **Latest from the saga:** [{sl['title']}](./{sl['path']})\n> - 🔥 **Streak:** {wk} · **Next level:** {lvl_txt}")
    text = re.sub(r"(<!-- quest:start -->\n).*?(\n<!-- quest:end -->)", lambda m: m.group(1) + box + m.group(2), text, flags=re.S)
    # estudando agora
    learn = PHASES[ph][2 if pt else 3]
    text, n = re.subn(r"(- 🌱 \*\*(?:Estudando agora|Currently learning):\*\* ).*", lambda m: m.group(1) + f"{learn} ({'Fase' if pt else 'Phase'} {ph})", text)
    assert n == 1
    labels = ("🟢 Em andamento", "✅ Vencida", "🔒") if pt else ("🟢 In progress", "✅ Cleared", "🔒")
    return status_table(text, "phases", 3, labels, ph, s["finished"])

def roadmap(text, s, lang):
    lv, xp, ph = s["level"], s["xp"], s["phase"]
    pt = lang == "pt"; L = LEVELS[lv]; nxt, need = next_level(s)
    cur_min = L[0]; nxt_min = LEVELS[nxt][0] if nxt else MAX_XP
    frac = 1.0 if nxt is None else min(max((xp - cur_min) / (nxt_min - cur_min), 0), 1)
    bar = "█" * round(frac * 20) + "░" * (20 - round(frac * 20))
    ph_name = PHASES[ph][0 if pt else 1]
    if pt:
        head = "| Nível | XP total | Fase atual | Streak | Chefões vencidos |\n|:---:|:---:|:---:|:---:|:---:|\n"
        row = f"| **{lv} · {L[1]}** | **{xp}** / {nxt_min} | 🟢 Fase {ph} — {ph_name} | 🔥 {s['streak']['current']} semanas | {min(ph, 9) if not s['finished'] else 9} / 9 |"
        nl = f"→ próximo nível: {LEVELS[nxt][1]} ({nxt_min} XP)" if nxt else "→ nível máximo"
        note = "> Gerado a partir do [`progress.yml`](./progress.yml) por `scripts/sync.py`. Não edite à mão."
    else:
        head = "| Level | Total XP | Current phase | Streak | Bosses defeated |\n|:---:|:---:|:---:|:---:|:---:|\n"
        row = f"| **{lv} · {L[2]}** | **{xp}** / {nxt_min} | 🟢 Phase {ph} — {ph_name} | 🔥 {s['streak']['current']} weeks | {min(ph, 9) if not s['finished'] else 9} / 9 |"
        nl = f"→ next level: {LEVELS[nxt][2]} ({nxt_min} XP)" if nxt else "→ max level"
        note = "> Generated from [`progress.yml`](./progress.yml) by `scripts/sync.py`. Do not edit by hand."
    panel = f"{head}{row}\n\n```\nXP  [{bar}]  {round(frac * 100)}%   {nl}\n```\n\n{note}"
    text = sub_block(text, "panel", panel)
    labels = ("🟢 Atual", "✅", "🔒") if pt else ("🟢 Current", "✅", "🔒")
    text = status_table(text, "phases", 5, labels, ph, s["finished"])
    # datas das conquistas: linhas "| emoji | nome | como | data |"
    def ach(m):
        emoji = m.group(1); date = s["achievements"].get(emoji, "")
        return f"{m.group(0).rsplit('|', 2)[0]}| {date} |" if date else f"{m.group(0).rsplit('|', 2)[0]}| |"
    pat = re.compile(r"(<!-- sync:achievements -->\n)(.*?)(\n<!-- /sync:achievements -->)", re.S)
    assert pat.search(text), "marcador sync:achievements ausente"
    return pat.sub(lambda m: m.group(1) + re.sub(r"^\| (\S+) \| [^|]+ \| [^|]+ \|[^|]*\|$", ach, m.group(2), flags=re.M) + m.group(3), text)

def sheet(text, s, lang):
    lv = s["level"]; L = LEVELS[lv]; pt = lang == "pt"
    lvl = f"| **{'Nível' if pt else 'Level'}** | {lv} · *{L[3] if pt else L[4]}* ({L[1] if pt else L[2]}) |"
    text, n1 = re.subn(rf"^\| \*\*{'Nível' if pt else 'Level'}\*\* \|.*$", lvl, text, flags=re.M)
    text, n2 = re.subn(r"^\| \*\*XP\*\* \|.*$", f"| **XP** | {s['xp']} |", text, flags=re.M)
    assert n1 == n2 == 1, "linhas de nível/XP da ficha não encontradas"
    return text

def circles(text, s):
    ph, fin = s["phase"], s["finished"]
    for n in range(10):
        st = "done" if (n < ph or fin) else ("current" if n == ph else "locked")
        if n == 9: st += " revealed" if (ph >= 9 or fin) else " hidden"
        text, k = re.subn(rf'(<g id="circle-{n}" class=")[^"]*(")', rf"\g<1>{st}\2", text)
        assert k == 1, f"circle-{n} não encontrado"
    return text

TARGETS = [
    ("README.md", lambda t, s: readme(t, s, "en")),
    ("README.pt-BR.md", lambda t, s: readme(t, s, "pt")),
    ("ROADMAP.md", lambda t, s: roadmap(t, s, "pt")),
    ("ROADMAP.en.md", lambda t, s: roadmap(t, s, "en")),
    ("saga/ficha.md", lambda t, s: sheet(t, s, "pt")),
    ("saga/ficha.en.md", lambda t, s: sheet(t, s, "en")),
    ("assets/circles-pt.svg", circles),
    ("assets/circles-en.svg", circles),
]

def main():
    check = "--check" in sys.argv
    s = load(); stale = []
    for rel, fn in TARGETS:
        p = ROOT / rel; old = p.read_text(encoding="utf-8"); new = fn(old, s)
        if new != old:
            stale.append(rel)
            if not check: p.write_text(new, encoding="utf-8", newline="")
    if check and stale:
        sys.exit("Fora de sincronia com progress.yml: " + ", ".join(stale) + "\nRode: python scripts/sync.py")
    print(("Atualizados: " + ", ".join(stale)) if stale and not check else "Tudo em sincronia.")

if __name__ == "__main__":
    main()
