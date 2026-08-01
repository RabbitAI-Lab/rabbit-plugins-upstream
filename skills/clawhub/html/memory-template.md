# Working File Templates — HTML

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — Configuration table keys and preference areas alike | `~/Clawic/data/html/config.yaml` | Key by key, read-modify-write |
| Pages and templates, rendering quirks, pain points, due dates, box index | `~/Clawic/data/html/memory.md` | Rewritten in place; stays small |
| Pages and templates: purpose, engine, `lang`, landmark structure, LCP element | `## Pages` in `memory.md`; `~/Clawic/data/html/pages.md` once it outgrows the section | One row per page or template |
| Client-specific behavior: a browser, screen reader, email client, CMS or build step that does something non-obvious | `## Quirks` in `memory.md`; `~/Clawic/data/html/quirks.md` once it outgrows the section | One row per behavior, with the surface and version |
| Accessibility passes, validation runs, performance measurements | `~/Clawic/data/html/audits/<year>.md` | Append-only, cut by year |
| Things you produced that get re-read — a `<head>` block, an accessible component pattern, a complex table's header map, an email template, a sanitizer allowlist, a decision about a native element vs a library | `~/Clawic/data/html/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| Hostnames: canonical host, `www`-vs-apex, locale→hostname map | `~/Clawic/data/domains/domains.md` (**shared**) | One row per hostname, every source in one file |
| The site or app this work belongs to, and the decisions taken on it | `~/Clawic/data/projects/<project>.md` (**shared**) | One file per project |
| **Anything durable this table does not name** | `~/Clawic/data/html/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

Deciding where something unnamed goes, in this order: (1) would another skill want to read it — a hostname, a project, a person? Then it belongs in the shared box, not here. (2) Is it a text read whole when its subject comes up — a pattern, a policy, a decision with its reasoning, a template? Then `artifacts/`, its own file from the first one. (3) Is it one more row of something that accumulates? Then a section of `memory.md` until the split threshold.

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A page or template was mapped, or its structure, `lang`, engine or LCP element was established | `## Pages` |
| A browser, screen reader, email client, CMS or build step behaved non-obviously | `## Quirks`, with the surface and version |
| An accessibility pass, a validation run, or a field-metrics review happened | A row in `audits/<year>.md` |
| A component pattern, form pattern, table header map, `<head>` block or email template finally worked | `artifacts/`, with the reason each part is there and what it was verified against |
| A decision was made between a native element and a library, or a base format, or a facade vs a real embed | `artifacts/`, with what was rejected and why |
| A sanitizer allowlist was agreed | `artifacts/sanitizer-allowlist.md` |
| A canonical host, `www`-vs-apex choice, or locale→hostname map was agreed | Its row in `domains.md` (shared) |
| The markup belongs to a tracked project, and a decision was taken on it | One line in `projects/<project>.md` (shared), pointing at the artifact by name |
| The same failure appeared twice | `## Pain Points`; the second occurrence earns an artifact |
| A re-audit, validation sweep, email client re-test or embed review was scheduled or run | `## Due` |
| The user declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Everything except artifacts, audit records and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/html/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Artifacts are the exception: a pattern, a template or a decision is born as its own file whatever its size, because it is read whole and only when its subject comes up. Audit records are the other exception: they are a timeline, cut by year, and never live inside `memory.md`.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep. Markup is a dense carrier: analytics ids and inline script config, `<meta>` site-verification tokens, signed CDN and embed URLs, session ids and CSRF tokens in hidden inputs, ESP or form-endpoint keys in an email template. Strip each value **before** writing and leave its pointer in place, in this shape: `<kind>:<locator>`.

`env:GA_MEASUREMENT_ID` · `env:FORM_ENDPOINT` · `keychain:esp-api` · `1password:Work/Site/analytics` · `bitwarden:Site/cms` · `vault:secret/site/embed` · `file:~/.netrc`

In a text, the pointer goes where the value was: `<input type="hidden" name="csrf" value="<env:CSRF_TOKEN>">`. Say in one line that you did it.

In this domain — **not secrets, keep them**: element and attribute names, class and id names, URLs and paths without credentials or signatures, hostnames, `lang` and `hreflang` values, image and font filenames, CSP directive names, WCAG criterion numbers, browser and screen-reader versions, email client names, measured metrics.

**Secrets, strip them**: API keys and measurement ids the user treats as private, site-verification token values, CSRF and session token values, signed URL query parameters and their expiry signatures, form-endpoint keys, ESP and SMTP credentials, CSP `nonce` values, basic-auth strings inside URLs, anything in a `.env` pasted alongside a template.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [shared domains box](#shared-domains-box) · [shared projects box](#shared-projects-box) · [artifacts/](#artifacts) · [audits/](#audits) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/html/` if it does not exist.

```yaml
markup_flavor: jsx
browser_support: widely-available
a11y_target: wcag-aa
document_lang: en-GB
structured_data: json-ld
inline_code_policy: nonce
untrusted_html: sanitize
email_client_floor: outlook-desktop
output_shape: fragment

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
tooling:
  formatter: prettier
  validator: html-validate
  cms: none
conventions:
  attribute_order: [class, id, data-*, aria-*, role]
  void_style: no-trailing-slash
  otp_field: single-input
platform:
  surfaces: [marketing-site, email]
  rtl_in_scope: false
constraints:
  banned_embeds: [social-post-widgets]
  no_js_baseline: true
cadence:
  a11y_audit: quarter
  email_client_retest: quarter
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# HTML Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Pages and templates (22) → `pages.md`; read before changing any template or answering "how is this page built"
- Client quirks (17) → `quirks.md`; read before promising a behavior on Outlook, Safari or a screen reader
- Audits and validation runs (2026) → `audits/2026.md`; read before an audit, to avoid re-reporting an accepted issue
- Checkout dialog pattern → `artifacts/pattern-checkout-dialog.md`; read before touching any modal
- Sanitizer allowlist for comments → `artifacts/sanitizer-allowlist.md`; read before changing what user HTML may contain
- Order-confirmation email → `artifacts/email-order-confirmation.md`; read before any campaign or template change

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Screen-reader pass on the pattern library | quarter | 2026-05-12 | 2026-08-12 |
| Email client screenshot set | quarter | 2026-06-02 | 2026-09-02 |
| Field metrics review (LCP/CLS/INP p75) | month | 2026-07-01 | 2026-08-01 |
| Third-party embed review | quarter | 2026-04-20 | 2026-07-20 |

## Pages
| Page / template | Purpose | Engine | lang | Structure | LCP element | Notes |
|---|---|---|---|---|---|---|
| `/` (home.njk) | marketing landing | Nunjucks | en-GB | banner · nav · main · contentinfo | hero `<img>`, preloaded | h1 is the product name, deliberate |
| `/pricing` | plans | Nunjucks | en-GB | + named `<section>` per plan | h1 text | table has a two-level header (see artifact) |
| `/checkout` | payment | React | en-GB | main only, no nav | first paint text | autofill tokens verified on iOS and Android |

## Quirks
| Surface | Behavior | Workaround | Seen |
|---|---|---|---|
| Outlook 2019 Windows | ignores `max-width` on tables | `width` attribute plus inline `style` | 2026-06-02 |
| VoiceOver + Safari 17 | `<ul>` with `list-style:none` loses list semantics | `role="list"` on the ul | 2026-05-12 |
| CMS editor (v9.2) | strips `loading` and `fetchpriority` on paste | images injected via the template, not the editor | 2026-07-14 |
| Gmail Android app, non-Gmail account | media queries ignored | mobile-first single column, no query needed | 2026-06-02 |

## Pain Points
2026-03: duplicate ids from a cloned `<template>` broke every `label[for]` on the repeated rows. Ids now assigned at clone time.
2026-06: hero image lazy-loaded by a global default; LCP went from 1.9s to 3.4s. `loading="eager"` pinned in the template.

## How They Work
Two sites plus a transactional email set. Wants the attribute and the line, not the essay. Ships behind a strict CSP with per-response nonces.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Cadences come from `cadence` in `config.yaml` when the user has declared them, and from `auditing.md` otherwise.
- **`## Pages`**: one row per page or template, not per URL. `Structure` is the landmark skeleton and any deliberate exception; `LCP element` is what was measured, not what was assumed. A row is what makes "does this new page match the others" answerable without opening files.
- **`## Quirks`**: always name the **surface and version** (browser, screen reader + browser pair, email client, CMS, build tool) and the date. A quirk without its surface is folklore, and it is why the same Outlook bug gets rediscovered every year.
- **`## Pain Points`**: a failure whose cause was not obvious, or one that appeared twice. The second occurrence earns an artifact.
- These headings are exactly the ones `pages.md` and `quirks.md` get when their sections outgrow this file, so each split stays a copy-paste.

| Status | Meaning |
|---|---|
| `ongoing` | Still learning their sites and conventions |
| `complete` | Know their templates, stack and constraints well |

## Shared domains box

Lives at `~/Clawic/data/domains/domains.md` and is shared with every other skill that touches hostnames — the user may not have any of them installed, so the format travels with this skill.

```markdown
# Domains

| Hostname | Registrar | Expires | Points to | Notes |
|----------|-----------|---------|-----------|-------|
| example.com | — | — | — | canonical host: `https://example.com` (apex, no trailing slash); x-default |
| es.example.com | — | — | — | hreflang `es`, alternate of example.com |
```

- **Identity is the hostname.** Read the file before adding. If the row exists, update it in place — never a second row for the same host.
- **Write only what you verified.** This skill establishes the canonical host, the `www`-vs-apex choice, and the locale→hostname map; those go in `Notes`. Leave `Registrar`, `Expires` and `Points to` empty rather than guessing — another skill owns those columns and will fill them.
- **Foreign columns win.** If `domains.md` already exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- **Retirement is part of the inventory.** When a hostname is dropped or a locale is retired, delete the row and note the date in `## Pages`. An inventory that only grows stops being an inventory.
- **Scale cut**: one row per hostname while there are ≤40. Past that, group by apex in `~/Clawic/data/domains/<apex>.md` with the same columns, and `domains.md` becomes the index. If you arrive and the folder already looks like that, follow it — do not start a parallel `domains.md`.
- Never a credential, a DNS API token, or a signed URL. Pointers only.

## Shared projects box

Lives at `~/Clawic/data/projects/<project>.md`, one file per project, shared with every skill that works on the same job.

- **Identity is the project name**, and the filename is that name in kebab-case. Read the folder before writing: if a file for the project already exists, append your line to it — never a second file for the same project under a different spelling.
- Write **one line** per markup decision that matters at project level — "checkout modal is native `<dialog>`, library rejected 2026-07-26 (see html artifact)" — and keep the full reasoning in `artifacts/`, referenced by name. Duplicating the artifact here is how two skills end up contradicting each other.
- Never create a project file for work the user has not framed as a project.
- **Retirement is `status: done | cancelled — <date>` inside the file, never deletion**: it is the record of what was shipped.
- **Scale cut**: past ~20 closed projects, move the closed ones to `~/Clawic/data/projects/archive/<project>.md` — same filename, no renaming, so a link by project name still resolves. If you arrive and the folder already has an `archive/`, follow it — do not invent a second convention.
- If the project belongs to a client, the client goes in `~/Clawic/data/contacts/contacts.md` and is referenced here by name only.

## artifacts/

One file per thing, at `~/Clawic/data/html/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **an accessible component pattern that finally worked**, **a `<head>` block for a site**, **a form pattern with its autofill tokens**, **a complex table's header map**, **an email template**, **a sanitizer allowlist**, **a decision between a native element and a library**. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn. Every secret inside is already a pointer.

```markdown
# Pattern — checkout confirm dialog
*Read before touching any modal. Verified 2026-07-26, NVDA+Firefox and VoiceOver+Safari 17.*

Native `<dialog>` + `showModal()`; `<form method="dialog">` for the actions.
Name: aria-labelledby → the h2. Focus: autofocus on Cancel, because Delete is destructive.
Keyboard contract: Escape closes; focus returns to the trigger automatically.
Known gap: backdrop click does not close — deliberate for destructive actions.
```

```markdown
# Decision — native dialog, not the modal library
*Read before adding any overlay dependency. 2026-07-26.*

Decision: `<dialog>` + `showModal()` everywhere.
Rejected: the modal library — 14 KB, its own focus trap that fought `inert`, and no top layer.
Cost: backdrop-click dismissal is three lines of our own code.
Revisit when: a design needs anchored positioning the platform cannot express yet.
```

```markdown
# Head block — example.com
*Read before changing any template head. 2026-07-26.*

...the block, with each line's reason, and every token replaced by its pointer...
```

## audits/

The timeline of every pass. Append-only, one file per year, never rewritten.

```markdown
# Audits — 2026

| Date | Scope | Method | Critical | Serious | Fixed | Remaining (and why) |
|------|-------|--------|----------|---------|-------|---------------------|
| 2026-05-12 | pattern library | NVDA+Firefox, VoiceOver+Safari 17, manual keyboard | 1 | 4 | 4 | combobox announcement on JAWS — untested, no licence |
| 2026-06-30 | all templates | html-validate + axe, rendered output | 0 | 2 | 2 | — |
| 2026-07-01 | field metrics | CrUX p75 | — | — | — | LCP 2.1s, CLS 0.04, INP 180ms |
```

- `Remaining` always carries the reason it was accepted. Without it, the next pass re-reports it and the audit stops being read.
- `Method` names the tool and version, or the AT+browser pair. "Tested with a screen reader" is not a method.
- A behavior discovered during an audit belongs in `## Quirks`, not here: this file is a timeline, the quirks box is knowledge.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`pages.md` — `## Pages`, with one `## <site>` heading above it when more than one site is in play. This is the file that answers "how is this page built and what must not change" without opening a template.

`quirks.md` — `## Quirks`, optionally grouped `## Browsers`, `## Screen readers`, `## Email clients`, `## Tooling` once it is long. Each row keeps its surface, version and date. The reason this file exists: client behavior is the one class of fact in this domain that cannot be re-derived from the spec.
