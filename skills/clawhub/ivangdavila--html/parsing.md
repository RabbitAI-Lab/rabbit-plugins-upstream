# The Parser — Recovery, Nesting, Encoding, Quirks

HTML has no syntax errors: every document parses, and the parser's recovery rules decide what you actually get. When rendering disagrees with the source, the parser is the explanation.

**Contents:** [Quirks Mode](#quirks-mode) · [Foster Parenting](#foster-parenting) · [Auto-Closing](#auto-closing) · [Active Formatting Reconstruction](#active-formatting-reconstruction) · [Void and Self-Closing](#void-and-self-closing) · [Optional Tags](#optional-tags) · [Character References](#character-references) · [Whitespace](#whitespace) · [Attributes](#attributes) · [Raw Text Elements](#raw-text-elements) · [Reading the Parsed DOM](#reading-the-parsed-dom)

## Quirks Mode

| Mode | Triggered by | Effect |
|---|---|---|
| No-quirks (standards) | `<!DOCTYPE html>` as the first thing in the file | Correct box model and modern behavior |
| Limited-quirks (almost standards) | Certain legacy doctypes | Mostly correct; inline image layout in table cells differs |
| Quirks | Missing doctype, a malformed one, or anything before it | Legacy box model (`width` includes padding and border), `%` heights behave differently, and dozens of smaller divergences |

Anything before the doctype — a comment, a stray character, output from a template engine, a BOM followed by whitespace — pushes the document into quirks mode. Check with `document.compatMode`: `CSS1Compat` is standards, `BackCompat` is quirks. A page that "looks like the CSS is half applied" and has a doctype on line 2 is the classic case.

XML declarations (`<?xml …?>`) at the top of an HTML file are a parse error and force quirks mode — a common artifact of XHTML-era templates.

## Foster Parenting

Content that is not allowed inside a table's structure is moved **out of the table and inserted immediately before it**. This is spec behavior, not a bug:

```html
<table>
  Total:            <!-- rendered ABOVE the table -->
  <tr><td>1</td></tr>
</table>
```

- Legal children of `<table>`: `caption`, `colgroup`, `thead`, `tbody`, `tfoot`, `tr` (and `<script>`/`<template>`).
- Legal children of `<tr>`: `td`, `th` (and `<script>`/`<template>`).
- A `<div>`, a text node, or an un-cleared template loop directly inside `<table>` or `<tr>` is foster-parented.
- This is the reason `<template>` exists for un-rendered rows: template content is inert and escapes the rule (`templates.md`).
- Whitespace and comments are tolerated; visible text is not.

## Auto-Closing

Some elements close themselves when a disallowed element starts. The two that bite:

| Written | Parsed as |
|---|---|
| `<p>a<div>b</div>c</p>` | `<p>a</p><div>b</div>c<p></p>` — two paragraphs, one empty, and `c` orphaned |
| `<li>a<li>b` | Two list items — the closing tag is optional and the parser infers it |
| `<a>x<a>y</a></a>` | Un-nested: anchors cannot nest, so the second opens a sibling |
| `<form>` inside `<form>` | The inner one is dropped entirely |
| `<button><button>` | Un-nested the same way |

The general rule: an element whose content model forbids what comes next is closed for you. `<p>` is the one authors hit constantly, because it forbids all block content.

## Active Formatting Reconstruction

An unclosed inline formatting element (`<b>`, `<i>`, `<em>`, `<strong>`, `<a>`, `<span>` and friends) is **re-opened** by the parser inside subsequent block elements. That is why one missing `</em>` italicizes the rest of the page rather than just the rest of the paragraph:

```html
<p><em>Note</p><p>Next paragraph</p>   <!-- both paragraphs are emphasized -->
```

The same mechanism, applied to `<a>`, makes an entire page's content a link. When a formatting problem starts partway down a page and continues to the end, look for the last correctly-closed tag before it.

## Void and Self-Closing

The complete void element list — these never have a closing tag and never have children:

`area` · `base` · `br` · `col` · `embed` · `hr` · `img` · `input` · `link` · `meta` · `source` · `track` · `wbr`

- The trailing slash (`<br />`) is permitted and ignored in HTML. It is required in XML, JSX and most template languages, which is why `markup_flavor` decides which form is emitted.
- A trailing slash on a **non-void** element is ignored entirely: `<div />` opens a div that is never closed. This is the single most common bug when copying JSX into a `.html` file.
- Inline SVG and MathML are foreign content and *do* honor self-closing: `<circle />` inside `<svg>` is correct.

## Optional Tags

`</p>`, `</li>`, `</td>`, `</tr>`, `</th>`, `</thead>`, `</tbody>`, `</option>`, `<html>`, `<head>`, `<body>` and `<tbody>` may all be omitted, and the parser inserts them. Two consequences:

- `<tbody>` exists in the DOM whether you wrote it or not, so `table > tr` never matches (SKILL.md Implicit Defaults).
- Omitted tags are legal but not readable. Write them; the bytes are recovered by compression.

## Character References

- Mandatory in text: `&` → `&amp;`, `<` → `&lt;`. In attribute values also `"` (or `'`, depending on the quote used).
- **The ambiguous-ampersand rule**: in an *attribute value*, a named reference without a semicolon followed by `=` or an alphanumeric is left alone — which is why `href="?a=1&copy=2"` is safe. In *text content*, the same string decodes: `a=1&copy=2` renders `a=1©=2`. Same characters, different context, different result.
- `&nbsp;` is a real character (U+00A0), not a space: it does not collapse, it does not break lines, and it breaks naive string comparisons and search.
- Numeric references (`&#8203;`, `&#x200B;`) always require the semicolon.
- Do not escape non-ASCII text as entities; UTF-8 is the encoding and `é` is a character.

## Whitespace

- Runs of whitespace in normal flow collapse to one space, and the collapse happens at layout, not at parse — the DOM keeps every character.
- Whitespace between inline elements is rendered: the gap between `<li>` blocks styled `inline-block` is real text.
- `<pre>`, `<textarea>` and `<code>` inside `<pre>` preserve it exactly. Indenting a `<textarea>` in the source injects that indentation into the value — the parser drops only a single leading newline immediately after the tag.
- Leading/trailing whitespace inside `<button>` and `<a>` becomes part of the accessible name and shows in tooltips.

## Attributes

- Attribute names are case-insensitive in HTML and lower-cased in the DOM. In SVG and MathML they are case-**sensitive**: `viewBox`, `preserveAspectRatio`.
- Duplicate attributes: the **first** one wins, the rest are dropped silently.
- Boolean attributes are true by presence. `disabled="false"` is `disabled`. Remove the attribute to make it false.
- Unquoted values end at the first whitespace — always quote (`security.md`).
- Unknown attributes are kept in the DOM and are valid to read; use `data-*` for anything of your own so a future standard attribute does not collide.
- `data-*` values are strings, always, and appear in `dataset` as camelCase (`data-user-id` → `dataset.userId`).

## Raw Text Elements

`<script>` and `<style>` are raw text: nothing inside is parsed as markup **except** the literal string `</script>` / `</style>`, which ends the block wherever it appears — including inside a JS string or a comment. Escape it as `<\/script>` when it must appear in code (`security.md`). `<title>` and `<textarea>` are escapable raw text: character references work, tags do not.

## Reading the Parsed DOM

When the rendering does not match the source:

1. Look at the **elements panel** or `document.body.innerHTML` after load — that is the tree the browser built, not your file.
2. Diff it against the source mentally: inserted `<tbody>`, split `<p>`, content moved out of a table, an inline element re-opened.
3. Run the document through a conformance validator: it reports unclosed tags, illegal nesting, duplicate ids and bad attribute values, all of which the parser silently repaired (`auditing.md`).
4. If a template engine or CMS produced it, check the output, not the template — engines emit stray whitespace and unclosed tags of their own.

**When the parser or a CMS is found to rewrite markup in a specific way** — a template engine that swallows a closing tag, an editor that strips `loading` attributes, a build step that reorders the head — record it in `## Quirks` of `~/Clawic/data/html/memory.md` with the tool and version (`memory-template.md`). These are the facts that are impossible to re-derive and cost an hour each time. **A validation run** belongs in `~/Clawic/data/html/audits/<year>.md` alongside accessibility passes (`auditing.md`).
