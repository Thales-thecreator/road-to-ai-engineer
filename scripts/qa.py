"""QA do repositório: roda no CI a cada push (ver .github/workflows/qa.yml).

Verifica links e âncoras internas, pares PT/EN, contas de XP das fases detalhadas,
tabelas, JSON do Obsidian, .gitignore, segredos/dados pessoais, metadados de imagens e e-mails dos commits.
Sai com código 1 se encontrar erro.
"""
import re, glob, os, json, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")  # console do Windows não é UTF-8
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ERR = []
def err(cat, msg): ERR.append(f"[{cat}] {msg}")
def read(f): return open(f, encoding="utf-8").read()
# no Windows o glob devolve "\\"; normaliza para os prefixos "templates/" etc. funcionarem
def files(p): return [f.replace(os.sep, "/") for f in glob.glob(p, recursive=True)]

MD = [f for f in files("**/*.md")
      if not f.startswith(".claude/skills/") or f.startswith(".claude/skills/mestre/")]

def anchors(text):
    ids = set(re.findall(r'<a id="([^"]+)"', text))
    for h in re.findall(r"^#{1,6} (.+)$", text, re.M):
        ids.add(re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-"))
    return ids

def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)

# 1. links e âncoras internas (templates usam caminhos de exemplo: ignorados)
for f in MD:
    if f.startswith("templates/"): continue
    text = strip_code(read(f))
    for m in re.finditer(r'(?:\]\(|src="|href=")(?!https?:|mailto:|#?")([^)"\s]+)', text):
        link = m.group(1); path, _, anc = link.partition("#")
        tgt = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if path and not os.path.exists(tgt): err("link", f"{f} → {link}"); continue
        if anc and tgt.endswith(".md") and anc not in anchors(read(tgt)): err("âncora", f"{f} → {link}")

# 2. pares PT/EN e seletor de idioma
pairs = [(f, f[:-6] + ".md") for f in files("**/*.en.md") if not f.startswith("templates/")]
pairs += [("README.md", "README.pt-BR.md"), ("SECURITY.md", "SECURITY.pt-BR.md")]
for a, b in pairs:
    if not os.path.exists(b): err("par", f"{a} sem par {b}"); continue
    A, B = read(a), read(b)
    for name, rx in [("checkboxes", r"- \[[ x]\]"), ("seções h2", r"^## "), ("linhas de tabela", r"^\|")]:
        ca, cb = len(re.findall(rx, A, re.M)), len(re.findall(rx, B, re.M))
        if ca != cb: err("paridade", f"{a} vs {b}: {name} {ca}≠{cb}")
    for f, t in [(a, A), (b, B)]:
        if not re.search(r"nglish", t) or not re.search(r"ortugu[êe]s", t): err("seletor", f"{f} sem seletor de idioma")

# 3. XP das fases detalhadas: missões + chefão = XP da fase
for f in ["tracks/00-tutorial/README.md", "tracks/01-python/README.md"]:
    t = read(f)
    head = int(re.search(r"XP da fase:\*\* (\d+)", t).group(1))
    ms = sum(int(x) for x in re.findall(r"^- \[[ x]\] \*\*M\d\.\d+\w?.*?— (\d+) XP", t, re.M))
    tot = int(re.search(r"Total de missões:\*\* (\d+)", t).group(1))
    boss = int(re.search(r"Chefão — .*?· (\d+) XP", t).group(1))
    elite = re.search(r"Mini-chefão de elite — .*?· (\d+) XP", t)
    boss += int(elite.group(1)) if elite else 0
    if ms != tot: err("xp", f"{f}: missões somam {ms}, declarado {tot}")
    if tot + boss != head: err("xp", f"{f}: {tot}+{boss} (chefões) ≠ XP da fase {head}")

# 3b. todo comando do /mestre (argument-hint) aparece na página de comandos
hint = re.search(r'argument-hint: "(.*)"', read(".claude/skills/mestre/SKILL.md")).group(1)
for part in hint.split("|"):
    cmd = re.sub(r"\s+(<.*|M\d\.\d+\w?)$", "", part.strip())
    for f in ["COMANDOS.md", "COMANDOS.en.md"]:
        if f"/mestre {cmd}" not in read(f): err("comandos", f"{f} não documenta `/mestre {cmd}`")

# 4. tabelas com número de colunas consistente
for f in MD:
    lines = read(f).split("\n"); code = False
    for i, l in enumerate(lines):
        if l.startswith("```"): code = not code
        if code or not (l.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1])): continue
        n = l.count("|"); j = i + 2
        while j < len(lines) and lines[j].startswith("|"):
            if lines[j].count("|") != n: err("tabela", f"{f}:{j + 1}")
            j += 1

# 5. JSON do Obsidian
for f in files(".obsidian/*.json"):
    try: json.load(open(f, encoding="utf-8"))
    except Exception as e: err("obsidian", f"{f}: {e}")

# 6. .gitignore protege segredos e não esconde notas
for p, want in [(".env", True), ("kaggle.json", True), ("x/credentials.json", True), ("a.pem", True),
                ("privado/x.md", True), ("tracks/00-tutorial/notes/n.md", False), ("notebook.ipynb", False)]:
    got = subprocess.run(["git", "check-ignore", "-q", p]).returncode == 0
    if got != want: err("gitignore", f"{p}: ignorado={got}, esperado={want}")

# 7. segredos e dados pessoais
pat = r"(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|hf_[A-Za-z0-9]{30,}|[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}|@(gmail|hotmail|outlook|yahoo)\.com)"
out = subprocess.run(["git", "grep", "-nIE", pat, "--", ".", ":!.claude/skills"], capture_output=True, text=True, encoding="utf-8").stdout
if out.strip(): err("segredo", out.strip())

# 8. metadados de imagens (GPS, câmera)
r = subprocess.run([sys.executable, "scripts/clean_images.py", "--check"], capture_output=True, text=True, encoding="utf-8")
if r.returncode != 0: err("metadados", (r.stderr or r.stdout).strip())

# 9. e-mails dos commits (privacidade)
for mail in set(subprocess.run(["git", "log", "--format=%ae"], capture_output=True, text=True, encoding="utf-8").stdout.split()):
    if not mail.endswith(("noreply.github.com", "noreply@anthropic.com", "noreply@github.com")):
        err("privacidade", f"commit com e-mail público: {mail}")

print("\n".join(ERR) if ERR else "QA: tudo certo ✅")
sys.exit(1 if ERR else 0)
