# VoiceHue Voice Studio Reference (`/v1/voice-studio`)

Use `POST https://voicehue.com/v1/voice-studio` (or the `voice_studio` MCP tool)
to design, clone, list, rename, delete, and synthesize **private personal voices**
owned by the authenticated account.

- Private voice IDs use the `pv_` prefix and are private to the caller's account.
- Public voices continue to use `/v1/audio/speech`, `/v1/audio/dialogue`, and `/v1/audio/speech/jobs`.

## Mandatory Safety & Billing Guardrails

1. **Always quote first**: Before running `design`, `save`, `clone`, or
   `synthesize`, call `action: "quote"` with `for_action` and the exact parameters.
   If `credits > 0`, show the user the quoted cost (3 internal credits = 1
   allowance character) and obtain explicit approval before submitting.
2. **Pass `max_credits` and a stable UUID `request_id`**: Every mutation
   (`design`, `save`, `clone`, `synthesize`, and `delete`) must include
   `max_credits` (from the approved quote, or `0` for free actions like `delete`)
   and a freshly generated UUID `request_id`.
3. **Never retry a timed-out mutation with a new `request_id`**: If a request
   times out or returns HTTP `202`, poll `action: "operation"` using the returned
   `operation_id` (or the original `request_id` if no `operation_id` was received)
   before deciding whether to retry.
4. **Voice cloning consent**: Never set `consent: true` until the user explicitly
   confirms they own the voice or have permission from the speaker. Reference
   audio must be WAV or MP3, 3–120 seconds, up to 2 MB.
5. **Check availability & language before synthesis/creation**: Call `action: "list"`
   and select only voices with `available: true` (expired hosting or pending
   verification voices appear for management but cannot synthesize). Private voice
   IDs match `pv_<32 hex chars>`. For `design` or `clone`, always pass `language`
   explicitly (defaults to `"zh"` if omitted).

## Actions Summary

| Action | Cost / Quote needed? | Key Fields |
|---|---|---|
| `capabilities` | Free, no quote | `{ "action": "capabilities" }` |
| `list` | Free, no quote | `{ "action": "list" }` -> returns `slot_usage` and voices with `available` / `availability_reason` |
| `quote` | Free | `{ "action": "quote", "for_action": "design|save|clone|synthesize|delete", ... }` |
| `design` | Quote first | `engine` (`standard`/`premium`), `language`, `description` (20–1,000 chars), `text` (100–1,000 chars), `request_id`, `max_credits` |
| `save` | Quote first | `operation_id`, `candidate` (`0..2`), `name` (≤48 chars), `request_id`, `max_credits` |
| `clone` | Quote first + `consent: true` | `engine`, `language`, `name`, `audio_base64`, `audio_mime` (`audio/mpeg` or `audio/wav`), `consent: true`, `request_id`, `max_credits` |
| `synthesize` | Quote first | `voice_id` (`pv_...`), `text` (≤5,000 chars), `request_id`, `max_credits` -> returns signed `audio_url` (valid 15 min) |
| `rename` | Free, no quote | `voice_id`, `name` (keeps same `voice_id`) |
| `delete` | Free (`max_credits: 0`) | `voice_id`, `request_id` (UUID), `max_credits: 0` (only deletes caller's own private voice; confirm with user first) |
| `operation` | Free, no quote | `operation_id` (or original `request_id`) to recover status or refresh a 15-minute `audio_url` |

## Example Payload Sequence (with `<SKILL_DIR>/scripts/voicehue.mjs studio`)

1. Write `quote.json` inside the workspace:
   ```json
   {
     "action": "quote",
     "for_action": "synthesize",
     "voice_id": "pv_YOUR_PRIVATE_VOICE_ID",
     "text": "Welcome back to our weekly update."
   }
   ```
2. Run `node <SKILL_DIR>/scripts/voicehue.mjs studio --payload-file ./quote.json`.
3. Ask the user to approve the returned `credits` (if nonzero).
4. Write `synth.json` with `action: "synthesize"`, the approved `max_credits`,
   and a UUID `request_id`, then run `node <SKILL_DIR>/scripts/voicehue.mjs studio --payload-file ./synth.json`.

See `https://voicehue.com/developers#voice-studio` for full details.
