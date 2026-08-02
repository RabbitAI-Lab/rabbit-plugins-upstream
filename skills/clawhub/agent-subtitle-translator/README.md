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

## Typical Agent workflow

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
```
