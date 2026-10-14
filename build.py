#!/usr/bin/env python3
"""Build index.html and FIRMWARES.md from data/firmwares.json + data/github-meta.json.

    python3 build.py              # writes index.html, FIRMWARES.md
    python3 tools/fetch_github.py # refreshes data/github-meta.json (60 unauthenticated calls/hour)
"""
import json, pathlib, re, datetime as dt
root = pathlib.Path(__file__).resolve().parent
data = json.loads((root/"data/firmwares.json").read_text())
meta = json.loads((root/"data/github-meta.json").read_text())
today = dt.date.today()

def gh_key(url):
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", url or "")
    return f"{m[1]}/{m[2]}" if m else None

for d in data:
    d.pop("rank", None); d.pop("type", None); d.pop("midi_in", None)
    k = gh_key(d.get("repo")); m = meta["repos"].get(k) if k else None
    d["gh"] = k
    d["stars"] = m.get("stargazers_count") if m and "error" not in m else None
    d["pushed"] = m.get("pushed_at", "")[:10] if m and "error" not in m else ""
    # health: objective where we have data, otherwise from status text
    if m and m.get("error") == 404:
        d["health"], d["health_note"] = "removed", "repository gone (404)"
    elif m and m.get("archived"):
        d["health"], d["health_note"] = "archived", "archived on GitHub"
    elif d["pushed"]:
        age = (today - dt.date.fromisoformat(d["pushed"])).days
        d["health"] = "active" if age <= 14 else "quiet" if age <= 60 else "stale"
        d["health_note"] = f"last push {d['pushed']} ({age} d ago)"
    elif "Closed" in d["license"] or "Proprietary" in d["license"]:
        d["health"], d["health_note"] = "closed", "closed source, no public repo"
    elif d["status"] in ("Teased",):
        d["health"], d["health_note"] = "vapor", "announced, nothing released"
    else:
        d["health"], d["health_note"] = "unknown", "not on GitHub"
    s = d["status"]
    d["ready"] = ("web" if re.search(r"Web installer|Web patcher", s, re.I) else
                  "file" if re.search(r"Prebuilt|Script|Stock", s, re.I) else
                  "build" if re.search(r"Build", s, re.I) else
                  "paid" if re.search(r"Commercial", s, re.I) else
                  "closed" if re.search(r"Closed", s, re.I) else
                  "none")
data.sort(key=lambda d: d["name"].lower())

tpl = (root/"template.html").read_text()
html = tpl.replace("/*__DATA__*/[]", json.dumps(data, ensure_ascii=False)) \
          .replace("__BUILT__", today.isoformat()).replace("__COUNT__", str(len(data)))
# artifact.html: body-only (the claude.ai Artifact tool adds the document skeleton)
(root/"dist").mkdir(exist_ok=True)
(root/"dist/artifact.html").write_text(html)
# index.html: complete document for GitHub Pages / any static host
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Crect width=%2232%22 height=%2232%22 rx=%226%22 fill=%22%230e0f14%22/%3E%3Ctext x=%2216%22 y=%2222%22 font-family=%22monospace%22 font-size=%2216%22 font-weight=%22700%22 text-anchor=%22middle%22 fill=%22%2329d3ff%22%3EFM%3C/text%3E%3C/svg%3E">\n'
       '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}[hidden]{display:none!important}</style>\n'
       + html.replace("</style>\n\n<div class=\"wrap\">", "</style>\n</head>\n<body>\n<div class=\"wrap\">", 1)
       + '\n<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";'
         'mermaid.initialize({startOnLoad:true,theme:matchMedia("(prefers-color-scheme: light)").matches?"neutral":"dark"});</script>\n'
       '</body>\n</html>\n')
(root/"index.html").write_text(doc)

# Markdown mirror
def c(s): return str(s or "").replace("|", "\\|").replace("\n", " ")
H = {"active":"active","quiet":"quiet","stale":"stale","removed":"REMOVED","archived":"archived","closed":"closed source","vapor":"announced only","unknown":"n/a"}
out = [f"# FM-1 Firmware Atlas", "", f"{len(data)} firmwares for the M-VAVE FM-1. Built {today} from `data/firmwares.json` and GitHub activity in `data/github-meta.json`.", "",
       "Health: active = pushed within 14 days, quiet = 15-60 days, stale = older. The scene started July 2026, so stale means abandoned-looking here.", ""]
ORDER = ["Classic synth","Groovebox","Drum machine","Sampler","Chord instrument","Physical model","Generative","Controller","Factory","Platform / dev","Kids","Game / novelty"]
for pur in sorted({d["purpose"] for d in data}, key=lambda x: ORDER.index(x) if x in ORDER else 99):
    rows = sorted([d for d in data if d["purpose"]==pur], key=lambda d: d["name"].lower())
    out += [f"## {pur} ({len(rows)})", "", "| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |", "|---|---|---|---|---|---|---|---|---|---|"]
    for d in rows:
        name = f"[{c(d['name'])}]({d['repo']})" if d.get("repo") else c(d["name"])
        inst = c(d["status"]) + (f" ([installer]({d['install']}))" if d.get("install") else "")
        out.append(f"| {name} | {c(d['emulates'])} | {c(d['engines'])} | {c(d['sounds'])} | {c(d['sequencer'])} | {c(d['midi'])} | {H[d['health']]} {d['pushed']} | {d['stars'] if d['stars'] is not None else ''} | {inst} | {c(d['license'])} |")
    out.append("")
out += ["## Why each one exists", ""] + [f"- **{c(d['name'])}** ({c(d['author'])}): {c(d['why'])}" for d in data]
(root/"FIRMWARES.md").write_text("\n".join(out) + "\n")
print(f"built index.html + dist/artifact.html ({len(html)//1024} KB), FIRMWARES.md; {sum(d['health']=='active' for d in data)} active, {sum(d['health']=='quiet' for d in data)} quiet, {sum(d['health']=='stale' for d in data)} stale, {sum(d['health']=='removed' for d in data)} removed")
