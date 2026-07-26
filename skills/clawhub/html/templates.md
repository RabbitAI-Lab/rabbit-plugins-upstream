# Templates, Slots, and Web Components

The markup side of components: what `<template>` actually does, what crossing the shadow boundary costs, and why a component can render as an empty box.

**Contents:** [`template`](#template) · [Custom Elements in Markup](#custom-elements-in-markup) · [Shadow DOM and What It Blocks](#shadow-dom-and-what-it-blocks) · [Slots](#slots) · [Declarative Shadow DOM](#declarative-shadow-dom) · [Forms Across the Boundary](#forms-across-the-boundary) · [Accessibility Across the Boundary](#accessibility-across-the-boundary) · [Server-Rendered Markup](#server-rendered-markup) · [When Not to Use a Component](#when-not-to-use-a-component)

## `template`

```html
<template id="row">
  <tr><th scope="row"></th><td></td></tr>
</template>
```

- Content is parsed but **inert**: not rendered, scripts do not run, images and media do not load, and `document.querySelector` does not see inside it. That inertness is the feature — it is the only way to keep an unrendered `<tr>` outside a table without the parser foster-parenting it (`parsing.md`).
- Clone with `content.cloneNode(true)` per instance. Reusing the same nodes moves them instead of copying.
- Ids inside a template become duplicates the moment it is cloned twice. Use classes and `data-*` inside templates, and assign unique ids at clone time when a `for`/`aria-*` reference needs one (SKILL.md Rule 2).
- `<template>` is also the standard placeholder for repeating form rows: put the index into the `name` at clone time (`forms.md`).
- `<slot>` outside a shadow root does nothing.

## Custom Elements in Markup

- The name **must contain a hyphen** (`user-card`, not `usercard`) — that is what marks it as custom and guarantees no future standard element collides with it.
- Before its definition is registered, the element is an unknown inline element with no styling and no behavior. Two consequences: unstyled flash, and a page that shows nothing where the component should be if the script fails to load.
- `:defined` / `:not(:defined)` in CSS is the hook for placeholder styling; hiding undefined elements entirely trades a flash for a blank.
- Autonomous custom elements (`<user-card>`) are supported everywhere; customized built-ins (`<button is="fancy-button">`) are not implemented in WebKit — do not rely on `is=`.
- Attributes are the public API: string in, parsed inside. Complex data goes through properties, which means it cannot be expressed in server-rendered HTML — a real constraint on which components can be SSR'd.
- A custom element with no explicit role has none. `<user-card>` announces nothing; give it a role or wrap real elements inside it.

## Shadow DOM and What It Blocks

| Crosses the boundary | Does not cross |
|---|---|
| Inherited CSS properties (`color`, `font`, custom properties) | Outside selectors matching inside nodes, and vice versa |
| CSS custom properties — the intended theming channel | Global stylesheets, resets, utility classes |
| `::part()` and `::slotted()`, the deliberate openings | Arbitrary styling of internals |
| Composed events (most UI events, retargeted to the host) | `document.querySelector` reaching inside an open shadow root without `.shadowRoot` |
| Focus (it goes in) | Simple `label[for]`, `aria-labelledby`, and `aria-controls` id references |
| Form submission via form-associated custom elements | Plain inputs inside a shadow root, which are not submitted with the outer form |

`mode: "open"` exposes `.shadowRoot`; `mode: "closed"` hides it from your own code too and stops most testing tools — rarely worth it.

## Slots

```html
<user-card>
  <span slot="name">Ada</span>
  <p>Default-slot content.</p>
</user-card>
```

- Slotted content stays in the **light DOM**: it is styled by the page's stylesheets, appears in the page's DOM, and is visible to search engines and to code that never learned about the component.
- Fallback content between `<slot>` tags shows only when nothing is assigned.
- One default (unnamed) slot; any number of named ones. Content with a `slot` name that does not exist in the template is never rendered — a silent failure that reads as "the component ignores my markup".
- Slot assignment ignores DOM position: markup order in the light DOM does not have to match the rendered order, which can desynchronize the visual order from the tab order (`accessibility.md`).

## Declarative Shadow DOM

```html
<user-card>
  <template shadowrootmode="open">
    <style>:host { display: block }</style>
    <slot name="name"></slot>
  </template>
  <span slot="name">Ada</span>
</user-card>
```

- Lets the server ship a shadow root with no JS, which removes the blank-until-hydration window for content components. Baseline 2024.
- The `<template shadowrootmode>` is consumed by the parser: it only works in HTML parsed as a document, not in `innerHTML` unless the API is opted into explicitly.
- The element still upgrades when its definition loads; the declarative root is the pre-render, not a replacement for the class.
- Under `browser_support: legacy` this is not available, and a content component that needs SSR should be plain markup instead.

## Forms Across the Boundary

- An `<input>` inside a shadow root is **not** submitted with an ancestor `<form>`. Either keep form controls in the light DOM (via slots) or make the component form-associated (`static formAssociated = true` plus `ElementInternals`).
- Form-associated custom elements can set value, validity, and a validation message that participates in constraint validation — the only way a component behaves like a real control.
- `<label for>` cannot reach a control inside a shadow root. Either the label lives inside the same root, or the component exposes its own labeling via `ElementInternals`.

## Accessibility Across the Boundary

- `aria-labelledby` and `aria-describedby` are **id references and do not cross shadow boundaries**. A label in the light DOM cannot name an element inside a shadow root by id.
- Workarounds, in order: put the name inside the same root; copy the text into `aria-label` on the internal element; or set the role and name through `ElementInternals` (`this.internals_.role`, `.ariaLabel`).
- Focus order inside a shadow root follows its own DOM order and is spliced into the document order at the host — so a component that renders its slots out of order produces a tab sequence that does not match the screen.
- `delegatesFocus: true` on the shadow root sends focus on the host to the first focusable internal element, which fixes the common "clicking the component focuses nothing" bug.

## Server-Rendered Markup

- Markup that only becomes interactive after hydration is markup that is broken for the first seconds of every visit and forever if the bundle fails. Render real links and real buttons inside `<form>`s so the pre-hydration document still works.
- Hydration mismatches come from markup the parser rewrote and the framework did not expect: an implicit `<tbody>`, a `<p>` auto-closed by a block child, whitespace inside `<pre>` and `<textarea>` (`parsing.md`).
- `<template>` is how frameworks ship un-rendered markup; leaving instance-specific ids inside is the recurring hydration bug.
- Streaming and out-of-order rendering rely on the parser tolerating incomplete documents — which it does; unclosed elements are recovered, not fatal.

## When Not to Use a Component

| Situation | Better |
|---|---|
| One page, one use | Plain markup |
| Content that must be indexed and shared | Plain markup or light-DOM slots |
| A styled wrapper around a native control | CSS on the native control |
| Something that only exists to hold a class name | A `<div>` |
| A design-system primitive used in three frameworks | A web component genuinely wins here |

**When a component's markup contract is settled** — what attributes it takes, which slots exist, what it exposes through `::part()` and custom properties, how it is labeled — save it to `~/Clawic/data/html/artifacts/component-<name>.md` and add its `## Boxes` line in the same turn (`memory-template.md`). This is the file that answers "why is the name set through `ElementInternals` here" six months later. **A shadow-boundary limitation discovered the hard way** (a label that cannot reach, a form that submits nothing) is a row in `## Quirks` of `memory.md`, with the browser version it was seen on.
