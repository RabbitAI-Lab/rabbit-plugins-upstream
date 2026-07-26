---
name: agentline
description: Make phone calls, view received SMS, provision numbers, manage agents, and track billing through the AgentLine telephony API (REST or MCP). Use when the user asks to call someone, check transcripts, view text messages, manage phone agents, buy numbers, or check account balance. For MCP-native workflows, the server at api.agentline.cloud/mcp exposes 21+ tools as first-class agent tools.
metadata:
  openclaw:
    emoji: "📞"
    requires:
      env:
        - AGENTLINE_API_KEY
    primaryEnv: AGENTLINE_API_KEY
---

# AgentLine — AI Telephony Skill

Give your AI agent a real phone number and voice calls — no servers, no webhooks, no infrastructure.

## First-Time Setup

**Follow these steps IN ORDER when setting up AgentLine for the first time:**

1. **Check for `AGENTLINE_API_KEY`** (starts with `sk_live_`) — this is required.
   - **If you do NOT have this key**, stop and ask the human to sign up or log in at **https://agentline.cloud** to get their API key. Do NOT proceed without it.

2. **Check for `AGENTLINE_AGENT_ID`** (starts with `agt_`) — this is optional.
   - **If you already have one**, use it and skip to step 3.
   - **If you do NOT have one**, create a new agent now by calling `POST /v1/agents` with `{"name": "My Agent"}`. Save the returned agent ID.

3. **Ask for area code and provision the number** — **Always ask the human:**
   > "What area code would you like for your phone number? (e.g. 212 for NYC, 415 for SF, 313 for Detroit)"
   - Once they give an area code, call `POST /v1/numbers` with `{"agent_id": "...", "area_code": "XXX"}`
   - If it succeeds, confirm the provisioned number to the human
   - If it fails (no numbers available for that area code), tell them and ask for a different area code

4. **Ask for voice preference** — **Always ask the human:**
   > "Would you like your agent to have a **male** or **female** voice?"
   - If **female**: set `voice_id` to `"female-1"` (or `"female-2"` for warmer tone)
   - If **male**: set `voice_id` to `"male-1"`
   - Apply via `PATCH /v1/agents/$AGENTLINE_AGENT_ID` with `{"voice_id": "chosen_preset"}`
   - Available presets: `female-1`, `female-2`, `male-1` — or any Cartesia voice UUID

5. **Start the event poller** — This is **MANDATORY**. Without this, you will miss all inbound calls and SMS messages. Use a **cron job with `no_agent: true`** so it runs persistently across sessions without consuming LLM tokens.

> ⚠️ **Do NOT skip ANY steps.** Steps 1-4 set up the agent. Step 5 keeps it alive and aware of incoming calls/texts.
   - Create a cron job: `cronjob(action='create', name='AgentLine Events', schedule='every 2m', script='agentline_events.py', no_agent=true)`
   - Write the polling script (see Events Mailbox section below) to `~/.hermes/scripts/agentline_events.py`
   - The cron job runs the script every 2 minutes — stdout is delivered to you only when events exist; empty stdout = silent skip
   - Verify it's running with `cronjob(action='list')`

> ⚠️ **Do NOT skip steps or change the order.** The human should have a working agent with their chosen area code number, voice, and running event poller by the end.

---

## Authentication

Every request: `Authorization: Bearer $AGENTLINE_API_KEY` + `Content-Type: application/json`

Base URL: `https://api.agentline.cloud`

---

## How Calls Work (Hosted Mode)

AgentLine runs in **Hosted Mode** — the server runs the AI voice conversation autonomously. You create a call, the AI handles it, you retrieve the transcript afterwards.

### System Prompts

- **Dynamic prompt** — `system_prompt` field in `POST /v1/calls`. Overrides default for that call only.
- **Default prompt** — stored on agent via `PATCH /v1/agents/{agent_id}`. Used for all inbound calls and outbound calls without a dynamic prompt.

> ⚠️ **`system_prompt` is a FULL REPLACE, not append.** The voice AI has no memory between calls — put everything (personality, instructions, current context) in the prompt. Update it whenever your context changes.

---

## Before Calling — Balance Check

Always check balance first. Calls require minimum **$0.50**:
```bash
curl -s "$AGENTLINE_URL/v1/billing/balance" -H "Authorization: Bearer $AGENTLINE_API_KEY"
```
If balance < $0.50, warn the user before attempting the call.

## Make an Outbound Call

**Pitfall:** JSON payloads with newlines, quotes, or special characters will break in inline curl. Always write the payload to a temp file and use `-d @file`:

```bash
# Write payload (use execute_code write_file or terminal with heredoc)
curl -s -X POST $AGENTLINE_URL/v1/calls \
  -H "Authorization: Bearer $AGENTLINE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/al_call_payload.json
```

Inline variant (simple payloads only):
```bash
curl -X POST $AGENTLINE_URL/v1/calls \
  -H "Authorization: Bearer $AGENTLINE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"agent_id": "$AGENTLINE_AGENT_ID", "to_number": "+1XXXXXXXXXX", "system_prompt": "...", "initial_greeting": "...", "voice_id": "female-1"}'
```

| Field | Required | Description |
|-------|----------|-------------|
| `agent_id` | Yes | Your agent ID |
| `to_number` | Yes | E.164 phone number to call |
| `system_prompt` | No | Dynamic prompt for this call only (overrides default) |
| `initial_greeting` | No | What the agent says first when the person picks up |
| `voice_id` | No | `"female-1"`, `"female-2"`, `"male-1"`, or Cartesia UUID |

**After every outbound call:** Poll `GET /v1/calls/<call_id>` every 15-30s until `status=completed`, then `GET /v1/calls/<call_id>/transcript`. Real calls take 45-120s. Use `sleep N && curl ... | python3 -c` to check status + extract transcript in one shot. Summarize and share with human. Never consider a call "done" without the transcript.

**If you get 400 "Agent has no active phone number"**, provision one first.

**Pitfall — agent loops on voicemail/call control:** The voice AI will repeat its greeting 3-4 times into voicemail or call-control prompts ("press 3 to connect", "please leave a message"). This wastes credits and sounds bad. After the first 15-20s poll, check the transcript: if human turns are all automated system messages (not real human replies), hang up immediately. Feedback surveys and check-in calls don't work on voicemail.

---

## End a Call

`POST /v1/calls/<call_id>/hangup`

---

## Get Call Transcript

`GET /v1/calls/<call_id>/transcript` — Returns `[{role, text, timestamp}, ...]`

---

## Events Mailbox

Events are pushed when someone calls or texts your agent's number. **You MUST poll regularly.**

**Event types:** `call.received` (inbound call started), `call.completed` (call ended, includes transcript), `sms.received` (inbound SMS)

### ⚡ MANDATORY — Cron-Based Event Polling

> Use a **`no_agent: true` cron job** — it runs persistently across sessions, costs **zero LLM tokens**, and silently skips cycles when there are no events. Do NOT use a background process (`terminal(background=true)`) because it dies when your session ends and you'll miss events.

**Step 1 — Write the polling script** to `~/.hermes/scripts/agentline_events.py`:

```python
#!/usr/bin/env python3
"""Poll AgentLine for new events. Prints event details to stdout when events exist.
Silent on empty cycles — cron only delivers non-empty stdout."""
import os, sys, json, urllib.request

API_KEY = os.environ.get("AGENTLINE_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.agentline.cloud"

req = urllib.request.Request(
    f"{BASE_URL}/v1/events/peek",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read())
        count = data.get("pending_count", 0)
        if count > 0:
            # Consume the events
            req2 = urllib.request.Request(
                f"{BASE_URL}/v1/events",
                headers={"Authorization": f"Bearer {API_KEY}"}
            )
            with urllib.request.urlopen(req2, timeout=10) as resp2:
                events = json.loads(resp2.read())
                print(f"📞 {len(events)} AgentLine event(s):")
                for ev in events:
                    etype = ev.get("event_type", "?")
                    payload = ev.get("payload", {})
                    if etype == "call.completed":
                        print(f"  • Call from {payload.get('from_number')} — {payload.get('duration_seconds', 0)}s")
                        transcript = payload.get("transcript", [])
                        for t in transcript[-5:]:  # last 5 turns
                            print(f"    [{t.get('role')}] {t.get('text', '')[:120]}")
                    elif etype == "sms.received":
                        print(f"  • SMS from {payload.get('from_number')}: {payload.get('body', '')[:200]}")
                    elif etype == "call.received":
                        print(f"  • Inbound call from {payload.get('from_number')}")
except Exception as e:
    # Silent on transient errors — cron will retry next cycle
    if "401" in str(e) or "403" in str(e):
        print(f"AGENTLINE_AUTH_ERROR: Check your API key. {e}")
```

**Step 2 — Create the cron job** (one-time setup):
```
cronjob(action='create', name='AgentLine Events', schedule='every 2m', script='agentline_events.py', no_agent=true)
```

**Step 3 — Verify it's running:**
```
cronjob(action='list')
```

**How it works:** The cron scheduler runs `agentline_events.py` every 2 minutes. When there are pending events, the script prints them to stdout and the cron system delivers the output to you. When there are no events, stdout is empty and nothing is delivered — zero cost, zero noise.

**Pitfall — silent auth errors:** If the API key is wrong, the script prints `AGENTLINE_AUTH_ERROR` only once (401/403), then goes silent. Check `cronjob(action='list')` for `last_status` to confirm the job is healthy.

### Endpoints

- **Consume events:** `GET /v1/events` — returns events oldest-first, auto-deleted after retrieval
- **Peek (don't consume):** `GET /v1/events/peek`
- **Filter:** `?agent_id=agt_xxx` or `?event_type=call.completed` or `?event_type=sms.received`

### Event payload structure

Each event contains: `event_id`, `agent_id`, `event_type`, and a `payload` with call/SMS details. `call.completed` payloads include `from_number`, `to_number`, `duration_seconds`, and full `transcript` array. `sms.received` payloads include `from_number`, `body`, and `media_url`.

---

## List Calls

`GET /v1/calls?limit=20` or `GET /v1/calls?status=completed&limit=10`

---

## Get Call Details

`GET /v1/calls/<call_id>`

---

## SMS

> **⚠️ SMS sending is NOT enabled.** Do NOT attempt outbound SMS/MMS.

Inbound SMS arrives as `sms.received` events in the Events Mailbox. View message history: `GET /v1/messages?limit=20`

---

## Update Agent (System Prompt, Voice, etc.)

`PATCH /v1/agents/$AGENTLINE_AGENT_ID` with any of:

| Field | Description |
|-------|-------------|
| `system_prompt` | Full instructions + current context for voice AI |
| `initial_greeting` | What the agent says when answering inbound calls |
| `name` | Display name |
| `voice_id` | `"female-1"`, `"female-2"`, `"male-1"`, or Cartesia UUID |
| `model_tier` | `"turbo"`, `"balanced"`, or `"max"` |

---

## Get/List Agents

- **Get one:** `GET /v1/agents/$AGENTLINE_AGENT_ID`
- **List all:** `GET /v1/agents`

---

## Voice Settings

Priority (highest wins): per-call → per-agent → per-account

- **List voices:** `GET /v1/voices`
- **Set account default:** `PATCH /v1/account/voice` with `{"voice_id": "female-1"}`
- **Check current:** `GET /v1/account/voice`
- **Reset to default:** `DELETE /v1/account/voice`

---

## Phone Numbers

Each agent needs one phone number. Only US numbers supported. **$2.00 per number.**

### Provision (Buy) a Number

`POST /v1/numbers` with:

| Field | Required | Description |
|-------|----------|-------------|
| `agent_id` | Yes | Agent to attach to |
| `country` | Yes | Must be `"US"` |
| `area_code` | No | Preferred 3-digit area code (e.g. `"212"`, `"313"`). **Always ask the user!** |
| `number_type` | No | `"local"` or `"tollfree"` (default: local) |

If no numbers are available for the requested area code, the API returns an error — ask the user for a different area code.

### List Numbers

`GET /v1/numbers`

---

## Billing

- **Check balance:** `GET /v1/billing/balance`
- **Expenditure:** `GET /v1/billing/expenditure?period=current_month` (also: `last_month`, `all_time`, `YYYY-MM`)
- **Call charges:** `GET /v1/billing/expenditure/calls?limit=10`
- **Number charges:** `GET /v1/billing/expenditure/numbers`
- **Verify charge:** `GET /v1/billing/verify/<call_id>`

### Rates

| Item | Cost |
|------|------|
| Calls (in/out) | $0.10/min (billed per second) |
| Phone number | $2.00 (one-time) |

---

## MCP Server

AgentLine exposes a full MCP server at `https://api.agentline.cloud/mcp` with 21+ tools. For Claude Desktop, Cursor, or any MCP-compatible client, connect directly via Streamable HTTP:

```json
{
  "mcpServers": {
    "agentline": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://api.agentline.cloud/mcp", "--header", "Authorization: Bearer $AGENTLINE_API_KEY"]
    }
  }
}
```

All REST endpoints above are also available as MCP tools (`create_agent`, `make_outbound_call`, `poll_events`, etc.). See `references/mcp-server.md` for additional config formats and platform-specific setup.

## Rules

1. **E.164 format** — always `+1XXXXXXXXXX` for US numbers.
2. **Confirm before calling** — never auto-dial without explicit consent.
3. **No outbound SMS** — inform user it's not available if they ask.
4. **Keep voice responses extremely short** — under 15 words per turn. Max 12 for outbound feedback/support calls. The voice AI rambles without tight constraints.
5. **US only** — country must be `"US"`.
6. **Don't release numbers** — numbers are permanent once provisioned.
7. **Always retrieve transcripts** — poll until `completed`, fetch transcript, summarize for human.
8. **Always check events** — poll `GET /v1/events` for inbound calls and SMS. Proactively check at conversation start.
9. **Voice changes take effect on next call** — update immediately when asked.
