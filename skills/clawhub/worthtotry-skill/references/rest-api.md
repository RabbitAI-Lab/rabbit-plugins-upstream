# REST API

Use this when MCP is unavailable, when you need an endpoint MCP does not expose (comments, launch
stories), or when the person prefers a token to an OAuth consent screen.

Base URL: `https://worthtotry.com/api/v1`
Spec: `https://worthtotry.com/api/v1/openapi.json`
Reference: `https://worthtotry.com/api-docs`

## Authentication

Reads need nothing. Writes need `Authorization: Bearer <token>`, where the token is a personal
access token the person creates in their dashboard. Ask them for one; do not try to mint it.

The same ceiling applies here. Nothing in this API publishes a listing, sets a launch date, or takes
a payment.

## Endpoints

| Method | Path                     | Auth   | What it does                       |
| ------ | ------------------------ | ------ | ---------------------------------- |
| GET    | `/tools`                 | —      | Search and page the catalogue      |
| GET    | `/tools/{slug}`          | —      | One listing in full                |
| GET    | `/tools/{slug}/comments` | —      | Read a discussion                  |
| POST   | `/tools/{slug}/comments` | Bearer | Comment, or reply to one           |
| GET    | `/categories`            | —      | Every category, with counts        |
| POST   | `/readiness`             | —      | Audit a URL before submitting      |
| POST   | `/submissions`           | Bearer | Open a draft listing               |
| POST   | `/posts`                 | Bearer | Add a launch story to your listing |
| GET    | `/me/submissions`        | Bearer | Your listings and their status     |

## Audit a URL

```
curl -s -X POST "https://worthtotry.com/api/v1/readiness" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://theproduct.com"}'
```

Same six checks, same shape, as `check_submission_readiness`.

## Open a draft

```
curl -s -X POST "https://worthtotry.com/api/v1/submissions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://theproduct.com","tagline":"...","categories":["developer-tools"]}'
```

Body accepts `url` (required), `name`, `tagline`, `description`, `categories`, `pricing`,
`openSource`, `twitterHandle`, `targetKeyword` — the same fields and the same limits as
`submit_tool`. Returns 201 with a review link.

## Add a launch story

```
curl -s -X POST "https://worthtotry.com/api/v1/posts" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"toolSlug":"the-product","title":"...","body":"...","publishWithTool":true}'
```

`title` up to 120 characters, `body` 200 to 20,000 characters, **no links**. It is saved as a draft:
with `publishWithTool` true it goes live with the listing, otherwise the author publishes it. The
listing must be one the caller owns, or the response is 403.

## Errors

Every failure returns `{ "ok": false, "error": { "code", "message", "fields" } }` with a code of
`unauthorized`, `forbidden`, `not_found`, `invalid_request`, `duplicate`, `rate_limited` or
`server_error`. `fields` maps a field name to its message on a validation failure — relay those
verbatim.

Out-of-range values are rejected with 422, not silently clamped. A `limit` of 500 is an error, not a
page of 50.

Writes are rate limited per token; a 429 carries `retry-after` in seconds. Wait it out, do not
retry immediately.
