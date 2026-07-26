# Security — Untrusted Markup, Injection, Isolation

The markup layer's threat is simple to state and easy to get wrong: any string that reaches the HTML parser can become code. Governed by `untrusted_html` and `inline_code_policy`.

**Contents:** [The Five Escaping Contexts](#the-five-escaping-contexts) · [Sinks](#sinks) · [Sanitizing](#sanitizing) · [Attributes That Execute](#attributes-that-execute) · [Links](#links) · [Isolation With `sandbox`](#isolation-with-sandbox) · [CSP From Markup](#csp-from-markup) · [Subresource Integrity](#subresource-integrity) · [Forms and Credentials](#forms-and-credentials) · [Uploaded and Embedded Files](#uploaded-and-embedded-files) · [Review Checklist](#review-checklist)

## The Five Escaping Contexts

One escaper for all five is an XSS. Escape for the context the value lands in:

| Context | Escape | Failure if you use HTML escaping only |
|---|---|---|
| HTML text | `& < >` | — |
| Attribute value (quoted) | `& < > " '` | An unquoted attribute breaks out on a space: `value=x onmouseover=alert(1)` |
| URL attribute (`href`, `src`, `action`, `formaction`) | Validate the **scheme** first, then percent-encode | `javascript:`, `data:text/html`, and `vbscript:` all pass HTML escaping untouched |
| Inside `<script>` | JSON-encode and escape `<`, `/`, U+2028/U+2029 | `</script>` inside a string ends the block; the rest is markup |
| Inside `<style>` or a `style` attribute | Do not interpolate user data into CSS at all | `url()` and legacy expressions |

Always quote attribute values. An unquoted attribute is terminated by whitespace, which turns any injected space into a new attribute.

## Sinks

Anything that parses a string as HTML:

`innerHTML` · `outerHTML` · `insertAdjacentHTML` · `document.write` · `<iframe srcdoc>` · `DOMParser.parseFromString` · jQuery-style `$(html)` · framework "raw HTML" escapes (`dangerouslySetInnerHTML`, `v-html`, `{@html}`) · SVG `innerHTML` · `Element.setHTMLUnsafe`.

Safe alternatives that never parse markup: `textContent`, `setAttribute` (with a validated value), `document.createElement` + property assignment, template literals rendered by a framework's default escaping.

## Sanitizing

- **Allowlist, never blocklist.** Stripping `<script>` leaves `<img onerror>`, `<svg onload>`, `<iframe srcdoc>`, `<a href="javascript:">`, `<style>` with imports, `<math>`/`<foreignObject>` namespace confusion, and mutation XSS where the sanitizer's parse and the browser's parse disagree.
- Sanitize with a maintained library, on **output**, in the same environment that will render it. Sanitizing on input freezes the rules at the moment of storage; a bypass fixed next year never reaches the stored row.
- Define the allowlist explicitly and write it to `artifacts/sanitizer-allowlist.md`: which elements, which attributes per element, which URL schemes, whether `class`/`id`/`style`/`data-*` survive. "Default config" is not a specification and changes between library versions.
- The `Sanitizer` API is arriving in browsers; until it is available in the target set, a library is the answer. Under `untrusted_html: trusted-types`, enforce Trusted Types with CSP so the sinks above throw instead of parsing.
- Markdown is not a sanitizer. Most Markdown renderers pass raw HTML through by default (`markdown`).

## Attributes That Execute

| Vector | Note |
|---|---|
| Any `on*` handler | Never allow through a sanitizer; blocked entirely by a CSP without `unsafe-inline` |
| `href`/`src`/`action`/`formaction` with `javascript:` | Validate the scheme against an allowlist (`https`, `http`, `mailto`, `tel`, relative) |
| `data:` URLs in `href`, `iframe src`, `object data` | `data:text/html` executes in your origin — block the scheme, allow `data:image/*` only where needed |
| `srcdoc` | Full HTML parsing inside the frame; sandbox it |
| `style` attribute | Cannot execute in current browsers, but can hide, cover, or reposition content over a real control (clickjacking within your own page) |
| SVG `<script>`, `<use href>` to a remote document, event attributes | An uploaded SVG rendered inline is executable markup — serve user SVGs as `<img>` (which is script-inert) or sanitize them |
| `<meta http-equiv="refresh">` in injected content | Redirects the whole page |
| `<base href>` in injected content | Rebases every relative URL in the document to an attacker's origin |

## Links

- `target="_blank"`: current browsers imply `noopener`, but embedded webviews and older engines do not. Keep `rel="noopener"`; add `noreferrer` when the destination should not see where the click came from.
- User-generated links: `rel="nofollow ugc noopener"` and `target="_blank"` if the site's convention wants it.
- Show the destination host for links in user content; an anchor's text can claim any destination.
- Never build a redirect endpoint that takes an arbitrary target URL from a query parameter without an allowlist.

## Isolation With `sandbox`

`<iframe sandbox>` with an empty value removes: scripts, forms, popups, top-level navigation, pointer lock, same-origin identity, downloads, and modals. Add back individually:

| Token | Grants |
|---|---|
| `allow-scripts` | JS execution |
| `allow-forms` | Form submission |
| `allow-popups` | `window.open`; add `allow-popups-to-escape-sandbox` only deliberately |
| `allow-same-origin` | Keeps the frame's own origin — **never together with `allow-scripts` for same-origin content** (SKILL.md Traps) |
| `allow-downloads` | File downloads |
| `allow-top-navigation-by-user-activation` | Navigating the top frame, only from a real interaction |

Serve untrusted content from a **separate origin** (a distinct hostname, not a path), so origin isolation does the work even if a sandbox token is wrong. `credentialless` on the frame prevents it from carrying credentials to its origin.

## CSP From Markup

- A real CSP is an HTTP header. The `<meta http-equiv="Content-Security-Policy">` form works for most directives but **ignores `frame-ancestors`, `report-uri`/`report-to`, and `sandbox`** — so clickjacking protection cannot be delivered from markup at all.
- `inline_code_policy: nonce` means every emitted inline `<script>`/`<style>` carries `nonce="{{nonce}}"` and the server generates a fresh value per response. A reused nonce is equivalent to `unsafe-inline`.
- `inline_code_policy: forbidden` means no inline code and no `on*` handlers at all: event binding happens in an external script.
- A strict CSP forbids inline handlers, `javascript:` URLs, and `eval` — it is defense in depth, not a substitute for escaping.
- Clickjacking defense is `frame-ancestors 'none'` (or `X-Frame-Options: DENY`) as a header, plus never rendering sensitive actions in a framable page.

## Subresource Integrity

```html
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-…" crossorigin="anonymous" defer></script>
```

- `integrity` without `crossorigin="anonymous"` is not enforced for cross-origin requests — a silent no-op.
- SRI pins one exact file. A CDN URL without a version, or one that serves different bytes per user agent, cannot be pinned.
- A mismatch blocks the resource entirely; that is the intent, and it needs a fallback plan for third-party code you cannot control.

## Forms and Credentials

- `method="post"` for anything that changes state; GET puts values into URLs, history, logs and referrers (`forms.md`).
- CSRF protection is a hidden token plus a `SameSite` cookie policy — the token is markup, the policy is a header.
- Never put a secret in a hidden input, a `data-*` attribute, an inline script, or a comment. "Hidden" in HTML means "not painted", not "not in the source".
- Password fields need the right `autocomplete` tokens so managers work; blocking paste and capping length below 64 characters weakens security, it does not strengthen it (`forms.md`).
- Autofill can be abused by off-screen fields: never render form controls the user cannot see beside real credential fields.

## Uploaded and Embedded Files

- User-uploaded SVG, HTML, and PDF are all active content. Serve them from a separate origin with `Content-Disposition: attachment` where possible, and never inline an uploaded SVG into the page.
- `<img src="user.svg">` does not execute scripts inside the SVG; `<svg>` inlined into the DOM does.
- Filenames rendered back into the page are untrusted strings like any other.

## Review Checklist

- Every interpolation point is escaped for the exact context it lands in
- No `on*` attributes in emitted markup unless `inline_code_policy: allowed`, and none ever in user content
- Every URL from user data has its scheme validated before rendering
- Rich user HTML goes through an allowlist sanitizer at render time, with the allowlist written down
- Untrusted embedded content is on a separate origin and sandboxed with the minimum token set
- No `allow-scripts` + `allow-same-origin` on content from your own origin
- Third-party scripts carry `integrity` + `crossorigin`, or a reason why they cannot
- No secret, token, key, or session identifier appears anywhere in the markup — including comments and `data-*`

**When a sanitizer allowlist is agreed**, save it to `~/Clawic/data/html/artifacts/sanitizer-allowlist.md` — elements, attributes per element, permitted URL schemes, and what was deliberately excluded and why — and add its `## Boxes` line in the same turn (`memory-template.md`). It is a security control, and a control nobody wrote down is a control that drifts. **Never write a token, key, nonce value, or session id into any file under `~/Clawic/data/`**, including markup the user pastes for review: replace each value with its pointer (`env:GA_MEASUREMENT_ID`, `keychain:esp-api`) before saving, and say in one line that you did.
