# ✏️ Excalidraw Diagrams for Obsidian

Generate Excalidraw diagrams from a short boxes-and-arrows spec, with a deterministic Python layout and validator. Supports Obsidian `.excalidraw.md` and standalone `.excalidraw`, layered layouts, groups and cycles. Text/arrows bind in both directions; structural validation catches malformed bindings and reports layout warnings.

Uses Python's standard library, makes no network calls and requires `--force` to overwrite an existing target. Source specs and output stay in the selected destination.

## Install

From ClawHub: `openclaw skills install @ricardodpalmeida/excalidraw-diagrams`. Or copy this folder into your workspace `skills/` directory. Needs Python 3.9 or newer and nothing else.

## Try it

```bash
python3 scripts/build_diagram.py --spec examples/ci-pipeline.json --out ci-pipeline.excalidraw
python3 scripts/validate.py ci-pipeline.excalidraw
```

Open the file on excalidraw.com, or use a `.excalidraw.md` name and open it in Obsidian with the Excalidraw plugin. The spec format is documented in `SKILL.md`.

## Files

- `SKILL.md` holds the agent instructions and the spec format.
- `scripts/build_diagram.py` builds the drawing. It never overwrites a file without `--force` and makes no network calls.
- `scripts/validate.py` checks structure, two-way bindings, fonts and overlaps.
- `references/excalidraw-format.md` documents the file format for hand edits.
- `examples/` has sample specs; `tests/` runs with `python3 -m unittest discover -s tests`.

## License

[MIT-0](LICENSE) (MIT No Attribution): use, copy, modify and redistribute it for any purpose, with no attribution required. The same license applies on ClawHub.

## More from the author

Made by Ricardo Pacheco Almeida. I write about applied AI, agents and enterprise architecture at [ricbits](https://me.ricbits.cc).

| Skill | What it does |
|-------|--------------|
| [whetstone](https://github.com/Ricardodpalmeida/whetstone) | Reviews consequential code changes with checks proportional to their impact. |
| [LadybugDB openCypher](https://clawhub.ai/ricardodpalmeida/ladybug-opencypher-updated) | Design and query LadybugDB graphs with openCypher, including imports, full-text search and Neo4j query adaptation. |
| [Book Capture for Obsidian](https://clawhub.ai/ricardodpalmeida/book-capture-obsidian) | Turns a cover photo, barcode, ISBN or Goodreads export into linked Obsidian book notes and a library dashboard. |
| [Microsoft Learn MCP](https://clawhub.ai/ricardodpalmeida/mslearn-mcp) | Grounds Azure, .NET, Microsoft 365 and Power Platform answers in official Microsoft Learn docs. |
