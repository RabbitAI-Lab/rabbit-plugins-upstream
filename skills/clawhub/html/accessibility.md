# Accessibility at the Markup Layer

Names, roles, states, focus, and the four different ways to hide something. Everything here is decided in HTML; contrast and motion are decided in CSS, and testing is `auditing.md`.

**Contents:** [The Accessible Name](#the-accessible-name) · [The Rules of ARIA](#the-rules-of-aria) · [ARIA That Is Usually Wrong](#aria-that-is-usually-wrong) · [Focus](#focus) · [The Four Ways to Hide](#the-four-ways-to-hide) · [Modality](#modality) · [Live Regions](#live-regions) · [Images and Non-Text Content](#images-and-non-text-content) · [Conformance Targets](#conformance-targets) · [Skip Links and Bypass](#skip-links-and-bypass) · [Reduced Motion and Zoom](#reduced-motion-and-zoom) · [Markup Review Pass](#markup-review-pass)

## The Accessible Name

Computed in strict precedence — the first one present wins, and the rest are never read:

1. `aria-labelledby` (concatenates the referenced elements' text, in the order listed)
2. `aria-label`
3. The native source for that element: `<label>` for form controls, `alt` for images, `<caption>` for tables, the button's own text content, `<legend>` for a fieldset, `<figcaption>` for a figure, `<summary>` for details
4. `title`
5. Nothing — the element is announced by role only ("button", "link")

Consequences worth memorizing:

- `aria-label` on a `<button>` **replaces** its visible text. A button reading "Delete" with `aria-label="Remove item 4"` is announced as the label; speech-input users saying "click Delete" then miss it. WCAG 2.5.3 requires the visible text to be contained in the accessible name — so `aria-label="Delete invoice 4821"` is fine, `aria-label="Remove"` is a failure.
- `aria-labelledby` may point at an element that is hidden with `display:none`, and it still works. Referencing a *missing* id yields an empty name and no warning.
- `aria-describedby` is additive, not a name: it is read after the name and role, for hints and error text.
- Naming only works on elements whose role supports it. `aria-label` on a `<div>`, `<span>`, or `<p>` with no role is ignored by the name computation.
- Only the *first* matching id is used when ids are duplicated (SKILL.md Rule 2).

## The Rules of ARIA

1. **Use a native element instead** whenever one exists with the semantics and behavior you need.
2. **Do not change native semantics** without cause. `<h2 role="tab">` is a real pattern; `<button role="link">` is a lie the keyboard then contradicts.
3. **Every ARIA control must be keyboard operable**, with the keys its pattern specifies — arrow keys for tabs, radios and menus; Escape to dismiss; Home/End where the pattern defines them.
4. **Never put `aria-hidden="true"` or `tabindex="-1"` on a focusable element.** A focusable element removed from the accessibility tree is a hole: the keyboard lands somewhere the screen reader cannot describe.
5. **Every interactive element has an accessible name.**

The blunt corollary: no ARIA is better than bad ARIA. An unlabeled `<button>` announces "button" and is still operable; a `<div role="button">` with no key handler is unreachable.

## ARIA That Is Usually Wrong

| Written | Problem |
|---|---|
| `role="button"` on `<button>` | Redundant; also a signal the author is reasoning about the wrong layer |
| `role="text"` | Erases the semantics of all children, including nested links |
| `aria-hidden="true"` on a focusable element | Rule 4 above |
| `aria-live` on a container that is added to the DOM at the same time as its message | Nothing is announced — the region must exist before the change |
| `aria-expanded` on the panel | It belongs on the **trigger**, describing the thing it controls |
| `aria-selected` on a link or list item outside a listbox/tab/grid | Only defined inside those patterns; use `aria-current` for "you are here" |
| `role="application"` | Suppresses the screen reader's browse mode for the whole subtree — almost never intended |
| `aria-required` alongside `required` | Duplicate; the native attribute already exposes the state |
| `title` as the only name | Not shown on touch, unreliably announced, invisible to keyboard users |
| `role="presentation"` on an element with focusable children | The children keep their semantics; the result is inconsistent |

`aria-current="page"` (also `step`, `location`, `date`, `time`, `true`) is the correct marker for the active item in navigation, breadcrumbs and pagination.

## Focus

- Natural DOM order is the tab order. Anything that reorders visually (CSS `order`, `grid-area`, absolute positioning) creates a mismatch between what is seen and what is tabbed — fix the DOM, not the tabindex.
- `tabindex="0"` puts a non-interactive element in the natural order; `tabindex="-1"` makes it programmatically focusable only (the target of "move focus here"). **Positive values are never right** — one `tabindex="1"` jumps ahead of the entire document.
- Never remove the focus indicator. If it clashes, restyle it; `:focus-visible` shows it for keyboard interaction only, which is what most people actually want.
- After a route change in a single-page app, focus does not move on its own. Move it to the new page's `<h1>` (with `tabindex="-1"`) and let the title change be announced.
- After deleting a row, move focus to the next row or to the list heading. Focus left on a removed element falls back to `<body>` and the user restarts from the top of the page.
- Focus order across a modal is handled by the top layer (`interactive.md`), not by a tabindex scheme.

## The Four Ways to Hide

| Technique | Visually | Screen reader | Focusable | Use for |
|---|---|---|---|---|
| `hidden` / `display:none` / `visibility:hidden` | Hidden | Hidden | No | Genuinely absent content |
| `aria-hidden="true"` | Visible | Hidden | **Yes** | Decorative visuals, duplicated text — never on anything focusable |
| Visually-hidden class (clip + 1px) | Hidden | Read | Yes | Skip links, labels for icon controls, extra context for link text |
| `inert` | Visible | Hidden | No | The rest of the page behind a modal or an off-canvas drawer |

`inert` is the one people miss: it removes an entire subtree from focus, hit-testing and the accessibility tree in one attribute, and `<dialog>.showModal()` applies it to the rest of the document automatically. Baseline since 2023.

A `hidden` attribute loses to any CSS `display` rule (SKILL.md Implicit Defaults) — `[hidden] { display: none !important; }` in the reset is the standard defense.

## Modality

- Use `<dialog>` + `showModal()` for anything modal: it provides the top layer, the `::backdrop`, Escape-to-close, focus containment and inertness of the rest of the page, with no JS beyond opening it (`interactive.md`).
- Focus moves into the dialog on open — to the first interactive element, or to the dialog's heading with `tabindex="-1"` when the first control is destructive.
- On close, focus **returns to the element that opened it**. `<dialog>` does this for you when it was opened from a real button; a custom implementation must store and restore it.
- Non-modal overlays (a dropdown, a toast) must not trap focus, must close on Escape, and must not be `aria-hidden` while visible.

## Live Regions

| Attribute | Behavior |
|---|---|
| `aria-live="polite"` | Announced at the next pause. The default choice for status, results counts, autosave |
| `aria-live="assertive"` | Interrupts immediately. Reserve for errors that stop the task |
| `role="status"` | Implicit polite + `aria-atomic="true"` |
| `role="alert"` | Implicit assertive |
| `aria-atomic="true"` | Read the whole region, not just the changed node — needed when the message is a sentence assembled from parts |
| `aria-busy="true"` | Suppress announcements while a region is being rebuilt, then set it false |

The two rules that make them work: the region must be **in the DOM before the message arrives**, and the message must be a **text change inside it**, not a replacement of the region itself. Empty region on load, then set its text content. Multiple live regions competing produce a queue nobody can follow — one polite region per page for status, plus `role="alert"` for genuine errors.

## Images and Non-Text Content

Decision table for `alt` (SKILL.md Rule 5 in full):

| The image | `alt` |
|---|---|
| Adds information not in the surrounding text | The information, in a sentence. Not "image of…" — the role is already announced |
| Is the only content of a link or button | The destination or action: `alt="Home"`, not `alt="logo"` |
| Repeats adjacent text (icon beside a label) | `alt=""` — announcing it twice is worse than not at all |
| Is decorative | `alt=""`, and `aria-hidden="true"` on inline SVG |
| Contains text | The same text, verbatim |
| Is a chart or diagram | One-sentence `alt` with the takeaway, plus the data in the page or a linked table |
| Is a CAPTCHA | Describe the purpose and provide a non-visual alternative |
| Is missing `alt` entirely | The file name is read out — never ship this |

`<figcaption>` is a caption, not a replacement for `alt`: the caption is read by everyone, the alt describes the picture to those who cannot see it. When they would be identical, `alt=""` and let the caption do the work.

## Conformance Targets

Gated by `a11y_target`. The markup-layer criteria that this skill can actually enforce:

| Criterion | AA | AAA |
|---|---|---|
| Text contrast (1.4.3 / 1.4.6) | 4.5:1 body, 3:1 for ≥24px or ≥18.66px bold | 7:1 body, 4.5:1 large |
| Non-text contrast (1.4.11) | 3:1 for control boundaries and meaningful graphics | — |
| Target size (2.5.8 / 2.5.5) | 24×24 CSS px, or spacing that yields it | 44×44 CSS px |
| Reflow (1.4.10) | No horizontal scroll at 320 CSS px width | — |
| Text spacing (1.4.12) | No loss of content at 1.5× line height, 0.12em letter, 0.16em word | — |
| Identify input purpose (1.3.5) | Correct `autocomplete` tokens (`forms.md`) | — |
| Focus not obscured (2.4.11) | Focused element not fully hidden by sticky headers | Not obscured at all (2.4.12) |
| Headings and labels (2.4.6) | Descriptive | — |
| Focus appearance (2.4.13) | — | Indicator ≥2px perimeter, 3:1 against adjacent colors |

Contrast values are computed in CSS; what this skill enforces is that the markup gives them something to attach to — real text instead of text baked into an image, a label instead of a placeholder, a button instead of a div.

## Skip Links and Bypass

```html
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header>…</header>
  <main id="main" tabindex="-1">…</main>
```

- First focusable element in the body. Visually hidden until focused, then visible — a permanently invisible skip link fails the criterion it exists to satisfy.
- The target needs `tabindex="-1"` in some browsers for focus (not just scroll) to move there.
- Multiple skip links are fine on a page with heavy navigation ("Skip to content", "Skip to search").
- Landmarks and a correct heading tree are the other two bypass mechanisms, and they serve more users than the skip link does (`semantics.md`).

## Reduced Motion and Zoom

- Autoplaying anything longer than 5 seconds needs a pause control (WCAG 2.2.2) — that includes carousels and looping background video (`media.md`).
- Never block zoom in the viewport tag (`head.md`).
- Content must survive 400% zoom without horizontal scrolling at 320px equivalent width; in markup terms that means no fixed-width containers and no layout that depends on a table for structure.

## Markup Review Pass

Run in this order — each step catches things the next one cannot:

1. **Tab through the page.** Everything interactive is reachable, the order matches the visual order, focus is always visible, nothing traps you, and nothing focusable is invisible.
2. **Read the heading tree** (an outline tool or the heading list of a screen reader). No skips, one `h1`, headings describe their sections.
3. **Read the landmark list.** One `main`, named `nav`s, no unnamed `section` regions.
4. **Check every control's name** in the accessibility inspector — not the visible text, the computed name.
5. **Check every image's alt** against the decision table.
6. **Trigger every error and every status message** with a screen reader on, and confirm each one is announced.
7. **Zoom to 400% and to 320px width.**

**After an accessibility pass**, append a row to `~/Clawic/data/html/audits/<year>.md`: date, scope, method (keyboard, screen reader and which, automated tool), issues by severity, what was fixed, what remains and why (`memory-template.md`). **When a pattern is finally announced correctly** — a combobox, an error summary, a live region that behaves — save it to `artifacts/pattern-<name>.md` with the screen reader and version it was verified on, and add its `## Boxes` line in the same turn. **How a specific screen reader announces a specific pattern** is a quirk, not a general fact: it belongs in `## Quirks` of `memory.md`, with the AT and browser version.
