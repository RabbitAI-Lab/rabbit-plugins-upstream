---
name: research-assistant
version: 0.1.0
description: Auto-illustrate research notes — read Bear notes tagged 「待整理」, match a topic-relevant GIF to each note's content, and insert it inline.
author: terrycarter1985
tags: [research, bear, gif, media, productivity]
metadata: {"moltbot":{"emoji":"🔬","os":["darwin"],"requires":{"bins":["grizzly","gifgrep"]}}}
capabilities: [note_taking, media_search, personal_productivity]
---

# Research Assistant

Turns rough research notes into illustrated ones. It finds every Bear note tagged
**待整理** ("to be organized"), derives a topic from each note's content, searches
for a relevant GIF, and inserts it into the note. Built on the `bear-notes`
(grizzly) and `gifgrep` skills.

> Platform: macOS only. Requires the Bear app running, a Bear API token, and the
> `grizzly` + `gifgrep` CLIs installed (see `bear-notes` and `gifgrep` skills).

## Prerequisites

- Bear app installed and running.
- Bear API token saved at `~/.config/grizzly/token`
  (Bear → Help → API Token → Copy Token).
- `grizzly` CLI (see `bear-notes` skill) and `gifgrep` CLI (see `gifgrep` skill).

## Quick Start

```bash
# Dry run: show what would change, insert nothing
./research_assistant.sh --tag 待整理 --dry-run

# Real run: insert one matched GIF per note
./research_assistant.sh --tag 待整理

# Limit how many notes to process in one pass
./research_assistant.sh --tag 待整理 --max 5
```

## How It Works

1. **Collect notes** — `grizzly open-tag --name "待整理" --enable-callback --json`
   lists every note carrying the tag.
2. **Read each note** — `grizzly open-note --id <ID> --enable-callback --json`
   pulls the full note body.
3. **Derive a topic** — the script takes the note title plus the most frequent
   meaningful words from the body to build a short GIF search query. This is
   intentionally simple and dependency-free; tune `topic_query()` if you want
   smarter extraction.
4. **Match a GIF** — `gifgrep "<topic>"` returns a relevant GIF URL.
5. **Insert inline** — the GIF is appended to the note as Markdown
   (`![topic](gif-url)`) via
   `grizzly add-text --id <ID> --mode append --token-file ~/.config/grizzly/token`.
   Use `--mode prepend` if you'd rather place it at the top.

## Options

- `--tag <name>` — tag to scan (default: `待整理`).
- `--max <n>` — process at most N notes (default: all).
- `--mode <append|prepend>` — where to insert the GIF (default: `append`).
- `--dry-run` — print planned actions without modifying any note.
- `--token-file <path>` — Bear token path (default: `~/.config/grizzly/token`).

## Notes & Limitations

- Idempotency: the script skips a note if it already contains a
  `<!-- research-assistant:gif -->` marker, so re-runs won't stack duplicate GIFs.
- Topic extraction is keyword-frequency based, not semantic. For niche notes,
  review the dry-run output before a real run.
- One GIF per note per pass by design — keeps notes readable.
- Bear must stay open and focused enough to honor x-callback-url requests.
