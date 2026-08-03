# Agent Subtitle Translator Skill

<p align="center">
  <img src="assets/icon-large.png" alt="Agent Subtitle Translator logo" width="180">
</p>

[简体中文](README.zh-CN.md)

Translate one SRT, VTT, or ASS subtitle file with local timeline handling, strict ID validation, and safe ASS structure preservation.

This repository is a Skill first. The bundled CLI performs deterministic decoding, parsing, batching, validation, and composition; the executing Agent uses its available translation model, so the CLI needs no external LLM API key.

> ⭐ If this Skill helps you, please [star the repository](https://github.com/Lumen01/agent-subtitle-translator). It helps more people discover the project and supports continued improvements.

## Install the Skill

### Ask an Agent to install it

Copy this prompt to an Agent with terminal access:

```text
Read https://github.com/Lumen01/agent-subtitle-translator/blob/main/README.md and install the Agent Subtitle Translator Skill according to its “Install Manually” section. Before changing anything, inspect existing installations and preserve unrelated files. Unless I explicitly request one runtime only, prefer one shared multi-Agent installation under ~/.agents/skills and expose it to each requested runtime without creating conflicting copies. Install the declared Python dependency in an appropriate user or managed environment, then confirm that the runtime can discover the installed SKILL.md. Do not overwrite or delete an existing installation without first comparing it and reporting the conflict.
```

### Install manually

#### Shared by multiple Agents

Install one shared copy for Codex, Claude, OpenCode, and other compatible runtimes:

```bash
git clone https://github.com/Lumen01/agent-subtitle-translator.git ~/.agents/skills/agent-subtitle-translator
python3 -m pip install --user -r ~/.agents/skills/agent-subtitle-translator/requirements.txt
```

Point each runtime at the shared copy if it requires its own skills directory:

```bash
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s ~/.agents/skills/agent-subtitle-translator ~/.codex/skills/agent-subtitle-translator
ln -s ~/.agents/skills/agent-subtitle-translator ~/.claude/skills/agent-subtitle-translator
```

Inspect each destination first; do not replace an existing file, directory, or link blindly.

#### One runtime only

Clone directly into that runtime's documented skills directory. For example:

```bash
git clone https://github.com/Lumen01/agent-subtitle-translator.git ~/.codex/skills/agent-subtitle-translator
python3 -m pip install --user -r ~/.codex/skills/agent-subtitle-translator/requirements.txt
```

The installed skill root must contain a discoverable `SKILL.md`.

## Prompt an Agent to use it

Name the skill, one input file, and the required target language. The source language is optional.

```text
Use $agent-subtitle-translator to translate ~/Movies/movie.en.srt to Simplified Chinese (zh-Hans). Keep the original timing, do not overwrite existing output, and report any degradation.
```

```text
Use $agent-subtitle-translator to translate ~/Movies/signs.ass from English to Brazilian Portuguese (pt-BR). Preserve ASS styles and event metadata wherever safe.
```

The Agent prepares batches of at most 32 entries, translates them using its available model, retries invalid batch structures, validates stable IDs and markers, and composes only after every batch maps safely. The Skill does not impose a concurrency cap; completed batches are merged by stable ID, not completion order.

## Supported formats and output

| Input | Output | Behavior |
| --- | --- | --- |
| SRT | SRT | Preserve timing; normalize indices and timeline order. |
| VTT/WebVTT | SRT | Convert locally to normalized SRT. |
| ASS | ASS | Preserve the document and event structure; replace only visible Dialogue text. |

Default output is `<stem>.<normalized-BCP47>.<ext>`, for example `movie.zh-Hans.srt` or `movie.pt-BR.ass`. Existing work directories, validated responses, subtitle outputs, and reports are not overwritten unless the corresponding explicit overwrite flag is used. SRT and ASS outputs use UTF-8 BOM.

The CLI recognizes UTF BOMs and UTF-8 directly. It uses `charset-normalizer` for common legacy encodings and stops when the result is too ambiguous to map safely. Preparation reports entry counts, time range, ordering, empty text, format conversion, and ASS-specific preservation facts.

## ASS style preservation and karaoke degradation

Original ASS tags never go to the translation model. Inline style ranges become paired neutral markers such as `⟦S1⟧...⟦/S1⟧`; the markers can move with their meaning in the target language. Hard line breaks become unique movable `BR` markers. After translation, the CLI validates marker count, identity, closure, and nesting before restoring the original tags.

For example, this source:

```text
What date is {\b1\c&H00FFFF&}today{\r}?
```

can safely become:

```text
{\b1\c&H00FFFF&}今天{\r}是几号？
```

If an inline-style response still cannot be restored after a retry, the Agent may explicitly downgrade only that subtitle entry to static text and must report its ID. Count, ID, wrapper, hard-break, or fixed-structure mismatches remain fatal; the Skill never borrows adjacent translations or guesses character positions.

Entries containing `\k`, `\K`, `\kf`, or `\ko` karaoke timing are intentionally downgraded one entry at a time. The output keeps the event timeline, base Style, fields, and safe whole-line positioning, but removes syllable timing and no-longer-applicable character animation. This is reported as a degradation, not a translation failure. Other ordinary ASS entries in the same file retain their supported styling.

## Agent execution order

When an Agent uses this Skill, it must complete the following gates before starting a subtitle task:

1. Check the environment from the Skill directory: install or verify the Python dependency from `requirements.txt`, verify Python can run `scripts/subtitle_tool.py --help`, verify Node.js is 20 or newer, install Node dependencies with `npm install` when needed, and run `npm run build` successfully.
2. Check `http://127.0.0.1:4317/api/health`. Reuse the service only when it is healthy, identifies `subtitle-visualizer`, and reports a compatible Skill version. Otherwise start the service after resolving any occupied-port conflict.
3. Open the service URL. Prefer the Agent's in-app browser; when it is unavailable, open the same URL in the user's default browser. If the user named a browser, try that browser first and apply the fallback rules if it fails. `npm run visualizer:open` is only for starting a new service, not for a healthy instance that is already running.
4. Wait for the browser page to load successfully, report the URL and browser result, then run `visualizer:bridge -- identify`.
5. Only after the browser gate passes, create the task, translate batches, validate responses, and compose through bridge.

The CLI block below is a deterministic core reference. In a visualizer run, do not start with `prepare` before these gates and do not mix CLI composition with bridge composition for the same task and output path.

## Deterministic CLI reference

The Agent normally runs these commands from the installed skill directory:

```bash
python3 scripts/subtitle_tool.py prepare /path/movie.ass --target-language zh-Hans --source-language en

python3 scripts/subtitle_tool.py validate-response \
  --manifest /path/.movie.zh-Hans.subtitle-work/manifest.json \
  --batch 1 \
  --response /path/responses/batch-0001.txt

python3 scripts/subtitle_tool.py compose \
  --manifest /path/.movie.zh-Hans.subtitle-work/manifest.json
```

See `python3 scripts/subtitle_tool.py --help` and each subcommand's `--help` for collision and retry flags. The generated batch prompts contain text and stable IDs but no timelines or raw ASS override tags.
The final composition report is written alongside the subtitle as `<output-path>.report.json`; for example, `SPS.ja.srt` produces `SPS.ja.srt.report.json`. If the output already exists, choose a new path or pass the explicit overwrite flag only when replacement is intentional.

## Local translation visualizer

This Skill starts a local, display-only Web workspace when it is used. It presents the Agent-created task queue on the left and the selected task's batches, validation, retries, degradations, timing, subtitle preview, and event stream on the right. Subtitle files, target languages, and translation controls remain in the Agent; the Web page does not accept task input. The original Python CLI remains the deterministic processing core.

For an Agent visualizer run, use the bridge as the single task execution path. The direct CLI commands above remain available for CLI-only use; do not compose the same task and output path through both paths.

Run or reuse the local service from the Skill directory:

```bash
npm install
curl -fsS http://127.0.0.1:4317/api/health
```

Reuse the instance when the health response is HTTP 200 with `status: "ok"`, `service: "subtitle-visualizer"`, and a version compatible with this Skill (`1.1.0` for this release); open its URL and skip starting another process. If the request fails or reports an incompatible version, address the occupied port before starting the current release. If the port is occupied by another service, report the conflict and choose a different port or resolve it deliberately. The service binds to `127.0.0.1` and persists local task history under `~/.agent-subtitle-translator/visualizer`. The Agent must open the printed URL in the in-app browser when available. If the user names a browser and it opens successfully, keep using that browser and do not open another one; otherwise use the user's default system browser when no in-app browser is available. The Agent continues reporting the same task progress in its own response. The visualizer does not call a translation provider or require an API key. The Agent sends real execution updates through the bridge:

```bash
npm run visualizer:bridge -- identify \
  --agent "Agent name" \
  --model "Model name" \
  --model-version "5.6" \
  --model-series "Sol" \
  --reasoning-strength "high"

npm run visualizer:bridge -- create \
  --input ~/Movies/movie.en.srt \
  --target-language zh-Hans

npm run visualizer:bridge -- batch-start --task TASK_ID --batch 1
# Send batches/batch-0001.txt to the available translation model.
npm run visualizer:bridge -- submit-response \
  --task TASK_ID \
  --batch 1 \
  --response /tmp/batch-0001.txt

npm run visualizer:bridge -- compose --task TASK_ID
```

Bridge composition refuses to replace an existing subtitle or report by default. Use a fresh `--output` path for a separate result, or add `--overwrite` when intentionally replacing the exact existing pair:

```bash
npm run visualizer:bridge -- compose --task TASK_ID --overwrite
```

The report is stored beside the output as `<output-path>.report.json`.

The Web page displays the reported Agent in the session line, records the reported model on each task card, and separately displays the shared program and Skill version from package.json. Pass the complete model identifier in `--model` whenever it is known, such as `GPT-5.6 Luna Hight`. `--model-version`, `--model-series`, and `--reasoning-strength` are optional, so older or other models can omit them and the Web page leaves those fields out. Do not invent values that the Agent cannot verify. Run identify at the beginning of each visualizer session. The Web page only displays tasks created and controlled by the Agent. Direct CLI-only workflows can run without the Web service; when the visualizer is active, keep task creation, validation, and composition on the bridge path.

## Automatic ClawHub Publishing

The GitHub Actions workflow at `.github/workflows/clawhub-publish.yml` publishes
this skill whenever relevant files are pushed to `main`. It uses ClawHub's
official reusable workflow, which skips unchanged content and automatically
creates the next patch version when the skill changed.

Before the first run, add a repository Actions secret named `CLAWHUB_TOKEN`:

1. Create a ClawHub API token from the ClawHub web UI while signed in as the
   owner of this skill.
2. In GitHub, open **Settings → Secrets and variables → Actions** for this
   repository and create the `CLAWHUB_TOKEN` secret with that value.
3. Run **Publish Subtitle Translator to ClawHub** once from the Actions tab, or
   push a relevant change to `main`.

The token is only passed to the publishing workflow and must never be committed
to this repository.

## Develop and test

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/subtitle_tool.py tests/test_subtitle_tool.py
python3 /path/to/skill-creator/scripts/quick_validate.py .
npm install
npm test
```
