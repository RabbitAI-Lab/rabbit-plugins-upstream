---
name: voice-lead-recovery
description: Turn voicemails and sales-call recordings into recovered revenue. Extracts requested service, urgency, objections, and promised follow-up; remembers prior contact; prepares the next action. Use when an agent handles inbound call/voicemail leads for contractors, agencies, or service businesses. Requires a BlueColumn API key (bc_live_*).
---

# Voice Lead Recovery — BlueColumn Skill

Every unanswered voicemail is a quote you never sent. This skill turns call recordings and voicemails into structured leads, remembers each caller across conversations, and tells the agent what to do next — so no inquiry dies between the phone and the estimate.

## Setup

Get a free key at https://bluecolumn.ai/login (no card). Keys look like `bc_live_*`. Base URL: `https://api.bluecolumn.ai`.

## Capture the lead

Send the voicemail or call audio; BlueColumn transcribes it and stores the structured lead.

```bash
curl -X POST https://api.bluecolumn.ai/remember \
  -H "Authorization: Bearer $BLUECOLUMN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "audio_url": "https://example.com/voicemail-2026-09-29-0812.mp3",
    "text": "VOICEMAIL LEAD — caller Dana (602-555-0147). Requests: roof inspection after storm. Urgency: high, water coming in garage. Objections: worried about cost, asked for financing options. Promised follow-up: call back with inspection slot today. Tone: stressed, motivated. Source: voicemail, 09-29 08:12.",
    "title": "lead - roof inspection - Dana 602-555-0147"
  }'
```

## Before you call back

Pull the caller's history and open promises the moment you have the number.

```bash
curl -X POST https://api.bluecolumn.ai/recall \
  -H "Authorization: Bearer $BLUECOLUMN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "What do we know about Dana 602-555-0147 and what did we promise?"}'
```

## Log the outcome fast

After the call, store the result so the next touch is informed.

```bash
curl -X POST https://api.bluecolumn.ai/note \
  -H "Authorization: Bearer $BLUECOLUMN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Dana booked inspection 09-30 10:00. Send financing PDF before visit. If not home, text instead of call.", "tags": ["lead", "roofing", "scheduled"]}'
```

## Workflow

1. **On new voicemail/call** — store the audio + a structured summary (service, urgency, objection, promise).
2. **Before replying** — recall the caller's full history and open promises.
3. **After contact** — store a one-line outcome note with the next action.
4. **Daily** — recall open leads ("which leads haven't been contacted in 24h?") and surface the oldest first.

## Billing

If the API returns `402` or `429`, read `topup_url` / `upgrade_url` from the error body and surface that link to the user — do not retry.

## Docs

API reference: https://bluecolumn.ai/docs — fields are `text`, `q`, `tags` (not `content`/`query`/`note`).
