#!/usr/bin/env python3
"""Refresh data/github-meta.json with last push, stars, archived flag for every GitHub repo in the dataset.
Unauthenticated GitHub API allows 60 calls/hour; set GITHUB_TOKEN to raise it."""
import json, re, os, time, pathlib, urllib.request, urllib.error
root = pathlib.Path(__file__).resolve().parents[1]
data = json.loads((root/"data/firmwares.json").read_text())
out_p = root/"data/github-meta.json"
old = json.loads(out_p.read_text()) if out_p.exists() else {"repos": {}}
meta = old["repos"]
hdr = {"User-Agent": "fm1-atlas", "Accept": "application/vnd.github+json"}
if os.environ.get("GITHUB_TOKEN"): hdr["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
for d in data:
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", d.get("repo", ""))
    if not m: continue
    key = f"{m[1]}/{m[2]}"
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/repos/{key}", headers=hdr), timeout=20) as r:
            j = json.load(r); rem = int(r.headers.get("X-RateLimit-Remaining", "0"))
        meta[key] = {"pushed_at": j["pushed_at"][:10], "stargazers_count": j["stargazers_count"], "archived": j["archived"],
                     "license": (j.get("license") or {}).get("spdx_id"), "fork_of": (j.get("parent") or {}).get("full_name"), "description": j.get("description")}
        print(f"{key:45s} {meta[key]['pushed_at']} stars {meta[key]['stargazers_count']} (remaining {rem})")
        if rem <= 1: print("rate limit reached, keeping older entries for the rest"); break
    except urllib.error.HTTPError as e:
        meta[key] = {"error": e.code}; print(f"{key:45s} HTTP {e.code}")
        if e.code == 403: break
out_p.write_text(json.dumps({"fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "repos": meta}, indent=1))
print("saved", out_p)
