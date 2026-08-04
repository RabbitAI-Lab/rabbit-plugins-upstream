---
name: kirklin-typst
description: >-
  Create polished, compile-tested Typst documents from curated kirklin templates
  and build them to PDF with per-page PNG previews. Use when the user wants to
  write, typeset, or compile a Typst document — especially an academic or research
  paper in NeurIPS/arXiv style (the neurips-paper template) — or says "make a Typst
  paper", "write a conference paper in Typst", "typeset this as a paper", "compile
  this .typ", or "turn this into a PDF paper". This is a template framework: pick a
  template under templates/, copy and customize it, then build with
  scripts/compile.sh (typst compile, per-page PNG previews). New document types are
  added as templates.
---

# kirklin-typst

Curated Typst templates plus a one-command build. Each template is a complete,
compile-tested document you copy and fill in; `scripts/compile.sh` turns it into a
PDF with page previews. Paths below are relative to this skill's directory.

## When to use

- Writing a research / academic paper (NeurIPS / arXiv style) → `neurips-paper`.
- Compiling any `.typ` to PDF and showing previews.
- More document types will arrive as templates — always check `references/templates.md`
  before assuming a type isn't covered.

## Why Typst

Typst compiles in a **single fast pass** — no multi-run `latexmk` dance. It resolves
cross-references, citations, and the outline incrementally, and ships **one engine**,
so the build is just `typst compile`. Templates are plain `.typ` with an ordinary
module system (`#import`, `#include`), so styling lives in readable functions instead
of macros.

## Workflow

1. **Pick a template.** Match the user's document type to a template using the
   catalog in [references/templates.md](references/templates.md).
2. **Copy it out.** Copy the whole template directory to the user's working area
   (default `./outputs/`). Templates are self-contained — the style function,
   figures, and section files travel with them.
3. **Customize.** Edit the main `.typ` (title, authors, sections). Each template's
   own `README.md` documents its file map and exactly what to replace.
4. **Compile.**
   ```bash
   bash scripts/compile.sh <path>/paper.typ --preview
   ```
   Runs `typst compile` (single pass — references, citations, and outline resolved
   automatically), writes the PDF, and renders one PNG per page.
5. **Deliver.** Read the PNG previews to confirm the result, show them to the user,
   and hand over the PDF.

## Templates

| Template | Produces | Build file |
|---|---|---|
| `neurips-paper` | Single-column NeurIPS/arXiv-style research paper (sample: *Attention Is All You Need*) | `templates/neurips-paper/paper.typ` |

Full details, variants, and "when to use each" → [references/templates.md](references/templates.md).

## Compiling

```bash
bash scripts/compile.sh FILE.typ [--preview] [--preview-dir DIR] [--dpi N] \
     [--root DIR] [--font-path DIR]
```

Typst has a single engine, so there's no engine flag and no multi-pass build.
`--root` sets the project root Typst may read files from (default: the file's
directory); `--font-path` adds a directory of custom fonts. Requires the `typst`
CLI, plus `poppler-utils` (`pdftoppm`) for previews. Run `scripts/compile.sh --help`
for the full list.

## Adding a template

This skill is a framework — new document types are added as template directories,
not by editing a monolith. The contract (required layout, quality rules, how to
register) is in [references/adding-templates.md](references/adding-templates.md).

## Conventions

- Write generated documents into `./outputs/` for user visibility; never edit a
  template in place — copy it first.
- Always render and view PNG previews after compiling, then show the user.
- Prefer **self-contained** templates: vendor the style as a local `.typ` function
  rather than depending on a `@preview` package that needs a network fetch.
- Escape Typst specials in user-supplied prose with a backslash: `#` `$` `@` `*`
  `_` `` ` `` `<` `>` `[` `]` and `\` itself (e.g. `C\#`, `20\% off`… note `%` is
  *not* special in Typst — only `//` starts a comment). Inside math (`$…$`),
  `_ ^ & #` are structural — enter literals as `\_`, `\^`, `\&`, `\#`.
