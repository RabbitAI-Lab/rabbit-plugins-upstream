// neurips.typ — a self-contained NeurIPS 2017-style paper style.
//
// No @preview package: the styling is this single function, so the template
// compiles offline with nothing to fetch. It targets the look of the real
// `nips_2017.sty`: Times body + Times-compatible math, a heavy rule / thin rule
// title, bold author names with symbol footnotes (* † ‡), a page-1 venue line,
// and page numbers thereafter. Apply it with a show rule:
//
//   #import "neurips.typ": neurips
//   #show: neurips.with(title: "...", authors: (...), abstract: [...])
//
// authors: an array of dictionaries with keys `name`, `affiliation`, `email`,
// and an optional `note` (its own extra footnote). An empty affiliation is
// skipped. Every author shares the equal-contribution mark (*).

#let neurips(
  title: "Title",
  authors: (),
  abstract: [],
  equal-contribution: [Equal contribution.],
  venue: none,
  authors-per-row: 4,
  body,
) = {
  set document(title: title, author: authors.map(a => a.name))

  set page(
    paper: "us-letter",
    margin: (x: 1.5in, top: 1in, bottom: 1in),  // -> 5.5in x 9in text block
    footer: context {
      let p = here().page()
      set align(center)
      if p == 1 {
        if venue != none { text(size: 9pt, venue) }
      } else {
        text(size: 10pt)[#p]
      }
    },
  )

  set text(font: "Times New Roman", size: 10pt)
  show math.equation: set text(font: "STIX Two Math")
  set par(
    justify: true,
    leading: 0.62em,
    spacing: 0.62em,
    first-line-indent: (amount: 1em, all: false),
  )

  // symbol footnotes (* † ‡ §), small text — as in NeurIPS
  set footnote(numbering: "*")
  show footnote.entry: set text(size: 8pt)

  // numbered, bold headings sized by level
  set heading(numbering: "1.1")
  show heading: it => {
    set text(size: (12pt, 11pt, 10pt).at(calc.min(it.level, 3) - 1), weight: "bold")
    set block(above: 1.15em, below: 0.6em)
    it
  }

  // booktabs-ish tables; table captions above, figure captions below
  set table(stroke: none)
  show figure.where(kind: table): set figure.caption(position: top)
  show figure.caption: set text(size: 9pt)
  show link: set text(fill: rgb("#1a0dab"))

  // ---- title, framed by a heavy rule above and a thin rule below ----
  line(length: 100%, stroke: 4pt)
  v(5pt)
  align(center, text(size: 17pt, weight: "bold", title))
  v(6pt)
  line(length: 100%, stroke: 0.4pt)
  v(0.45in)

  // ---- authors, chunked into centered rows ----
  let cell(a, idx) = align(center, {
    set par(justify: false, leading: 0.5em)
    set text(size: 10pt)
    [
      #strong(a.name)#if idx == 0 [#footnote(equal-contribution)<nips-eq>] else [#footnote(<nips-eq>)]#if a.at("note", default: none) != none [#footnote(a.note)] \
      #if a.affiliation != "" [#a.affiliation \ ]
      #text(size: 9pt, raw(a.email))
    ]
  })
  // authors-per-row: an int (uniform) OR an array of per-row counts, e.g. (4, 3, 1)
  let row-sizes = if type(authors-per-row) == array {
    authors-per-row
  } else {
    let n = calc.max(authors-per-row, 1)
    range(0, authors.len(), step: n).map(_ => n)
  }
  let rows = ()
  let start = 0
  for size in row-sizes {
    if start >= authors.len() { break }
    let stop = calc.min(start + size, authors.len())
    rows.push(range(start, stop))
    start = stop
  }
  if start < authors.len() { rows.push(range(start, authors.len())) }
  for r in rows {
    align(center, grid(
      columns: (auto,) * r.len(),
      column-gutter: 2.4em,
      ..r.map(idx => cell(authors.at(idx), idx)),
    ))
    v(0.95em)
  }
  v(0.28in)

  // ---- abstract ----
  align(center, text(size: 12pt, weight: "bold")[Abstract])
  v(0.15em)
  pad(x: 0.5in, text(size: 10pt, abstract))
  v(0.34in)

  // ---- body ----
  body
}
