---
name: danube
description: Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services. Search, inspect, and execute tools over native MCP or plain curl, with explicit confirmation before anything that writes, sends, spends, or deletes.
metadata:
  openclaw:
    emoji: "🌊"
    homepage: https://docs.danubeai.com/sdk/openclaw
    requires:
      env:
        - DANUBE_API_KEY
      bins:
        - curl
    primaryEnv: DANUBE_API_KEY
    envVars:
      - name: DANUBE_API_KEY
        required: true
        description: Danube API key from https://danubeai.com/dashboard/api-keys (API Keys in the dashboard sidebar; an opaque token — no fixed prefix)
    always: false
---

# Danube — Governed Tool Access for Agents

Danube makes an organization's own tools — plus a large and growing catalog of ready-made services — callable by AI agents through a single API key, with permissions, spending limits, and an audit trail handled by the platform. The catalog changes constantly and includes tools the user's organization connected privately, so **never assume what is available — search first.**

## Guardrails (read these first)

- **Read freely, act with consent.** Discovery — listing services, searching tools, reading schemas, checking ratings, balances, or limits — needs no confirmation. Before any action that **writes, sends, posts, deletes, purchases, spends wallet funds, stores a credential, changes spending limits, or creates/updates/deletes a skill or workflow** — and before **any batch execution** — show the user the exact tool and parameters and get an explicit "yes".
- **Honour the confirmation handshake.** If `execute_tool` comes back with `_meta.confirmation_required: true`, the account's key requires consent for destructive calls: show the user the tool and the `parameters` from the response, get an explicit yes, then call again with the `confirm_token` (valid 5 minutes). Never call again with the token without asking. **Re-send your own original parameters, not the ones the response displayed** — those are passed through the redactor first, so a credential-shaped value comes back as `[REDACTED:…]`, while the token is signed over what you actually sent; echoing the masked form back invalidates it.
- **Its silence is not a safety verdict.** That gate reads the publisher's `metadata.destructive` **first, and whatever it says wins**; only when the tool row carries no such flag does the method decide — anything but GET/HEAD/OPTIONS, so an HTTP verb or `COMPOSITE` qualifies. So the flag works in both directions: it can mark a tool served by an **MCP server** (those carry the method `MCP`, which says nothing about what they do, and go through unmarked otherwise), and it can clear *any* tool whose method would otherwise qualify — a `DELETE` or a `COMPOSITE` just as readily as the POST-based read the opt-out was meant for. A call that arrives without a handshake has not been judged harmless: the rule above is the only thing in front of it, and the account may not have `require_confirmation` turned on at all.
- **In a batch, the handshake is per entry — and only completable over REST.** Each entry of `POST /tools/call/batch` takes its own `confirm_token` beside its `tool_input`, and an entry refused for consent comes back as an element with `success: false` and its own `confirmation_required` block (the token, `expires_in`, the tool and the parameters) while the batch as a whole still answers `200`. `batch_execute_tools` over MCP carries neither direction: a `confirm_token` on a call is dropped before the request, and the element you get back keeps only the message. If an entry needs confirmation there, take that one call out of the batch and run it through `execute_tool`, which does take the token.
- **Never invent credentials.** Only store an API key the user has explicitly handed you in this conversation, and confirm before storing. Otherwise send them to https://danubeai.com/dashboard to connect the service themselves.
- **Least data.** Pass only the parameters the task needs; don't forward unrelated personal data to third-party services.
- **Respect limits.** Don't raise spending limits or fund wallets unless the user asks for exactly that.
- **Report specifics.** After executing, say which tool ran, with what inputs, and what came back — not just "done".

## Setup

### 1. Get an API key

From the dashboard: https://danubeai.com/dashboard/api-keys (**API Keys** in the sidebar). Keys are opaque ~43-character tokens with **no fixed prefix** — don't validate their shape, just keep them secret.

Or let the user authorize this agent with the OAuth 2.0 Device Authorization flow (RFC 8628):

```bash
curl -s -X POST https://api.danubeai.com/v1/auth/device/code \
  -H "Content-Type: application/json" -d '{"client_name": "OpenClaw"}'
# → {"device_code": "...", "user_code": "XXXX-XXXX", "verification_url": "...", "expires_in": 600, "interval": 5}
```

Tell the user to open `verification_url` in a browser and enter `user_code`. Then poll:

```bash
curl -s -X POST https://api.danubeai.com/v1/auth/device/token \
  -H "Content-Type: application/json" -d '{"device_code": "DEVICE_CODE_FROM_ABOVE"}'
```

`428` = not approved yet (poll every `interval` seconds) · `200` = `{"api_key": "…"}` · `410` = expired, start over.
The two failures come back in Danube's standard error envelope, with the OAuth state as the
*message*: `{"error": {"code": "precondition_required", "message": "authorization_pending"}}` and
`{"error": {"code": "gone", "message": "expired_token"}}`. Poll on the status code: the body's
only top-level key is `error`, and it holds an object — there is no `detail` key and no bare
state string to match.

**Respect `interval`, and know that a fourth status can appear.** The code is good for
`expires_in` seconds (600, i.e. ten minutes) and the two endpoints carry rate limits of their
own: 10 requests/minute on `/auth/device/code` and 30/minute on `/auth/device/token`. These
calls are unauthenticated, so there is no key to count them against — the bucket is keyed by
the client address *as the server sees it*, which behind a hosted deployment's edge may be far
more widely shared than your own machine or egress. Treat the 30/minute as a limit you could
meet even when nothing is wrong. At the advertised `interval` of 5 seconds you poll 12 times a
minute, which is the rate the flow is designed around; poll tighter and you are spending someone
else's headroom as well as your own.

The resulting `429` is **not** one of the three statuses above, so don't read it as a failed
authorization — it says nothing about whether the user has approved. Back off by `Retry-After`
(see *The two `429`s* below) and carry on polling **the same `device_code`**: a rate-limited
poll never reaches the handler, and an ordinary pending one changes nothing, so the code stays
valid for the rest of its ten minutes. Starting a fresh flow instead spends one of the
10/minute on the other endpoint and makes the user enter a new `user_code`.

### 2. Make the key available to OpenClaw

Set `DANUBE_API_KEY` in the environment, or in `openclaw.json`:

```json5
{ skills: { entries: { danube: { apiKey: "YOUR_DANUBE_API_KEY" } } } }
```

### 3a. Connect natively over MCP (recommended)

OpenClaw has a built-in MCP client. Register Danube's server once and its tools become ordinary OpenClaw tools (`search_tools`, `execute_tool`, …):

```bash
openclaw mcp set danube '{"url":"https://mcp.danubeai.com/mcp","transport":"streamable-http","headers":{"danube-api-key":"YOUR_DANUBE_API_KEY"}}'
openclaw mcp doctor danube --probe
```

Use the real key value in `headers` (not `${DANUBE_API_KEY}`). The server also speaks MCP OAuth: use `"auth":"oauth"` instead of `headers`, then `openclaw mcp login danube`.

To keep the tool list small, append `?tools=core` to the URL, or a comma list such as
`?tools=core,workflows`; without it all 31 tools are described to the model. The five groups are
`core` (10 — discovery, execution, credentials, and `report_tool`), `workflows` (6), `wallet` (6),
`skills` (5) and `feedback` (4 — `submit_rating`, `get_my_rating`, `get_tool_ratings`,
`get_recommendations`). `core` is added to whatever you ask for, so search and execute can't be
filtered out by accident (`?tools=wallet` lists 16). Unrecognised names are dropped silently: a
typo alongside a valid group just gives you fewer tools than you asked for (`?tools=core,workfows`
lists the same 10 as `?tools=core`), and if *none* of the names is a real group the parameter is
ignored altogether and you get the full 31. Either way it fails quietly, never with an error.

**The filter narrows `tools/list` and nothing else.** `tools/call` is deliberately not filtered, so
a connection opened with `?tools=core` can still run a tool from a group it never listed, as long
as it knows the name — live on 2026-09-23, `get_tool_ratings` and `get_spending_limits` both
returned normally over a `?tools=core` connection whose `tools/list` held ten tools. That is
convenient (no reconnecting to rate a tool you just ran) and worth not misreading in the other
direction: the parameter is a context-size setting, not a permission boundary. Nothing on the
connection restricts which of the 31 tools may be called. A key's own `allowed_services` /
`allowed_tools` permissions, set in the dashboard, are a different control and don't close that
gap either — they scope which *marketplace* services and tools the key may search and execute, not
which of Danube's own MCP tools it may use.

### 3b. Or use plain `curl` — no MCP needed

Every capability below is also a REST call against `https://api.danubeai.com/v1` with the header `danube-api-key: $DANUBE_API_KEY`. Copy-paste recipes: `{baseDir}/references/rest-api.md`.

## Working with tools

Every task follows **Explore → Inspect → (Confirm) → Execute → Report.**

| Goal | MCP tool | REST |
|---|---|---|
| See what services exist | `list_services(query, limit)` | `GET /services` |
| Find a tool for a task | `search_tools(query, service_id?, limit?)` | `GET /tools/search?query=…` |
| All tools of one service | `get_service_tools(service_id, limit?)` — `limit` defaults to **50** | `GET /services/{id}/tools` (no limit; returns every tool) |
| Full schema of one tool | returned by the calls above | `GET /tools/{tool_id}/describe` (prefer it to the bare `GET /tools/{tool_id}` — see below) |
| Run a tool | `execute_tool(tool_id, parameters, fields?)` | `POST /tools/call/{tool_id}` with `{"tool_input": {…}}` |
| Run up to 10 at once | `batch_execute_tools(calls)` | `POST /tools/call/batch` |
| Inspect one tool before first use | `describe_tool(tool_id)` | `GET /tools/{tool_id}/describe` |
| Read a stored result back | `fetch_result(execution_id, path?, max_response_chars?)` | `GET /tools/executions/{execution_id}/result?path=…&max_chars=…` |
| Remember a per-service default | `set_parameter_defaults(service_id, defaults)` | `PUT /services/{service_id}/parameter-defaults` |

**`GET /v1/tools/{tool_id}` works again — `/describe` is still what to read before executing,
and the collection route beside it is still unusable.** Until 2026-09-24 the per-tool route
answered `422`,
demanding a query parameter `r` that had no valid value, because its auth dependency was written
as `Depends(lambda r: …)` and FastAPI read that lambda's unannotated `r` as a required *query*
parameter. That is fixed: both routes now depend on the real dependency, and the per-tool route
returns the tool row normally — verified live on 2026-09-24, `200` with the full object both
plain and with a leftover `?r=1`. If you are talking to a backend deployed before that date you
may still meet the `422`; there is nothing to report or retry either way, just use `/describe`.

**Still read `GET /v1/tools/{tool_id}/describe` before a first call — but the two are not
nested, so know what each one drops.** `/describe` is what adds the things you actually need
before executing: `required`, the tool's recent `usage`, your own `examples`, saved `defaults`,
and *populated* `readiness`, `configuration_url` and `reliability`. The bare route declares
those last three and returns them `null` — it runs no enrichment — so it cannot answer "can I
call this now". What the bare route carries and `/describe` leaves out is the plumbing:
`base_url`, `path`, `slug`, `tags`, `version`, `metadata`, `security_schemes` and
**`sunset_date`**. That last one matters, because this file tells you to read `deprecated`
together with `sunset_date` and `/describe` has only the first two of that trio. Both take a
slug as readily as a UUID (verified live: `…/tools/gmail-send-email` and
`…/tools/gmail-send-email/describe` both `200`). One caution on the bare row: its pricing
fields are unenriched defaults, so `is_paid` reads `false` and `price_per_call_cents` `null`
even on a priced tool — read a price off a search result, never off this route.

**`GET /v1/tools` (the whole collection) is a separate problem and not worth calling.**
It takes no pagination parameters at all and returns *every* tool row in the catalog — 12,583
of them on 2026-09-24 — and you cannot get an answer out of it: probed four times that day it
answered `500` (after 9–12 s) or, once the edge's ~31 s ceiling was reached, `504`. The
unpaginated contract is the likely reason; the `500` is not explained by anything visible to a
caller. Either way, don't retry it. Use `GET /v1/tools/search?query=…` for discovery, or
`GET /v1/services/{id}/tools` for one service's full list.

**Without a key those two routes answer `401`, not the body** — the collection and per-tool
routes are mounted with a key dependency, and a dependency that rejects you raises before
anything else runs (verified live 2026-09-24). Read a `401` there as being about your key.
`/describe` is *not* on that router and needs no key at all — it answered `200` unauthenticated
on 2026-09-24. Over MCP none of this applies: `search_tools`, `get_service_tools` and
`describe_tool` all carry the schema.

### Reading what comes back

`execute_tool` returns `{result, _meta}` once a call actually reaches a tool. When the tool
returned JSON, the already-parsed object is at **`result.data`** — read that;
`result.content[0].text` is the same thing serialised for MCP clients that only read the
transport envelope, so don't `json.loads()` your way down to it. Don't index `_meta`
blindly: it is absent when the lookup itself failed (no `tool_id` or `tool_name` given, or
neither resolves).

**When the payload is not JSON there is no `result.data` at all** — plan for that rather than
reading a missing key as an empty result. Danube adds `data` only when the upstream body (or,
on an MCP server, one of its text blocks) parses as JSON, so a tool that answers in Markdown
or prose has none, whichever kind of service it is: live, the HTTP tool `ClawHub - Get Skill
File` returned 25,635 characters of Markdown under `content[0].text` with no `data`, and the
MCP-backed `Cloudflare Documentation.migrate_pages_to_workers_guide` did the same with its
5,423-character guide. Fall back in this order: `result.data` when it is there, then
`result.structuredContent` on an MCP-backed tool that sends one, and only then
`result.content[0].text`. `structuredContent` comes second on purpose: `max_response_chars`
trims `content[]` text blocks and **nothing else**, so on a large result the text block can
come back cut while `structuredContent` beside it is whole — live on
`Cloudflare Documentation.search_cloudflare_documentation`, a call capped at 100 chars
returned a 100-char text block with a truncation note and ~16 KB of intact `structuredContent`.
Read the trade before relying on it: that block is not covered by your cap and its size is not
counted in `_meta`, so preferring it can pull far more into your context than you asked for.
Over REST Danube adds no `data` key on any path: `result` is the upstream body, or for an
`mcp_server` service the upstream envelope, so a `data` you do find there is the upstream's own.

Oversized payloads are trimmed. A JSON array is trimmed at element boundaries, so it stays
parseable; plain text is cut mid-string with an inline `... [truncated - response was N
chars, …]` note; and a JSON object with no array big enough to trim degrades to
`{"_truncated_partial_json": "<prefix>", "_truncated": true}` — valid JSON, but the
object's own keys are gone, so re-request it rather than parsing that. Check
`_meta.truncated`, and `_meta.truncation_note` for what went. To get the rest, raise
`max_response_chars` (default 50000, hard max 500000) or follow `_meta.cursor` when the
upstream paginates. When a tool is resolved by *name*, a publisher's lower per-tool default
can apply, so trimming below 50000 is normal there. **Inside `batch_execute_tools` the
per-element default is lower — 32000 over MCP, since a batch multiplies it by up to ten** — so
a payload that survives a single call can still be trimmed as one element of a batch. (Raw
REST has no such batch default; an entry with no `max_response_chars` gets 500000.) Truncated
≠ broken — don't `report_tool` it.

**A slow MCP-backed tool can be given more time.** `execute_tool` takes `timeout_seconds` for a
single call — 1 to 300, defaulting to about 30 — and `POST /tools/call/{tool_id}` accepts the
same key beside `tool_input`. It reaches only tools served by an MCP server (an Apify actor
run, a crawl, a report rendered server-side are the cases worth raising it for). **On an `api`
service it is accepted and then ignored**: an HTTP tool's budget comes from its own catalog row
(30 s unless the publisher set otherwise), which a caller cannot extend — so if one of those
keeps timing out, the fix is a narrower request or a `report_tool`, not a bigger number. Past
300 seconds the work belongs in an asynchronous flow either way: start it, keep the handle it
returns, and poll with that service's own status tool.

**Credential values are masked before you ever see them.** Every tool response passes
through Danube's redactor on the way out, and unless the tool is one specifically declared
as returning a credential (see below), anything that reads as a secret — API keys, tokens,
passwords, connection strings — comes back as `[REDACTED:<FIELD>]`. That is
platform policy, not a broken tool: don't `report_tool` it, and don't ask the tool to
return the raw value. When there is something to report, the redaction object carries an
exact `count` plus a `fields` list — the first 50 masked values, each with its `path`,
`key`, and the `rule` that caught it — and a `mode`. It lives at `_meta.redaction` over
MCP, where the key is absent when nothing was masked, and at top-level `redaction` over
REST, where the key is always present and simply `null`. Either way, test the value, not
the key. Pagination cursors and identifiers are exempt by name, so paging keeps working.

A tool whose whole *purpose* is to mint a credential is not redacted into uselessness.
Where Danube can, it captures the secret for you: the new value is stored as the user's
credential for the target service and `_meta.redaction.stored_credentials` says where it
landed, so the service's later calls pick it up through ordinary credential injection and
you never hold the value.

**Where it can't, the secret reaches you raw** — a tool marked as returning a credential
with no capture mapping, a self-hosted deployment (custody stays in the customer's own
environment), or a store that failed. These come back completely unmasked with
`_meta.redaction.passthrough_reason` explaining why, alongside `count: 0`. This is
not limited to short-lived handoff tokens like a Plaid *link* token: a Plaid **access**
token, a rotated webhook signing secret, and other durable secrets pass through this way.
Treat anything that arrives unmasked as a live secret — show the user where to put it,
don't echo it back, and don't paste it into a later call's parameters.

Discovery tips:
- Every search result carries `readiness`: `ready` means you can execute it now, `needs_credential` means the service needs a credential this account has not connected (send the user to `configuration_url`), `unavailable` means the service is retired. Ready tools are listed first; prefer a ready tool over a better-named one that needs setup.
- Every result also carries `deprecated`, `deprecation_message` and `sunset_date`. A deprecated tool is still listed and still runs while its sunset date is absent or in the future — that is an advance warning, and the message usually names what to use instead, so read it and switch rather than reporting the tool. Once the date has passed the tool disappears from search altogether, and `execute_tool` refuses it before calling anything — the message reads "… was deprecated and passed its sunset date (DATE): … No call was made." Both transports now name it outright: `error_type` is `tool_sunset` with `fault: "danube"` — top-level over REST, in `_meta` over MCP. (Until 2026-09-10 the value was the upper-case `TOOL_SUNSET` and the MCP layer passed no field at all, so keep matching the message text too if you may be talking to an older backend.) Search again for the replacement; nothing about it is retryable.
- **A priced tool says so on the search result, before you call it.** Every result carries four pricing fields over both transports: `is_paid` and `price_per_call_cents` (the credits price) and `x402_enabled` with `x402_price_usdc_atomic` (the USDC one). `describe_tool` / `GET /tools/{tool_id}/describe` carries **none** of them, so the result you already have is where to read a price — a `describe` call won't tell you. Name the cost to the user before running a paid tool rather than discovering it from the refusal: a *credits* balance below the price is refused before the upstream call (see `insufficient_balance` below), which costs a round trip and reads like breakage when it isn't. (A thin *USDC* balance is the exception — it falls back to the credits wallet and goes ahead.) What none of these fields tells you is the pricing *mode* — see that same section for why an x402 price can still be re-derived at call time.
- Describe the *outcome* in natural language (`"send an email"`, `"create a GitHub issue"`, `"translate text"`); search is semantic.
- **But when you already know a tool's exact name, search for exactly that.** A tool whose name or slug matches the query exactly is pinned first, ahead of the readiness and reliability re-orderings, so `results[0]` is the tool you named. Every result now carries a `slug` (`stripe-api-read`) beside its id, and a slug is accepted everywhere a tool id is *executed or inspected* — `execute_tool`, `describe_tool`, `POST /tools/call/{id}`, `GET /tools/{id}/describe` and the bare `GET /tools/{id}` (confirmed live 2026-09-24: `…/tools/gmail-send-email` and `…/tools/gmail-send-email/describe` both resolve to that tool). The quality-signal tools are the exception and want the UUID: see *The quality signal* below. Prefer the slug when showing the user what you're about to run; it is far more readable than a UUID. It is not a reason to skip searching, though: resolve the tool in this session rather than replaying an identifier from memory.
- Sample-data services (JSONPlaceholder, DummyJSON) are ranked behind every real result unless your query names one of them. They need no credential, so they would otherwise outrank the real tools of a service the user hasn't connected yet. If one turns up for a generic query, treat it as what it is — a fake-data sandbox, not an integration to offer the user.
- If the first query misses, rephrase and try again before concluding a capability doesn't exist. The catalog is far larger than you'd guess.
- `list_services` is served from a cache refreshed every 60 seconds, so a service connected or published moments ago can be missing from it for up to a minute; `search_tools` and `get_service_tools(service_id)` are not cached. Don't conclude a service doesn't exist from one `list_services` miss; search for one of its tools instead.
- **`get_service_tools` stops at 50 tools over MCP, and nothing in the answer says so.** Its
  `limit` parameter defaults to 50 and the list is simply cut to that length — no total, no
  cursor, no truncation flag — so the rest of a large service's tools are indistinguishable from
  tools it doesn't have. It is not an MCP-server quirk: the cut is unconditional, and the largest
  services in the catalog are `api` ones (Vercel has 407 tools). Live on 2026-09-20: Higgsfield carries 101 tool rows, the default call returned
  50 and `limit=200` returned all 101 — nothing clamps the number you pass, so pass a big one
  (500) rather than reasoning about the service's size. Two knock-on effects worth knowing: a
  list of exactly 50 proves nothing by itself, because a service that really has 50 looks
  identical; and `needs_configuration` is derived from the sliced list, so on a larger service
  that flag describes only the first 50 tools. The REST route takes no `limit` and returns the
  whole list, so `GET /services/{id}/tools` is already the complete answer — and when the
  question is really "can this service do X", `search_tools(query, service_id=…)` answers it
  without the page at all — mind that its own `limit` defaults to 10.
- **`list_services` can also fail outright over MCP, and it is not your parameters.** Some queries come back as a JSON-RPC error — code `-32602`, "Invalid request parameters" — with no result at all. It is a Danube-side defect rather than a bad argument: when a page of results contains a service whose `tool_count` arrives `null`, that page fails the MCP layer's own `Service` model, which declares the field as an `int`. So the failure belongs to the *page*, not to the service you were looking for, and it is stable for a given query rather than a passing blip — live on 2026-09-15, `query: "Day AI"` failed on five consecutive attempts while `"Outreach"` and `"Coupler"` returned normally on the same connection, and still failing on 2026-09-23. Re-sending the identical call will not clear it; a **different phrasing may**, because it reshuffles which rows land on the page (`"Day"` and `"dayai"` both succeeded and both returned Day AI first). The row that breaks the page is almost never the one you were looking for: the same query over REST (`GET /v1/services?query=Day AI`) returns Day AI itself with a `tool_count` of `0` and the `null` on the loosely-matched rows further down the page — so a healthy-looking target row tells you nothing about whether the MCP call will survive, and REST is where you can see which rows carry the `null`. The reliable routes are `search_tools` with the capability you want, which is unaffected, and `GET /v1/services` over REST, which returns those same rows without complaint. Nothing to `report_tool` either way — this is Danube's own API, not a marketplace tool.
- Read the tool's parameter schema (`required`, `type`, `enum`, `tips`) before executing; ask the user for anything required that you don't have. Never reuse tool IDs from memory — search again.
- **A parameter whose `type` reads `object (N properties)` carries its real schema beside it.** When a field's type is too complex for the summary string — a nested object, an array of objects, or a union — the parameter also has a `json_schema` key holding the upstream JSON Schema for that field: property names, types, bounds and descriptions. MCP-backed tools declare these routinely, and the summary alone leaves you guessing the keys. Live examples: `Apify - Call Actor`'s `callOptions` reads `object (5 properties)` and its `json_schema` names `build`, `memory` (128–32768), `timeout`, `maxItems` and `maxTotalChargeUsd` with a line of guidance each; `Apify - Fetch Actor Details`' `output` reads `object (9 properties)` and lists all nine booleans. It rides on `search_tools` results and on `describe_tool` alike. **Read it with `.get("json_schema")`, never by testing whether the key is there:** on `search_tools` a parameter that has none carries an explicit `"json_schema": null`, while on `describe_tool` and `get_service_tools` the key is left out altogether. **It is filled in for MCP-backed tools only**, so its absence tells you nothing about the parameter: an API-backed tool's complex body parameter reads a bare `object` with no `json_schema` at all, and its shape is described in the parameter's own `description` instead (`Airwallex - Create Payment Intent` spells several out that way). Read whichever of the two you get rather than inventing keys — it is catalog metadata, so nothing validates your object against it before the upstream sees it.
- Pass only parameters the schema declares. On the standard HTTP execution path, Danube drops anything the tool row doesn't declare *before* making the upstream request, so an invented parameter never reaches the provider. If such a call then fails, the error message ends with a note naming what was dropped — "`'x'` was not sent — `<tool>` does not declare that parameter, so Danube dropped it before making the request. If the upstream supports it, the tool's schema is missing it." Read that note rather than concluding the upstream ignored your value, and treat it as a sign the tool's schema may be missing a parameter the provider does support. Tools backed by an MCP server forward your parameters as given, so there the upstream really did see them.
- Results called in the last 30 days also carry `reliability`: `window_days`, `calls_7d`, `calls_30d`, `success_rate_30d`, `p50_seconds`, `p95_seconds`, `last_success_at`, `last_failure_at`, `last_error_class`, `last_error_type`, an `error_classes` breakdown, a `faults` breakdown, `auth_failures_30d`, `caller_failures_30d`, `danube_failures_30d`, `upstream_failures_30d`, `distinct_callers_30d`, `flagged` and `refreshed_at`. When two tools fit, prefer the higher success rate; a `flagged` tool (under 80% success on 20+ calls) is a last resort, and say so to the user. `success_rate_30d` is `null` under 10 calls — that is too small a sample to rank on, not a bad tool. Results are relevance-ordered with a bounded reliability nudge; pass `ready_only=true` to see only tools you can call now, or `min_success_rate=0.9` to drop tools with a known-poor 30-day rate.
- **The score counts only what the tool is answerable for.** Since 2026-09-10 the sample behind `calls_30d` and `success_rate_30d` is successes plus `upstream` failures — the third party's own. Failures attributed to the *caller* (a missing credential, values the upstream correctly rejected) or to *Danube* (a stale row, a request Danube built wrong) are reported beside the rate and left out of it, so neither can push a tool over the `flagged` line. `faults` breaks the 30-day failures down by `caller` / `upstream` / `danube`, and the three `*_failures_30d` counters give the same thing as totals. A large `danube_failures_30d` is a Danube-side bug already queued for repair, not a reason to steer the user off a working tool; a large `caller_failures_30d` (of which `auth_failures_30d` is the credential part) is other callers' setup, not the tool. This generalises the older rule that only `auth` failures were excluded.
- `last_error_type` is the execution engine's own verdict (the `error_type` vocabulary below) on the most recent **upstream** failure — not on the most recent failure of any kind. `last_failure_at` and `last_error_class` are drawn from that same upstream-only row, which is why a caller-side failure minutes ago leaves all three untouched: they describe how the *provider* last let this tool down. `last_error_type` is additionally `null` for failures recorded before 2026-09-10, so `last_error_class` is the one populated on older rows.
- Read `last_error_class` before writing a tool off: `validation`, `upstream_4xx`, `upstream_5xx`, `timeout` or `other` (null when the tool has no counted failure). Upstream throttling has no class of its own — a `429` lands in `upstream_4xx` or `upstream_5xx` depending on how the provider worded it, so neither one is proof of a server fault. `auth` — a caller's missing or invalid credential — never appears here by design; it shows up only in the counters — `error_classes`, `auth_failures_30d`, and the wider `caller_failures_30d` / `faults` that now contain it — and those failures are left out of `calls_30d` and `success_rate_30d` entirely, so they can't push a tool over the `flagged` line. A tool with a large `auth_failures_30d` is one other callers haven't connected, not a broken one: if your account has the service connected, judge it on the rate.
- Before a tool you have not used successfully in this session, call `describe_tool(tool_id)` (REST: `GET /tools/{tool_id}/describe`): it returns the schema, your `readiness` and `configuration_url`, `usage`, `examples`, `defaults`, and the same `reliability` block a search result carries — so you can compare a tool and read its schema in one call. **Two of those are scoped differently than they look.** `usage` (calls, success rate, `p50_seconds`, `common_errors`) covers the last 30 days **across all callers**, not yours (the most recent 500 executions in that window). It is how the tool behaves for everyone, which is what makes `common_errors` worth reading before a first call. `examples` is the opposite: it is **your own account's** last successful calls and nobody else's. `defaults` is what `set_parameter_defaults` has saved, i.e. the parameters you may safely omit — it merges your own with any your organization has set, so a value there may be a teammate's.
- **`examples` are real past calls, not sample data — copy the shape, not the values.** Each entry is `{parameters, executed_at}`, where `parameters` is the stored `request_params` of one of your account's own successful executions, verbatim — so it holds whatever was actually sent: real recipients, real message bodies, real record ids from some earlier task. It can also carry execution controls that are not schema parameters at all (`async`, `previewOutput` show up on the Apify entries), so check each key against the schema before copying it. Credential-shaped values have been masked since 2026-09-02 (older rows were never backfilled), but ordinary personal data never was. Use them to see which parameters a working call sets and how they're spelled, then fill in the values for *this* task — re-sending one verbatim can repeat a real action against a real third party. Don't echo them back to the user either; they may belong to a different piece of work. Note also that, unlike `usage`, `examples` has **no time window**: it is the three most recent successes however old, so an entry can predate a change in the tool's schema.
- If a service always needs the same identifier (Vercel `teamId`, a Sentry org slug, a DigitalOcean app id), save it once with `set_parameter_defaults(service_id, {"teamId": "…"})` after the user confirms it; later calls that omit it get it filled in (`_meta.defaults_applied` says which). Never save a key or token this way.
- Keep big results out of your context: pass `fields: ["items[].name", "pagination.next"]` to `execute_tool` to receive only those paths. The result is stored under `_meta.execution_id`; `fetch_result(execution_id, path)` (REST: `GET /tools/executions/{id}/result?path=…`) reads any other part of it back without re-running the tool.
- **The read-back has a size cap of its own, and it defaults to 50000 characters** — a whole
  stored result is not what a bare `fetch_result` necessarily hands you. It takes
  `max_response_chars` (REST: `max_chars` on the query string); the floor is 100 on both, the
  ceiling differs — 500000 over MCP, 2,000,000 over REST, the same ceiling the execute call uses.
  It trims exactly the way an execution response does, in all three of that paragraph's modes: a
  JSON array loses whole elements off its tail and stays valid JSON of the right shape, plain text
  is cut mid-string, and an object with no array big enough to trim degrades to
  `_truncated_partial_json` with its own keys gone. The array case is the one to watch, because a
  short-but-well-formed list is the one that reads as a complete answer. Live on 2026-09-20
  against a stored 194-element result: the default fetch returned 32 elements with
  `truncated: true` on both transports, while `max_response_chars: 500000` returned all 194 with
  `truncated: false` — the stored copy had been whole the whole time.
- **On a fetch, `truncated` reports the backend's trim and not the MCP layer's.** Read it
  (`_meta.truncated` over MCP, top-level `truncated` over REST) before treating a fetched result
  as complete — but over MCP it is only half the signal: a `max_response_chars` above 500000 is
  silently clamped to 500000 and applied *after* the backend has answered, so a result cut by
  that clamp comes back with the flag reading clean. Don't ask for more than 500000 there. When
  the stored result is genuinely larger, read it in pieces with `path`, or fetch the same handle
  over REST, where the ceiling is 2,000,000.
- **A batch entry takes `fields` too, and since 2026-09-10 it is honoured** — before that it was accepted and silently dropped. Put it beside `tool_input` on any element of `batch_execute_tools` (REST: any entry of `POST /tools/call/batch`). Each element then carries its own projection report and execution handle: `_meta.projection` / `_meta.execution_id` over MCP, `results[i].result.projection` / `.execution_id` over REST. **The two transports trim in opposite orders, so the advice differs.** Over MCP prefer `fields` to a bigger `max_response_chars`: the 32000-char per-element cap is applied *after* the backend has projected and stored, so a projection keeps a verbose payload whole, and `fetch_result` on the element's handle reaches everything the backend kept — up to its own 500000-char shaping limit, since the MCP layer never forwards your cap to it. Reaches, not returns: the fetch applies its own 50000-char default on the way back (see `max_response_chars` above), so raise that on the fetch or the handle hands you a trimmed copy of an untrimmed result. Over REST an entry's `max_response_chars` (default 500000 there, not 32000) trims *before* the result is projected and before it is stored — so there a narrower request is the only real lever, and fetching a trimmed element's handle back does not recover what the cap cut. Over MCP the element's payload also sits at `result` itself, with no `data` wrapper (over REST that slot holds the whole envelope, with the payload one level further in) — but either way the paths are written against the same shape you would use on the single call.
- **The stored copy has its own ceiling: 1,000,000 serialised characters** — but it is rarely the ceiling that binds, because what gets stored is what the response *shaping* already produced. Over MCP your `max_response_chars` on an execute call never reaches the backend at all (the MCP layer applies its own cap afterwards), so the stored copy is shaped at the backend's 500000 default and can't exceed it; the 1,000,000 ceiling only bites over REST, and only when a call asks for more than that. Past whichever limit applies first, a JSON result loses whole array elements from the tail (still valid JSON of the same shape, just short) and a plain-text one is simply cut at the limit. The REST handle then says so with `stored_truncated: true` and a `stored_meta` block giving the original size and what was dropped; `fetch_result` over MCP carries **neither** key, so there an oversized handle is quietly partial. If you are paging a very large result by path and the tail is missing, re-run the tool with a narrower request rather than concluding the upstream had nothing more.
- **On an MCP-backed tool, write `fields` and `path` against the upstream envelope, not against `result.data`.** The projection runs in the backend, on the result *before* the MCP layer shapes it — so it sees the upstream MCP server's envelope, while `data` is a key the MCP layer adds afterwards, which means a `data.…` path never reaches *that* key. (If the upstream server sends a `data` of its own, that one does match.) Start the path at `content[0].text.…` (a JSON-carrying text block is stepped into for you, see below) or at `structuredContent.…` where the server sends one. Confirmed live on both transports against `Cloudflare Documentation.migrate_pages_to_workers_guide`: `fields: ["content[0].type", "data.anything"]` kept the content block and reported `missing: ["data.anything"]`. One artifact to know about over MCP: if your projection keeps a `content[]` block of `type: "text"` but not its `text`, the MCP layer re-adds `"text": ""` on the way out (REST returns the block without it), so read `_meta.projection` rather than treating that empty string as something the tool returned. On an HTTP-backed tool none of this applies — there the projection sees the upstream body, which is the same object `result.data` holds.
- **`fields` is ignored outright when `result` itself is not an object or an array**, and says nothing about it. That happens on an **HTTP-backed** tool whose body is not JSON — it arrives as a raw string, and the projection is skipped: `projection` is `null` over REST and absent from `_meta` over MCP, which is not the same as `matched_nothing` and is the one case where a missing report means "never attempted" rather than "everything matched" (live: `fields` on `ClawHub - Get Skill File` returned its whole 25,635-character Markdown body untouched). It does **not** happen on an MCP-backed tool however prose-like its answer is, because `result` there is the envelope *dict* and the projection runs against that as usual. Narrow the request itself on the tools where `fields` can't help.
- **A path that matched nothing is reported, not silently empty.** Write `fields` and `path` against the shape described above, and when a projection comes back empty check the flag before concluding the tool returned nothing: on `execute_tool`, `_meta.projection.missing` lists the paths that hit nothing and `_meta.projection.matched_nothing` is true when none of them matched; on `fetch_result`, `_meta.path_matched` is `false` and the text block says so outright ("Nothing in the stored result matched the path … The result itself is intact"). REST reports the same thing as `path_matched` in the `GET /tools/executions/{id}/result` body. A `false` doesn't always mean the path is wrong — a path crossing a genuinely empty collection reports it too — so re-read the original shape rather than re-running the tool. The key is *absent*, not `false`, when the backend doesn't report it, so test it as `_meta.get("path_matched") is False`.
- **A path may continue into a string that carries JSON.** MCP-backed tools routinely hand back their real payload as text inside a string, and a path written straight through it used to match nothing. It is now resolved against the JSON document the string carries — either the string that *is* JSON, or JSON fenced in the `<untrusted-data-…>` markers Supabase's MCP server wraps results in — and the fragment comes back parsed, in place of the string. So write `fields` against the shape you can see in the payload and don't route around a string in the middle of it. A path *ending* at a string still returns the string unchanged, and prose with a JSON fragment loose somewhere inside it is still a miss. Since 2026-09-10 the step `<json>` is also accepted and skipped as an interior step, which means a path read straight off `_meta.redaction` — that report spells the same place as `content[0].text.<json>.deployment.phase` — can be pasted into `fields` or `path` verbatim instead of being hand-edited. (Before that date the marker was matched as a literal key and the path silently hit nothing.) The trade is that a real key spelled `<json>` is unreachable; no upstream is known to have one.

### When a call fails, read whose failure it was

A failed `execute_tool` is attributed for you, so you don't have to guess from prose whether
the provider is down, your parameters were wrong, or Danube's own catalog row is stale. Three
fields carry it — `_meta.error_type`, `_meta.fault` and `_meta.retryable` over MCP, the same
three at the top level of the response over REST:

| `fault` | What it means | What to do |
|---|---|---|
| `caller` | The request itself was rejected: a missing or invalid credential, a value the provider correctly refused, a resource you named that doesn't exist, a plan or spending cap | Fix the parameters or credentials before retrying. Not the tool's fault — don't `report_tool` it |
| `upstream` | The third party failed: a 5xx, a timeout, a refused connection, throttling it didn't tie to the user's plan, an MCP server that couldn't be reached | Retrying later may work. This is the only class that moves the tool's reliability score |
| `danube` | Danube's own handling: a stale catalog row, a request it built wrong, a credential it couldn't resolve, an internal exception | Neither a retry nor a `report_tool` helps — a genuine defect here is recorded for repair on its own, and the rest (a sunset tool, a retired service, a disabled tool) are deliberate catalog states, not bugs to chase. Pick another tool or tell the user |

`error_type` is the specific class inside that verdict (`missing_parameters`, `auth_required`,
`rate_limited`, `plan_rate_limited`, `timeout`, `endpoint_missing`, `upstream_tool_missing`,
`bad_request`, `not_found`, …), and `retryable` says whether the *identical* call could succeed
later — the transient upstream types, plus the one caller-side type whose window reopens on its
own (`plan_rate_limited`, below). Prefer these three fields to matching on the message text,
which is what the rest of this file falls back to for older backends.

**Two of those separate a throttle the user's own plan imposed from one the provider imposed.**
A `429`-style refusal the provider itself explains as *the connected plan's* ceiling — its
message carrying both a throttle word and something like "upgrade your plan", "/pricing",
"quota exceeded" or a monthly/daily limit — is `plan_rate_limited`, which is `fault: "caller"`
and `retryable: true`: the window reopens on its own, so waiting works, but the ceiling is the
user's own plan on that third-party service and calling harder will not move it. A plain `429`
with no such wording is `rate_limited` / `fault: "upstream"`. Since only `upstream` failures move
a tool's reliability score, the split is also what stops a plan cap — hit by fanning parallel
calls through a batch, say — from flagging a tool that works. Don't `report_tool` either one:
tell the user their plan on that service is the limit, and slow down rather than looping.

**That split is narrower than it looks: it needs the provider's own words, so it reaches
MCP-backed results and not an HTTP tool's `429`.** `plan_rate_limited` is decided by reading the
error *text*, which is available on an MCP server's `isError` body. An `api`-service tool's
failure is classified from its HTTP status line by a path that never sees the response body, so
its `429` stays `rate_limited` / `upstream` however plainly the body names the plan — and a
text-classified message that embeds a status (`HTTP 429`, `Client error '429 Too Many
Requests'`) short-circuits the same way, because the status is matched before the wording. This
is a known gap on Danube's side, not something your call can change. So on an HTTP-backed tool,
read a `rate_limited`/`upstream` verdict as possibly still being the user's plan cap, and check
the message before telling them a provider is throttling everyone.

Don't confuse either of these with the account's **Danube** plan quota, which is a different
layer with a confusingly similar name — see *The two `429`s* and *Rate limits* below.

**Over MCP the error text usually repeats the verdict**, opening with `Request error:`,
`<Service> error:` (the service is taken from the tool name's `<Service> - <Action>` shape, and
falls back to `Upstream service error` when the name doesn't have it) or `Danube error:`, then
a sentence of advice. Treat that as a convenience for showing the user, not something to match
on: two of the most common failures — `auth_required` and an insufficient wallet balance —
return their own dedicated text with no prefix at all, and over REST nothing is prefixed. The
three fields are the reliable signal.

Don't confuse `error_type` with the `last_error_class` in a search result's `reliability`
block: they are separate vocabularies. `error_type` is the execution engine's verdict on one
call; `last_error_class` is the reliability view's coarser after-the-fact bucket
(`validation`, `upstream_4xx`, `upstream_5xx`, `timeout`, `other`).

Inside `batch_execute_tools` the same three fields ride on each *element's* own `_meta`, not on
a top-level one — read them per element.

They can still be absent. A failure that never reached the execution engine has none: an
unresolvable `tool_id`, or, over MCP, a `tool_name` that matches nothing (which returns no
`_meta` at all). And a refusal the REST layer turns into a real HTTP status — `402` for a plan
cap, `503` for a disabled tool — *was* attributed, but the status is raised in place of the
body, so the fields don't survive to the caller. Read all three with `.get()` and fall back to
the message whenever they're missing.

### When a tool needs credentials

A result containing `"error_type": "auth_required"` (with `fault: "caller"`) means this user hasn't connected that service yet:
1. Prefer sending the user to the `configuration_url` in the error (or https://danubeai.com/dashboard) to connect it — the only path for OAuth services such as Gmail, Slack, or Google Calendar.
2. For API-key services, if the user explicitly gives you the key and confirms, call `store_credential(service_id, credential_type="bearer", credential_value=…)`, then retry.

`get_service_tools` reports `needs_configuration: true` only when *every* tool of the service is `needs_credential` for this account — every tool it returned, that is, which over MCP is the first 50 at most (see the discovery tip above); it is derived from the per-tool `readiness` field, which is the answer for any single tool. A service mixing credential-free and credential-bearing tools reports `false`, so read `readiness` on the tool you are about to call rather than the service-level flag.

When it *is* true, read the `configuration_required` block instead of guessing what to ask for. The keys are always present: `service_id`, `service_name`, `message`, `configuration_url`, `instructions` and `credential_schema`. `service_name` can still be null (the lookup behind it is best-effort) — fall back to the service you asked about rather than showing the user "null". For a service whose credential shape Danube knows, it also carries a `credential_schema` — the field names, labels, help text and any eligibility notes — and the `instructions` then name those fields ("Ask the user for: …"). `credential_schema` stays `null` for a service with no registered schema, which is common for plain API-key services; there, ask for the one key or send the user to `configuration_url`. Don't invent field names it doesn't list.

**On some MCP services a null `credential_schema` is not the tell it looks like.** A service
whose own MCP server runs an OAuth handshake — Coupler.io and Outreach are live examples —
answers `get_service_tools` with `needs_mcp_oauth: true`. Over MCP that arrives *alongside*
`needs_configuration: true` and a `configuration_required` block whose `credential_schema` is
`null`, which reads exactly like the plain API-key case above; over REST it arrives as
`{"tools": [], "needs_mcp_oauth": true, "mcp_oauth_info": {…}}` carrying **no
`needs_configuration` key at all**, so a curl caller has to test for this one on its own. The
right move either way is to send the user to the dashboard, which runs the handshake:
`https://danubeai.com/dashboard/tools/<service_id>` (over MCP this is already built for you as
`configuration_required.configuration_url`; over REST the response carries no URL, so compose
it from the `service_id`). Then read the tool list again once they say they've connected — the
tools are discovered from the MCP server only after authorization, by the background sync
described below. Two things not to do: don't walk the user through the
`authorization_endpoint` / `token_endpoint` / `registration_endpoint` in `mcp_oauth_info` —
those are the *provider's* and the dashboard is what drives them; and don't reach for
`store_credential` to get around the prompt. That endpoint does not refuse these services — it
will happily store a bearer value and the connection will send it — so a guessed or improvised
token gets accepted, stops *you* seeing the `needs_mcp_oauth` shape, and hides the Connect
prompt behind a credential that doesn't work. (The credential is yours alone, so the prompt is
still there for everyone else — you have hidden it only from yourself.) Store one only if the user actually hands you a
connection token their provider issued.

**This envelope is about the catalog, not about your account.** It appears only while Danube
holds no tool rows for the service at all, so a connector that authorizes by OAuth but whose
tools are already on record never produces it — Notion answers with an ordinary list of 44
tools and `needs_mcp_oauth: false` (live, 2026-09-15). Those entries carry the usual per-caller
`readiness`, which is what tells you whether *your* account still needs to connect. So read
`readiness` on the tool you mean to call as the per-account answer, exactly as for any other
service, and treat `needs_mcp_oauth` as the narrower "Danube hasn't seen this server's tools
yet either" case.

**An empty tool list can mean "not yet" rather than "none".** An MCP service's tools are
registered by a first sync that runs in the background (since 2026-09-13), so a service
connected moments ago may have none on record yet — registering a large server's takes tens of
seconds. `get_service_tools` then answers `tools: []` alongside `tool_sync` (`{"status":
"running"}`, later `"done"` or `"failed"`) and a `message` saying to read again; over REST,
`GET /services/{id}/tools` carries `needs_sync: true` as well. **Read it again in a few
seconds.** When the user connects the service in the dashboard the sync starts there; after
your own `store_credential` nothing is running until you read the tool list, and that first
read is what starts it — so the fix is always another read, never a call you have to make.
Treat `tool_sync` defensively: it can come back `{}` with no `status` at all, and over REST it can be missing from the object entirely. Neither `failed`
nor an empty `done` is final — a read five minutes later starts a fresh attempt. The `message`
also names `POST /services/{id}/refresh-tools`, but that endpoint needs the service **owner**
signed in to the dashboard and answers `401` to an API key, so it is something to tell the user
about, not something for you to call. Don't report a service the user just connected as having
no tools, and don't `report_tool` anything — no tool has been called.

`credential_value` takes either the raw secret or a **reference** — a pointer resolved when the tool runs, so the secret is never held centrally.

**References only work on some execution paths.** A reference is resolved on the standard HTTP auth-injection path — an `api` service whose tool isn't one of the provider-specific composite handlers — and by the in-VPC data-plane agent, which runs the services an org has marked `local_only`. Everything else reads the stored string **as the secret**: a hosted `mcp_server` service, and composite handlers for services like Firecrawl or Notion. Give one of those a `vault://…` string and it goes out as the credential itself, and the provider answers `401`. So: **store a reference only for a self-hosted deployment, or for a service that runs on the org's data-plane agent; otherwise store the value.** If you aren't sure which path a service takes, store the value — unless the service is `local_only`, where the paragraph below applies instead.

**On the data-plane path a reference is not merely supported — it is the only thing that works.**
The control plane strips every non-reference value out of the dispatch it sends the agent: a
plaintext secret is replaced with `null` and only its *existence* is flagged, so the value never
leaves Danube. The agent then refuses the call with `error_type: credential_reference_unresolved`
(`fault: "caller"`, not retryable) and a message naming the field — "… exists only as a central
plaintext value. Data-plane execution requires reference-based credentials (env:// or vault://);
re-store it as a reference." Since 2026-09-24 this reaches **MCP** services too: a `local_only`
MCP server has its calls *and* its tool discovery dispatched through the agent, so the
"`mcp_server` reads the stored string as the secret" rule above holds for a **hosted** MCP
service and is *reversed* for a `local_only` one. For a `local_only` service of any kind, ask the
user which form they have rather than defaulting to the value — there is no plaintext fallback.

| `credential_value` | Stored as | Resolves |
|---|---|---|
| `vault://<mount>/<path>#<field>` (the `#<field>` is required) | reference | against the `VAULT_ADDR` / `VAULT_TOKEN` of whatever process runs the tool — your data-plane agent or self-hosted deployment. The hosted service has no per-customer Vault setting, so it can't reach your Vault |
| `env://VAR_NAME` | reference | in the environment where the tool actually runs, so self-hosted / data-plane only. On the hosted service `env://` stores fine but **fails at execution time**: it is off by design there (`DANUBE_ALLOW_ENV_REFERENCES` is a self-hosted/dev switch, not something to ask Danube to enable) |
| the raw key | value | the working default on the hosted service — deprecated but accepted; self-hosted rejects it outright with `central_credential_ingestion_disabled` |

Never invent a variable name or vault path — use only what the user gave you, and ask which form they want if it isn't obvious. A successful store echoes `"stored_as": "reference"` or `"value"`, adding `"deprecated": true` and a `notice` when a plaintext value was stored. Note that a successful store proves nothing about whether the reference will resolve — that only shows up when the tool runs.

### The two `429`s, which share an error code

There are two unrelated refusals behind that status and **`error.code` does not tell them
apart** — both read `rate_limited`. The plan cap is raised as a plain `429` whose detail Danube's
envelope wraps, so it inherits the status's generic code; the rate limiter sets the same string
deliberately. Branch on `error.details`, which is where they actually differ:

| `error.details` holds | Which refusal | What to do |
|---|---|---|
| `usage` and `upgrade_url` (the relative `/pricing` — join it to `https://danubeai.com`) | The account's **plan quota** | Stop and tell the user. Retrying never clears it |
| `retry_after` | Danube's **rate limiter** | Yours to absorb: wait, then retry once. Don't mention it to the user |

Getting this backwards is the failure worth avoiding: an agent that matches `error.code ==
"rate_limited"` and retries will loop on a plan cap the rest of this file tells it to report.

`retry_after` is also in a `Retry-After` header, and `X-RateLimit-Limit` carries the limit that
was hit — as slowapi's description *string* (`"60 per 1 minute"`), not a number, so don't parse
it as one. Read `retry_after` and sleep it rather than inventing a backoff, but don't read
meaning into its value: it is currently a flat **60** on every rate-limited response, not a
computed time-to-reset.

### Rate limits — the budget you are spending

Searching and executing (`GET /tools/search`, `POST /tools/call/{tool_id}`,
`POST /tools/call/batch`) are limited by **API key**, at a rate set by the account's plan: 60
requests/minute on free, 1000 on pro, 2000 on team, 3000 on enterprise (a legacy `starter` tier
still sees 300). A plan upgrade takes up to five minutes to widen it, because the tier behind a
key is cached that long. These three endpoints all require a key, so there is no anonymous rate
to fall back to — a call without one is a `401`, not a slower lane.

**The budget is counted per key *and per URL path*, not as one pool.** Each path keeps its own
bucket, so `/tools/search` and `/tools/call/batch` have separate allowances, and — because the
tool id is *in* the path — so does every individual tool. On the free plan that means 60
calls/minute to any one tool rather than 60 across all of them: hammering a single tool in a
loop is what exhausts a bucket, while spreading work across different tools barely touches it.

**A batch is one request however many calls it carries** — `batch_execute_tools` and
`POST /tools/call/batch` both reach the backend as a single HTTP request (no per-call fallback
loop on either transport). Note *which* bucket that one request comes out of: `/tools/call/batch`
is its own path, so a batch never touches the per-tool bucket at all. Ten calls to the same tool
spend ten of that tool's minute when sent one at a time, and one of `/tools/call/batch`'s minute
when sent together. So batching is the move when you are looping over a single tool — but it is
not a general speed-up, and it buys you **only** rate-limit headroom: each entry is still checked
against the account's plan quota individually, so a batch of ten spends ten executions of the
plan allowance exactly as ten single calls would. Batch only calls you would have made anyway,
and remember a batch still needs the user's explicit yes.

### Paid tools, missing upstream tools, and the hosted-AI caps

**A tool the publisher charges for is refused before it runs, and tells you exactly how short
you are.** The balance check happens ahead of the upstream call, so nothing half-executes. The
verdict is `error_type: "insufficient_balance"` with `fault: "caller"` and `retryable: false`,
and the message is quotable: "Insufficient credits. This tool costs $X.XX. Your balance: $Y.YY.
Add credits at https://danubeai.com/dashboard/finances". Over REST the same two figures come back
machine-readably as `cost_cents` and `balance_cents` — `balance_cents` is the balance that was
too low, not a balance after a charge, because no charge happened. Over MCP neither field exists:
the two figures are in the message text, as dollars. What MCP's `_meta` adds instead is
`insufficient_balance: true` beside the three attribution fields, and the text gains numbered
top-up steps. This is one of the two failures that arrive with no `Request error:` / `Danube
error:` prefix, so match the fields, not the opening words. A tool priced in USDC (x402) refuses
on a **limit** rather than on an empty wallet, and which message you get depends on how it is
priced. Against the price Danube holds on record you get "x402 spending limit exceeded: Exceeds
your per-call limit of $X" (or the platform maximum, or the daily one) — the engine sets no
`error_type` for it, but the phrase "spending limit" is what classifies it onto the same verdict.
A USDC balance too thin for that price is *not* a refusal there: the call falls back to the
ordinary credits wallet and goes ahead. Two other x402 messages exist, and **you cannot tell in
advance which tools produce them** — a search result carries `x402_enabled` and the price, but
nothing an API key can read exposes the pricing *mode*, and `describe` carries no pricing at
all — so match on the message, never on the tool. Both come from a price
re-derived at call time from the upstream's own `PAYMENT-REQUIRED` header, which can exceed what
the earlier check cleared. "Insufficient USDC. Required: $X.XXXX. Balance: $Y.YYYY" classifies
correctly, and over MCP carries the same numbered top-up steps as the credits case. "x402 payment
blocked: …" — carrying the same three limit reasons as above — matches none of the engine's text
rules, so it is mis-filed as `unknown` with `fault: "danube"`, and over MCP it even arrives
prefixed `Danube error:` with advice to wait for a repair. That one is the rare case where the
message beats the verdict: ignore the label, it is the account's own limit rather than a Danube
bug, and there is nothing for you to `report_tool` (the platform files its own row for it). Both
top-up links reach one page:
`/dashboard/wallet` redirects to `/dashboard/finances?tab=wallet`, the same Finances page the
credits message names. Show the user the two figures and the link; don't retry, and don't raise a
spending limit unless they ask for exactly that.

`error_type: "upstream_tool_missing"` is the one failure that is **Danube's** fault rather than
yours or the provider's: the catalog row points at a tool its MCP server no longer offers. (It is
a body-shaped error, not an HTTP status — over REST the call still answers `200` with
`status: "error"`; over MCP it arrives as `isError: true` with the fields below in `_meta`.) Danube tries to repair it on the spot first — it re-reads the server's tool list and, if
the tool was merely renamed, re-runs your call under the new name and hands you the real result,
so most drift never reaches you at all. What you see is the case where the tool is genuinely
gone. The response carries `retryable: false`, the `upstream_tool` the row pointed at, and
`available_tools` — the tools the server *does* offer. Take the answer at face value: it has
already been reported automatically, so don't `report_tool` it and don't retry. Pick a
replacement from `available_tools`, or search again.

Danube's own AI tools (`Danube - Summarize Text`, `Translate Text`, `Webpage Summary`, and the
six others that call a model — not `Danube - Screenshot`) carry a **separate daily cap on a free
account: 20 successful executions per UTC day**, on direct `execute_tool` calls as well as on
workflow steps. Past it the call is refused with "Daily limit for Danube's AI tools reached
(N/20 today on the free plan). It resets at 00:00 UTC…" — over REST an HTTP `402` whose
`error.code` is `payment_required`, over MCP a result with `isError: true` quoting the same
message in `content[0].text`. Tripping it *inside* a workflow is not a 402 at all: that step
simply fails with the message and the run comes back `200` with `status: "failed"`. It resets,
so it is not the lifetime workflow cap below; either wait or tell the user to upgrade, and
don't `report_tool` it.

### Tools the user's organization registered

Alongside the catalog, an organization can register its own services with visibility `internal` (Danube runs the calls) or `local_only` (the organization's in-network data-plane agent runs them). They show up in `search_tools` and `list_services` only for members of that organization, and only for the tools the organization's policies grant this user; everyone else gets a `404`, the same as a tool that does not exist. Which organization you act in is set by the key: a key created for an organization acts for it on its own, and a `danube-org-id` header (an organization id the user belongs to) chooses one explicitly and wins over the key. Four things to read:

- **`403` with `Your organization does not have access to this tool`** is the organization's policy, not the key's `allowed_tools`. Don't retry and don't `report_tool` it: tell the user an admin of the organization has to grant the tool (or its service) to them, a team they are in, or their role. A public catalog tool can be refused this way too, when the organization you act in explicitly denies it; that deny does not follow you outside the organization's context. A tool the policy withholds is normally hidden from search, so this mostly appears on an id you were holding.
- **Generic tools on a connected system.** A system an admin connected from one URL carries a small governed surface next to any named tools. For an API it is `<Service> - Request` (parameters `method`, `path`, `query`, `body`, `headers`; the credential is injected for you, so never put one in `headers`). For a database it is `<Service> - List tables`, `<Service> - Describe table` and `<Service> - Query` (one read-only `SELECT` in `sql`). Prefer a named tool when one fits. Otherwise call **List tables** and **Describe table** before **Query**, so the statement names real tables and columns, and keep a Request to `GET` or `HEAD` unless the user asked for a write. The service's access policy decides what these tools may reach: which methods and path prefixes, which tables, which columns come back masked as `[REDACTED:<column>]`, and the row cap.
- **`error_type: permission_denied` with `fault: caller` on one of those tools is the policy, not a bug.** The message names the refused method, path or table. Don't retry the same call, don't look for another path to the same data, and don't `report_tool` it: tell the user what was refused and that an admin can widen the policy on the service page, or promote the call as a named tool. A write (`POST`, `PUT`, `PATCH`, `DELETE`) may instead come back as `confirmation_required` when the policy asks for consent: show the user the call and repeat it with the token, like any other confirmed call.
- **Connecting or registering a system** is an owner/admin action. `POST /organizations/{org_id}/connect` takes one input (`kind: "api"` with `api.base_url`, `kind: "database"` with `database.connection_ref`, `kind: "mcp"` with `mcp.server_url`) and `"dry_run": true` first, which discovers and previews without writing anything; `POST /organizations/{org_id}/services` with `source` (`openapi_url`, `openapi_spec`, `mcp`, `connector` or `database`) is the advanced path for a document or spec the user already holds. Two visibility rules are worth passing on, both enforced at registration with a `400` (a `dry_run` surfaces the same reason before anything is written, but as a `200` with the text in `errors[]` — read the list, not the status): a **database** connector must be `local_only` on the hosted service, because the query runs where the DSN lives, and anything else is refused with "Database connectors run only through an organization's data-plane agent on the hosted service; register the connector for the organization with visibility local_only" (on the `connect` route, `kind: "database"` defaults to `local_only` for you); and an **MCP** server may be `local_only` since 2026-09-24, but only a *remote* one — a stdio server is refused with "Only remote MCP servers can be registered for an organization" whatever visibility was asked for. Confirm with the user before the real write, like any other. Guide: https://docs.danubeai.com/organizations/internal-tools

## Beyond tools

Available through the same connection, same guardrails:
- **Skills:** `search_skills`, `get_skill`, `create_skill`, `update_skill`, `delete_skill`
- **Workflows:** `list_workflows`, `create_workflow`, `update_workflow`, `delete_workflow`, `execute_workflow`, `get_workflow_execution`
  - A workflow can outlive the call that started it. `execute_workflow` answering
    `status: "running"` with an `execution_id` means it is **still going, not failed** —
    poll `get_workflow_execution(execution_id)`. Never re-run it: a second concurrent run
    duplicates every write the first one makes. Over `curl` you get a plain timeout rather
    than that response, so treat *any* timeout on an execute call the same way.
  - **A failed run is not an error status.** A workflow whose steps fail still answers
    normally, with `status: "failed"` in the body. Read the body's `status` and the
    per-step results — don't infer success from the absence of an error.
  - HTTP `402` blocks the run before any step executes: a free-tier account gets 5
    *successful* lifetime workflow runs that use a Danube-hosted AI step. The message says
    so verbatim ("You've used all 5 free AI-powered workflow runs…"); match on that and the
    402. The envelope's `code` is `payment_required` — a plan refusal, not an outage.
    Tell the user to upgrade — retrying won't help, *this* cap never resets, unlike the
    daily hosted-AI cap above.
- **Quality signal:** `get_tool_ratings`, `get_my_rating`, `submit_rating`, `report_tool`, `get_recommendations` — if a tool fails or returns bad output, `report_tool` it so it gets fixed. All five want a tool's UUID, and two of them say nothing when they don't get one: read the next section before trusting what they return.
- **Wallet & agents:** `get_wallet_balance`, `get_spending_limits`, `update_spending_limits`, `fund_agent_wallet`, `register_agent`, `get_agent_info`
- **The user's own profile:** not a tool at all — the MCP resource `identity://user` (REST: `GET /v1/identity/api`). See *The one MCP resource* below.

### The quality signal: ids that must be UUIDs, and a zero that isn't one

**Every one of these takes a tool's UUID, not the slug the rest of this file tells you to
prefer** — and they fail in four different ways, only one of which is loud.

`submit_rating` and `report_tool` are the loud ones: over MCP they check the value themselves and
refuse before sending anything ("tool_id must be a tool's UUID. Use search_tools to look it up…").
`report_tool`'s `reason` is a closed set too — `broken`, `degraded`, `incorrect_output`,
`timeout`, `other` — refused the same way, before a report is filed.

A UUID that is well-formed but names no tool is a separate case, and since 2026-09-24 it is
answered cleanly: `submit_rating` comes back `404` ("No tool with id …") rather than the `500` it
used to raise. So a `404` here means the id is stale or mistyped, not that rating is broken —
re-resolve the tool with `search_tools` and submit against the id you get back. As with
`get_my_rating` below, the status only survives over REST: through MCP the refusal arrives
flattened into a string, so there is no code to branch on and the message is the signal.

`get_my_rating` has no such guard and fails one step later, at the backend, with a `400`. Over
REST that is the ordinary envelope, `{"error": {"code": "validation_error", "message": "tool_id
must be a tool UUID, got: 'gmail-send-email'"}}`; over MCP the same refusal arrives flattened into
a string — `{"error": "API request failed with status 400 (Details: {…})", "isError": true}` — so
there is no `error.code` to match on. Both live, 2026-09-22.

**`get_recommendations` doesn't fail at all, which is worse.** Its `tool_id` goes into a query on
a UUID column inside a `try` that only logs, and the same unresolved string is what the endpoint
excludes from its own results — so a slug raises nothing, matches no co-usage, and quietly leaves
you with the generic popular list. The tell is the tool recommending itself: live on 2026-09-22,
`get_recommendations("supabase-execute-sql")` returned `Supabase - Execute SQL` at the top of its
own recommendations, while the same call on that tool's UUID left it out. Judge the answer by
`reason` as well — `Frequently used together` is a real co-usage hit, `Popular` is the fallback
every caller gets.

So take the `id` off the search result for all five, even though the `slug` is what you showed the
user.

Over plain REST one of them does take a slug: `POST /tools/{tool_id}/report` looks the tool up by
id *or* slug and stores the resolved UUID, so the same operation is accepted over curl and refused
over MCP. Sending the UUID works on both, so send the UUID.

**`get_tool_ratings` is the one that won't tell you.** It validates nothing and swallows the
failed lookup deliberately, so that a public endpoint never `500`s on a bad id — which means a
slug, a tool name or a typo comes back as `{"avg_rating": null, "rating_count": 0}`, exactly what
a real, unrated tool returns. Nothing to report; just don't read a zero from it as confirmation
that the id was right.

**And a genuine zero is not a verdict on the tool.** The aggregate behind it counts only ratings
whose `source` is `user`, so ratings left by agents dogfooding Danube are excluded from it
entirely; it is also a materialized view on a five-minute refresh schedule (a run that would
overlap the previous one is skipped rather than queued, so five minutes is the floor), which means
a rating submitted moments ago is not in it yet. Live on 2026-09-22, `Gmail - Send Email`
(`6f0c4361-d0cc-45df-8ee6-87b9cc1e0d37`) answered `get_my_rating` with a five-star rating and
`get_tool_ratings` with `rating_count: 0` on that same UUID. Rank tools on the `reliability` block
that rides on every search result — real calls and success rates — and treat a star average as a
bonus when there is one, never as evidence that an unrated tool is untrusted.

Read the keys the response actually carries, too: `avg_rating` and `rating_count`, not the
`average_rating` / `total_ratings` that `get_tool_ratings`' own description promises.

### The one MCP resource: what Danube already knows about the user

Beside its 31 tools the server exposes exactly one MCP **resource** — `identity://user` — and no
prompts and no resource templates, so `prompts/list` comes back empty and there is nothing else to
enumerate (live, 2026-09-23). Reading it returns the user's own Danube profile, scoped to your API
key: `about_me` (name, role, company, bio, industry, expertise, interests, location, timezone),
`key_people`, `contacts`, `preferences` (writing tone, communication style, language, important
dates) and `current_focus` (goals, priorities, projects), plus `_meta` and a `_schema` describing
the profile form's sections and their fields. Read the object you actually get rather than this
list: `_schema` is template-driven, so another account's sections can differ, and it covers only
the form's own sections — `contacts` is a top-level key with no section in it. Over REST the same
object is `GET /v1/identity/api`. Reading it is
discovery, so it needs no confirmation — it is a good way to address the user correctly or match a
tone they have already stated, instead of asking them again.

Three things to know before you rely on it:

- **It is declared `text/plain` and the body is JSON.** Parse it; don't branch on the `mimeType`.
- **A failure arrives as content, not as an error.** The handler catches its own exceptions and
  returns `{"error": "…"}` as the resource text, so a read can "succeed" while carrying nothing
  usable. Check for an `error` key before reading the rest.
- **It is personal data, and the least-data rule covers it.** Free to read is not free to forward:
  don't pass any of it into a third-party tool's parameters unless the task actually calls for it.
  Sections are often empty — a user who filled in little of the form simply has little here, which
  is not an error and not something to `report_tool`.

It is unaffected by the `?tools=` group filter, which hooks `tools/list` only, so a narrowed
connection still lists and reads it. In `resources/list` it appears under the handler's own name,
`get_identity_resource`, rather than a friendly label — match on the `uri`.

Something not working? `{baseDir}/references/troubleshooting.md`

## Links

- Dashboard: https://danubeai.com/dashboard · Docs: https://docs.danubeai.com · OpenClaw guide: https://docs.danubeai.com/sdk/openclaw
- MCP server: https://mcp.danubeai.com/mcp · Privacy: https://danubeai.com/privacy · Terms: https://danubeai.com/terms
