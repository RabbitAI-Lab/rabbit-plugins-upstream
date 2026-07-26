# Data Tables

A table is a two-dimensional relationship. If the content has no rows and columns that mean something together, it is not a table — it is a list, a definition list, or a layout (which is CSS, except in email).

**Contents:** [The Baseline](#the-baseline) · [Headers](#headers) · [Complex Tables](#complex-tables) · [Caption vs Heading](#caption-vs-heading) · [Structural Elements](#structural-elements) · [Sorting and Interaction](#sorting-and-interaction) · [Responsive Tables](#responsive-tables) · [When Not a Table](#when-not-a-table)

## The Baseline

```html
<table>
  <caption>Q3 revenue by region</caption>
  <thead>
    <tr><th scope="col">Region</th><th scope="col">Revenue</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">EMEA</th><td>1,204,000 USD</td></tr>
  </tbody>
</table>
```

Five things this gets right: a caption, `<th>` for headers instead of styled `<td>`, `scope` on every header, a row header so each cell has both coordinates, and units inside the cell text rather than only in the header.

## Headers

- `<th>` is a header cell; `<td>` is data. A bold `<td>` is a data cell that looks like a header and is announced as data.
- `scope="col"` on column headers, `scope="row"` on row headers. Without `scope`, browsers guess from position, and the guess fails as soon as the table has both.
- `scope="colgroup"` / `scope="rowgroup"` for a header spanning a group of columns or rows.
- A row header is what makes a cell self-describing: screen readers announce "EMEA, Revenue, 1,204,000 USD" when moving cell to cell. Without one, the user hears only the number.
- `abbr` on a `<th>` supplies a short form announced in each cell for long headers.

## Complex Tables

When headers span, nest, or sit in more than one dimension, `scope` stops being sufficient. Then, and only then, use `headers`/`id`:

```html
<th id="q3">Q3</th><th id="q3-rev" headers="q3">Revenue</th>
…
<td headers="q3 q3-rev emea">1,204,000 USD</td>
```

- Every data cell lists every header id that applies, space-separated, in the order they should be read.
- It is verbose and easy to break; the maintenance cost is the argument for splitting a complex table into several simple ones, which is almost always better for sighted users too.
- Never mix `scope` and `headers` in one table — support for the combination is inconsistent.
- Two-level column headers with no `headers` attributes are the single most common inaccessible table on the web.

## Caption vs Heading

- `<caption>` is the table's accessible name, must be the **first child** of `<table>`, and is announced when the user enters the table. It is what makes a page with six tables navigable.
- A `<h3>` above the table is read in document order but is not connected to the table; assistive tech does not announce it on entry. Use both when the visual design needs a heading, or style the caption to look like one.
- `aria-labelledby` on the table pointing at a heading is the fallback when the CMS cannot emit a caption.
- Summarize the structure of a complex table in a sentence before it (or in `<caption>`), not in the obsolete `summary` attribute.

## Structural Elements

| Element | Purpose |
|---|---|
| `<thead>` / `<tbody>` / `<tfoot>` | Row grouping. Browsers repeat `<thead>` across printed pages, and it is the hook for a sticky header |
| `<tbody>` | Inserted by the parser whether you write it or not (SKILL.md Implicit Defaults) — write it, so your selectors match your source |
| `<tfoot>` | Totals; may be written before or after `<tbody>` in the source and renders last either way |
| `<colgroup>` / `<col>` | Column-level styling hooks (`width`, `span`); the only styling that reaches a whole column without touching every cell |
| `rowspan` / `colspan` | Legitimate; each spanning cell still needs correct header association |

`<tfoot>` totals should also carry a row header ("Total") so the number is not announced bare.

## Sorting and Interaction

- The header of a sortable column contains a `<button>`; the `<th>` carries `aria-sort="ascending" | "descending" | "none"` — exactly one column at a time.
- Announce the result of sorting in a polite live region ("Sorted by Revenue, descending, 24 rows") — the visual arrow is invisible to a screen-reader user.
- Selectable rows: a real `<input type="checkbox">` in the first cell with an accessible name identifying the row ("Select EMEA"), not an unlabeled box in every row.
- Editable cells or virtualized rows leave the table pattern and enter `role="grid"` — a full keyboard contract with arrow navigation. Do not adopt it halfway; a `role="grid"` without arrow-key handling is worse than a plain table (`interactive.md`).
- Pagination controls belong outside the table, in a `<nav aria-label="Table pagination">`.

## Responsive Tables

Narrow screens and real tables conflict. In order of preference:

1. **Horizontal scroll with a focusable container.** `<div role="region" aria-label="Q3 revenue" tabindex="0">` around the table: keyboard users can scroll it, and it stays a table. The `tabindex="0"` is what makes it operable — a scrollable region that cannot receive focus is a WCAG failure.
2. **Fewer columns on small screens.** Hide genuinely secondary columns with CSS and expose them in a per-row disclosure.
3. **Stacked cards, one per row.** Restyled with CSS while the markup stays a table; header text is repeated via `::before` and `content` from a `data-*` attribute. Fragile, and the repeated header text is not announced — acceptable for simple two-column data only.
4. Never rebuild the table as `<div>`s with ARIA table roles to make it responsive: you inherit the entire contract and lose the browser's own table navigation.

## When Not a Table

| Content | Use instead |
|---|---|
| Key/value metadata, spec sheets | `<dl>` (`semantics.md`) |
| A list of items with the same fields | A list of cards, or a table only if the columns are compared across rows |
| Page layout | CSS grid or flex — except in HTML email, where tables are the layout engine (`email.md`) |
| Code with line numbers | `<pre><code>` with CSS counters; a table breaks copy-paste |
| A calendar grid | A table is correct: days are a two-dimensional relationship |

**When a complex table's header association is finally correct** — a two-level header with its `headers`/`id` map, or a responsive pattern that survives a screen reader — save it to `~/Clawic/data/html/artifacts/table-<name>.md` with the reason the structure is shaped that way, and add its `## Boxes` line in the same turn (`memory-template.md`). These get rebuilt from scratch every time the report changes, and the association is what gets lost.
