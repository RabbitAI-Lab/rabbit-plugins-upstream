---
name: "strength-training-recording-summary"
description: "Summarize strength-training recordings/transcripts into WorkoutSummary notes with durations, sets/reps, and coach cues."
license: "MIT"
---

# Strength Training Recording Summary

Use this skill when the user wants a strength-training session recording or transcript converted into a compact summary note for future reference.

Load `references/summary-workflow.md` when you need transcription backend details, Trainwell-style local artifact handling, audio cleanup commands, dataset matching rules, or helper-script behavior.

## Accepted Inputs

- Audio recordings: `.m4a`, `.mp3`, `.wav`, `.caf`
- Transcript files: `.md`, `.txt`, `.srt`, `.vtt`, `.json`
- Mixed-language trainer sessions, including Chinese/English audio or transcripts

## How To Invoke

The user can ask naturally, for example:

```text
Use strength-training-recording-summary on /path/to/workout.m4a
Summarize this strength training transcript: /path/to/session.md
Create a WorkoutSummary for my Chinese/English trainer recording
```

## Example Output

```text
WorkoutSummary 2026-06-20
Total length: 01:21:44
Exercises completed: 14

1. Dumbbell lateral raise, ~4 min total, 2 groups * 12 reps
- Keep shoulders down and stop before shrugging.

2. Goblet squat, ~3 min, 3 groups * 10 reps
- Slow the descent and keep pressure through the mid-foot.
```

## Transcription Notes

Prefer an input transcript when one already exists. For audio, choose the first ready backend that fits the user's privacy and language needs:

- local Whisper CLI when installed; this is the default for local or Chinese/English trainer recordings
- Groq Whisper when `GROQ_API_KEY` is configured and the user accepts cloud transcription
- OpenAI or another compatible API when the user has credentials ready or explicitly chooses it

For Trainwell-style Chinese-dominant sessions, prefer:

```bash
whisper "$SOURCE_AUDIO" --model turbo --language Chinese --task transcribe --output_format all --output_dir "$OUTDIR"
```

Use `--output_format all` or another segment-preserving format so timestamps survive into the summary. If English exercise names are badly mangled, retry auto-detect or compare transcript snippets before summarizing.

Keep raw transcript artifacts only when useful or requested. For recurring Trainwell-style local workflows, save transcript Markdown under a source-adjacent `sources-markdown` folder and summaries under `summary-markdown`. For generic one-off use, print the result or save only to an explicit output path.

Do not embed API keys in the skill or output. If no transcription backend is ready, explain the options and ask which one the user wants to set up.

## Summary Rules

- Start with `WorkoutSummary <date>`.
- Include total session length and number of completed exercises.
- Use duration on each exercise line, not raw timestamp ranges.
- For split/non-contiguous work, show the combined duration, e.g. `~4 min total`.
- Count completed groups/sets and reps from the transcript; mark approximate values with `~` when needed.
- Standardize exercise names against `hasaneyldrm/exercises-dataset` when practical, but do not mention `dataset match` in the final output.
- Put useful coach notes directly under the exercise without labels like `trainer-specific cue`.
- Preserve the user's requested output language when known.
- Never invent weights, reps, sets, pain details, diagnoses, or medical conclusions.

## Helper Scripts

Use bundled helpers when useful:

```bash
python scripts/calc_duration.py '03:50-05:17 07:51-10:00'
python scripts/match_exercises.py --lang zh --top-k 3 "哑铃侧平举"
```

## Validation

Before finalizing, check that:

- the transcript source and any generated artifacts are in the expected local location
- timestamps or duration calculations support each exercise duration
- the exercise order matches the trainer's sequence
- sets/reps/duration are marked approximate when uncertain
- cloud transcription was used only when configured or explicitly accepted
- the final note contains coach-specific cues rather than generic exercise instructions
