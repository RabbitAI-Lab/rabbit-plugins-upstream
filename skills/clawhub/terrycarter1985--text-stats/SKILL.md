---
name: text-stats
description: Analyze text files and produce statistics: word count, character count (with/without spaces), reading time estimate, sentence count, paragraph count, and most frequent words. Use when you need quick insights into the structure and size of a text document.
metadata:
  openclaw:
    emoji: "📊"
---

# Text Stats

Produce a statistics report for a text or Markdown file.

## When to use

- You have a `.txt` or `.md` file and need to know its size/complexity quickly
- Estimate reading time for an article or document
- Find the most common words in a body of text
- Batch-analyze a directory of text files

## Prerequisites

- Python 3.6+ available as `python3`

## Usage

### Single file

```bash
python3 scripts/text_stats.py path/to/file.md
```

### Directory (all .txt and .md files)

```bash
python3 scripts/text_stats.py path/to/directory/
```

### JSON output (for piping)

```bash
python3 scripts/text_stats.py path/to/file.md --json
```

### Minimum word frequency filter (top-N)

```bash
python3 scripts/text_stats.py file.md --min-count 3 --top 15
```

## Output

Human-readable report by default:

```
=== Text Stats: article.md ===
Words:        1,247
Chars (raw):  8,432
Chars (nosp): 6,891
Sentences:    63
Paragraphs:   24
Reading time: ~5 min (250 wpm)

Most common words (top 10):
  the (124)  and (87)  that (52)  ...
```

With `--json`:

```json
{
  "file": "article.md",
  "words": 1247,
  "chars_raw": 8432,
  "chars_no_spaces": 6891,
  "sentences": 63,
  "paragraphs": 24,
  "reading_time_min": 5,
  "top_words": [["the", 124], ["and", 87], ["that", 52]]
}
```

## Options

| Flag | Default | Description |
|---|---|---|
| `--json` | off | Output JSON instead of text |
| `--min-count` | 2 | Minimum occurrences for top-word list |
| `--top` | 10 | Max entries in top-word list |
| `--wpm` | 250 | Words-per-minute for reading estimate |
