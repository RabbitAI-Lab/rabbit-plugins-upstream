# VoiceHue TTS Skill — Example Inputs & Expected Outputs

> All commands below run from the user's workspace directory (`cwd`), invoking the installed skill via `<SKILL_DIR>/scripts/voicehue.mjs` (for example `~/.agents/skills/voicehue-tts/scripts/voicehue.mjs`).

## Example 1: Turn a Markdown Doc Into Clean Audio (Auto-Stripped + Auto Long-Text)

**User prompt:**
> Convert `./docs/release-notes.md` into a clear narration MP3 at `./audio/release-notes.mp3` so I can listen on my commute.

**Agent steps:**
1. Verify setup and remaining quota:
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs check
   ```
2. Query narration voices:
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs voices --language en-US --tier standard --tag narration
   ```
3. Synthesize directly from Markdown (`.md` automatically strips frontmatter, code blocks, URLs, and Markdown symbols; `--auto` seamlessly switches to a background job if 5,001–20,000 chars):
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs speak \
     --voice vh-ethan \
     --text-file ./docs/release-notes.md \
     --auto \
     --out ./audio/release-notes.mp3
   ```

**Expected agent response:**
- **File**: `./audio/release-notes.mp3`
- **Voice**: Ethan (`vh-ethan`, English, male, standard)
- **Length**: 3,420 characters, `~218.4s` (`MP3`, `1.0x`, Markdown cleaned)

---

## Example 2: Two-Host Podcast From Plain-Text Script

**User prompt:**
> Turn this summary into a lively 2-host Chinese podcast MP3 at `./audio/podcast-ep1.mp3`.

**Agent steps:**
1. Query live Chinese standard voices:
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs voices --language zh-CN --tier standard
   ```
2. Write `./audio/podcast-ep1.txt` (human-readable `Speaker: line` format):
   ```text
   柏川：欢迎收听本期技术播客，今天聊聊怎么把技术文档直接变成通勤语音。
   清禾：大家好！只要一个自然文本剧本，就能直接合成双人对话 MP3。
   ```
3. Synthesize directly with `--script-file` and `--voices`:
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs dialogue \
     --script-file ./audio/podcast-ep1.txt \
     --voices "柏川=vh-baichuan,清禾=vh-qinghe" \
     --pause-ms 450 \
     --out ./audio/podcast-ep1.mp3
   ```

**Expected agent response:**
- **File**: `./audio/podcast-ep1.mp3`
- **Speakers**: 柏川 (`vh-baichuan`), 清禾 (`vh-qinghe`) — 2 turns merged into 1 MP3
- **Length**: 60 characters, `duration_seconds` reported from API/audio header

---

## Example 3: Video Voiceover with Pronunciation Fixes

**User prompt:**
> Turn this intro into a warm English female voiceover at `./audio/intro.mp3`. Pronounce "SQL" as "sequel".

**Agent steps:**
1. Write `./audio/pronunciations.json`: `[{"from": "SQL", "to": "sequel"}]`
2. Run:
   ```bash
   node <SKILL_DIR>/scripts/voicehue.mjs speak \
     --voice vh-mia \
     --text "Meet DataPulse. Write plain English questions, run instant SQL queries, and share dashboards." \
     --pronunciations ./audio/pronunciations.json \
     --out ./audio/intro.mp3
   ```

**Expected agent response:**
- **File**: `./audio/intro.mp3`
- **Voice**: Mia (`vh-mia`, English, female, standard)
- **Pronunciations applied**: `SQL` -> `sequel`

---

## Example 4: Boundary Handling (Missing Key or Exceeded Quota)

- **Missing `VOICEHUE_API_KEY`**: Agent runs `check`, reports that `VOICEHUE_API_KEY` is not set in env or `./.env`, and guides the user to create a free key at `https://voicehue.com/dashboard/keys` (never asks for the key in chat).
- **Exceeded daily quota**: Agent reports the exact remaining characters and UTC 00:00 reset time from `usage`, and asks whether to shorten the text or split across days instead of silently truncating.
