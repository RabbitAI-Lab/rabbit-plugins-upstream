# Strength Training Recording Summary Workflow

This skill turns strength-training recordings or transcripts into clean `WorkoutSummary <date>` notes for future reference. It does not require a specific app, hosted storage, or retrieval feature. Groq and OpenAI-compatible APIs are optional transcription backends, not requirements.

The useful behavior is:

1. receive a local strength-training recording or transcript
2. transcribe audio with an available backend when needed
3. preserve enough timestamps to calculate exercise durations
4. standardize exercise names and count completed work
5. write a concise summary note
6. print or save the result as requested

## Core Guardrails

- Preserve transcript timestamps when the input format provides them.
- Keep the workflow local by default: do not upload to hosted storage, create remote workout sessions, or store vector indexes unless the user explicitly asks.
- Print the summary in chat or stdout by default.
- Save generated transcripts or summaries only when asked, when the user supplied an explicit output path, or when operating a known recurring app workflow that has local artifact folders.
- Do not create web portals, review screens, retrieval indexes, or database records unless the task changes from `summarize this session` to `build an app pipeline`.
- Do not embed real API keys in the skill, output, logs, examples, or publishable package.

## Inputs

Accept common strength-training recording formats:

- `.m4a` / MP4 AAC
- `.mp3`
- `.wav`
- `.caf` when local tooling can convert it safely
- existing transcript or summary source files such as `.md`, `.txt`, `.srt`, `.vtt`, or `.json`

Before transcription, inspect:

- file exists
- file size
- container/magic bytes if a transcription call fails
- duration if local tools such as `ffprobe` are available

Useful inspection command:

```bash
ffprobe -hide_banner "$AUDIO"
```

## Choosing A Transcription Backend

Pick the first suitable backend that is ready:

1. Existing transcript file.
   - If the user provides `.txt`, `.srt`, `.vtt`, `.json`, or Markdown transcript output, summarize that directly.
2. Local Whisper CLI.
   - Default for privacy-sensitive local work and Chinese/English trainer recordings when installed.
   - Check with `command -v whisper`.
3. Groq Whisper.
   - Fast cloud option when `GROQ_API_KEY` is configured and the user accepts cloud transcription.
4. OpenAI or another compatible speech-to-text API.
   - Use only when the user has that provider configured or explicitly chooses it.

If none is ready, do not pretend transcription is available. Explain the options and ask which backend the user wants to set up.

## Trainwell-Style Local Transcription

Use this path for app-exported trainer recordings where the user expects repeatable local artifacts, especially Chinese/English Trainwell-style sessions.

1. Locate the source recording or transcript. Common folder names are:
   - `recordings/`
   - `sources/`
   - `sources-markdown/`
   - `summary-markdown/`
2. If a transcript already exists in Markdown, SRT, VTT, TXT, or JSON, summarize that directly.
3. For Chinese-dominant audio, prefer local Whisper:

```bash
whisper "$SOURCE_AUDIO" \
  --model turbo \
  --language Chinese \
  --task transcribe \
  --output_format all \
  --output_dir "$OUTDIR"
```

4. Preserve segment timestamps from Whisper outputs. Convert or copy the transcript into Markdown only after retaining enough timing information for exercise durations.
5. Save raw/converted transcript Markdown under `sources-markdown` when the workflow is recurring or the user asked for files.
6. Save final summaries under `summary-markdown` when the workflow is recurring or the user asked for files.
7. If exact sets, reps, or durations are ambiguous, use `~`, `about`, or `roughly`; do not invent precision.

Prefer local Whisper over browser, phone, or Google recognizer transcription unless the user explicitly accepts sending audio to that service or the audio is already known to work better there.

## Local Whisper Option

Local Whisper needs no API key if the CLI is installed:

```bash
whisper "/path/to/workout.m4a" \
  --model turbo \
  --task transcribe \
  --output_format all \
  --output_dir ./transcripts
```

For privacy-sensitive or Chinese/English trainer recordings, use local Whisper first when available. Use `--language Chinese` when Chinese is dominant, especially for Trainwell-style recordings. If the trainer frequently says English exercise names and language forcing harms names, retry without `--language` and compare snippets before final summary. Keep `--output_format all` when practical because `.srt`, `.vtt`, `.json`, and `.txt` give useful cross-checks.

## Groq Option

Use Groq's OpenAI-compatible audio transcription endpoint only when `GROQ_API_KEY` is configured and cloud transcription is acceptable:

```bash
curl https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F "file=@/path/to/workout.m4a" \
  -F "model=whisper-large-v3-turbo" \
  -F "response_format=verbose_json" \
  -F "timestamp_granularities[]=segment"
```

Operational notes:

- Keep `GROQ_API_KEY` in the environment, never in the skill or output.
- Prefer `verbose_json` so segment timestamps are available for the summary.
- If the account has a 25 MB audio limit, split or compress long recordings before upload.
- If Groq returns no text, inspect container and content type. `.m4a` should usually be sent as an audio file with a real `.m4a` filename.

## Other Cloud APIs

Use provider-specific commands or SDKs only when the user has credentials ready. Keep these rules provider-neutral:

- request segment-level timestamps when supported
- do not hardcode API keys
- do not commit generated transcripts unless asked
- report provider limits clearly when a file is too large

## Optional Local Preprocessing

Use local preprocessing only when needed:

- Convert CAF/LPCM to WAV if the selected backend rejects CAF.
- Convert odd containers to `.wav` or `.m4a` while keeping speech intelligible.
- Compress oversized files before upload, commonly to mono, 16 kHz, around 24 kbps when quality is sufficient for speech.
- Split long files into smaller ordered parts, commonly 15-minute chunks, and offset timestamps when merging transcripts.
- Prefer lossless stream copy splitting first; re-encode only when chunks are still too large or the container fails.

Useful `ffmpeg` examples:

```bash
ffmpeg -i input.caf -ac 1 -ar 16000 output.wav
ffmpeg -i input.m4a -ac 1 -ar 16000 -b:a 24k output.m4a
ffmpeg -i input.m4a -f segment -segment_time 900 -c copy part_%03d.m4a
```

## Summary Extraction

Build the final summary from the trainer's actual sequence. Capture:

- title line: `WorkoutSummary <date>`
- total workout length
- number of completed exercises
- exercise or drill name
- duration, not raw time range
- groups, sets, rounds, reps, duration, or holds
- important breaks or coaching pauses
- trainer cues and corrections only when they add something beyond reference exercise instructions
- homework, follow-up, or next-session plans

Preferred output:

```text
WorkoutSummary <date>
Total length: 45:20
Exercises completed: 6

1. Canonical exercise name, ~2 min, 2 groups * 10 reps/side
- Direct note or cue; no `dataset match` or `trainer-specific cue` label.
```

Rules:

- Use one numbered item per exercise.
- Keep the first line to canonical name, duration, and completed volume.
- Use duration on every exercise line, not raw time ranges. For split/non-contiguous groups, use total duration such as `~4 min total`.
- Use `scripts/calc_duration.py` to calculate durations from transcript ranges when helpful.
- Count completed groups/sets and reps from the transcript; if uncertain, mark approximate.
- Put the highest-value note on the next line as one bullet, without labels.
- Do not invent weights, reps, pain observations, or diagnoses.
- Do not include a table unless explicitly requested.

## Exercise Dataset Cross-Reference

Use `hasaneyldrm/exercises-dataset` to standardize exercise names and avoid repeating generic instruction text when practical.

Dataset usage rules:

- Do not put the full `data/exercises.json` into the model conversation.
- Treat it as a local/reference data source.
- Load or cache it outside the prompt.
- Bring only top candidate records or compact snippets into the final summary step.
- Use code or shell tools for fuzzy matching when available; use the LLM for judgment only after narrowing candidates.
- If confidence is low, keep the spoken/trainer name and optionally add `approx.` rather than forcing a bad match.

Use the bundled helper before final summarization when useful:

```bash
python scripts/match_exercises.py --lang zh --top-k 3 "深蹲" "侧平举"
python scripts/match_exercises.py --lang en --top-k 5 "dumbbell lateral raise"
```

## Duration Helper

Use `scripts/calc_duration.py` for calculating duration from one or more transcript ranges:

```bash
python scripts/calc_duration.py 00:00-01:42
python scripts/calc_duration.py 03:50-05:17 07:51-10:00
```

Use the returned duration on the summary line instead of raw ranges. For split/non-contiguous work, add `total` if it helps clarity, e.g. `~4 min total`.

## Chinese/English Sessions

For mixed Chinese/English training audio:

- Preserve practical exercise meaning over literal translation.
- Do not force all exercise names into English if the trainer used Chinese and the user expects Chinese output.
- Prefer canonical dataset names for standardization, but keep helpful Chinese labels or trainer-spoken names when they disambiguate.
- Clean up noisy transcript fragments into normal exercise names.
- Keep trainer emphasis points such as breathing, bracing, foot pressure, knee tracking, tempo, shoulder position, and tennis-transfer homework.
- Compare Chinese trainer cues against `instructions.zh` / `instruction_steps.zh` first. Fall back to English when Chinese fields are missing or unhelpful.

## What Is Intentionally Out Of Scope

- Next.js API routes
- remote workout session records
- Neon/Postgres tables
- web portal behavior
- review/finalization screens

Only add those pieces if the user explicitly asks for a full application pipeline.
