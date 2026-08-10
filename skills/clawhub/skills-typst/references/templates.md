# Template Catalog

The registry of available kirklin-typst templates. Match the user's request to a
template here, then follow the main workflow in [../SKILL.md](../SKILL.md).

---

## neurips-paper

- **Produces:** a single-column, NeurIPS/arXiv-style research paper — title with
  rules, a 4/3/1 multi-author block with `*`/`†`/`‡` footnotes, all numbered
  sections, display equations, four `booktabs`-style tables (including a complex
  Model Variations table with colspan/rowspan), **real figure images** (the
  architecture and attention diagrams, embedded via `image()`), numbered citations,
  a 40-entry `.bib` bibliography, and an attention-visualization appendix.
- **When to use:** academic / research papers, ML or CS conference submissions,
  preprints, or anything that should look like a published NeurIPS / arXiv paper.
- **Sample content:** recreates *Attention Is All You Need* (Vaswani et al., 2017),
  so the compiled output looks finished, not skeletal.
- **Build:**
  ```bash
  bash scripts/compile.sh templates/neurips-paper/paper.typ --preview \
       --preview-dir examples/neurips-paper
  ```
- **Design:**
  | File | Role | Notes |
  |---|---|---|
  | `paper.typ` (default) | The document | Sets title, authors, abstract; `#include`s section files |
  | `neurips.typ` | The style | A local `#neurips(...)` show-rule function — **no `@preview` fetch**, compiles offline |
- **Adapt it:** see `templates/neurips-paper/README.md` for the file map and exactly
  what to replace (title, `authors`, section `.typ` files, the figure, the `.bib`).
- **Preview:** rendered pages in `examples/neurips-paper/`.

---

<!-- Add new templates below in the same shape: Produces / When to use / Build /
     Design / Adapt it / Preview. Keep one H2 per template. -->
