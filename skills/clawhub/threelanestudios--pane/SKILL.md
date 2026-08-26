---
name: pane
description: "Operate Pane through its local Gateway: create notes, tasks, and projects via chat sessions; manage AI sessions; sync agent identity files."
version: 1.2.0
metadata:
  openclaw:
    emoji: "🗂️"
    homepage: "https://paneapp.ai/?utm_source=clawhub"
    requires:
      env:
        - PANE_GATEWAY_URL
        - PANE_GATEWAY_TOKEN
      bins:
        - curl
    primaryEnv: PANE_GATEWAY_TOKEN
    envVars:
      - name: PANE_GATEWAY_URL
        required: true
        description: "Base URL of the local Pane Gateway (e.g. https://127.0.0.1:8443)"
      - name: PANE_GATEWAY_TOKEN
        required: true
        description: "Bearer token from Pane Gateway pairing (POST /pair)"
      - name: PANE_GATEWAY_INSECURE_TLS
        required: false
        description: "Set to 1 to skip TLS verification for self-signed gateway certs (dev convenience, not recommended for production)"
---

# Pane

Operate a locally running [Pane](https://paneapp.ai/?utm_source=clawhub) app through its Gateway
HTTP API: create/manage notes, tasks, projects, and folders **conversationally**
via chat sessions; manage sessions directly; sync agent identity files.

Requires `PANE_GATEWAY_URL` and `PANE_GATEWAY_TOKEN` already provisioned (see
Setup). Every authenticated call uses `exec` + `curl` — the gateway needs a
custom `Authorization: Bearer` header and a self-signed TLS cert by default,
so `web_fetch` is not a good fit here.

Pane is a local-first desktop workspace (macOS/Linux) where you and your AI
share notes, tasks, and projects — one place for conversations, documents,
and boards. Pane is a paid app — pricing at paneapp.ai. This skill requires
a running, paired Pane Gateway.

## Setup (one-time, human-in-the-loop)

Pairing exchanges a 6-digit code (shown in the Pane app / gateway logs, 5-min
expiry) for a 90-day bearer token. This skill assumes a human has already
paired and exported the env vars — it does **not** walk through pairing
interactively, since the code is time-limited and shown in the Pane UI, not
to this agent.

If the user asks you to pair for them and gives you a live code immediately,
fetch the gateway's cert first (see TLS handling below), then pair:

```bash
curl -sS "$PANE_GATEWAY_URL/v1/health" | jq -r '.tls_cert_pem' > /tmp/pane-gateway.pem
CACERT=/tmp/pane-gateway.pem

curl -sS --cacert "$CACERT" \
  -X POST "$PANE_GATEWAY_URL/pair" \
  -H "Content-Type: application/json" \
  -d '{"code":"123456"}'
```

Response: `{"token": "...", "expires_at": "...", "tenant_id": "default", "gateway_version": "..."}`.
Save `token` as `PANE_GATEWAY_TOKEN`. Never print/log the token in full in chat
transcripts — treat it as a secret.

## TLS handling

Pane Gateway uses a self-signed cert by default (`GATEWAY_TLS_MODE=selfsigned`).
Two options, in order of preference:

**1. Pin the cert (recommended).** Fetch the cert once via the unauthenticated
health check, save it, and pass it to every subsequent call:

```bash
curl -sS "$PANE_GATEWAY_URL/v1/health" | jq -r '.tls_cert_pem' > /tmp/pane-gateway.pem
curl -sS --cacert /tmp/pane-gateway.pem "$PANE_GATEWAY_URL/v1/health"
```

**2. Skip verification (dev only).** If `PANE_GATEWAY_INSECURE_TLS=1` is set,
use `-k`/`--insecure`. Do not default to this silently — only use it when the
env var is explicitly set, and mention to the user that verification is
skipped.

```bash
if [ "$PANE_GATEWAY_INSECURE_TLS" = "1" ]; then
  curl -sS -k "$PANE_GATEWAY_URL/v1/health"
else
  curl -sS --cacert /tmp/pane-gateway.pem "$PANE_GATEWAY_URL/v1/health"
fi
```

The rest of this doc uses `--cacert "$CACERT"` in examples; substitute `-k`
per the above when `PANE_GATEWAY_INSECURE_TLS=1`.

## Headline capability: conversational note/task/project operations

**The Pane Gateway does NOT expose direct REST endpoints for note, task,
project, or folder CRUD.** Those operations only exist as Tauri-internal
commands used by Pane's in-app AI assistant. The way an external agent
creates/edits notes, tasks, projects, and folders is by **messaging through a
Pane chat session** — Pane's own in-app AI reads the message, decides which
tool(s) to call, and executes them app-side.

Flow:

1. **Create a session** — `POST /v1/sessions`
2. **Send a message** describing what you want — `POST /v1/sessions/:id/messages`
3. Pane's assistant interprets the message and calls the appropriate
   tool(s) internally: `create_note`, `edit_note`, `append_to_note`,
   `create_project`, `create_folder`, `set_status`, `search_notes`, etc.
4. **Read the result** — `GET /v1/sessions/:id/messages` (poll) or
   `GET /v1/sessions/:id/messages/stream` (SSE, real-time)

Write your message like you're talking to a capable assistant that already
knows Pane's data model — be specific about title, project, and any status/due
date, the same way you'd phrase it to a human assistant. Don't try to call
`create_note` etc. yourself; there is no such REST endpoint.

### Worked example: create a note

```bash
CACERT=/tmp/pane-gateway.pem

# 1. Create a session (oc_agent_id is the OpenClaw agent Pane should route to
#    — usually "main" unless the user has a specific Pane-side agent in mind)
SESSION=$(curl -sS --cacert "$CACERT" \
  -X POST "$PANE_GATEWAY_URL/v1/sessions" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"oc_agent_id":"main","title":"Agent task"}')
SESSION_ID=$(echo "$SESSION" | jq -r '.session_id')

# 2. Send a message describing the desired note
curl -sS --cacert "$CACERT" \
  -X POST "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/messages" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content":"Create a note called '\''Meeting Notes'\'' in the Work project with today'\''s agenda: 1. Budget review 2. Q3 roadmap"}'

# 3. Poll for the response (Pane's assistant needs a moment to run tools)
sleep 3
curl -sS --cacert "$CACERT" \
  "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/messages?limit=10" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" | jq '.messages'
```

The assistant's reply in `messages` confirms what it did (e.g. "Created
'Meeting Notes' in Work"). If the reply is ambiguous or reports failure,
re-phrase the request with more specific project/folder names — Pane's
assistant resolves `project_id`/`folder_id`/`note_id` by name or UUID, so
typos or ambiguous names ("the work project" when two projects contain
"work") can misfire.

### What you can ask for conversationally

Phrase requests around these operations (Pane's in-app AI executes them):

- **Create a note/task** — title, project (required), folder, status
  (`cabinet`/`todo`/`in_progress`/`review`/`done`), due date, initial content,
  priority (`low`/`medium`/`high`/`urgent`).
- **Edit a note** — change content, title, status, or due date. Reference the
  note by title or ID.
- **Append to a note** — add text to the end without replacing existing
  content (preferred over "edit" for adding to logs/journals).
- **Create a project** — top-level container, just needs a name.
- **Create a folder** — needs a name and a parent project.
- **Set a task's status** — move between cabinet/todo/in_progress/review/done.
- **Search notes** — find notes by title/content match.

Do not attempt to construct direct REST calls like `POST /v1/notes` — they
do not exist. If unsure whether Pane executed an action, ask it to confirm
("search for the note you just created") in a follow-up message on the same
session.

## Proactive multi-step work in Pane sessions

When a request in a Pane session implies multi-step or long-running work,
do not complete it in one turn and do not wait to be prompted between steps.
Instead:

1. Acknowledge the task and do the first step now. Confirm in that same reply that the remaining steps are scheduled.
2. Schedule each subsequent step as a one-shot cron targeting this same Pane session:
   ```bash
   openclaw cron add --at "+90s" --message "<next step instruction>" --session-key "<this session's key>" --no-deliver --delete-after-run
   ```
   Your current session key is in the `## Runtime` section of your system prompt (`session=agent:<agentId>:openai-user:pane-<sessionId>`). Use it exactly.
3. Never use `--announce`, any delivery mode, or `--session isolated`. The Pane transcript is the delivery: Pane polls this session and shows your reply automatically.
4. Report each completed step as its own reply. Schedule silently — do not narrate cron mechanics to the user.
5. Delivery latency is up to 60 seconds per step while the user has the session open. Messages sent while Pane is closed appear when the user next opens the session.

## Direct REST operations

All authenticated routes require `Authorization: Bearer $PANE_GATEWAY_TOKEN`.
`/v1/health` and `/pair` are unauthenticated (health returns a reduced
payload without auth).

### Health check

```bash
curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/health"
# Authenticated (fuller response incl. oc_connection_status):
curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/health" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"
```

### Agents & models (introspection)

```bash
curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/agents" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"

curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/models" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"
# Force refresh (bypass 30s cache):
curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/models?refresh=1" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"
```

### Sessions

```bash
# Create
curl -sS --cacert "$CACERT" -X POST "$PANE_GATEWAY_URL/v1/sessions" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"oc_agent_id":"main","title":"My session","context_hint":"optional hint"}'

# List
curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/sessions" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"

# Send a message (idempotency_key auto-generated if omitted; pass your own to
# safely retry a POST without risking a duplicate send)
curl -sS --cacert "$CACERT" \
  -X POST "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/messages" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content":"Hello Pane","idempotency_key":"'"$(uuidgen)"'"}'

# Read messages (paginated: before/since cursors, limit up to 200, default 50)
curl -sS --cacert "$CACERT" \
  "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/messages?limit=50" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"

# Abort an in-flight generation
curl -sS --cacert "$CACERT" -X POST "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/abort" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"

# Delete a session
curl -sS --cacert "$CACERT" -X DELETE "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"
```

Message content is capped at 1 MiB. Message bodies from `GET messages` are
opaque JSON objects passed through from OpenClaw — inspect with `jq` rather
than assuming a fixed schema; look for `role`/`content`-style fields.

### Streaming (SSE)

`GET /v1/sessions/:id/messages/stream` returns `text/event-stream`. Use curl's
`-N` (no-buffer) flag to consume it live:

```bash
curl -sS -N --cacert "$CACERT" \
  "$PANE_GATEWAY_URL/v1/sessions/$SESSION_ID/messages/stream" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"
```

To resume after a disconnect, pass `Last-Event-ID: <sequence>` to replay
buffered events (falls back to a `replay.gap` event if the buffer has already
rolled past that sequence). This is a real HTTP SSE stream, not WebSocket —
run it as a background `exec` process if you need to consume it alongside
other work; do not attempt to open a WebSocket connection to the gateway
(clients never connect via WS — only the gateway's internal
Gateway→OpenClaw link uses WS).

### Direct chat proxy

`POST /v1/chat/completions` proxies straight to OpenClaw's OpenAI-compatible
chat endpoint (8 MiB body limit, supports `"stream": true`/`false`). Prefer
the session endpoints above for anything that should show up in Pane's UI —
use this only when you need a raw one-off completion outside of a Pane
session.

```bash
curl -sS --cacert "$CACERT" -X POST "$PANE_GATEWAY_URL/v1/chat/completions" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"model":"openclaw","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

### Identity file sync (not general notes)

Sync endpoints move a fixed allowlist of **agent identity files**
(`SOUL.md`, `MEMORY.md`, `IDENTITY.md`, `AGENTS.md`, `USER.md`, `TOOLS.md`,
plus `HEARTBEAT.md`/`BOOTSTRAP.md`/`RULES.md` and `memory/*.md`/`logs/*.md`
for the main agent only). This is the OC↔Pane agent-identity sync mechanism,
unrelated to the notes/cabinet data model — do not use this for general note
content.

```bash
# Full initial sync (all agents, all allowlisted files)
curl -sS --cacert "$CACERT" "$PANE_GATEWAY_URL/v1/sync/initial" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"

# Pull pending changes for one agent
curl -sS --cacert "$CACERT" \
  "$PANE_GATEWAY_URL/v1/sync/pull?oc_agent_id=main" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN"

# Confirm processed changes
curl -sS --cacert "$CACERT" -X DELETE "$PANE_GATEWAY_URL/v1/sync/pull/confirm" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"oc_agent_id":"main","processed_ids":["id1","id2"]}'

# Push a file (checksum is SHA-256 hex of content, verified server-side)
CONTENT='# Updated memory'
CHECKSUM=$(printf '%s' "$CONTENT" | shasum -a 256 | cut -d' ' -f1)
curl -sS --cacert "$CACERT" -X POST "$PANE_GATEWAY_URL/v1/sync/push" \
  -H "Authorization: Bearer $PANE_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg agent main --arg fn MEMORY.md --arg content "$CONTENT" --arg cs "$CHECKSUM" \
    '{oc_agent_id:$agent, filename:$fn, content:$content, checksum:$cs}')"
```

Push is capped at 10 MiB and rejects any filename not on the allowlist
(`GatewayError::InvalidRequest`, 400).

See `references/gateway-api.md` for the full endpoint reference including
request/response field details.

## Known limitations (do not work around these)

- **No direct note/task/project/folder REST CRUD.** Use the conversational
  session flow above. Do not construct calls like `POST /v1/notes` — they
  return 404 (fallback handler).
- **No WebSocket for clients.** Only `exec`+`curl` over plain HTTP/SSE.
- **Sync endpoints are identity-file-only**, not a general note-editing
  channel — the allowlist is enforced server-side and anything else is
  rejected.

## Common errors & troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `curl: (60) SSL certificate problem` | Self-signed cert, not pinned | Fetch `tls_cert_pem` from `/v1/health` and use `--cacert`, or set `PANE_GATEWAY_INSECURE_TLS=1` and use `-k` |
| `401 {"error":"unauthorized",...}` | Missing/expired/invalid `Authorization` header | Confirm `Bearer $PANE_GATEWAY_TOKEN` is set; token expires 90 days after pairing — re-pair if expired |
| `curl: (7) Failed to connect` | Gateway not running, or wrong port | Confirm `PANE_GATEWAY_URL` matches the running gateway (default port per Pane docs); check the Pane app is open |
| `404 {"error":"not_found","message":"Unknown endpoint"}` on any `/v1/notes`, `/v1/tasks`, `/v1/projects` path | Those routes don't exist | Use the conversational session flow instead |
| `413`/`{"error":"payload_too_large",...}` | Message >1 MiB or sync push >10 MiB or chat body >8 MiB | Shorten the payload |
| Session message sent but nothing seems to happen | Pane's assistant runs async; you polled too soon | Wait 2-5s (or use the SSE stream) before reading messages |
| Assistant's reply says it couldn't find the project/note | Ambiguous or misspelled name in your message | Re-phrase with the exact project/folder/note title, or `search_notes` first via a session message |
| Idempotent retry returns the same `message_id` unexpectedly | Working as intended — same `idempotency_key` reused | Generate a new `idempotency_key` (e.g. `uuidgen`) for a genuinely new message |
| Scheduled step never appeared in Pane | `--session-key` was not used (or `--session isolated` was used), or a delivery mode was set | Verify `--session-key` was used (not `--session isolated`) and no delivery mode; confirm the key matches the `## Runtime` line |

## Publishing (for the skill maintainer, not the agent)

```bash
npm i -g clawhub
clawhub login
clawhub whoami

clawhub skill publish ./pane \
  --slug pane \
  --name "Pane" \
  --version 1.0.0 \
  --changelog "Initial release: conversational note/task/project ops via chat sessions, session/chat/sync REST operations"
```

Org-scoped publish target: `@ThreeLaneStudios/pane`. See `PUBLISHING.md` for
the full command reference.
