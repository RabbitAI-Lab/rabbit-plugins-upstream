# VoiceHue Text to Speech Skill (`voicehue-tts`)

Give your AI agent natural text-to-speech, Markdown-to-audio narration,
two-host podcast dialogue generation, pronunciation control, long-article
conversion (up to 20,000 characters), and VoiceHue API integration across
**600+ voices in 40+ languages**.

Works with **Claude Code**, **Codex**, **Cursor**, **Antigravity**, **Gemini CLI**,
and any agent supporting the open `SKILL.md` specification.

## Prerequisites

1. **Node.js 18+** (uses built-in `fetch` and `node:crypto` — zero external npm
   packages to install).
2. **A free VoiceHue API key**:
   - Sign in at [voicehue.com/dashboard/keys](https://voicehue.com/dashboard/keys)
     and create an API key (free plan: 10,000 characters/month, 2,000/day,
     10 requests/minute across standard voices, plus daily free trial on premium
     voices; see [voicehue.com/developers](https://voicehue.com/developers) for
     full plan details).
   - Export `VOICEHUE_API_KEY` in your shell/agent environment, **or** place
     `VOICEHUE_API_KEY=<your-voicehue-api-key>` inside your project's `.env.local`
     or `.env` (the CLI reads only `VOICEHUE_API_KEY` from the current directory):
     ```bash
     export VOICEHUE_API_KEY="<your-voicehue-api-key>"
     ```
   - Never commit `.env` files or hardcode API keys in source files.

> Listing voices (`voices`) and running connectivity checks (`check`) work even before setting a key.

## Quick Verification

Run these from your own project folder (do not `cd` into the skill directory):

```bash
# 1. Verify Node.js, API connectivity, key detection, and quota
node ~/.agents/skills/voicehue-tts/scripts/voicehue.mjs check

# 2. List free standard voices by language & tag (no API key required)
node ~/.agents/skills/voicehue-tts/scripts/voicehue.mjs voices --language en --tier standard
node ~/.agents/skills/voicehue-tts/scripts/voicehue.mjs voices --language zh-CN --tag narration

# 3. Synthesize a test clip (or convert any Markdown file cleanly with --auto)
node ~/.agents/skills/voicehue-tts/scripts/voicehue.mjs speak \
  --voice vh-mia \
  --text "Hello from VoiceHue." \
  --out ./hello.mp3
```

## What Is Included

| Path | Purpose |
|---|---|
| `SKILL.md` | Agent instructions, recurring workflows, live-sync rules, quota guardrails, error handling, and output format |
| `scripts/voicehue.mjs` | Zero-dependency Node.js CLI (`check`, `voices`, `usage`, `speak`, `dialogue`, `job`, `studio`) with Markdown cleaning, plain-text podcast script parsing, auto long-text routing, MP3/WAV duration reporting, and safe 429/5xx retries |
| `references/voices.md` | Live catalog guide, standard voice snapshot, regional language matching, and quota summary |
| `references/api-and-workflows.md` | Complete REST API & OpenAI SDK examples, pronunciation lists, webhook verification, MCP configs, batching, and optional `ffmpeg` video muxing |
| `references/voice-studio.md` | Safe workflow for private voice design and cloning (`/v1/voice-studio`) |
| `examples/example-input-output.md` | Concrete prompts, commands, and expected agent outputs |

## Support & Documentation

- Skill download & setup guide: [https://voicehue.com/developers#agent-skill](https://voicehue.com/developers#agent-skill)
- Direct ZIP download: [https://voicehue.com/skills/voicehue-tts.zip](https://voicehue.com/skills/voicehue-tts.zip)
- Developer docs: [https://voicehue.com/developers](https://voicehue.com/developers)
- Voice library (with audio previews): [https://voicehue.com/voices](https://voicehue.com/voices)
- OpenAPI 3.1 spec: [https://voicehue.com/openapi.json](https://voicehue.com/openapi.json)
- Contact: `support@voicehue.com`
