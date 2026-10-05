---
name: open-agent-guide
description: Use when an agent needs to read or contribute to the Open Agent Guide public catalog of AI-native organizations, products, models, MCP servers, agent skills, and integrations. Covers signup, API token storage, the v1 read endpoints, and submitting catalog edits.
version: 0.2.1
metadata:
  openclaw:
    primaryEnv: OAG_TOKEN
    envVars:
      - name: OAG_TOKEN
        required: false
        description: Open Agent Guide API token (prefix `oag_`). Required for authenticated endpoints (`/me/...`, submissions, reviews). Anonymous catalog reads work without it.
      - name: OAG_BASE_URL
        required: false
        description: Base URL for the Open Agent Guide API. Defaults to `https://www.openagentguide.com` for reads and batch scripts. Override only for staging or self-hosting.
    requires:
      anyBins:
        - curl
        - http
    homepage: https://www.openagentguide.com
    emoji: "🗂️"
---

# Open Agent Guide

Use this skill when an agent needs to **read** or **contribute to** the public
Open Agent Guide catalog of AI-native organizations, products, models, MCP
servers, agent skills, and integrations.

## When to use this skill

Triggers:

- "find products that support MCP / A2A / headless signup"
- "what compliance certifications does `{product}` publish?"
- "look up `{organization}` in the catalog"
- "submit an edit to a product's trust center URL"
- "propose a new MCP server / API spec / developer kit"

NOT for:

- scraping vendor websites directly — use the catalog as the source of truth
- managing your local OpenClaw skill library (that is the `clawhub` CLI)
- private/internal inventories — this is a public catalog, MIT-0 data

## Configuration

| Env var        | Required                         | Default                          | Purpose                             |
| -------------- | -------------------------------- | -------------------------------- | ----------------------------------- |
| `OAG_TOKEN`    | only for authenticated endpoints | —                                | Bearer token, prefix `oag_`         |
| `OAG_BASE_URL` | no                               | `https://www.openagentguide.com` | Override for staging / self-hosting |

Read examples and batch scripts use `https://www.openagentguide.com` by default.
Set `OAG_BASE_URL` only when targeting a staging or self-hosted instance.

## Quick start (no auth)

Catalog reads are anonymous-capable. The OpenAPI spec is the source of truth for
the live API shape — fetch it first whenever you are unsure:

```bash
: "${OAG_BASE_URL:=https://www.openagentguide.com}"
curl -fsSL "$OAG_BASE_URL/api/v1/openapi.json" \
  | jq '.paths | keys[]' | head
```

Then a real read:

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/catalog/products/" \
  | jq '.results[] | {id, name, slug}'
```

## Get a token (one-time setup)

Authenticated endpoints — your own profile, products you use, and submissions —
need an API token. Sign up and receive your first token in one call:

```bash
curl -fsSL -X POST "$OAG_BASE_URL/api/v1/users/signup/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your-handle",
    "email": "you@example.com",
    "password": "<strong-password>",
    "name": "Your Name",
    "account_type": "individual",
    "token_name": "first-token"
  }' | tee /tmp/oag-signup.json | jq '.api_token | {id, bearer_token, authorization_header}'
```

The response carries:

- `api_token.bearer_token` — the raw `oag_…` value, shown **once**
- `api_token.authorization_header` — preformatted `Bearer oag_…`, drop it
  straight into `-H "Authorization: ..."` for your first call
- `next_steps` — links the API itself advertises (current user, submission
  targets, submission fields, create submission, docs)

Signup is rate-limited to **10 per hour per IP**. If you hit `429`, read the
`Retry-After` header before retrying.

## Remember the token

The skill expects `$OAG_TOKEN` in the environment. Pick one storage layout and
stick to it:

| Environment        | Recommended storage                                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Local shell        | `~/.config/open-agent-guide/env` (chmod 600), sourced from your shell rc                                                                     |
| macOS keychain     | `security add-generic-password -a "$USER" -s oag-token -w "<bearer>"`; read with `security find-generic-password -a "$USER" -s oag-token -w` |
| Linux secret store | `secret-tool store --label "OAG" service oag user "$USER"`; read with `secret-tool lookup service oag user "$USER"`                          |
| OpenClaw agent     | Declared above as `metadata.openclaw.primaryEnv: OAG_TOKEN`; OpenClaw resolves it from its secret store at activation time                   |
| CI                 | Repository secret `OAG_TOKEN`; reference via `${{ secrets.OAG_TOKEN }}`                                                                      |

Hard rules:

- Never paste the token into source files, prompts, transcripts, or chat
  history.
- Never commit `.env*` files that contain it.
- Rotate immediately if a token leaks (see "Rotating and revoking" below).

## Making authenticated calls

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/users/me/" \
  -H "Authorization: Bearer ${OAG_TOKEN}"
```

The `authorization_header` field returned at signup is already in this shape —
use it verbatim during the first session.

## Rotating and revoking

List your tokens, then rotate or revoke by id:

```bash
# List
curl -fsSL "$OAG_BASE_URL/api/v1/users/me/tokens/" \
  -H "Authorization: Bearer ${OAG_TOKEN}" | jq

# Rotate (returns a NEW bearer_token; the old value stops working immediately)
curl -fsSL -X POST "$OAG_BASE_URL/api/v1/users/me/tokens/<token-id>/rotate/" \
  -H "Authorization: Bearer ${OAG_TOKEN}" | jq '.bearer_token'

# Revoke
curl -fsSL -X DELETE "$OAG_BASE_URL/api/v1/users/me/tokens/<token-id>/" \
  -H "Authorization: Bearer ${OAG_TOKEN}"
```

See [references/onboarding.md](references/onboarding.md) for the full token
lifecycle, including issuing additional named tokens for separate workloads.

## Common workflows

### Search the catalog

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/catalog/products/?search=mcp&page_size=25" \
  | jq '.results[] | {slug, name, organization: .organization.slug}'
```

### Pull a single product with related data

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/catalog/products/<product-id>/" | jq
```

### Propose an edit to a catalog record

Use `POST /api/v1/submissions/`. Submissions are reviewed before being merged
into the public catalog. Keep the payload minimal — only fields that change:

```bash
curl -fsSL -X POST "$OAG_BASE_URL/api/v1/submissions/" \
  -H "Authorization: Bearer ${OAG_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "app_label": "catalog",
    "model": "product",
    "object_id": "<product-uuid>",
    "description": "Evidence: https://vendor.example/trust — the trust center lists SOC 2 and enforced MFA.",
    "payload": { "trust_center_url": "https://vendor.example/trust" }
  }' | jq
```

Before drafting, fetch the writable field shape:

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/submissions/fields/?app_label=catalog&model=product&view=summary" \
  -H "Authorization: Bearer ${OAG_TOKEN}" | jq
```

### Only emit a field you can cite — leave the rest unset

Every claim in the payload is held to a citation bar: the review that gates the
merge rejects the whole submission if a payload field asserts something no cited
source states. So a field you cannot back is not "missing data" you should fill
with your best guess — it is a claim you should omit. Represent genuine
uncertainty by leaving the field unset (unknown), not by inventing a value.

This bites hardest on **asserted-negative booleans** — `open_source=false` and
`self_hostable=false`. Almost no vendor publishes a source stating a product is
*not* open source or *not* self-hostable, so for a closed-source commercial SaaS
these flags are structurally uncitable. Emitting them as `false` therefore gets
the entire submission rejected for those two fields alone, even when every other
claim is cited. **Do not emit `open_source` / `self_hostable` (or any boolean)
as `false` unless a source explicitly states the negative — leave the field
unset.**

Leaving them unset costs nothing you had: the AI-native score awards a
portability point for either flag only when it is `true` (see
`catalog/scoring.py`), so an uncitable `false` scores identically to unset while
blocking the merge. Unset simply caps the top score the record can reach until a
citable source appears; `false` you cannot cite fails the whole proposal.

### Keep provenance out of `description` — no "verified on `<date>`" line

The fact-check reads `description` as claim-bearing text. A first-person line
about the *act of verifying* —
`"Verified 2026-09-04 against the vendor's own pages."`,
`"Confirmed on the trust center on …"` — is extracted as the claim *"the
submission was verified on `<date>`"*, which no vendor page can cite, so it
comes back `insufficient_evidence` and rejects the whole submission on its own.
Write `description` as evidence URLs plus a neutral summary of what changed —
never a datable claim about having checked. (Same failure shape as the
asserted-negative booleans above.)

### Emit a `*_url` field only when that URL is among your cited sources

The fact-check turns `terms_of_service_url` / `privacy_policy_url` /
`trust_center_url` / `status_page_url` into a claim of the form *"X's ToS URL is
`<url>`"* and looks for a page that states it. A real, reachable URL that no
cited page names comes back `insufficient_evidence`; worse, a URL that fails to
fetch (e.g. a canonical privacy URL that redirects into a bot-gated app)
escalates to `unsupported` and **fails** the submission. Reachability is already
covered by the separate `urls` check, so this is double jeopardy against a
citation that often can't exist. Prefer URLs a page self-corroborates (the
privacy page whose own text says "Privacy Policy"), and expect some to bounce:
be ready to drop `terms_of_service_url` / `status_page_url` / a bot-gated
`privacy_policy_url` and resubmit without it.

### Cite each compliance cert — and each RBAC / MFA association — to the plainest static page that names it

A compliance-cert claim survives only if the crawler renders the cited page's
text and that text literally names the cert. A SafeBase-style trust center (e.g.
`security.vendor.com`) that lists "SOC 2 Type 2", "ISO 27001", "PCI-DSS" as
plain HTML fact-checks cleanly; a JS-heavy docs page whose cert list is in the
rendered DOM but not the fetched HTML does not. Cite the most static trust page
that spells the cert out, and confirm the cert string is in the fetched HTML,
not just the rendered page.

The **same rule applies to `access_controls` (RBAC) and `mfa_types`**: each is a
world-claim held to the citation bar exactly like a cert, and each is
page-render-dependent in exactly the same way (supported off a plainly-listed
security page, `unsupported` off a JS-heavy one). Cite them to the plainest
static page that literally names the control ("role-based access control",
"passkeys", "TOTP"), not a marketing overview whose text renders client-side.

### Populate `api_specs` freely — identity is reachability-checked, not fact-checked

An `api_specs` entry's identity — `name`, `slug`, `spec_type`, and the spec
`url` — is **record structure**, not a fact-checked world-claim. The spec `url`
returns a self-describing OpenAPI document that the `urls` reachability check
already fetches, so its identity is verified there rather than by a claim a
vendor page must corroborate. Almost no vendor page states "product X documents
an OpenAPI spec named Y at Z" in a citeable form, so holding it to the citation
bar used to sink otherwise-clean submissions — that is now scoped out. Add an
`api_specs` entry whenever the vendor publishes a spec; just make sure the spec
`url` resolves (a reachable `200` OpenAPI document, or a protected status), the
same bar the `urls` check applies to any URL.

### Populate MCP servers freely

An MCP server in the payload round-trips cleanly end to end. The endpoint passes
the `urls` reachability check even when it answers a bare GET with `401` / `403`
/ `405` / `429` (the "protected" set is treated as reachable), and the
fact-check synthesizes *"operates an MCP server at `<endpoint>`"* / *"documents
its MCP server at `<docs>`"* as **supported** when you cite the docs page. Add
MCP servers whenever the vendor documents one.

### Break pricing into one offer per plan

When a product publishes named pricing plans/tiers — the typical Free / Starter
/ Standard / Professional / Enterprise ladder — model **each plan as its own
`Offer`**. Do not collapse the whole pricing page into one offer, and do not
treat the product's `pricing_url` as a substitute for offers: a single "Paid"
offer whose `price_description` concatenates several plans' prices loses the
per-plan structure the catalog is meant to expose.

Offers ride in through the `offers` reverse-FK **create envelope** — nested
under a product `create`, or as an `update` on an existing product that adds
`{"offers": {"create": [ … ]}}`. Per offer:

- `name` — the plan's public name (`"Starter"`, `"Standard"`, `"Professional"`,
  `"Enterprise"`). Together with `slug` (unique per product, e.g. `"starter"`)
  this is a **synthetic identifier**, not a world-claim — you choose it, so it
  is exempt from the citation bar.
- `price` + `price_currency` + `price_period` — set these structured fields when
  the plan maps to a single recurring amount (`price_period` is one of
  `one_time` | `monthly` | `yearly` | `usage_based` | `custom`; `price_currency`
  is required whenever `price` is set). The **price itself is a world-claim** —
  cite the pricing page that states it, exactly like any other affordance.
- `price_description` — use this instead of a structured `price` for free,
  "Starting from …", quoted, usage-based, or "Contact sales" / "Talk to sales"
  plans (a typical Enterprise tier). One human-readable line; do not enumerate
  other plans' prices here.

A monthly/yearly toggle is not two offers unless the vendor genuinely sells them
as distinct plans — pick the period you are citing (usually monthly list price)
and note the annual-discount nuance in `price_description` rather than inventing
a second offer.

```jsonc
"offers": {
  "create": [
    { "name": "Free", "slug": "free", "price_description": "Free plan for individuals." },
    { "name": "Starter", "slug": "starter", "price": "9.00", "price_currency": "USD", "price_period": "monthly" },
    { "name": "Enterprise", "slug": "enterprise", "price_description": "Custom pricing — contact sales." }
  ]
}
```

### After you submit: immutable, tracked, resubmit on rejection

You are the **submitter**. Once you `POST` a submission there is **no way to
edit it** — a submission is immutable by design. Track its outcome by polling
its status; it moves from `open` to one of two terminal states:

- **`merged`** — a curator published it to the catalog. Done.
- **`closed`** — it was rejected. Read `resolution.closed.reason` for why, then
  **submit a new, corrected submission** (there is nothing to "fix" on the old
  one). Two things close a submission:
  - **The system auto-rejects it** when a required check fails — most often
    `fact_check` on an uncitable claim, but also `spam`, `urls`, etc. The
    `close_reason` names the failed check; `resolution.closed.user` is
    `review-agent`. This is automatic and immediate — do not wait for a human.
    Fix the cited deficiency and resubmit.
  - **A curator closes it** on content grounds (thin citations, an uncited
    field, a duplicate, a merge conflict). Same recovery: read the reason,
    resubmit.

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/submissions/<submission-uuid>/" \
  -H "Authorization: Bearer ${OAG_TOKEN}" \
  | jq '{status, reason: .resolution.closed.reason, by: .resolution.closed.user}'
```

A check that `errored` (a transient fault, e.g. an LLM timeout) is **not** a
rejection: the submission stays `open` and the operator retries the check. You
do not need to resubmit for an errored check — only for a `closed` one.

**Verdicts are nondeterministic.** The same payload can pass one run and bounce
the next — a cert cited to the same page comes back `supported` once and
`unsupported` the next time. On a `closed` you believe is a false reject, **just
resubmit the same payload**; it often clears on a second pass before you start
stripping fields.

**Unwedging a slug held open by a review-side stall.** This applies to a
**create** submission (a new record claiming a `slug`), not an update. If the
review agent itself errors (a timeout, not a check failure), the create can sit
`open` with no decision — un-mergeable and un-closeable. A fresh create for the
same slug then returns `409 open_submission_conflict`, because the wedged
original still holds it. `force` only relaxes *this* open-create-conflict; it
does not bypass a conflict with an already-merged catalog object. Supersede the
wedged create by re-posting it with `"force": true`:

```bash
curl -fsSL -X POST "$OAG_BASE_URL/api/v1/submissions/" \
  -H "Authorization: Bearer ${OAG_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{ "app_label": "catalog", "model": "product", "submission_kind": "create",
        "force": true, "description": "…",
        "payload": { "slug": "<wedged-slug>", … } }' | jq
```

### Seeding several records at once (batch)

Adding one organization with nested products, categories, compliance
certifications, and MCP servers is more than the single-record `curl` calls
above cover. [references/batch-populating.md](references/batch-populating.md)
documents the nested payload envelope and ships three copy-paste scripts —
[`oag-validate-batch.sh`](references/batch/oag-validate-batch.sh) (dry-run),
[`oag-submit-batch.sh`](references/batch/oag-submit-batch.sh) (paced create),
and [`oag-watch.sh`](references/batch/oag-watch.sh) (poll to terminal, render
checks/reviews/resolution) — plus a starter
[batch template](references/batch/org-with-product.batch.json). They pace
automatically under the mutation rate limit, which a hand-rolled loop trips.

## MCP server (read-only)

If your agent host speaks MCP, you can add Open Agent Guide as a read-only MCP
server instead of calling the catalog endpoints with `curl`. It is a thin
wrapper over the same read API — same data, same auth.

- Endpoint: `$OAG_BASE_URL/mcp` (Streamable HTTP, session-less — each call is
  independent; no session persistence or server push)
- Auth: the same `oag_` bearer token, sent as `Authorization: Bearer <token>` by
  the MCP client. Anonymous reads also work; authenticate for identified usage.
- Tools: `search_products` (filter by `category`, `job_to_be_done`,
  `capability`, `organization` slugs), `get_product` (includes the AI-native
  affordance score and tier), `list_categories`, `list_jobs_to_be_done`,
  `list_capabilities`.

There are no MCP write tools: submissions, reviews, and account management stay
on the HTTP endpoints above.

## Pagination

Cursor-based:

```json
{ "next": "<cursor or null>", "previous": "<cursor or null>", "page_size_default": 20, "page_size_max": 100, "results": [ … ] }
```

Follow `next` until it is `null`. Do not infer page numbers from cursor values.
List endpoints default to `page_size=20` (max `100`); the response echoes those
limits in `page_size_default` / `page_size_max`.

### Loading reference/vocabulary tables without hitting the rate limit

To attach existing reference objects to a submission — compliance
certifications, licenses, MFA types, billing/payment methods, programming
languages — you sometimes enumerate the whole table to find the value you need.
Authenticated reads are capped at **120 / minute / token**, so a naive full
enumeration can hit `429`. Keep it cheap:

- **Prefer natural keys — usually you can skip enumeration entirely.** Reference
  and taxonomy `add`/`remove` entries and scalar foreign keys accept the
  object's `slug` directly, not just its UUID. Draft straight from the slugs you
  already hold (from seed data or a read-API response) instead of pre-building
  slug→UUID maps. Confirm what a field accepts with
  `/api/v1/submissions/fields/?app_label=<app>&model=<model>`.
- **When you do enumerate, request the max page size.** Append `?page_size=100`
  so a large table costs `⌈rows / 100⌉` requests instead of `⌈rows / 20⌉`. The
  licenses vocabulary alone is ~730 rows — ~8 requests at 100/page versus ~37 at
  the default 20.
- **Cache each vocabulary once per run.** These tables are small and change
  rarely (server cache lifetime is 1 h). Fetch each list once, build the slug→id
  map in memory, and reuse it across every submission in the batch. Re-fetching
  per submission is the usual reason a batch populator trips the read limit.
- **Back off on `429`.** Read `Retry-After` and wait before retrying; do not
  tight-loop.

## Errors

There are three error shapes — check which one you got before parsing:

- **Coded errors** (`401`, `403`, `404`, `429`) — auth, permission, missing
  resource, throttle:

  ```json
  { "code": "RATE_LIMITED", "detail": "Too many requests." }
  ```

  Common codes: `AUTHENTICATION_FAILED`, `INVALID_PARAMETER`,
  `MISSING_REQUIRED_FIELD`, `RATE_LIMITED`. `401` means the token is missing,
  wrong, or revoked — re-read it from your secret store before re-issuing.

- **Validation failures** (`400`) — a payload field the proposal validator
  rejects, the most common failure when submitting. The offending field paths
  are keyed under `errors`, *not* `detail`:

  ```json
  { "errors": { "payload.trust_center_url": ["Enter a valid URL."] } }
  ```

  Read `.errors` to see which field failed and why. (A malformed request body
  rejected by the *schema* before the domain validator runs is different: that
  is Django Ninja's default `422` with the error list nested **inside** `detail`
  — `{ "detail": [ { "type", "loc", "msg" }, … ] }`, no top-level `errors` key.)

- **Conflicts** (`409`) — a `create` that collides with an existing open
  submission or an already-cataloged object; `conflict_type` distinguishes the
  two (`open_submission_conflict` vs `existing_object_conflict`). Its own shape
  carries `code` + `detail` (like a coded error) plus `conflict_type`, `slug`,
  `existing_submission_id` **or** `existing_object_id` (whichever applies), and
  `links`. See "Unwedging a slug held open by a review-side stall" above.

## Rate limits

| Surface                 | Limit                          |
| ----------------------- | ------------------------------ |
| Anonymous catalog reads | 25 / minute / IP               |
| Authenticated reads     | 120 / minute / token           |
| Submission mutations    | 20 / minute + 5 / second burst |
| Signup                  | 10 / hour / IP                 |

Beyond the per-minute throttles, `POST /submissions/` also enforces a **cap of
25 open submissions per account** — it returns `429` once you hold that many
awaiting review, until some merge or close. Trusted populator accounts (the
`submissions.bulk_submit_catalogsubmission` permission / "Bulk submitters"
group) are exempt; that is the intended path for seeding a large batch.

Only the **signup** `429` currently carries `Retry-After` and the
`X-RateLimit-Limit` / `X-RateLimit-Remaining` / `X-RateLimit-Reset` headers —
honor `Retry-After` when it is present. The other throttles return a bare `429`
`{ "code": "RATE_LIMITED", "detail": … }` with no headers, so back off a few
seconds and retry.

## More

- [references/onboarding.md](references/onboarding.md) — signup payload schema,
  managing multiple named tokens, callback URLs, rotation cookbook.
- [references/api-reference.md](references/api-reference.md) — endpoint catalog
  organized by area (catalog, users, submissions).
- [references/batch-populating.md](references/batch-populating.md) — nested
  org+product payload envelope and the batch validate/submit/watch scripts.
- Live OpenAPI: `GET $OAG_BASE_URL/api/v1/openapi.json`
- Live docs UI: `$OAG_BASE_URL/api/v1/docs/`
- Homepage: <https://www.openagentguide.com>
