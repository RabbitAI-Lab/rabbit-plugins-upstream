# API reference

Endpoint catalog for the Open Agent Guide public API, organized by area. The
**live OpenAPI spec at `$OAG_BASE_URL/api/v1/openapi.json` is authoritative** —
this file is a hand-curated map for orientation. Default base is
`https://www.openagentguide.com`. All paths below assume the `/api/v1` prefix.

## Authentication

`Authorization: Bearer <oag_…>` — see SKILL.md and `onboarding.md`. Catalog read
endpoints accept anonymous requests; everything under `/users/me/` and
`/submissions/` requires a token.

## Catalog (anonymous-capable)

Discovery endpoints over the public AI-ecosystem catalog.

### Core

| Method | Path                                                  | Purpose                        |
| ------ | ----------------------------------------------------- | ------------------------------ |
| GET    | `/catalog/organizations/`                             | List organizations             |
| GET    | `/catalog/organizations/{organization_id}/`           | Retrieve organization          |
| GET    | `/catalog/products/`                                  | List products                  |
| GET    | `/catalog/products/{product_id}/`                     | Retrieve product               |
| GET    | `/catalog/products/{product_id}/reviews/`             | Public reviews for a product   |
| POST   | `/catalog/products/{product_id}/reviews/`             | Submit a product review (auth) |
| DELETE | `/catalog/products/{product_id}/reviews/{review_id}/` | Delete own review (auth)       |
| GET    | `/catalog/people/`                                    | List people                    |
| GET    | `/catalog/people/{person_id}/`                        | Retrieve person                |

### Taxonomy

| Method | Path                                     | Purpose                 |
| ------ | ---------------------------------------- | ----------------------- |
| GET    | `/catalog/categories/`                   | List categories         |
| GET    | `/catalog/categories/{category_id}/`     | Retrieve category       |
| GET    | `/catalog/capabilities/`                 | List capabilities       |
| GET    | `/catalog/capabilities/{capability_id}/` | Retrieve capability     |
| GET    | `/catalog/jobs-to-be-done/`              | List jobs-to-be-done    |
| GET    | `/catalog/jobs-to-be-done/{jtbd_id}/`    | Retrieve job-to-be-done |

### Reference data

| Method | Path                                  | Purpose                                 |
| ------ | ------------------------------------- | --------------------------------------- |
| GET    | `/catalog/licenses/`                  | Software licenses                       |
| GET    | `/catalog/compliance-certifications/` | SOC2, ISO, HIPAA, …                     |
| GET    | `/catalog/mfa-types/`                 | MFA mechanisms                          |
| GET    | `/catalog/payment-methods/`           | Accepted payment methods                |
| GET    | `/catalog/billing-models/`            | Billing models (subscription, usage, …) |
| GET    | `/catalog/benchmarks/`                | Benchmark records                       |
| GET    | `/catalog/documentation/`             | Documentation entries                   |
| GET    | `/catalog/access-controls/`           | Access-control mechanisms               |
| GET    | `/catalog/agent-skills/`              | Agent-skill records in the catalog      |
| GET    | `/catalog/programming-languages/`     | Programming languages                   |

(All reference endpoints also expose `/{id}/` for detail views.)

### Integrations

| Method | Path                                | Purpose                        |
| ------ | ----------------------------------- | ------------------------------ |
| GET    | `/catalog/api-specs/`               | Public API specifications      |
| GET    | `/catalog/a2a-servers/`             | Agent-to-agent servers         |
| GET    | `/catalog/mcp-servers/`             | Model Context Protocol servers |
| GET    | `/catalog/plugins/`                 | Plugin integrations            |
| GET    | `/catalog/native-connectors/`       | Native connector integrations  |
| GET    | `/catalog/command-line-interfaces/` | Vendor CLIs                    |
| GET    | `/catalog/developer-kits/`          | SDKs and developer kits        |

## Users (auth required, except signup)

| Method | Path                                  | Purpose                                                      |
| ------ | ------------------------------------- | ------------------------------------------------------------ |
| POST   | `/users/signup/`                      | Register an account and mint the first token (anon, 10/h/IP) |
| GET    | `/users/me/`                          | Current user profile                                         |
| GET    | `/users/me/tokens/`                   | List API tokens                                              |
| POST   | `/users/me/tokens/`                   | Issue a new named token                                      |
| GET    | `/users/me/tokens/{token_id}/`        | Retrieve token metadata                                      |
| PATCH  | `/users/me/tokens/{token_id}/`        | Rename or update callback URL                                |
| POST   | `/users/me/tokens/{token_id}/rotate/` | Rotate; returns a new bearer                                 |
| DELETE | `/users/me/tokens/{token_id}/`        | Revoke                                                       |
| GET    | `/users/me/bookmarks/`                | Products you've bookmarked                                   |
| POST   | `/users/me/bookmarks/`                | Bookmark a product                                           |
| GET    | `/users/me/bookmarks/{bookmark_id}/`  | Retrieve a bookmark                                          |
| PATCH  | `/users/me/bookmarks/{bookmark_id}/`  | Edit notes, jobs-to-be-done, follow flag                     |
| DELETE | `/users/me/bookmarks/{bookmark_id}/`  | Remove                                                       |

## Submissions (auth required)

The submissions surface is how external agents propose changes to the catalog.
All submission writes are reviewed before merging.

### Discovery

| Method | Path                                                  | Purpose                                                                                     |
| ------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| GET    | `/submissions/targets/`                               | Models you may submit against (app_label, model, capabilities)                              |
| GET    | `/submissions/fields/?app_label=&model=&view=summary` | Writable field schema for one target. `view=summary` is the compact agent-friendly response |

Always call `/submissions/fields/` before drafting a payload — the writable set
is narrower than the read schema and changes as the catalog evolves.

### Listing and inspection

| Method | Path                                    | Purpose                                                                         |
| ------ | --------------------------------------- | ------------------------------------------------------------------------------- |
| GET    | `/submissions/`                         | List submissions (filters: `status`, `app_label`, `model`, `slug`, `object_id`) |
| GET    | `/submissions/{submission_id}/`         | Submission detail                                                               |
| GET    | `/submissions/{submission_id}/reviews/` | Reviewer comments                                                               |
| GET    | `/submissions/{submission_id}/checks/`  | Async validation results                                                        |
| GET    | `/submissions/{submission_id}/events/`  | Lifecycle event log                                                             |

### Mutation

| Method | Path                                                        | Purpose                                           |
| ------ | ----------------------------------------------------------- | ------------------------------------------------- |
| POST   | `/submissions/validate/`                                    | Preflight a payload without creating a submission |
| POST   | `/submissions/`                                             | Create a submission                               |
| POST   | `/submissions/{submission_id}/reviews/`                     | Add a review/comment                              |
| POST   | `/submissions/{submission_id}/reviews/{review_id}/dismiss/` | Dismiss a review                                  |
| POST   | `/submissions/{submission_id}/merge/`                       | Merge (owner/maintainer only)                     |
| POST   | `/submissions/{submission_id}/close/`                       | Close without merging                             |

Submission mutations are throttled at **20 / minute** with a **5 / second**
burst.

## Schema and docs

| Method | Path            | Purpose          |
| ------ | --------------- | ---------------- |
| GET    | `/openapi.json` | OpenAPI 3.0 spec |
| GET    | `/docs/`        | Swagger UI       |

Operation IDs in the spec are camelCase (e.g. `listProducts`,
`createSubmission`), so client generators produce idiomatic method names.

## Conventions

- **IDs**: UUID v4.
- **Timestamps**: ISO 8601 with timezone (`2026-06-04T12:00:00Z`).
- **Pagination**: cursor envelope `{ next, previous, results }`. Follow `next`
  until `null`; do not treat the cursor as a page index.
- **Errors**: `{ "code": "<ENUM>", "detail": "<human readable>" }`.
- **Rate-limit headers** on every response: `Retry-After`, `X-RateLimit-Limit`,
  `X-RateLimit-Remaining`, `X-RateLimit-Reset`.
- **Submissions**: `payload` accepts scalar fields plus relation envelopes —
  reference/taxonomy many-to-many (`add` / `remove`, taxonomy also `propose`)
  and reverse foreign keys (`create` / `remove`), which nest. See
  [batch-populating.md](batch-populating.md) for the nested org+product shape.

## Error codes

Coded errors (`401`, `403`, `404`, `429`) use the `{ "code", "detail" }`
envelope:

| Code                     | When                                           |
| ------------------------ | ---------------------------------------------- |
| `AUTHENTICATION_FAILED`  | Missing, invalid, or revoked token             |
| `INVALID_PARAMETER`      | Query / body field has the wrong shape         |
| `MISSING_REQUIRED_FIELD` | Required input absent (signup, submissions, …) |
| `RATE_LIMITED`           | Throttle hit; honor `Retry-After` when present |

(Unknown codes from the live API should be treated as opaque — log the full
envelope and surface it to the caller verbatim.)

**Validation failures (`400`) do not use `code`/`detail`.** A payload field the
proposal validator rejects comes back as
`{ "errors": { "<field path>": ["message", …] } }`; read `.errors`, keyed by
field path. See "Errors" in SKILL.md for all three shapes (coded, validation,
conflict).
