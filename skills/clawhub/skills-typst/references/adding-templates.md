# Adding a Template

kirklin-typst grows by adding templates, not by editing one giant document. A
template is a self-contained directory a user can copy and compile on its own.

## Required layout

```
templates/<name>/
  <main>.typ          # the document — title, authors, body
  <style>.typ         # the style function it imports (keep styling out of the body)
  README.md           # what it produces, its file map, what to replace
  <assets…>           # any .bib, images, or #include section files it needs
```

## Quality rules

1. **Self-contained.** Bundle every dependency (style function, images, `.bib`,
   section files). A user who copies only `templates/<name>/` must be able to
   compile it with nothing else. **Prefer a local `.typ` style function over a
   `@preview` package** — a package needs a network fetch on first compile, which
   breaks offline/sandboxed builds. Vendor it instead.
2. **Compile-tested.** It must build cleanly through `scripts/compile.sh` with
   **zero** Typst errors (warnings tolerated, but read them and fix what you can).
3. **Real sample content.** Fill it with realistic content so the output looks like
   a finished document — not `#lorem(50)` placeholders or empty sections.
4. **Documented.** `README.md` gives the file map and names exactly what a user
   swaps to make it their own.
5. **Previewed.** Commit rendered PNGs (and the sample PDF) under `examples/<name>/`
   so the look is visible without compiling.

## Register it

1. Add a row to the `## Templates` table in [../SKILL.md](../SKILL.md).
2. Add a section to [templates.md](templates.md) with the standard shape:
   Produces / When to use / Build / Design / Adapt it / Preview.

## Typst notes

- **Fonts:** stick to fonts that ship with Typst (`New Computer Modern`,
  `Libertinus Serif`, `Times New Roman`, `STIX Two`) so the template renders the
  same everywhere. Check with `typst fonts`. If a template needs a bundled custom
  font, ship it in the template dir and document `--font-path`.
- **Bibliography:** Typst reads BibTeX `.bib` **and** Hayagriva `.yml` natively via
  `#bibliography(...)`. To match LaTeX's `plain` (full author names, numbered,
  alphabetical), `style: "association-for-computing-machinery"` is the closest
  bundled style; `"ieee"` gives initials + citation order instead.
- **References:** label with `<key>` and cite/reference with `@key` — resolved in the
  same single pass, no BibTeX round-trips.
- **Figures — use real images:** when recreating a real document, embed its actual
  figure files with `#figure(image("Figures/…"))` and bundle them in the template
  dir. Typst's `image()` takes PNG/JPG/GIF/SVG but **not PDF** — convert first
  (`pdftoppm -png in.pdf out`). Reserve native drawing (`rect`/`grid`/`line`) for
  genuinely simple schematics with no source image; a hand-drawn stand-in for a real
  figure reads as "not the same document".

## Prefer authentic sources

When recreating a known document (a paper, a report format, a publisher's style),
match the **real** layout (margins, fonts, rules) faithfully rather than eyeballing
an approximation. Keep the style in its own `.typ` so a user can retarget a different
venue by editing one function.

## Checklist

- [ ] `templates/<name>/` compiles via `scripts/compile.sh --preview`
- [ ] `README.md` explains the structure and what to replace
- [ ] `examples/<name>/` has PNG previews (and a sample PDF)
- [ ] Registered in `SKILL.md` and `references/templates.md`
