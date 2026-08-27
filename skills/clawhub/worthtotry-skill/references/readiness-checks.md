# The six readiness checks

`check_submission_readiness` returns exactly these six, always in this order, each as
`{ id, label, status, detail, fix }`. `fix` is null when the check passes.

## Scoring

| id                 | Weight | Status when it does not pass |
| ------------------ | -----: | ---------------------------- |
| `title`            |     20 | `fail`                       |
| `meta-description` |     15 | `warn`                       |
| `og-image`         |     15 | `warn`                       |
| `logo`             |     15 | `fail`                       |
| `duplicate`        |     15 | `fail`                       |
| `badge`            |      0 | `info`                       |

A `pass` earns the full weight, a `warn` earns half, a `fail` earns nothing. `score` is the total as
a percentage, rounded.

`badge` carries no weight and cannot move the score in either direction, because it is not a
property of the page's readiness — it is an optional extra its owner may or may not want. `info` is
its own status for that reason: it is not a lesser `warn`. Do not present it as something to fix.

The score is information, not a gate. Nothing is blocked by a low score.

`submittable` is false **only** when `duplicate` fails.

---

## `title` — Page title

Fails when the page has no `<title>`.

> **detail (fail)** The page has no `<title>`.
> **fix** Add a `<title>` describing what the product does.

A missing title also weakens the drafted listing: the extracted name is derived from it, so a page
without one falls back to a guess from the hostname.

## `meta-description` — Meta description

Warns when there is no meta description.

> **detail (warn)** No meta description, so search engines will invent one.
> **fix** Add `<meta name="description" content="...">` of about 150 characters.

## `og-image` — Social share image

Warns when there is no `og:image`.

> **detail (warn)** No og:image, so links to your site share as bare text.
> **fix** Add `<meta property="og:image" content="https://...">` at 1200x630.

This is not the listing screenshot. The screenshot is captured separately when the draft is opened
in a browser.

## `logo` — Logo source

Fails when no favicon or icon can be used as a logo.

> **detail (fail)** No favicon or icon we can use as a logo.
> **fix** Add `<link rel="apple-touch-icon" href="...">` with a square image, 512x512 or larger.

A listing cannot go to review without a logo. If this fails, either the page gets one or the person
uploads a file in the browser — there is no way for you to supply it. SVG icons and images that
cannot be decoded are treated as absent.

## `duplicate` — Duplicate listing

Fails when the host is already listed. **This is the only check that blocks a submission.**

> **detail (fail)** This URL is already listed as /tools/<slug>.
> **fix** Claim or update the existing listing instead of submitting again.

Matching is on the canonical host, so `www.` and a different path will not get around it. When this
fails, stop and hand the person the existing listing path from `detail`.

## `badge` — Badge backlink (optional)

Returns `info`, never `fail`, when the page HTML contains no link back to the directory.

> **detail (info)** No link to <host> was found in the page HTML. Nothing here needs it — launching
> is free either way. Adding one earns the verified mark and the tiebreaker in the ranking.
> **fix** Optional: add this to your footer — `<a href="https://worthtotry.com" target="_blank" rel="noopener"><img src="https://worthtotry.com/badges/featured.png" alt="Featured on us" width="244" height="56" /></a>`

Quote the `fix` from the live response rather than this file — it is generated with the current
badge URL.

The check looks at the HTML the server returns, so a badge injected by client-side JavaScript will
not be seen. It is re-verified on a schedule after publication, and the listing's owner can re-run
it on demand from their dashboard.

**The badge is not required and buying your way out of it is not a thing.** Launching is free
whether or not the link is there, the listing is identical either way, and there is no plan that
sells an exemption. What the link earns is narrow and worth stating exactly: a verified mark on the
listing, inclusion in the verified filter at `/tools?verified=1`, and the tiebreaker in the ranking
— two listings level on votes are separated by the one whose site links back. It never lifts a
listing above one with more votes, and it buys nothing from a moderator.

Report it as a choice with that upside. Do not describe it as a requirement, a cost, or something
the person needs to fix, and do not decide for them.
