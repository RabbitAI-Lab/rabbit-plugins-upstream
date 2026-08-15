# Native Interactive Elements — and the Patterns With No Element

The decision is always the same: does the platform already ship this behavior? If it does, taking it costs one element; building it costs a keyboard contract you maintain forever.

**Contents:** [`dialog`](#dialog) · [Popover](#popover) · [`details` and `summary`](#details-and-summary) · [Native Widgets](#native-widgets) · [Patterns With No Element](#patterns-with-no-element) · [Keyboard Contracts](#keyboard-contracts) · [Escape Hatches and Support](#escape-hatches-and-support) · [Contenteditable and Drag](#contenteditable-and-drag)

## `dialog`

```html
<dialog id="confirm">
  <form method="dialog">
    <h2>Delete invoice 4821?</h2>
    <p>This cannot be undone.</p>
    <button value="cancel">Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>
```

| Behavior | `showModal()` | `show()` / `open` attribute |
|---|---|---|
| Top layer, above every `z-index` | Yes | No |
| `::backdrop` | Yes | No |
| Rest of the document inert | Yes | No |
| Escape closes it | Yes | No |
| Focus moved in on open, restored on close | Yes | Partially |

- **Use `showModal()` for anything modal.** `show()` and the `open` attribute produce a non-modal panel that looks right and behaves wrong — the most common `<dialog>` bug.
- `<form method="dialog">` closes the dialog on submit without navigating, and sets `returnValue` to the activated button's `value`. No JS at all for a confirm dialog.
- Give the dialog an accessible name: `aria-labelledby` pointing at its heading. `role="dialog"` is implicit; do not add it.
- Autofocus lands on the first focusable element. When the first control is destructive, put `autofocus` on the safe one, or focus the heading with `tabindex="-1"`.
- Closing on backdrop click is not built in: compare `event.target` to the dialog element. Do not add it to destructive dialogs.
- Scroll lock behind the dialog is CSS (`overflow: hidden` on the root while open); the top layer does not stop the page scrolling.
- Baseline across browsers since March 2022.

## Popover

The attribute API for transient, non-modal surfaces — menus, tooltips, disclosure cards, notification panels:

```html
<button popovertarget="menu">Options</button>
<div id="menu" popover>…</div>
```

- Gets the top layer and light-dismiss (Escape, click outside) with no JS. `popover="manual"` opts out of light dismiss; `popover="hint"` allows a second, nested layer for tooltips.
- Does **not** trap focus and does not make the page inert — which is correct for menus and wrong for modals. Anything modal is `<dialog>`.
- Anchor positioning is a separate CSS feature and is not universally available yet; until it is, position with the existing layout or a positioning library.
- A popover is not automatically a menu: a real menu still needs arrow-key navigation and the right roles.
- Baseline 2024. Under `browser_support: legacy`, use a disclosure pattern with `aria-expanded` and your own outside-click handling instead.

## `details` and `summary`

```html
<details name="faq">
  <summary>How do refunds work?</summary>
  <p>…</p>
</details>
```

- Free: keyboard operability, `aria-expanded` state, and browser find-in-page that opens the panel to reveal a match — none of which a JS accordion gets for nothing.
- `name` on several `<details>` makes them an exclusive accordion (one open at a time) with no JS. Widely available since 2024.
- `open` attribute sets the initial state; print styles usually want everything open.
- `<summary>` must be the first child, and it may contain a heading: `<summary><h3>…</h3></summary>` keeps the outline intact.
- Animating the height requires CSS interpolation of `content-visibility`/`height` — historically the reason people rebuilt it in JS. Under `browser_support: legacy`, a JS disclosure with `aria-expanded` and `hidden` on the panel is the fallback.
- Do not use `<details>` for content that must be findable by search engines' rendering of visible text if the crawler's behavior matters — content inside is in the DOM, but the collapsed state affects some snippet extraction.

## Native Widgets

| Element | What it buys | Trap |
|---|---|---|
| `<select>` | Full keyboard, platform picker, type-ahead | Options cannot be styled beyond very limited properties; do not rebuild it for aesthetics without accepting the listbox contract |
| `<datalist>` | Suggestions on a free-text input | Rendering is browser-controlled; no async source, no custom rows |
| `<progress value max>` | Determinate progress with a native announced value | Omit `value` for indeterminate |
| `<meter value min max low high optimum>` | A gauge with a *known* range — disk usage, score | Not a progress bar; the semantics differ and so does the announcement |
| `<output>` | Live-region-by-default result of a calculation | `for` lists the ids of the inputs it derives from |
| `<input type="range">` | Slider with full keyboard | Needs a visible value; the thumb position is not readable |
| `<input type="date">` etc. | Native picker and validation | ISO value regardless of display locale (`forms.md`) |
| `<fieldset disabled>` | Disables every control inside at once | Also omits them all from submission (`forms.md`) |

## Patterns With No Element

Everything below requires ARIA plus a keyboard implementation. Follow the ARIA Authoring Practices pattern exactly — a half-implemented pattern is worse than a plain list of links.

| Pattern | Roles | Keyboard you must implement |
|---|---|---|
| Tabs | `tablist` / `tab` / `tabpanel`, `aria-selected`, `aria-controls` | Arrows between tabs, Home/End, one tab stop for the whole list (roving `tabindex`) |
| Combobox / autocomplete | `combobox` + `listbox` + `option`, `aria-expanded`, `aria-activedescendant` | Down opens, arrows move, Enter selects, Escape closes and restores |
| Menu / menubar | `menu` / `menuitem` | Arrows, Home/End, type-ahead, Escape. Only for application menus — a nav list of links is not a menu |
| Tree | `tree` / `treeitem`, `aria-expanded`, `aria-level` | Arrows including left/right to collapse/expand |
| Data grid | `grid` / `row` / `gridcell` | Arrow navigation across cells, one tab stop for the grid |
| Carousel | `region` + `group` per slide | Previous/next buttons, pause control, live region announcing position |
| Toast / notification | `role="status"` or `role="alert"` | Must not steal focus; must be reachable afterwards (`accessibility.md`) |
| Tooltip | `role="tooltip"` + `aria-describedby` | Shows on hover **and** focus, dismissible with Escape, does not disappear while the pointer moves toward it (WCAG 1.4.13) |
| Drag and drop reordering | — | Always provide a keyboard alternative: move up/down buttons, or cut/paste semantics |

Cost estimate before choosing: a correct combobox is roughly 200 lines of JS plus tests, and it is re-broken by every framework upgrade. A `<datalist>` is one element. Choose the pattern only when the product genuinely needs what it adds.

## Keyboard Contracts

The keys users expect, independent of framework:

| Key | Expectation |
|---|---|
| Tab / Shift+Tab | Move between *components*, not within them |
| Arrows | Move within a composite widget (tabs, radios, menu, grid) |
| Space | Activate a button, toggle a checkbox, scroll the page when nothing is focused |
| Enter | Activate a link or button, submit a form from a text field |
| Escape | Close the topmost dismissible thing, cancel an edit |
| Home / End | First and last item within a widget |

Radio groups already implement roving focus natively — one tab stop, arrows to change. That is the model to copy for any custom composite.

## Escape Hatches and Support

Under `browser_support`:

| Feature | `evergreen` | `widely-available` | `legacy` |
|---|---|---|---|
| `<dialog>` | Ship it | Ship it | Ship it (baseline 2022) |
| Popover API | Ship it | Ship it with a fallback path | Disclosure pattern instead |
| `<details name>` exclusive accordion | Ship it | Ship it; degrades to independent panels | Independent panels |
| Declarative shadow DOM | Ship it | Behind a check (`templates.md`) | Avoid |
| `inert` | Ship it | Ship it (baseline 2023) | Manual focus containment |

Degradation matters more than presence: `<details name>` in an unsupporting browser gives independent accordions, which is a harmless downgrade. A popover in an unsupporting browser is an always-visible div, which is not.

## Contenteditable and Drag

- `contenteditable` produces browser-specific markup on paste and Enter; anything beyond a single-line field needs a real editor library and a documented sanitizing step on save (`security.md`).
- `contenteditable="plaintext-only"` avoids most of it when rich text is not required.
- A contenteditable region needs `role="textbox"`, `aria-multiline`, and an accessible name — none are implicit.
- `draggable="true"` gives mouse drag and no keyboard path at all; the keyboard alternative is not optional.
- `spellcheck="false"` on codes, names, and identifiers; `autocapitalize="none"` and `autocorrect="off"` on usernames and anything case-sensitive on mobile.

**When an interactive pattern is finally correct** — a dialog with its focus restoration, a combobox verified against a screen reader, a popover fallback for `browser_support: legacy` — save it to `~/Clawic/data/html/artifacts/pattern-<name>.md` with the keyboard contract it implements and the AT it was tested on, and add its `## Boxes` line in the same turn (`memory-template.md`). **When a decision is made between a native element and a library**, that is an artifact too: record what was rejected and why, or it is re-argued next quarter.
