# courtlistener-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**3 endpoints across 1 platform group(s).**

## CourtListener (3)

### `courtlistener_courts`

- **HTTP:** `GET /courtlistener/courts`
- **What:** Browse CourtListener courts. Lists CourtListener's anonymous public court directory. Provide court_id to retrieve one court. page is used only for directory browsing and is 1-indexed. The endpoint does not retrieve dockets, opinions, judges, or account data.
- **Params:** `court_id` (string, optional) — CourtListener court identifier; `page` (integer, optional) — Directory page, 1-indexed

### `courtlistener_people`

- **HTTP:** `GET /courtlistener/people`
- **What:** Browse CourtListener judicial people. Lists CourtListener's anonymous public judicial-person directory, 20 people per page, with a cursor for the next page. Provide person_id to retrieve one public person record, which also carries position_count (the judicial and non-judicial positions on the person's public profile); directory listings omit position_count because the directory does not show positions. Sensitive biographical fields are excluded.
- **Params:** `cursor` (string, optional) — Opaque cursor from a prior response's next_cursor field; omit it for the first page. Ignored with person_id; `person_id` (integer, optional) — CourtListener person identifier

### `courtlistener_search`

- **HTTP:** `GET /courtlistener/search`
- **What:** Search CourtListener opinions. Searches CourtListener's public opinion search by text and returns one page of up to 20 opinion results (case name, court, date filed, docket number, citations, snippet and opinion URL) with a cursor for the next page. Each result's court is the short court name CourtListener shows next to the case; court_id is not returned. The endpoint does not return opinion text, dockets, judges, alerts, or account data.
- **Params:** `cursor` (string, optional) — Opaque cursor from a prior response's next_cursor field; omit it for the first page; `q` (string, **required**) — Opinion search text
