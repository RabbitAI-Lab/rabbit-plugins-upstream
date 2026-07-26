---
name: elevenlabs-tts
description: Generate the voiceover MP3 AND derive word-level subtitle timings for a short-form video job. Calls ElevenLabs' timestamped endpoint, saves audio/voiceover.mp3, computes word boundaries from character alignment, and rewrites input.json's subtitles[] to match the actual voiceover timing. Use whenever the orchestrator hands off voiceover generation.
metadata: {"openclaw":{"requires":{"env":["ELEVENLABS_API_KEY","ELEVENLABS_VOICE_ID"],"bins":["curl","jq","base64","python3"]},"primaryEnv":"ELEVENLABS_API_KEY"}}
---

# elevenlabs-tts

Generate the voiceover audio AND real subtitle timings for one short-form video job.

## What this skill does (and why)

Two artifacts are produced from one ElevenLabs call:
1. `audio/voiceover.mp3` — the spoken audio
2. Rewritten `subtitles[]` inside `input.json` — word-level timings derived from the actual audio, not predicted

The brief's original `subtitles[]` is a prediction made when the brief was written, based on an assumed words-per-minute. ElevenLabs rarely produces audio at exactly that speed, so predicted timings drift from real audio. This skill replaces predictions with measurements: the timings come from ElevenLabs' alignment data, which describes when each character/word actually plays in the audio.

## Inputs

A job folder path. Inside, `input.json` contains:

- `tts.script` — the text to synthesize
- `tts.voice_profile.stability`, `.similarity` (→ `similarity_boost`), `.style`, `.speed`
- `subtitles[]` — predicted timings; this skill OVERWRITES this with measured timings

Voice ID is resolved deterministically (no LLM copying of opaque ids): an optional
per-channel `voices.json` (`channels[<job.channel>]`) → `voices.json.default` → env
`ELEVENLABS_VOICE_ID`. Empty falls through, so an unconfigured channel uses the global env
voice. See `config/voices.sample.json` for the file shape; point at your own copy with the
`VOICES_JSON` env var (default `config/voices.json`).

## Stage gate (status.json)

This skill reads and writes `<job_folder>/status.json` to support idempotent re-runs.

### Gate check — run BEFORE any other step

```bash
STATUS_FILE="$JOB/status.json"

# Initialize if absent (should already exist from image-gen, but be safe)
if [ ! -f "$STATUS_FILE" ]; then
  jq -n '{
    schema_version: 1,
    stages: {images: "pending", voiceover: "pending", render: "pending"},
    artifacts: {images_completed: 0, voiceover_duration_ms: null, output_path: null},
    errors: []
  }' > "$STATUS_FILE"
fi

STAGE_STATUS=$(jq -r '.stages.voiceover // "pending"' "$STATUS_FILE")
if [ "$STAGE_STATUS" = "done" ]; then
  echo "Skipped (voiceover stage already done)"
  exit 0
elif [ "$STAGE_STATUS" = "failed" ]; then
  echo "FAILED: voiceover stage previously failed. Check status.json. Exiting." >&2
  exit 1
fi

# Mark running
jq '.stages.voiceover = "running"' "$STATUS_FILE" > "${STATUS_FILE}.tmp" && mv "${STATUS_FILE}.tmp" "$STATUS_FILE"
```

### On success — write done + artifacts

```bash
AUDIO_DUR=$(jq -r '.subtitles[0].end' "$JOB/input.json")
jq --arg dur "$AUDIO_DUR" --arg path "$DEST_AUDIO" \
  '.stages.voiceover = "done" | .artifacts.voiceover_duration_ms = ($dur | tonumber * 1000 | floor) | .artifacts.voiceover_path = $path' \
  "$STATUS_FILE" > "${STATUS_FILE}.tmp" && mv "${STATUS_FILE}.tmp" "$STATUS_FILE"
```

### On any failure — write failed + error

```bash
jq --arg msg "<short error description>" \
  '.stages.voiceover = "failed" | .errors += [{"stage": "voiceover", "message": $msg, "time": (now | strftime("%Y-%m-%dT%H:%M:%SZ"))}]' \
  "$STATUS_FILE" > "${STATUS_FILE}.tmp" && mv "${STATUS_FILE}.tmp" "$STATUS_FILE"
```

## Provider details

- Endpoint: `https://api.elevenlabs.io/v1/text-to-speech/<voice_id>/with-timestamps`
- Auth header: `xi-api-key: $ELEVENLABS_API_KEY`
- Model: `eleven_multilingual_v2`
- Response: JSON with `audio_base64` and `alignment` (character-level timings)

## Steps

1. Confirm `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID` env vars are set.

   Then resolve the per-channel voice id (deterministic — never let the model copy an opaque
   id). The job's channel comes from whichever of these exists; the voice id is looked up in
   `voices.json` with a fall-through chain ending at the env voice:

```bash
   VOICES_JSON="${VOICES_JSON:-config/voices.json}"
   # find the job's channel from any available source (env wins, then job files)
   CH="${PIPELINE_CHANNEL:-}"
   for f in "$JOB/state.json" "$JOB/handoff.meta.json" "$JOB/input.json"; do
     [ -n "$CH" ] && break
     [ -f "$f" ] && CH=$(jq -r '.channel // .meta.channel // empty' "$f" 2>/dev/null || true)
   done
   VOICE_ID=""
   if [ -f "$VOICES_JSON" ]; then
     [ -n "$CH" ] && VOICE_ID=$(jq -r --arg c "$CH" '.channels[$c] // ""' "$VOICES_JSON" 2>/dev/null)
     [ -z "$VOICE_ID" ] && VOICE_ID=$(jq -r '.default // ""' "$VOICES_JSON" 2>/dev/null)
   fi
   [ -z "$VOICE_ID" ] && VOICE_ID="$ELEVENLABS_VOICE_ID"
   [ -z "$VOICE_ID" ] && { echo "no voice id resolved (channel=$CH)"; exit 1; }
   echo "voice: channel=${CH:-<none>} -> $VOICE_ID"
```

2. Read `<job_folder>/input.json`. Extract `tts.script`, `tts.voice_profile.stability`, `tts.voice_profile.similarity`, `tts.voice_profile.style`, `tts.voice_profile.speed`.

3. Validate: script non-empty string; speed in [0.7, 1.2]; other voice_profile fields in [0.0, 1.0].

4. Ensure `<job_folder>/audio/` exists.

5. Build the request body:

```bash
   REQ_FILE=$(mktemp)
   jq -n \
     --arg t "$SCRIPT" \
     --argjson sb "$STABILITY" \
     --argjson sim "$SIMILARITY" \
     --argjson st "$STYLE" \
     --argjson sp "$SPEED" \
     '{
       text: $t,
       model_id: "eleven_multilingual_v2",
       voice_settings: {
         stability: $sb,
         similarity_boost: $sim,
         style: $st,
         speed: $sp
       }
     }' > "$REQ_FILE"
```

6. Submit to the timestamped endpoint. Unlike plain TTS, the response is JSON (not raw audio), so don't use `-o` to direct it to a file with an mp3 extension:

```bash
   RESP_FILE=$(mktemp)
   HTTP_CODE=$(curl -sS -X POST \
     "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID/with-timestamps" \
     -H "xi-api-key: $ELEVENLABS_API_KEY" \
     -H "Content-Type: application/json" \
     -d @"$REQ_FILE" \
     -w "%{http_code}" \
     -o "$RESP_FILE")
```

7. Error check. On non-200, the response is a JSON error not a TTS payload:

```bash
   if [ "$HTTP_CODE" != "200" ]; then
     ERR_MSG=$(jq -r '.detail.message // .detail // .message // "unknown"' "$RESP_FILE" 2>/dev/null || echo "HTTP $HTTP_CODE")
     echo "First attempt failed (HTTP $HTTP_CODE): $ERR_MSG. Retrying..." >&2
     sleep 2
     # retry once with same call
     HTTP_CODE=$(curl -sS -X POST \
       "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID/with-timestamps" \
       -H "xi-api-key: $ELEVENLABS_API_KEY" \
       -H "Content-Type: application/json" \
       -d @"$REQ_FILE" \
       -w "%{http_code}" \
       -o "$RESP_FILE")
     if [ "$HTTP_CODE" != "200" ]; then
       ERR_MSG=$(jq -r '.detail.message // .detail // .message // "unknown"' "$RESP_FILE" 2>/dev/null || echo "HTTP $HTTP_CODE")
       echo "FAILED: ElevenLabs $ERR_MSG" >&2
       rm -f "$REQ_FILE" "$RESP_FILE"
       exit 1
     fi
   fi
```

8. Extract and save the audio. The base64-encoded MP3 is in `.audio_base64`:

```bash
   DEST_AUDIO="$JOB/audio/voiceover.mp3"
   jq -r '.audio_base64' "$RESP_FILE" | base64 -d > "$DEST_AUDIO"

   SIZE=$(stat -c%s "$DEST_AUDIO" 2>/dev/null || stat -f%z "$DEST_AUDIO")
   if [ -z "$SIZE" ] || [ "$SIZE" -lt 5000 ]; then
     echo "FAILED: audio file too small ($SIZE bytes)" >&2
     rm -f "$REQ_FILE" "$RESP_FILE"
     exit 1
   fi
```

9. Derive word-level timings from character alignment. ElevenLabs returns:
   - `alignment.characters[]` — each character as a string
   - `alignment.character_start_times_seconds[]` — when each character starts in audio
   - `alignment.character_end_times_seconds[]` — when each character ends

   Group runs of non-whitespace characters into words. Each word's start = its first character's start_time; end = its last character's end_time. Punctuation stays with the adjacent word.

   The jq below does this grouping. It produces a flat array of `{word, start, end}` objects matching the schema's `subtitleWord` definition:

```bash
   WORDS_FILE=$(mktemp)
   jq '
     .alignment as $a |
     [range(0; $a.characters | length)] |
     map({
       ch: $a.characters[.],
       s: $a.character_start_times_seconds[.],
       e: $a.character_end_times_seconds[.]
     }) |
     # group into words: split on whitespace runs
     reduce .[] as $c (
       {words: [], current: {word: "", start: null, end: null}};
       if ($c.ch | test("\\s")) then
         if .current.word == "" then .
         else
           .words += [.current] | .current = {word: "", start: null, end: null}
         end
       else
         .current.word += $c.ch
         | (if .current.start == null then .current.start = $c.s else . end)
         | .current.end = $c.e
       end
     ) |
     # flush trailing word if any
     (if .current.word != "" then .words += [.current] else . end) |
     .words
   ' "$RESP_FILE" > "$WORDS_FILE"

   # Post-process: drop SSML break tags from the word list.
   #
   # ElevenLabs returns the break-tag CHARACTERS literally in the alignment, so a
   # tag like <break time="0.3s"/> arrives as the character run "<break time=..."
   # The whitespace word-grouper above therefore splits a single tag into more
   # than one fragment, e.g. '<break' followed by 'time="0.3s"/>' (and into three
   # fragments if the tag is written with extra spaces like <break time="0.3s" />).
   #
   # A small state machine fixes this: once we see a fragment that starts with
   # '<break', we drop every fragment until the tag closes (the first fragment
   # containing '>'). This catches the trailing 'time="0.3s"/>' fragment that the
   # old code missed and leaked as a zero-duration fake word.
   #
   # We do NOT shift the remaining timings. ElevenLabs' character times already
   # reflect the real pauses the break tags produced in the rendered audio, so the
   # surviving words stay in sync with voiceover.mp3 as-is. (Subtracting each
   # break's duration as an offset — as an earlier version attempted — would push
   # every later word earlier than the audio and de-sync the subtitles.)
   FILTERED_WORDS=$(mktemp)
   python3 -c "
import json

words = json.load(open('$WORDS_FILE'))
out = []
in_break = False

for w in words:
    word = w.get('word', '')

    # Drop break-tag fragments. Stay 'in_break' until we see the closing '>'.
    if in_break or word.startswith('<break'):
        in_break = '>' not in word
        continue

    w['start'] = round(w['start'], 3)
    w['end'] = round(w['end'], 3)

    # Safety net: clamp degenerate zero-width words so renderers don't choke.
    # (~1 frame at 24fps.) Remove this block if you'd rather keep raw timings.
    if w['end'] <= w['start']:
        w['end'] = round(w['start'] + 0.04, 3)

    out.append(w)

json.dump(out, open('$FILTERED_WORDS', 'w'))
print(f'Dropped {len(words) - len(out)} break-tag fragment(s), kept {len(out)} words')
" >> "$JOB/tts.log" 2>&1
   mv "$FILTERED_WORDS" "$WORDS_FILE"
```

10. Rewrite `input.json`'s `subtitles[]` to match the schema. The schema expects subtitles grouped into sentence-level blocks, each with `text`, `start`, `end`, and a `words[]` array. For simplicity, this skill produces ONE subtitle block containing all words. The visual result is identical (word-by-word karaoke), but with measured timings throughout.

    Note: this is a simplification. If you want sentence-level grouping (multiple subtitle blocks), the brief generator should pre-mark sentence boundaries and we'd carry those through. For now, one block:

```bash
    # Save measured timings as standalone backup before rewriting input.json
    WORDS_BACKUP="$JOB/audio/voiceover_timings.json"
    jq -n --slurpfile words "$WORDS_FILE" '{words: $words[0]}' > "$WORDS_BACKUP"

    # Strip SSML break tags from subtitle text so the downstream renderer's word count matches
    CLEAN_SCRIPT=$(jq -r '.tts.script' "$JOB/input.json" | sed 's/<break[^/>]*\/>//g')

    UPDATED_INPUT=$(mktemp)
    jq --slurpfile words "$WORDS_FILE" --arg text "$CLEAN_SCRIPT" '
      .subtitles = [{
        text: $text,
        start: $words[0][0].start,
        end: $words[0][-1].end,
        words: $words[0]
      }]
    ' "$JOB/input.json" > "$UPDATED_INPUT"

    mv "$UPDATED_INPUT" "$JOB/input.json"
```

11. Clean up:

```bash
    rm -f "$REQ_FILE" "$RESP_FILE" "$WORDS_FILE"
```

12. Print success summary:

```bash
    WORD_COUNT=$(jq '.subtitles[0].words | length' "$JOB/input.json")
    AUDIO_DURATION=$(jq -r '.subtitles[0].end' "$JOB/input.json")
    SIZE_KB=$((SIZE / 1024))
    echo "OK $DEST_AUDIO"
    echo "Size: $SIZE_KB KB"
    echo "Words: $WORD_COUNT, audio duration: ${AUDIO_DURATION}s"
    echo "Subtitles in input.json rewritten with measured word-level timings"
    echo "Backup: $WORDS_BACKUP"
```

## Notes

- The `with-timestamps` endpoint costs the same as plain TTS — it's a free upgrade in terms of cost. Latency is slightly higher because the response is larger.
- Character alignment includes punctuation. The grouping treats `"hello,"` as a single word (with the comma attached); this matches how most subtitle renderers handle punctuation.
- **SSML break tags** (`<break time="X.Xs"/>`) in the TTS script are dropped from the word-level timings. ElevenLabs returns the tag's characters literally in the alignment, and the whitespace word-grouper splits a single tag into more than one fragment, so a small state machine in step 9 removes every fragment from `<break` through the closing `>`. The remaining word timings are kept exactly as ElevenLabs measured them — those already include the real pauses the break tags produced in the rendered audio, so the subtitles stay in sync. (An earlier version tried to subtract each break's duration as an offset; that never actually ran — the duration lived in a fragment the code never inspected — and would have de-synced the subtitles from the audio if it had.) Break tags never appear in the output `subtitles[].words[]`.
- The step 9 Python also clamps any word where `end <= start` (rare, but ElevenLabs can occasionally emit a zero-width real word) by extending its end by ~40ms. Remove that block if you'd rather keep raw timings.
- If you need sentence-level subtitle grouping (multiple blocks like an earlier multi-block brief had), the brief should preserve sentence boundaries somewhere — e.g. add a `tts.sentence_breaks` array of character indices. The current implementation produces ONE block; the karaoke animation still highlights word-by-word.
- This skill MUTATES `input.json`. After this skill runs, the `subtitles[]` field reflects measured timings. The original predicted timings are lost. If you need both, copy `input.json` to `input.json.original` before running.
- `audio_duration` in input.json is NOT updated by this skill. For long-form jobs, run [reconcile-timeline](../reconcile-timeline/SKILL.md) next to re-anchor the timeline and set `audio_duration` to the measured total.

## Output

On success:
```
OK <abs-path-to-mp3>
Size: <N> KB
Words: <N>, audio duration: <S>s
Subtitles in input.json rewritten with measured word-level timings
```

On failure:
```
FAILED: <reason>
```
…to stderr, exit non-zero.
