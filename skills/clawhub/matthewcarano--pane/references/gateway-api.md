# Pane Gateway API Reference

Full endpoint reference for the Pane Gateway HTTP API. Load this file when
`SKILL.md`'s inline examples aren't enough detail — e.g. you need exact
request/response field names, pagination semantics, or size limits.

All endpoints are served over HTTPS (self-signed by default) on the local
Pane Gateway process (default host `127.0.0.1`, port from Pane's setup —
confirm via `PANE_GATEWAY_URL`). All routes below are prefixed with
`$PANE_GATEWAY_URL`.

## Auth model

- `POST /pair` and `GET /v1/health` are unauthenticated (health returns a
  reduced payload without a token; a fuller payload if a valid bearer token
  is presented).
- Every other route requires `Authorization: Bearer <token>`.
- Tokens are opaque, generated at pairing, valid 90 days, auto-rotated ~7
  days before expiry (rotation is handled by Pane's own app-side logic, not
  something this skill triggers).
- Missing/invalid/expired token → `401` with body
  `{"error":"unauthorized","status":401,"message":"Missing or invalid authorization token", ...}`.

## `POST /pair`

Exchange a 6-digit pairing code for a bearer token.

Request:
```json
{ "code": "123456" }
```

Response `200`:
```json
{
  "token": "hex-encoded-256-bit-token",
  "expires_at": "2026-11-14T00:00:00Z",
  "tenant_id": "default",
  "gateway_version": "0.x.y"
}
```

Errors: `401` if the code is wrong or expired (codes expire after 5 minutes;
a wrong code does NOT invalidate the still-active correct code — the user can
retry).

## `GET /v1/health`

Liveness + TLS pinning info. Unauthenticated response omits
`oc_connection_status` and `gateway_version`.

Unauthenticated response `200`:
```json
{
  "status": "healthy",
  "uptime": 1234,
  "tls_fingerprint": "sha256-hex-of-spki-der",
  "tls_cert_pem": "-----BEGIN CERTIFICATE-----...",
  "gateway_hostname": "optional-hostname-or-null"
}
```

Authenticated response `200` adds:
```json
{
  "oc_connection_status": "connected" | "disconnected" | "...",
  "gateway_version": "0.x.y"
}
```

`tls_cert_pem` is the value to save for `--cacert` pinning (see SKILL.md TLS
handling section). `tls_fingerprint` is a SHA-256 SPKI pin, useful if you want
to verify the cert out-of-band instead of trusting whatever `/v1/health`
returns on first contact (TOFU).

## `GET /v1/agents`

Lists OpenClaw agents registered with this gateway/tenant.

Response `200`:
```json
{ "agents": [ { "oc_agent_id": "main", "name": "...", "model": "...", "role": "...", "workspace": "...", "registered_at": "..." } ] }
```

## `GET /v1/models`

Lists available models (cached 30s server-side unless `?refresh=1`).

Response `200`:
```json
{
  "models": [ { "id": "...", "name": "...", "provider": "...", "context_window": 200000, "reasoning": true, "input": ["text"] } ],
  "source": "openclaw",
  "refreshed_at": "2026-08-16T..."
}
```

## `GET /v1/metrics`

Prometheus text-format metrics (`Content-Type: text/plain; version=0.0.4`).
Authenticated. Not typically useful for a conversational agent — informational
only.

## Sessions

### `POST /v1/sessions`

Request:
```json
{ "oc_agent_id": "main", "title": "optional title", "context_hint": "optional hint" }
```
`oc_agent_id` is required — it's the OpenClaw agent Pane routes the session
to (usually `"main"`).

Response `200`:
```json
{ "session_id": "gateway-uuid", "created_at": "...", "oc_session_id": "oc-internal-id" }
```
Use `session_id` (the gateway UUID) in all subsequent path params — it is a
gateway-local ID, distinct from the internal `oc_session_id`.

### `GET /v1/sessions`

Response `200`:
```json
{
  "sessions": [
    {
      "session_id": "...",
      "title": "...",
      "oc_agent_id": "...",
      "created_at": "...",
      "last_message_at": "... or null"
    }
  ]
}
```

### `DELETE /v1/sessions/:session_id`

Response `200`: `{ "deleted_at": "..." }`

### `GET /v1/sessions/:session_id/messages`

Query params:
- `limit` (default 50, max 200)
- `before` (cursor, optional)
- `since` (cursor, optional)

Response `200`:
```json
{ "messages": [ { "...opaque OC message object..." } ], "has_more": false, "next_cursor": null }
```
`messages[]` entries are pass-through JSON from OpenClaw's `chat.history` —
inspect with `jq` rather than assuming exact field names beyond the general
shape (role/content-style fields).

### `POST /v1/sessions/:session_id/messages`

Request:
```json
{ "content": "message text", "role": "user", "idempotency_key": "optional-uuid" }
```
- `content`: required, max 1 MiB (1,048,576 bytes). Oversized → `413`.
- `role`: defaults to `"user"`.
- `idempotency_key`: auto-generated UUID if omitted. Re-sending the SAME key
  returns the original accepted response instead of re-sending — use this
  deliberately for safe retries, and generate a fresh key for genuinely new
  messages.

Response `200`:
```json
{ "message_id": "gateway-uuid", "accepted_at": "...", "oc_message_id": "..." }
```
`accepted_at` only confirms the message was queued — Pane's assistant
processes it asynchronously. Poll `GET .../messages` or use the SSE stream to
see the reply.

### `GET /v1/sessions/:session_id/messages/stream`

Server-Sent Events (`text/event-stream`). Supports `Last-Event-ID` header for
replay of buffered events after a reconnect; if the requested sequence has
aged out of the buffer, you get a `replay.gap` event instead:
```
event: replay.gap
data: {"requested_sequence": N, "oldest_available": M, "message": "..."}
```
Normal events carry an `id:` (sequence number) and `event:` type (e.g.
`message.delta`, `message.complete`) with the payload as `data:`. Keep-alive
comment lines are sent every 15s.

curl consumption pattern:
```bash
curl -sS -N --cacert "$CACERT" \
  "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/messages/stream" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Last-Event-ID: 42"   # optional, to resume from sequence 42
```
Run this via a backgrounded `exec` if you need to keep working while
streaming; do not block the whole session waiting on a long stream unless
that's the explicit task.

### `POST /v1/sessions/:session_id/abort`

Response `200`: `{ "aborted_at": "..." }`. Aborts an in-flight generation for
that session; safe to call even if nothing is running.

## `POST /v1/chat/completions`

OpenAI-compatible chat completion proxy to OpenClaw, 8 MiB body limit.
Supports `"stream": true` (SSE response) or `false` (single JSON response).
The gateway overwrites `model` server-side to route through OpenClaw's
default agent — the `model` you send is informational only and does not
select a specific downstream model.

This bypasses Pane's session/message model entirely — nothing sent here
shows up in the Pane UI's chat history. Prefer session endpoints unless you
specifically need a stateless one-off completion.

## Sync endpoints

Identity-file sync only — a fixed allowlist, not general note storage.

Full allowlist:
- Main agent: `SOUL.md`, `MEMORY.md`, `IDENTITY.md`, `AGENTS.md`, `USER.md`,
  `TOOLS.md`, `HEARTBEAT.md`, `BOOTSTRAP.md`, `RULES.md`, plus depth-1
  `memory/*.md` and `logs/*.md` (no nested subdirectories).
- Sub-agents: `SOUL.md`, `MEMORY.md`, `IDENTITY.md`, `AGENTS.md`, `USER.md`,
  `TOOLS.md` only (no HEARTBEAT/BOOTSTRAP/RULES, no memory/logs).

### `POST /v1/sync/push`

Request:
```json
{ "oc_agent_id": "main", "filename": "MEMORY.md", "content": "...", "checksum": "sha256-hex-of-content" }
```
- Max 10 MiB content.
- `checksum` must be the SHA-256 hex digest of `content` — the server
  recomputes and rejects (`400`) on mismatch, so compute it correctly:
  `printf '%s' "$CONTENT" | shasum -a 256 | cut -d' ' -f1`.
- `filename` must be on the allowlist for the agent's role (main vs.
  sub-agent) — non-allowlisted files are rejected `400`.

Response `200`: `{ "written_at": "...", "checksum": "..." }`

### `GET /v1/sync/pull?oc_agent_id=main`

Response `200`: `{ "pending_changes": [ /* PendingChange objects */ ] }`

### `DELETE /v1/sync/pull/confirm`

Request:
```json
{ "oc_agent_id": "main", "processed_ids": ["id1", "id2"] }
```
Response `200`: `{ "confirmed": 2 }`

### `GET /v1/sync/initial`

Bulk fetch of all agents' allowlisted files (no request body).

Response `200`:
```json
{
  "agents": [
    {
      "oc_id": "main",
      "name": "...",
      "files": [ { "filename": "SOUL.md", "content": "...", "checksum": "..." } ]
    }
  ]
}
```

## Error shape

All non-2xx responses use this shape:
```json
{
  "error": "unauthorized" | "invalid_request" | "payload_too_large" | "...",
  "status": 401,
  "message": "human-readable explanation",
  "retry_after": null,
  "max_bytes": null
}
```
`retry_after` / `max_bytes` are populated for rate-limit and payload-too-large
errors respectively.

## Unreachable/blocked-in-v1 endpoints

These do **not** exist on the gateway and should never be constructed:
`POST/GET/PUT/DELETE /v1/notes*`, `/v1/tasks*`, `/v1/projects*`,
`/v1/folders*`. Requests to any of these hit the router's fallback handler
(404). Use the conversational session flow in `SKILL.md` instead.
