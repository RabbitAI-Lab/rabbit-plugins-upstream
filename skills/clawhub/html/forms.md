# Forms — Submission, Labeling, Validation

Forms are where HTML still owns real behavior: what gets sent, under what key, with what keyboard, validated how. Most "form bugs" are one missing attribute.

**Contents:** [What Actually Gets Submitted](#what-actually-gets-submitted) · [Method and Encoding](#method-and-encoding) · [Labeling](#labeling) · [Input Types](#input-types) · [Keyboards: `inputmode` and `enterkeyhint`](#keyboards-inputmode-and-enterkeyhint) · [Autofill Tokens](#autofill-tokens) · [Constraint Validation](#constraint-validation) · [Error Messages](#error-messages) · [Grouping](#grouping) · [Multi-Control Patterns](#multi-control-patterns) · [File Uploads](#file-uploads) · [Passwords and OTP](#passwords-and-otp) · [Buttons in Forms](#buttons-in-forms) · [Form Review Checklist](#form-review-checklist)

## What Actually Gets Submitted

The rules that produce "the field is missing from the payload":

| Rule | Consequence |
|---|---|
| Only controls with a `name` are submitted | A control named only by `id` sends nothing, silently |
| `disabled` controls are omitted entirely | Use `readonly` when the value must still be sent — `readonly` also stays focusable and copyable |
| Unchecked checkboxes and unselected radios send nothing | No key at all, not `false`. Pair with `<input type="hidden" name="x" value="0">` **before** the checkbox: the later checked value wins in every server parser that takes the last occurrence |
| A control outside the `<form>` still submits if it carries `form="form-id"` | The escape hatch for sticky footers, dialogs, and layouts that cannot nest |
| Multiple controls may share a `name` | Sent as repeated keys — how checkbox groups and `<select multiple>` work; add `[]` only if the backend expects it |
| `<button type="submit" name value>` is submitted | And only the button that was activated — how one form supports Save and Delete |
| Empty text inputs send an empty string | Not "nothing" — an empty string overwrites a stored value on a PATCH |

## Method and Encoding

| Case | Attributes |
|---|---|
| Search, filters, anything shareable | `method="get"` — the state ends up in the URL, which is the feature |
| Anything that changes state, or carries PII | `method="post"` — GET puts values in the URL bar, the history, server logs, and the `Referer` header |
| File upload | `method="post" enctype="multipart/form-data"` — the default urlencoded encoding sends only the file name |
| Large text payloads | POST; practical URL ceilings sit around 2,000 characters across servers and proxies |

`action` omitted posts to the current URL. `target="_blank"` on a form is nearly always a mistake. `novalidate` on the form (or `formnovalidate` on one button) skips constraint validation — the correct way to make a "Save draft" button that accepts an incomplete form.

## Labeling

Every control needs a programmatic name. In order of preference:

1. `<label for="email">Email</label><input id="email" name="email">` — explicit, works when the layout separates them.
2. `<label>Email <input name="email"></label>` — implicit wrapping, no ids to keep unique. A label may contain only one labelable control.
3. `aria-label="Search"` — only when the design has no visible text at all.
4. `aria-labelledby="id-of-visible-text"` — when the visible name lives in another element.

Notes that decide real bugs:

- A `<label>` also gives the control a bigger click target. That is why wrapping a checkbox in its label removes the "the checkbox is hard to hit" complaint without any CSS.
- Labelable elements: `button`, `input` (except `type=hidden`), `meter`, `output`, `progress`, `select`, `textarea`. A `<div>` role-based control is not labelable by `<label>`.
- Placeholder is not a label (SKILL.md Rule 4). Nor is a `title`: it never appears on touch and is announced inconsistently.
- Required fields: mark them in the visible label text, and use the `required` attribute so the state is exposed. An asterisk with a legend elsewhere is the pattern that fails when the legend scrolls away.
- Hint text belongs in `aria-describedby`, not in the label — a name of "Password must be at least 12 characters and contain…" is read on every visit to the field.

## Input Types

| Type | Buys you | Watch |
|---|---|---|
| `email` | Keyboard with `@`, loose format validation | Validation accepts `a@b`; server still validates |
| `tel` | Telephone keypad | **No format validation at all** — pair with `pattern` |
| `url` | URL keyboard, requires a scheme | Users type `example.com`; normalize server-side rather than rejecting |
| `number` | Spinner, numeric keyboard | Locale-dependent parsing, silent drop of non-numeric input, scroll-wheel changes the value. Wrong for phone numbers, card numbers, postcodes, and OTPs — use `text` + `inputmode="numeric"` |
| `search` | Clear button, search keyboard | Wrap in `<search>` (`semantics.md`) |
| `date`, `time`, `datetime-local`, `month`, `week` | Native picker and calendar | Value format is always ISO regardless of displayed locale; range via `min`/`max`; no way to restrict arbitrary dates without JS |
| `color` | Native picker | sRGB hex only |
| `range` | Slider | Needs a visible current value — the thumb is not readable |
| `file` | Picker | `accept="image/*"`, `multiple`, `capture` on mobile |
| `checkbox` / `radio` | Real semantics and keyboard | Radios need a shared `name` to be a group |
| `hidden` | Non-visual value | Not secure, not private, still user-editable |
| `password` | Masking, manager integration | With the right `autocomplete` token, or managers will not save it |

## Keyboards: `inputmode` and `enterkeyhint`

`inputmode` changes the virtual keyboard without changing validation or parsing — the fix for numeric fields that must stay `type="text"`:

`numeric` (digits only, PIN/OTP) · `decimal` (adds the separator) · `tel` · `email` · `url` · `search` · `none` (custom on-screen keypad).

`enterkeyhint` renames the Enter key: `enter` · `done` · `go` · `next` · `previous` · `search` · `send`. On a single-field search box, `enterkeyhint="search"` removes the "how do I submit this" moment on mobile.

## Autofill Tokens

`autocomplete` is a **closed vocabulary**, not free text. Correct tokens are a WCAG 1.3.5 requirement at AA and the difference between a 40-second checkout and a 4-minute one.

| Field | Token |
|---|---|
| Full name / parts | `name` · `given-name` · `family-name` |
| Email, phone | `email` · `tel` (`tel-national`, `tel-extension`) |
| Street address | `street-address`, or `address-line1`/`address-line2` |
| City, region, postcode, country | `address-level2` · `address-level1` · `postal-code` · `country-name` |
| Organization | `organization` · `organization-title` |
| Card | `cc-name` · `cc-number` · `cc-exp` (or `cc-exp-month`/`cc-exp-year`) · `cc-csc` |
| Login | `username` · `current-password` · `new-password` |
| One-time code | `one-time-code` — enables SMS autofill on iOS and Android |
| Never autofill this | `off` — respected inconsistently; browsers override it on address and card fields they are confident about |

Shipping versus billing: prefix the group — `shipping street-address`, `billing postal-code`. Without the prefix the browser fills both blocks with the same address.

## Constraint Validation

Attributes: `required`, `min`, `max`, `step`, `minlength`, `maxlength`, `pattern`, `multiple`, plus the implicit rules of `type`.

- `pattern` is an implicitly anchored JS regex — no `^`/`$` needed — and **must** carry a `title` describing the rule, because the browser's default message is the title text.
- `maxlength` prevents typing past the limit but does not fire validation; `minlength` fires only after the field has been edited.
- `step` interacts with `min`: `min="1" step="2"` permits 1, 3, 5 — not even numbers. A `step` mismatch produces "Please enter a valid value", which is the least helpful message in the platform.
- **Style errors with `:user-invalid`, not `:invalid`.** `:invalid` matches every empty required field on first paint, so the whole form is red before the user types. `:user-invalid` waits until the field has been interacted with or submission attempted. Widely available since 2023; the pre-2023 workaround is a `.was-submitted` class on the form.
- Validation runs on submit and reports on the **first** invalid control only; the browser scrolls to it and shows a bubble that vanishes on the next keystroke and is not announced by every screen reader. This is why serious forms use `novalidate` plus their own error list.
- Client validation is UX. The endpoint is public (SKILL.md Traps).

## Error Messages

The pattern that works with assistive tech:

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" required
       aria-describedby="email-err" aria-invalid="true">
<p id="email-err">Enter an email address, like name@example.com.</p>
```

- `aria-invalid="true"` only while the error is present — never as a static attribute.
- The message text is referenced by `aria-describedby`, so it is read after the field's name and type.
- On submit failure, move focus to the first invalid field (or to a summary at the top of the form that links to each error) and make the summary a heading or an `alert` region. Silence after a failed submit is the most common form accessibility failure.
- Error text names the fix, not the rule: "Enter an email address, like name@example.com", not "Invalid input".

## Grouping

- Radio and checkbox groups need `<fieldset>` + `<legend>`: the legend is announced with each option, which is the only way "Standard / Express" makes sense out of context.
- The legend must be the **first child** of the fieldset. Style it freely; some resets break its layout, which is a CSS problem, never a reason to drop it.
- A one-control fieldset is noise. Related-but-not-mutually-exclusive fields (an address block) can use a `<section aria-labelledby>` or a heading instead.
- `<optgroup label>` groups `<option>`s; the label is not selectable and is announced as a group.

## Multi-Control Patterns

| Pattern | Markup |
|---|---|
| Short fixed suggestion list | `<input list="ids">` + `<datalist>` — free text still allowed, styling not controllable |
| Multi-select | `<select multiple>` (poor UX on touch) or a checkbox group in a fieldset — usually better |
| Dependent selects (country → region) | Repopulate options and announce the change in a live region; keep the second control disabled until the first has a value, and re-enable it before submit |
| Progressive form / wizard | One `<form>` per step with real submissions, or a single form with `<fieldset>` steps; either way each step gets a heading and focus moves to it |
| Repeating rows | A `<template>` cloned per row (`templates.md`) with the index in the `name`: `items[0][qty]` |
| Search-as-you-type | `role="combobox"` pattern (`interactive.md`), plus a debounced live region announcing the result count |

## File Uploads

- `accept` filters the picker and is a hint, not a guarantee — validate type and size on the server.
- `multiple` yields a `FileList`; the visible text stays "3 files" unless you render the names yourself.
- `capture="environment"` opens the rear camera directly on mobile; omit it to let the user choose the gallery.
- The native control's button text and its focus ring cannot be styled: hide the input with a visually-hidden class (never `display:none`, which removes it from the tab order) and pair it with a `<label>` styled as a button.
- Drag-and-drop is an enhancement layered on top; the input must remain reachable.

## Passwords and OTP

- `autocomplete="current-password"` on sign-in, `new-password` on registration and change forms — this is what tells a manager to offer a saved credential versus generate a new one.
- Keep the username field in the DOM on a password-only step (`autocomplete="username"`, `readonly`), or managers cannot associate the credential.
- A "show password" toggle is a `<button type="button">` with `aria-pressed` that flips `type` between `password` and `text` (SKILL.md Implicit Defaults — without `type="button"` it submits).
- Do not block paste, and do not set `maxlength` below 64: both break password managers.
- OTP: `<input type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6">` as **one field**, not six boxes — six boxes break autofill, paste, and screen readers.

## Buttons in Forms

| Attribute | Use |
|---|---|
| `type="submit"` | The default; the primary action |
| `type="button"` | Anything that is not a submit — toggles, "add row", "cancel" |
| `type="reset"` | Almost never; users hit it by accident and lose their work |
| `formaction` / `formmethod` | Two destinations from one form (Save, Publish) |
| `formnovalidate` | Save-as-draft on an incomplete form |
| `name`/`value` on the submit button | Distinguishes which action was taken, server-side |
| `disabled` while submitting | Prevents double submit; re-enable on error, or the user is stranded |

## Form Review Checklist

- Every control has a `name` and a real, visible label
- Every `id` referenced by `for`, `aria-describedby` or `aria-labelledby` exists exactly once in the document
- `type`, `inputmode` and `autocomplete` are all set deliberately on every field
- Radio and checkbox groups are wrapped in `fieldset`/`legend`
- Errors are text next to the field, referenced by `aria-describedby`, with `aria-invalid` toggled and focus moved on failed submit
- `method="post"` for anything that changes state; `multipart/form-data` if there is a file
- The submit button is reachable by keyboard and the form submits on Enter from a text field
- Nothing depends on JS to submit: a `<form>` with an `action` still works if the handler fails

**When a form pattern finally works** — a checkout address block with its autofill tokens, a validated multi-step wizard, an accessible error summary — save it to `~/Clawic/data/html/artifacts/form-<name>.md` with the tokens and the reason each attribute is there, and add its `## Boxes` line in the same turn (`memory-template.md`). Deriving the right token set costs an afternoon of testing on real devices; nobody should pay it twice. **If the user states a convention** — always one field for OTP, error summary at the top, a house `pattern` for postcodes — that is a declaration: record it under `conventions` in `config.yaml`.
