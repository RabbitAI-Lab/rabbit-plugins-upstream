# ✏️ Excalidraw Diagrams for Obsidian

**Describe the boxes and arrows. Get a clean, hand-drawn Excalidraw diagram that opens straight in Obsidian.**

Language models are bad at writing Excalidraw JSON by hand. Labels drift out of shapes, arrows come loose and boxes pile up. This OpenClaw skill has the agent write a short spec instead, and a deterministic, dependency-free Python script does the rest.

- **Real layout.** Layered flowcharts, pipelines and architecture diagrams in either direction, with groups, cycles and arrows routed around nodes.
- **Files that behave.** Text and arrows bound both ways, so nothing detaches when you move a shape, and the Obsidian `.excalidraw.md` format with searchable labels.
- **Checked before handover.** A validator catches broken bindings, unreadable fonts and overlaps.
- **Safe with your vault.** It asks for the path, never overwrites without your OK and makes no network calls.

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
| [whetstone](https://github.com/Ricardodpalmeida/whetstone) | Makes a coding agent size every change by risk before it touches anything, then scale the process to match. |
| [LadybugDB openCypher](https://clawhub.ai/ricardodpalmeida/ladybug-opencypher-updated) | Design and query LadybugDB graphs with openCypher, including imports, full-text search and Neo4j query adaptation. |
| [Book Capture for Obsidian](https://clawhub.ai/ricardodpalmeida/book-capture-obsidian) | Turns a cover photo, barcode, ISBN or Goodreads export into linked Obsidian book notes and a library dashboard. |
| [Microsoft Learn MCP](https://clawhub.ai/ricardodpalmeida/mslearn-mcp) | Grounds Azure, .NET, Microsoft 365 and Power Platform answers in official Microsoft Learn docs. |
