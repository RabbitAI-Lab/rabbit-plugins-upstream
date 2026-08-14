---
name: flashcard-forge
description: >
  Convert any text — PDF excerpts, lecture notes, articles, textbook chapters —
  into spaced-repetition flashcards. Generates Anki-importable CSV with Q&A and
  cloze-deletion modes using regex-based extraction and sentence analysis.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - education
  - flashcards
  - anki
  - spaced-repetition
  - study
  - text-processing
---

# Flashcard Forge

> Turn walls of text into decks you'll actually review.

`Flashcard Forge` is a skill that transforms study material (PDFs, lecture
notes, articles, textbook chapters) into spaced-repetition flashcards. It
extracts key facts, definitions, and Q&A pairs using regex patterns and
sentence-structure analysis, then exports Anki-importable CSV files.

## When to Use

Activate this skill when you need to:

- Convert a textbook chapter or lecture transcript into flashcards
- Extract definitions, key facts, or Q&A from a body of text
- Generate cloze (fill-in-the-blank) cards for memorization
- Produce Anki-importable CSV from raw notes
- Study for an exam by turning reading material into active recall cards

## Modes

### Q&A Mode (`--mode qa`)

Extracts question-answer pairs and definition pairs:

- **Definition patterns**: "X is defined as Y", "X refers to Y", "X means Y"
- **Explicit questions**: sentences containing "What/Why/How/When/Where" markers
- **List patterns**: "There are N types of X: A, B, C"
- **Cause/effect**: "X causes Y", "X results in Y"
- **Comparison**: "Unlike X, Y does Z"

### Cloze Mode (`--mode cloze`)

Generates fill-in-the-blank cards by identifying key terms in each sentence and
masking them:

- Nouns and proper nouns are candidates for clozing
- Numbers, dates, and named entities are high-priority cloze targets
- Each card uses Anki's `{{c1::...}}` cloze syntax

### Auto Mode (`--mode auto`, default)

Runs both modes and merges results, deduplicating by question text.

## Quick Reference

| Need                        | Command                                                         |
| --------------------------- | --------------------------------------------------------------- |
| Q&A cards from a text file  | `python3 scripts/flashcard_forge.py notes.txt`                  |
| Cloze cards                 | `python3 scripts/flashcard_forge.py notes.txt --mode cloze`     |
| Anki CSV output             | `python3 scripts/flashcard_forge.py notes.txt -o deck.csv`      |
| Custom cloze count          | `python3 scripts/flashcard_forge.py notes.txt --max-cloze 3`    |
| Min sentence length filter  | `python3 scripts/flashcard_forge.py notes.txt --min-length 20`  |
| JSON output                 | `python3 scripts/flashcard_forge.py notes.txt --format json`    |

## How It Works

1. **Read & clean** — load the text, normalize whitespace, strip markdown
   artifacts.
2. **Segment** — split into sentences using punctuation-aware tokenization.
3. **Extract** — apply regex patterns (see `references/extraction-patterns.md`)
   to find definitions, Q&A, lists, cause/effect, and comparisons.
4. **Rank** — score each candidate by information density (presence of key
   terms, numbers, definitions).
5. **Deduplicate** — remove near-identical cards using Jaccard similarity.
6. **Export** — write Anki-importable CSV (semicolon-separated, quoted) or JSON.

See `references/anki-import.md` for how to import the CSV into Anki.

## Files

- `references/extraction-patterns.md` — catalog of regex extraction patterns
- `references/anki-import.md` — step-by-step Anki import guide
- `references/study-strategies.md` — best practices for flashcard-based learning
- `scripts/flashcard_forge.py` — the main extraction and export script
- `scripts/sample_text.txt` — example input demonstrating all pattern types

## Common Pitfalls

1. **Over-generation.** A long text can produce hundreds of mediocre cards. Use
   `--max-cards` to cap output and `--min-length` to filter trivial sentences.

2. **CSV delimiter conflicts.** Anki expects semicolon-separated values for
   basic cards. The script handles quoting automatically; don't open the CSV in
   Excel and re-save (it may change the delimiter).

3. **Cloze mode needs cloze note type.** Cloze cards only work with Anki's
   "Cloze" note type, not "Basic." See `references/anki-import.md`.

4. **Poor input quality.** Garbled OCR or deeply nested markdown confuses the
   sentence segmenter. Pre-clean the text for best results.

5. **Duplicates across runs.** The dedup step is within-file only. If you merge
   multiple outputs, dedup manually or use `--format json` and post-process.

## Verification Checklist

- [ ] Input text is reasonably clean (no raw HTML, minimal OCR artifacts)
- [ ] Chosen mode matches your Anki deck type (qa → Basic, cloze → Cloze)
- [ ] `--max-cards` set if the input is large
- [ ] CSV opens correctly in a text editor (fields quoted, semicolon-separated)
- [ ] Test-imported into Anki and reviewed 5-10 cards for quality

## License

MIT © Denis Voronin
