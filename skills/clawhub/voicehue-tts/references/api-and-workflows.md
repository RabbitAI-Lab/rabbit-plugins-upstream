# VoiceHue API, SDKs, Pronunciations & Audio Workflows

All endpoints live under `https://voicehue.com/v1` and use `Authorization: Bearer $VOICEHUE_API_KEY` (except `GET /v1/voices`, which is public). Full machine-readable specification: `https://voicehue.com/openapi.json`.

---

## 1. Pronunciation Lists (`pronunciations`)

Accepted by `POST /v1/audio/speech`, `POST /v1/audio/speech/jobs`, and `POST /v1/audio/dialogue` (top-level field applied to every block):

- Up to **200 entries**; each `from` and `to` up to **100 characters**.
- Plain text substitution applied before synthesis (works identically on every voice):
  - Longest matching term wins (`"New York City"` before `"New York"`).
  - Latin-script terms match whole words only (`"SQL"` does not alter `"MySQL"`).
  - Chinese, Japanese, and Korean terms match anywhere.
  - Optional `"match_case": true` enforces exact case.
  - Inline pause tokens like `[0.5s]` or `[500ms]` are preserved untouched.
  - Character limits and billing count the rewritten text.

Example `pronunciations.json`:
```json
[
  {"from": "SQL", "to": "sequel"},
  {"from": "Next.js", "to": "Next J S"},
  {"from": "重庆", "to": "崇庆"},
  {"from": "VoiceHue", "to": "Voice Hue", "match_case": true}
]
```

---

## 2. Multi-Voice Dialogue Contract (`POST /v1/audio/dialogue`)

Returns one merged MP3 (64 kbps mono) or 16-bit WAV file.

| Field | Range / Limit | Notes |
|---|---|---|
| `blocks` | 1–20 (free) / 1–100 (pro) | Ordered speaker lines; max 5,000 chars across all blocks (1,000/block on free) |
| `blocks[].voice` | required | Voice ID from `GET /v1/voices` |
| `blocks[].input` | required | Spoken text for this block |
| `blocks[].speaker` | optional, ≤40 chars | Metadata label only (never spoken) |
| `blocks[].speed` | `0.5` to `2` (default `1`) | Pitch-preserving speaking speed |
| `blocks[].pitch` | `-4` to `4` (default `0`) | Pitch shift in semitones |
| `blocks[].volume` | `25` to `200` (default `100`) | Volume percentage |
| `blocks[].pause_ms` | `0` to `5000` (default `400`) | Silence inserted after this block |
| `response_format` | `"mp3"` or `"wav"` | Default `"mp3"` |

- Counts as **one** request against the key's RPM limit; each block bills characters like `/v1/audio/speech`.
- Send an `Idempotency-Key` header so retries never charge a block twice.
- Response headers include `X-VoiceHue-Duration` (seconds) and `X-VoiceHue-Blocks`.

---

## 3. Long Texts & Signed Webhooks (`POST /v1/audio/speech/jobs`)

- Accepts up to **20,000 characters** per job (up to 5 open jobs per key).
- Returns `202 Accepted` with `{id, status: "queued", ...}`.
- Poll `GET /v1/audio/speech/jobs/{id}` until `status` is `completed` or `failed`.
- On `completed`, `audio.url` is valid for up to **24 hours** (bounded by the file's 24-hour retention; re-fetch the job if you need a fresh link while retained).
- Failed jobs are never charged.

### Verifying `callback_url` Webhooks (Node.js)

Fetch your signing secret once via `GET https://voicehue.com/v1/webhook-secret`. Callbacks send headers `VoiceHue-Event` (`speech.job.completed` or `speech.job.failed`), `VoiceHue-Job-Id`, and `VoiceHue-Signature: t=<unix>,v1=<hex>`:

```js
import crypto from "node:crypto";

export function verifyVoiceHueWebhook(rawBody, signatureHeader, secret) {
  if (typeof signatureHeader !== "string") return false;
  const parts = Object.fromEntries(
    signatureHeader.split(",").map((p) => {
      const idx = p.indexOf("=");
      return idx > 0 ? [p.slice(0, idx).trim(), p.slice(idx + 1).trim()] : ["", ""];
    })
  );
  const ts = Number(parts.t);
  if (!Number.isFinite(ts) || Math.abs(Date.now() / 1000 - ts) >= 300) return false;
  const expected = crypto.createHmac("sha256", secret).update(`${parts.t}.${rawBody}`).digest("hex");
  const got = parts.v1 || "";
  if (got.length !== expected.length) return false;
  return crypto.timingSafeEqual(Buffer.from(expected, "utf8"), Buffer.from(got, "utf8"));
}
```

---

## 4. OpenAI-Compatible SDK Integration

### Python
```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://voicehue.com/v1", api_key=os.environ["VOICEHUE_API_KEY"])

with client.audio.speech.with_streaming_response.create(
    model="voicehue-tts",
    voice="vh-mia",
    input="Hello from VoiceHue.",
    speed=1.0,
) as response:
    response.stream_to_file("hello.mp3")
```

### Node.js / TypeScript
```js
import OpenAI from "openai";
import fs from "node:fs";

const client = new OpenAI({
  baseURL: "https://voicehue.com/v1",
  apiKey: process.env.VOICEHUE_API_KEY
});

const audio = await client.audio.speech.create({
  model: "voicehue-tts",
  voice: "vh-mia",
  input: "Hello from VoiceHue."
});
fs.writeFileSync("hello.mp3", Buffer.from(await audio.arrayBuffer()));
```

---

## 5. Remote MCP Server (`https://voicehue.com/mcp`)

Stateless Streamable HTTP MCP server exposing 8 tools: `list_voices`, `text_to_speech`, `create_dialogue`, `create_speech_job`, `get_speech_job`, `get_usage`, `estimate`, `voice_studio`.

- **Claude Code**:
  ```bash
  claude mcp add --transport http voicehue https://voicehue.com/mcp \
    --header "Authorization: Bearer $VOICEHUE_API_KEY"
  ```
- **Codex CLI**:
  ```bash
  codex mcp add voicehue --url https://voicehue.com/mcp --bearer-token-env-var VOICEHUE_API_KEY
  ```
- **Cursor / Windsurf / Gemini CLI**: See `https://voicehue.com/developers#ai-tools`.

---

## 6. Batch Narration & Optional Local Video Muxing

- **Batch scripts**: Check `usage` first, sum total character count across all items, throttle to respect the key's RPM (10/min on free plan -> ~6.5s spacing), and pass a deterministic `--idempotency-key` per item (e.g. `lesson-01-en`) so resuming after a transient failure skips already-completed clips.
- **Adding generated voiceover to a screen recording** (only when the user explicitly requests video muxing and already has `ffmpeg` installed):
  ```bash
  ffmpeg -i demo.mp4 -i output/voiceover.mp3 -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest demo-narrated.mp4
  ```
