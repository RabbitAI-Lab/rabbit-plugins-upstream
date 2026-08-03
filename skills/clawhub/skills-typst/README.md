# skills-typst

Kirk Lin's Typst skill for AI agents — curated, compile-tested document templates
with a one-command PDF build. Describe a document; get a finished PDF. No typesetting
wrangling required.

## Layout

| Path | What |
|---|---|
| [`SKILL.md`](SKILL.md) | Skill entry point (the agent reads this) |
| [`templates/`](templates/) | Self-contained document templates — start with `neurips-paper` |
| [`scripts/compile.sh`](scripts/compile.sh) | Build a `.typ` to PDF + PNG previews |
| [`references/`](references/) | Template catalog and the "add a template" guide |
| [`examples/`](examples/) | Rendered previews of each template |

## Build

```bash
bash scripts/compile.sh templates/neurips-paper/paper.typ --preview
```

Requires the [`typst`](https://github.com/typst/typst) CLI (`brew install typst`)
and `poppler-utils` (`pdftoppm`) for previews.

## Templates

- **neurips-paper** — single-column NeurIPS/arXiv-style research paper. Self-contained:
  the NeurIPS-like styling is a local `neurips.typ` function, so it compiles offline
  with no `@preview` package fetch. Sample content recreates *Attention Is All You Need*.

Adding your own → [`references/adding-templates.md`](references/adding-templates.md).

## Install as an agent skill

`SKILL.md` uses the open Agent Skill format, so it isn't tied to any one AI agent.
Place (or symlink) this repository wherever your agent loads skills from, as a
folder named `kirklin-typst` (matching the `name:` in `SKILL.md`).

## Sibling

This is the Typst counterpart to [`skills-latex`](../skills-latex) — same framework
shape (templates + one-command build + previews), different engine.
