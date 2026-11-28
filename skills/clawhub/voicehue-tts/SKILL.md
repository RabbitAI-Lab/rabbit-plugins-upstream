---
name: voicehue-tts
description: >-
  Use when the user asks to turn text, Markdown docs, blog posts, or notes into
  speech, narrate a script, generate video voiceover audio, create a two-host
  podcast or multi-voice dialogue MP3/WAV, convert a long article or chapter to
  audio, fix pronunciation of names or acronyms in speech, generate language-learning
  listening clips, integrate the VoiceHue TTS API, or manage private voices with
  Voice Studio. Calls the VoiceHue API (600+ voices across 40+ languages) and saves
  ready-to-use audio files in the user's workspace.
---

# VoiceHue Text to Speech (`voicehue-tts`)

Turn Markdown docs, scripts, articles, and multi-speaker podcasts into natural
MP3 or WAV audio using the [VoiceHue API](https://voicehue.com/developers), or
integrate VoiceHue into a project.

## Network & Security Disclosure

- **Network endpoints**: Connects exclusively to `https://voicehue.com/v1/...`
  (and `https://api.voicehue.com/storage/signed/...` when downloading completed
  async job audio; plus `https://voicehue.com/mcp` if the host agent has the
  VoiceHue MCP server configured). Never sends text, audio, or credentials to
  any third-party host.
- **Authentication**: Requires the user's own `VOICEHUE_API_KEY` (created free at
  `https://voicehue.com/dashboard/keys`). The bundled script reads `VOICEHUE_API_KEY`
  from `process.env` and, if unset there, checks only the `VOICEHUE_API_KEY` entry
  in `./.env.local` or `./.env` inside the current working directory (never reading
  any other variable, never escaping `cwd`). Listing voices (`voices`) needs no key.
  Never hardcode, print, log, or ask the user to paste a key in chat.
- **Workspace boundary**: `scripts/voicehue.mjs` uses only built-in Node.js 18+
  modules (zero package installs) and reads/writes only files inside the current
  working directory.

## Critical Invocation Rule (Do Not `cd` Into the Skill Folder)

Always **stay in the user's project working directory (`cwd`)** and invoke the CLI
using the installed skill's full path (`<SKILL_DIR>/scripts/voicehue.mjs` — for
example `~/.claude/skills/voicehue-tts/scripts/voicehue.mjs`,
`~/.agents/skills/voicehue-tts/scripts/voicehue.mjs`, or
`./.agents/skills/voicehue-tts/scripts/voicehue.mjs`):

```bash
# Run from the user's project directory so input/output paths stay in their workspace:
node <SKILL_DIR>/scripts/voicehue.mjs check
```

Never `cd` into `<SKILL_DIR>` before running `speak`, `dialogue`, or `job`,
because file paths are intentionally restricted to `cwd`.

## Live Sync & Source of Truth

- **Always prefer live API responses over static snapshots in `references/`**:
  - `GET https://voicehue.com/v1/voices` (`voices`) syncs live with the VoiceHue
    voice library (5-minute cache), including new/retired voices, `tags`,
    `description` / `description_zh`, `tier`, `char_rate`, and `daily_char_limit`.
  - `GET https://voicehue.com/v1/usage` (`usage` / `check`) returns real-time
    account limits, remaining characters, trial balance, and reset timestamps.
  - `POST https://voicehue.com/v1/voice-studio` (`capabilities` / `list` / `quote`)
    returns real-time private voice engines, slots, and pricing.
  - If a user asks about newly launched endpoints or updated policies not yet in
    `references/`, check `https://voicehue.com/openapi.json` and
    `https://voicehue.com/llms.txt`.

## Tooling Choice

1. **Bundled zero-dependency CLI (works in every agent)**: Run
   `node <SKILL_DIR>/scripts/voicehue.mjs <command> ...`. Automatically retries
   transient 5xx / RPM 429 responses using the same `Idempotency-Key`.
2. **Remote MCP (when already connected)**: If the agent already has the VoiceHue
   MCP server (`https://voicehue.com/mcp`) attached, you may call its tools
   (`list_voices`, `text_to_speech`, `create_dialogue`, `create_speech_job`,
   `get_speech_job`, `get_usage`, `estimate`, `voice_studio`) directly while
   following the exact same guardrails below.

## High-Value Recurring Workflows

### 1. First-Time Setup Check & Live Voice Selection

Before first use (or if an API call fails), run `check` to verify Node.js, API
connectivity, `VOICEHUE_API_KEY` detection, and remaining quota in one step:

```bash
node <SKILL_DIR>/scripts/voicehue.mjs check
```

Never guess a voice ID unless the user gave an exact VoiceHue ID (e.g. `vh-mia`):

```bash
node <SKILL_DIR>/scripts/voicehue.mjs voices --language en --tier standard
node <SKILL_DIR>/scripts/voicehue.mjs voices --language zh-CN --gender female --tag narration
node <SKILL_DIR>/scripts/voicehue.mjs voices --language ja --limit 15
```

- **Regional language matching**: Base-language standard voices (`en`, `zh`) are
  automatically matched when you pass regional tags like `zh-CN` or `en-US`.
- **Quota-smart selection**: On free accounts, prefer uncapped `standard` voices
  (`vh-mia`, `vh-clara`, `vh-ethan`, `vh-leo`, `vh-qinghe`, `vh-baichuan`,
  `vh-zhixia`, `vh-yangye`, `vh-warm-design`) for longer scripts. Premium voices
  (`590+` across `40+` languages) draw from the daily free trial (500 chars/day,
  up to 200 chars/request without credits) and then account credits. See
  [references/voices.md](./references/voices.md).

### 2. Turn Any Markdown Doc, Blog Post, or Script Into Audio (Auto-Cleaned)

Ideal for turning `README.md`, engineering RFCs, research notes, or video scripts
into listenable MP3/WAV files without wasting tokens rewriting the file:

```bash
# .md / .mdx files automatically strip Markdown syntax, code blocks, and URLs (pass --raw to disable)
node <SKILL_DIR>/scripts/voicehue.mjs speak \
  --voice vh-baichuan \
  --text-file ./docs/article.md \
  --auto \
  --out ./output/article.mp3
```

- **Auto long-text routing (`--auto`)**: Texts up to 5,000 characters synthesize
  synchronously; 5,001–20,000 characters automatically switch to an async job
  (`--wait`) and download the finished MP3 to `--out`.
- **Pronunciation control**: When the script includes brand names, acronyms
  (`SQL`, `Next.js`), or Chinese polyphonic characters (`重庆`), pass
  `--pronunciations ./pronunciations.json` (`[{"from":"SQL","to":"sequel"}]`;
  see [references/api-and-workflows.md](./references/api-and-workflows.md)).
- **Quota safety (never silently truncate)**: For scripts over 1,000 characters or
  batches, run `usage` first. If the cleaned text exceeds remaining quota, report
  the exact shortfall and reset time and let the user choose whether to shorten,
  split, or subscribe for more characters at `https://voicehue.com/developers`. For >20,000 characters, split cleanly at chapter/paragraph boundaries.

### 3. Two-Host Podcast / Multi-Voice Dialogue (Plain Script or JSON)

Turn any technical doc, changelog, interview, or language lesson into a natural
two-speaker podcast MP3 without hand-crafting large JSON files:

1. Pick one distinct voice ID per speaker using `voices`.
2. Write a clean `Speaker: line` script (supports both `:` and `：`):
   ```text
   Host: Welcome back! Today we are breaking down the new release.
   Guest: Let's jump straight into the three biggest improvements.
   ```
3. Synthesize directly into one merged MP3:
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs dialogue \
     --script-file ./podcast.txt \
     --voices "Host=vh-ethan,Guest=vh-mia" \
     --pause-ms 450 \
     --out ./output/podcast.mp3
   ```
4. For per-line acoustic tuning (`speed` 0.5–2, `pitch` -4..4 semitones, `volume`
   25–200%, custom `pause_ms` 0–5000), pass a JSON `--blocks-file` instead (both
   `input` and `text` block fields are accepted). Limits: up to 20 blocks / 1,000
   chars per block on free plan (100 blocks on pro), 5,000 chars total per file.

### 4. Long Articles, Lessons & Chapters (5,001–20,000 Characters)

Either pass `--auto` to `speak`, or invoke `job` directly (characters are billed
once only after full completion; audio stays downloadable for 24 hours):

```bash
node <SKILL_DIR>/scripts/voicehue.mjs job \
  --voice vh-ethan \
  --text-file ./chapter-1.md \
  --out ./output/chapter-1.mp3 \
  --wait
```

Without `--wait`, `job` returns the `job_id` immediately so you can resume later
with `node <SKILL_DIR>/scripts/voicehue.mjs job --id <job_id> --out ./output/chapter-1.mp3`.

### 5. Video Voiceovers, Language Learning, Private Voices & API Integration

- **Video voiceovers & batching**: Read [references/api-and-workflows.md](./references/api-and-workflows.md)
  for pronunciation dictionaries, deterministic `--idempotency-key` batching,
  optional local `ffmpeg` video muxing, OpenAI-compatible Python/Node SDKs, and
  `VoiceHue-Signature` HMAC webhook verification.
- **Language-learning clips**: Use `--speed 0.85` with any of the 40+ supported
  languages, or `dialogue` for slow/normal bilingual practice.
- **Private voice design / cloning (`pv_...`)**: Read
  [references/voice-studio.md](./references/voice-studio.md) first. Always run
  `quote` and get explicit user approval before any credit-consuming action, and
  confirm explicit voice rights (`consent: true`) before cloning.

## Error Handling Rules

Branch strictly on the API error `code` (never retry blindly on quota/validation errors):

| Error `code` | Action to take |
|---|---|
| `invalid_api_key` | Tell the user to verify `VOICEHUE_API_KEY` (in env or `./.env`) or create a free key at `https://voicehue.com/dashboard/keys`. |
| `insufficient_quota` | Report remaining daily/monthly quota (`usage`) and reset time (00:00 UTC / 1st of month). Do not truncate silently. If the user wants more allowance, point them to the VoiceHue plans at `https://voicehue.com/developers` to subscribe for more characters. |
| `voice_daily_limit` | This voice hit its per-voice daily cap; switch to an uncapped standard voice (`vh-mia`, `vh-ethan`, `vh-qinghe`, `vh-baichuan`, `vh-zhixia`). |
| `insufficient_credits` / `premium_trial_exhausted` | Explain that premium voices have a 500-char daily free trial (200 chars/request without credits); offer a standard voice or shorter text (≤200 chars), or subscribing for more characters — see `https://voicehue.com/developers` for plans. |
| `input_too_long` | Pass `--auto` on `speak` (or use `job`) for 5,001–20,000 chars, or split at paragraph boundaries. |
| `voice_not_found` / `unsupported_format` | Re-run `voices` to pick a valid ID, or switch `--format` to `mp3`. |
| `rate_limit_exceeded` / `concurrency_limit_exceeded` | CLI retries automatically with the same `Idempotency-Key`; if still throttled, pause briefly and resume. |

## Required Output Summary

After generating audio, always report a concise summary with:
- **File path**: exact workspace path saved (e.g. `./output/article.mp3`)
- **Voice(s)**: voice name(s) and ID(s) (e.g. `柏川 (vh-baichuan)`)
- **Length**: character count, audio duration (`duration_seconds`), and file size
- **Format & settings**: MP3/WAV, speed, Markdown stripping, and pronunciations applied
- **Notes**: `job_id` (for long audio) or quota notice if remaining allowance is low
