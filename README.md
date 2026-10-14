# FM-1 Firmware Atlas

A map of every known firmware for the **M-VAVE FM-1** pocket FM synth: what each one tries to be, which engines and sounds it ships, how it talks MIDI, whether the project is still alive (from GitHub activity), and a six-step path for new owners.

- `index.html` is the whole site, a single static file, served at https://wero1414.github.io/atlas-fm-1/ via GitHub Pages.
- `dist/artifact.html` is the same page without the document skeleton, for the claude.ai Artifact viewer.
- `FIRMWARES.md` is the same data as Markdown tables.
- `data/firmwares.json` is the source of truth, one object per firmware. Edit it to add or fix an entry.
- `data/github-meta.json` holds last-push dates and stars, refreshed by `tools/fetch_github.py`.

## Build

```bash
python3 tools/fetch_github.py   # optional: refresh activity (60 unauthenticated GitHub calls/hour, or set GITHUB_TOKEN)
python3 build.py                # writes index.html and FIRMWARES.md
```

Health rules in `build.py`: active = pushed within 14 days, quiet = 15 to 60 days, stale = older, removed = repository returns 404.

## Related directories

- https://fm1-editor.com/firmware/ (versions, dates, stars, install notes)
- https://thefirmwarehub.com/ (one-click installer, run by zvenson)
- https://github.com/aroum/fm1-custom-fw (the most complete written directory; this atlas was seeded from it)
- https://github.com/cicloid/awesome-fm-1

## Contributing

Add a row to `data/firmwares.json` with: name, author, family, purpose, emulates, engines, sounds, sequencer, midi, clock, why, features, status, license, repo, install. Run `build.py`, open `index.html`, commit.

License for this repository's own files: CC0. Firmware names and descriptions belong to their authors.
