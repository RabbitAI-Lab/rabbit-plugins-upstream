---
name: agent-subtitle-translator
description: Translate one subtitle file at a time with deterministic local parsing, timeline preservation, strict batch mapping, and safe output composition. Use when an agent needs to translate SRT, WebVTT/VTT, or ASS subtitle files; preserve ASS sections, event fields, inline semantic styling, or hard line breaks; normalize VTT to SRT; detect karaoke degradation; or validate an LLM subtitle translation before writing it.
metadata:
  author: "Lumen"
---

# Agent Subtitle Translator

Translate only subtitle text with an available translation model. Delegate decoding, parsing, batching, marker validation, timeline mapping, and output writing to `scripts/subtitle_tool.py`. Never send timestamps or original ASS override tags to the model.

## Prerequisite

Run commands from this skill directory. The script uses only the standard library for UTF inputs; legacy encodings require `charset-normalizer`:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/subtitle_tool.py --help
```

Do not request or configure an external LLM API key for the script. Use the translation capability already available to the executing agent.

## Workflow

### 1. Prepare one file

Require a target BCP 47 tag. Accept an optional source tag; omit it to let the translation model detect the source language.

```bash
python3 scripts/subtitle_tool.py prepare /path/movie.ass \
  --target-language zh-Hans \
  --source-language en
```

Use `--work-dir` to choose the package location. The command otherwise creates a hidden sibling directory. Do not use `--overwrite-work` unless replacing that package is intentional.

Inspect the JSON report. Stop on decoding, empty-body, invalid-timeline, or structural errors. Note any out-of-order input and ASS karaoke IDs. Preparation creates:

- `manifest.json`: local structure, mapping, and validation facts; do not send it to the model.
- `batches/batch-NNNN.txt`: ready-to-send prompts containing stable IDs and text, never timelines.
- `validated/`: destination for verified batch results.

Each batch contains at most 32 entries. Do not increase that ceiling. Dispatch batches serially or concurrently using the agent's available scheduling; this skill imposes no concurrency limit.

### 2. Translate batches

Send each complete `batch-NNNN.txt` prompt to the translation model without rewriting its fixed instructions. Save the raw response as UTF-8 text.

Do not promise cross-batch consistency for names or terminology. The prompt supplies only the local batch context.

### 3. Validate every response

```bash
python3 scripts/subtitle_tool.py validate-response \
  --manifest /path/work/manifest.json \
  --batch 1 \
  --response /path/responses/batch-0001.txt
```

On any count, ID, order, wrapper, hard-break, fixed-structure, or style-marker error, resend that batch with the original prompt and the validator error as a correction request. Never fill a missing translation from a neighboring entry.

If the retried response still has a count, ID, wrapper, `BR`, or `F` mismatch, stop the entire job. Reliable timeline mapping is impossible.

If only ASS `S` style markers remain invalid after a retry, validate with `--allow-style-fallback`. This removes inline style markers only for the affected entries and records their IDs. Do not use this option before a retry.

```bash
python3 scripts/subtitle_tool.py validate-response \
  --manifest /path/work/manifest.json \
  --batch 1 \
  --response /path/responses/batch-0001-retry.txt \
  --allow-style-fallback
```

Use `--overwrite` only to replace the prior validated JSON for that batch.

### 4. Compose after all batches validate

```bash
python3 scripts/subtitle_tool.py compose --manifest /path/work/manifest.json
```

The script merges validated data by stable subtitle ID, independent of completion order. It refuses missing, duplicate, or extra IDs and refuses to overwrite output by default.

Read the final `.report.json` and tell the user:

- output path, format, encoding, entry count, and time range;
- count and IDs of karaoke degradations;
- count and IDs of inline-style fallbacks.

## Format behavior

- Write SRT input as UTF-8-BOM SRT.
- Normalize VTT input locally and write UTF-8-BOM SRT.
- Keep ASS as UTF-8-BOM ASS. Preserve non-dialogue sections, styles, comments, pure drawings, event order, timestamps, Layer, Style, Name, margins, Effect, and other event fields.
- Translate only visible ASS Dialogue text. Convert inline style scopes to paired neutral markers and `\N`/`\n` to movable `BR` markers, then restore validated structure.
- Degrade karaoke entries containing `\k`, `\K`, `\kf`, or `\ko` individually to static text. Preserve the base Style/event fields and safe whole-line positioning while removing syllable timing and inapplicable animation.
- Name default output `<stem>.<normalized-BCP47>.<ext>`, such as `movie.zh-Hans.srt` or `movie.pt-BR.ass`.

## Safety invariants

- Process exactly one input file per run.
- Never expose `manifest.json`, timestamps, or raw ASS override tags to the translation model.
- Never infer mapping from proximity, text similarity, or character positions.
- Never silently discard marker failures or degradations.
- Never overwrite a work package, validated result, subtitle, or report without the matching explicit overwrite flag.
