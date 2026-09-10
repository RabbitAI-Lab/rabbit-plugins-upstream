---
name: agent-subtitle-translator
description: Translate one subtitle file at a time with deterministic local parsing, timeline preservation, strict batch mapping, safe output composition, and an optional loopback-only visualizer. Use when an agent needs to translate SRT, WebVTT/VTT, or ASS subtitles; preserve ASS sections, event fields, inline semantic styling, or hard line breaks; normalize VTT to SRT; detect karaoke degradation; or validate an LLM subtitle translation before writing it.
metadata:
  author: "Lumen"
  openclaw:
    requires:
      bins:
        - node
        - npm
        - python3
    homepage: "https://github.com/Lumen01/agent-subtitle-translator"
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

### Runtime boundary

- The core workflow reads the one subtitle file selected by the user, writes its work package and final output, and never contacts a translation provider.
- The optional visualizer is a local display service. It binds only to `127.0.0.1`, stores task history under `~/.agent-subtitle-translator/visualizer`, and accepts bridge requests only through that local service.
- The bridge does not accept remote URLs, the service never launches a browser subprocess, and visualizer output is confined to the current task's private `output` directory.
- The Agent or user opens the visualizer URL explicitly. The visualizer is display-only and does not receive subtitle uploads or translation controls from the browser.

## Workflow

### Optional Agent visualizer workflow

The deterministic CLI workflow can run without a Web service. When the Agent or user chooses to observe progress in the visualizer, complete these steps before using the bridge:

1. **Check the environment.** Run from the Skill directory. Install or verify the Python dependency from `requirements.txt`, confirm Python can run `scripts/subtitle_tool.py --help`, confirm Node.js satisfies the package requirement (Node 20 or newer), install Node dependencies once with `npm install`, and run `npm run build` successfully.
2. **Check the Web service.** Request `http://127.0.0.1:4317/api/health`. Reuse the service only when the response is healthy, identifies `subtitle-visualizer`, and reports a compatible Skill version. Otherwise start the service after resolving any occupied-port conflict, then record the printed URL.
3. **Open the Web page when requested.** Navigate the selected browser to the printed local URL and report whether it loaded. Browser access is an observation step and does not grant the page task-input or translation permissions.
4. **Run the visualizer workflow.** Run `identify`, then create the task, start batches, submit and validate responses, and compose through `visualizer:bridge`. Keep reporting each meaningful operation in the Agent response.

The commands in the sections below describe the direct deterministic CLI workflow and the safety rules implemented by the bridge. During an Agent visualizer run, use the equivalent bridge commands after the local service is healthy. Do not compose the same task and output path through both workflows.

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

The script merges validated data by stable subtitle ID, independent of completion order. It refuses missing, duplicate, or extra IDs and refuses to overwrite output by default. If the output already exists, choose a new `--output` path or pass `--overwrite` only when replacing that exact output is intentional.

The final report is written next to the subtitle as `<output-path>.report.json`, not at the work directory root. For example, `SPS.ja.srt` has the report `SPS.ja.srt.report.json`.

Read the final report and tell the user:

- output path, format, encoding, entry count, and time range;
- count and IDs of karaoke degradations;
- count and IDs of inline-style fallbacks.

## Local visualizer workflow

The local visualizer is optional. Direct CLI-only use remains available when an Agent is invoking the deterministic tool without a visualizer session. The Web interface is display-only: it never accepts subtitle files, target languages, or translation controls. The Agent remains the only task input and execution surface.

The visualizer listens on `127.0.0.1` by default and stores task history outside the repository under `~/.agent-subtitle-translator/visualizer`.

Install the service once, then check for a reusable instance before starting it:

```bash
npm install
curl -fsS http://127.0.0.1:4317/api/health
# Run this only when the health check fails:
# npm run visualizer:start
```

Reuse the existing instance when `/api/health` returns HTTP 200 with `status: "ok"`, `service: "subtitle-visualizer"`, and a version compatible with this Skill (`1.1.1` for this release); open its URL only when the visualizer is requested and skip `npm run visualizer:start`. If the health request fails or reports an incompatible version, start the service only after addressing the occupied port. If the port responds with another service, report the conflict and use a different port or resolve it deliberately; do not terminate an unknown process automatically.

The visualizer does not call a translation model and keeps the deterministic safety contract; all task inputs and real translation stages come from the Agent through the bridge:

```bash
npm run visualizer:bridge -- identify \
  --agent "Agent name" \
  --model "Model name" \
  --model-version "5.6" \
  --model-series "Sol" \
  --reasoning-strength "high"

npm run visualizer:bridge -- create \
  --input /path/movie.ass \
  --target-language zh-Hans \
  --source-language en

npm run visualizer:bridge -- batch-start --task TASK_ID --batch 1
# Send the complete batches/batch-0001.txt prompt to the available translation model.
npm run visualizer:bridge -- submit-response \
  --task TASK_ID \
  --batch 1 \
  --response /path/responses/batch-0001.txt

npm run visualizer:bridge -- compose --task TASK_ID
```

Bridge composition refuses to overwrite an existing subtitle or report by default. Use a new `--output` path for a separate result, or pass `--overwrite` only when intentionally replacing the exact existing pair:

```bash
npm run visualizer:bridge -- compose --task TASK_ID --overwrite
```

The report path returned by bridge composition is `<output-path>.report.json`, alongside the generated subtitle.

If validation fails, report the failure in the Web task, retry with the original prompt and the validator error, then submit the retried response. Use `retry-batch --task TASK_ID --batch 1` before sending the retry. Use `--allow-style-fallback` only after the required retry and only when the remaining problem is an ASS `S` marker mismatch.

Run identify at the beginning of the visualizer session. The session line shows the reported Agent, each task card shows the model recorded for that task, and the program metadata line separately shows the shared program and Skill version read from package.json. Pass the complete model identifier in `--model` whenever the Agent knows it, such as `GPT-5.6 Luna Hight`; pass `--model-version`, `--model-series`, and `--reasoning-strength` when those fields exist, such as `GPT` + `5.6` + `Sol` + `high`. Older or other models may omit any optional field, and the Web page omits missing fields. Never invent a version, series, or reasoning value that the Agent cannot verify. Keep reporting the same progress in the Agent response after every meaningful bridge operation.

The Web interface supports multiple Agent-created tasks at once. The left queue shows each task and its overall status; the selected task shows batch progress, per-task and per-batch duration, visible subtitle text, validation/retry/degradation warnings, and the live event stream. The interface never displays the manifest, accepts task input, or sends timestamps and raw ASS override tags to the model.

### Agent-side progress output

The Agent must continue reporting progress in its own response while the Web page is open. Web events do not replace Agent output. At minimum, report:

- the visualizer URL and whether it was opened in the selected browser;
- task creation and subtitle preparation, including entry and batch counts;
- each batch start, validation result, retry, and degradation;
- final composition, output path, format, duration, and any warnings.

Keep these updates concise and synchronized with the bridge calls so the user can follow the same run in the Agent and in the Web page.

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
