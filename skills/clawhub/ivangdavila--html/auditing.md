# Auditing — Is This Page Actually Correct?

Conformance, accessibility and rendering are three separate questions with three different methods. Automated tools answer the smallest of them.

**Contents:** [What Each Check Catches](#what-each-check-catches) · [Conformance Validation](#conformance-validation) · [Errors Worth Fixing](#errors-worth-fixing) · [Automated Accessibility Testing](#automated-accessibility-testing) · [The Manual Pass](#the-manual-pass) · [Screen Reader Combinations](#screen-reader-combinations) · [Rendering and Client Testing](#rendering-and-client-testing) · [Gates in CI](#gates-in-ci) · [Cadence](#cadence) · [Recording the Result](#recording-the-result)

**Before an audit**, read `## Pages` and `## Quirks` in `~/Clawic/data/html/memory.md` and the last entries of `~/Clawic/data/html/audits/<year>.md`. Re-reporting an issue that was accepted with a reason, or re-discovering a client quirk already recorded, is what makes audits get ignored.

## What Each Check Catches

| Method | Catches | Blind to |
|---|---|---|
| Conformance validator | Unclosed tags, illegal nesting, duplicate ids, invalid attribute values, missing required attributes | Whether the markup means the right thing |
| Automated a11y scanner | Missing names, contrast, missing lang, ARIA misuse — roughly 30–40% of real WCAG failures | Focus order, keyboard traps, whether the name is *accurate*, whether the reading order makes sense, live-region timing |
| Keyboard pass | Traps, unreachable controls, invisible focus, order mismatches | Announcement quality |
| Screen reader pass | Names, roles, states, announcement order, live regions | Nothing else finds these |
| Visual/client screenshots | Layout breakage per browser or email client | Semantics |
| Field metrics | Real LCP, CLS, INP at the 75th percentile | Causes |

The number that matters: automated tools find well under half of WCAG failures. A green axe run is a floor, never a pass.

## Conformance Validation

- The W3C Nu validator (`validator.w3.org/nu`, also runnable locally) is the reference implementation. `html-validate` and similar linters are the CI-friendly equivalents with configurable rules.
- Validate the **rendered output**, not the template: engines and CMSes emit their own unclosed tags and reordered head elements (`parsing.md`).
- For a JS-rendered app, validate the hydrated DOM as well as the served HTML — they differ, and only one of them is what users get.
- Validators do not know your framework: custom elements are accepted, but framework-specific attributes may report as errors. Configure the allowlist once rather than ignoring the whole tool.

## Errors Worth Fixing

Not every validator message has the same weight:

| Priority | Message class | Why |
|---|---|---|
| Fix now | Duplicate id | Breaks `for`, `aria-*`, and fragment links silently (SKILL.md Rule 2) |
| Fix now | Unclosed or mis-nested element | The parser's repair changes the DOM (`parsing.md`) |
| Fix now | Missing `alt`, missing `lang`, missing `<title>` | Direct accessibility failures |
| Fix now | Illegal content model (block inside `<p>`, loose content in a table) | Silent restructuring |
| Fix now | Stray content before the doctype | Quirks mode |
| Fix | Invalid attribute value, obsolete element or attribute | Works today, breaks on a parser change |
| Fix | Missing required attribute on a form control (`name`, `type`) | Behavior bugs, not style |
| Judgment | Framework-specific attributes flagged as unknown | Configure the linter |
| Judgment | Trailing slashes on void elements | Harmless in HTML; required in JSX (`markup_flavor`) |

## Automated Accessibility Testing

- Run the scanner on a **fully rendered, interacted** page: open every dialog, expand every accordion, trigger every error state. A scanner on the initial paint audits an empty shell.
- Rules to never suppress without a written reason: name-role-value, contrast, valid ARIA attribute values, focus-order-semantics, duplicate ids, form labels.
- False positives exist (contrast on text over an image, ARIA that is deliberately non-standard). Every suppression carries a comment with the reason and the date — otherwise the next person deletes it or trusts it.
- Contrast checks measure computed CSS; text baked into an image is invisible to them.

## The Manual Pass

The full sequence, in the order that catches the most per minute:

1. **Unplug the mouse.** Tab through: everything interactive reachable, order matches the visual layout, focus always visible, no trap, nothing focusable hidden.
2. **Escape and arrow keys** on every widget: dialogs close, menus and tabs move by arrow, nothing swallows Escape.
3. **Heading list and landmark list** from a screen reader or an outline tool.
4. **Accessible name of every control** in the accessibility inspector — the computed name, not the visible text.
5. **Every error and status message** with a screen reader on.
6. **400% zoom, and a 320px-wide viewport**: no horizontal scroll, no clipped content, nothing obscured by sticky headers.
7. **Disable JS** and reload: what still works? Links, forms with an `action`, and content should survive.
8. **Disable images** and reload: the alt text is now the page — does it read?
9. **Forced-colors / high-contrast mode**: borders and icons that were conveyed only by background color disappear.

## Screen Reader Combinations

Assistive tech behavior is a function of the *pair*, not the reader alone. The floor set:

| Reader | Browser | Platform |
|---|---|---|
| NVDA | Firefox or Chrome | Windows — the most common combination in surveys |
| VoiceOver | Safari | macOS and iOS |
| TalkBack | Chrome | Android |
| JAWS | Chrome | Windows, enterprise |

Test the pattern, not the page: one dialog, one combobox, one error summary, one live region. A behavior verified on one pair goes into `## Quirks` with the pair named — "VoiceOver announces X" is not a general fact.

## Rendering and Client Testing

- Browsers: current Chromium, Firefox and WebKit is the floor; add whatever `browser_support` demands. WebKit is the one that surprises, and iOS Safari is the only WebKit that matters for touch.
- Email is a different discipline entirely: screenshots across the client set, because the differences are not derivable (`email.md`).
- Embedded webviews (in-app browsers in social apps) lag the standalone browser and are where "implicit noopener" and modern features are missing.
- Print: `@media print` output, `<thead>` repetition, and whether `<details>` panels are open.

## Gates in CI

Cheap, deterministic, and worth wiring before any manual process:

- HTML conformance on the rendered output of a representative page set — fail on the "fix now" classes above.
- Automated accessibility scan on the same set, failing on the never-suppress rules.
- A link check for `href="#id"` fragments and internal URLs.
- Uniqueness check for `id` attributes per document.
- Lighthouse or equivalent with a budget, run against a fixed environment — treat it as a trend, not a gate, because scores move with network conditions.

## Cadence

| Check | Every |
|---|---|
| Conformance + automated a11y in CI | Per commit |
| Manual keyboard pass on changed pages | Per release |
| Full screen-reader pass on the pattern library | Quarter |
| Email client screenshot set | Quarter, and after any client's major update |
| Third-party embed review (what it loads, what it requests) | Quarter |
| Field metrics review (LCP/CLS/INP at p75) | Month |

Whichever of these the user accepts becomes a row in `## Due` of `memory.md`, with its last-run and next-due dates.

## Recording the Result

**Every audit pass writes a row to `~/Clawic/data/html/audits/<year>.md`** in the same turn: date, scope (which pages or which pattern), method (tool and version, or the AT/browser pair), issues found by severity, what was fixed, what remains and the reason it was accepted (`memory-template.md`). Three things depend on it: not re-reporting an accepted issue, being able to say what changed since the last pass, and knowing whether a regression is new.

**A rendering or announcement behavior tied to a specific client** goes to `## Quirks` in `memory.md` with the surface and version, not into the audit log — the audit log is a timeline, the quirks box is knowledge. **A cadence the user accepts** becomes a `## Due` row in the same turn.
