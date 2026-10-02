# Batch populating

Seeding several catalog records in one pass — a new organization with nested
products, their categories, compliance certifications, and MCP servers — is more
than the single-record `curl` one-liners in [SKILL.md](../SKILL.md) cover. This
directory ships the three scripts a populator otherwise hand-rolls: a
`/validate/` dry-run, a paced submit pass, and a poller that renders each
submission's checks, reviews, and resolution.

The scripts are `bash` + `curl` + `jq`, matching the skill's existing style.
They own the non-obvious parts — the nested payload envelope, rate-limit pacing,
and walking the sub-resource links to answer "did my batch pass?" — so you don't
rediscover them per run.

> A contract test (`test_skill_batch_reference.py` in the `submissions` app)
> round-trips the template below through the live API endpoints and asserts
> every JSON path these scripts read. If the API drifts, that test fails — so
> the scripts and this doc can't silently rot.

## Files

| File                                                                     | Role                                                                     |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| [`batch/org-with-product.batch.json`](batch/org-with-product.batch.json) | Payload template: one org with a nested product and its relations        |
| [`batch/oag-common.sh`](batch/oag-common.sh)                             | Shared helpers — auth, rate-limit pacing, 429 back-off. Sourced, not run |
| [`batch/oag-validate-batch.sh`](batch/oag-validate-batch.sh)             | Dry-run every body against `POST /submissions/validate/`                 |
| [`batch/oag-submit-batch.sh`](batch/oag-submit-batch.sh)                 | Create each submission, capture the returned ids                         |
| [`batch/oag-watch.sh`](batch/oag-watch.sh)                               | Poll ids to a terminal state; render checks / reviews / resolution       |

## The batch file

A JSON array of submission bodies — the same shape you would `POST` to
`/submissions/` individually. Each body is
`{ app_label, model, submission_kind, description, payload }`.

The template is a **create** for a `catalog.organization` with one nested
product. The payload envelope is the part worth memorizing, because
`/submissions/fields/` describes each model in isolation but not how they nest:

```jsonc
"payload": {
  "name": "Example AI", "slug": "example-ai", "url": "…", "description": "…",
  "products": {                       // reverse FK (one-to-many): create | remove
    "create": [
      {
        "name": "Example Browser", "slug": "example-browser", "description": "…",
        "categories":                 { "add": ["browser-automation"] },  // taxonomy: add | remove | propose
        "compliance_certifications":  { "add": ["soc-2"] },               // reference vocab: add | remove
        "mcp_servers":                { "create": [ { "name": "…", "url": "…" } ] } // nested reverse FK
      }
    ]
  }
}
```

Three envelope kinds show up, each with its own operations:

- **Reverse FK (one-to-many)** — `products`, `mcp_servers`, `api_specs`,
  `offers`: `create` child objects (or `remove` by id). Nested creates recurse,
  so a product created under an org can itself carry `mcp_servers.create` and
  `offers.create`. **Model one `offer` per published pricing plan** (Free /
  Starter / Standard / Professional / Enterprise, …) rather than lumping the
  pricing page into a single offer — see SKILL.md → "Break pricing into one
  offer per plan".
- **Reference vocabulary (many-to-many)** — `compliance_certifications`,
  `licenses`, `access_controls`: `add` / `remove` an **existing** row. These are
  closed, staff-curated tables; you attach, you don't mint.
- **Proposable taxonomy (many-to-many)** — `categories`, `capabilities`,
  `jobs_to_be_done`: `add` / `remove` an existing term, or `propose` a brand-new
  one inline (deduped against existing slugs).

**Reference existing objects by natural key, not UUID.** Every `add` / `remove`
entry and scalar foreign key accepts the object's `slug` directly (ADR-0020), so
you rarely need to enumerate a vocabulary table first — draft straight from the
slugs you already hold. `soc-2`, `browser-automation` above are slugs. (See
SKILL.md → "Loading reference/vocabulary tables without hitting the rate
limit".)

Confirm the writable field set for any model before drafting:

```bash
curl -fsSL "$OAG_BASE_URL/api/v1/submissions/fields/?app_label=catalog&model=product&view=summary" \
  -H "Authorization: Bearer ${OAG_TOKEN}" | jq
```

## The loop: validate → submit → watch

```bash
export OAG_TOKEN=oag_...        # bearer token, see SKILL.md
# Optional: this is also the default for every batch script.
export OAG_BASE_URL=https://www.openagentguide.com
cd references/batch

# 1. Dry run. Catches payload-shape and natural-key errors before you create anything.
./oag-validate-batch.sh org-with-product.batch.json

# 2. Create. Paced under the mutation limit; writes new ids to submitted-ids.txt.
./oag-submit-batch.sh org-with-product.batch.json submitted-ids.txt

# 3. Watch to terminal. Renders per-check status, then the resolution reason.
./oag-watch.sh --file submitted-ids.txt
```

`oag-watch.sh` walks `links.checks` per submission because the detail endpoint
deliberately omits inline checks and reviews (sub-resource envelopes). It reads
the two-tier `resolution.{merged,closed}` shape to print *why* a submission
settled — `resolution.closed.reason` on a reject, `resolution.merged.summary` on
a merge.

## Rate limits and pacing

Submission mutations are capped at **20 / minute + 5 / second burst**. A
validate + submit + resubmit loop over ten items brushes that ceiling, and one
accidental re-run of a submit pass will return `429` mid-batch. The scripts pace
automatically:

- `oag-common.sh` sleeps `OAG_MUTATION_PACE_SECONDS` (default **3.5s**) between
  mutating calls — ~17/min, under the 20/min ceiling with headroom.
- On a `429` it waits and retries up to `OAG_MAX_ATTEMPTS` (default 5) —
  honoring `Retry-After` if present, else pausing `OAG_MUTATION_PACE_SECONDS`.
  The submission-mutation throttle currently sends no `Retry-After`, so the pace
  fallback is what fires; the open-submission-cap `429` below is *not*
  transient, so those attempts will exhaust and still fail (use a bulk-submitter
  account).

Two more caps to know:

- **Open-submission cap: 25 per user.** `POST /submissions/` returns `429` once
  you have 25 open submissions awaiting review. Trusted populator accounts in
  the "Bulk submitters" group (the `submissions.bulk_submit_catalogsubmission`
  permission) are exempt — that is the intended way to seed a large batch in one
  pass.
- **Authenticated reads: 120 / minute / token.** The watcher's per-submission
  `links.checks` fetch counts against this; a very large batch polled tightly
  can brush it, so `oag-watch.sh` sleeps `OAG_WATCH_INTERVAL` (default 15s)
  between rounds.

## Recovering rejects

Submissions are immutable — you don't fix one, you submit a corrected new one
(SKILL.md → "After you submit"). For a batch:

- Read each `resolution.closed.reason` from the watcher output, correct the
  offending body in the batch file, and re-run submit + watch on just those
  rows.
- **Verdicts are nondeterministic.** A body that closed on what looks like a
  false reject often clears on a straight resubmit before you start stripping
  fields — try that first.
- A create wedged `open` by a review-side stall holds its slug; supersede it by
  re-posting with `"force": true` (SKILL.md → "Unwedging a slug").

## Someday / maybe: an `oag` CLI

A possible future `oag` CLI could replace these scripts:

```text
oag validate <file>     # dry-run a batch
oag submit <file>       # create, pacing under the rate limits
oag status <id>         # one submission's checks / reviews / resolution
oag watch <ids…>        # poll a set to terminal
```

The CLI would own the payload envelope as typed constructors, pace calls under
the limits without the caller thinking about it, and render check/review/
resolution state as a table. **These scripts are its executable spec** — the
behaviors above are exactly what the CLI must reproduce.

It is intentionally deferred. Batch automation only pays off once the merge rate
is high enough to seed in volume; until then the scripts are enough. When it's
time to build it, first decide the implementation language and the tooling for
**creating and maintaining a CLI plus a reusable client library** in that
language — the CLI and the library want to share one typed model of the API, and
the choice of language, argument parser, HTTP client, and release/versioning
story should be made deliberately rather than defaulted to whatever wrote the
scripts.
