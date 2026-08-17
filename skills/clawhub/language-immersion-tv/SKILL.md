---
name: language-immersion-tv
description: "Turn movies and TV shows into language-learning material by analyzing subtitle files to extract vocabulary, build frequency decks, and create contextual flashcards. Use when learning a language through media immersion."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [language-learning, subtitles, vocabulary, flashcards, education, media]
---

# Language Immersion TV

## Overview

Language Immersion TV transforms the media you already watch into a personalized language-learning curriculum. It parses subtitle files (.srt, .vtt) from movies and TV shows, extracts the most useful vocabulary, builds frequency-ranked word lists, identifies idioms and multi-word expressions, and exports ready-to-study decks in Anki and CSV format.

The core insight: **you learn faster from content you actually enjoy**. Watching a show you love in your target language makes vocabulary stick because you have emotional context, visual cues, and narrative motivation.

## When to Use

- You're learning a language and want to learn from shows you actually watch
- You have subtitle files (.srt/.vtt) and want to extract useful vocabulary
- You want frequency-based vocabulary decks built from real dialogue
- You want to build a "watch and study" curriculum from a TV series
- **Don't use for:** learning a language from zero — use a structured beginner course first, then use this to accelerate from A2 onward

## How It Works

1. **Parse subtitles** — Read .srt/.vtt files, clean timestamps, extract clean dialogue text
2. **Tokenize & lemmatize** — Split into words, normalize to dictionary forms
3. **Frequency analysis** — Rank words by occurrence; identify high-value words you'll encounter again
4. **Phrase extraction** — Detect common collocations and idioms (e.g., "of course", "what's up", "never mind")
5. **Difficulty scoring** — Classify words as A1/A2/B1/B2/C1 based on frequency
6. **Deck export** — Generate Anki-compatible TSV, CSV, or JSON flashcards with context sentences

## Quick Start

```bash
# Analyze a single subtitle file
python scripts/immersion.py analyze subs/movie.srt --language en

# Build a vocabulary deck from a whole season
python scripts/immersion.py build-season subs/ --language es --output deck.json

# Export to Anki-importable TSV
python scripts/immersion.py export subs/movie.srt --language fr --format anki --output cards.tsv

# Compare vocabulary across multiple episodes to find common words
python scripts/immersion.py compare subs/ --language de --top 100
```

## Supported Languages

Built-in stopword lists and basic lemmatization for: **English, Spanish, French, German, Italian, Portuguese**.

Other languages work but without smart filtering — all words pass through.

## Workflow: Building a Study Curriculum from a TV Series

### Step 1: Collect subtitle files
Gather .srt or .vtt files for the series you're watching in your target language.

### Step 2: Build a master frequency list
```bash
python scripts/immersion.py build-season ~/Downloads/breaking-bad-subs/ --language en --output bb_master.json
```
This identifies the most frequent words across the whole series — the vocabulary you'll encounter repeatedly.

### Step 3: Export episode-by-episode decks
```bash
for f in ~/Downloads/breaking-bad-subs/*.srt; do
  python scripts/immersion.py export "$f" --language en --format anki --output "${f%.srt}.ts"
done
```

### Step 4: Study before watching
Before watching an episode, review its deck (50–100 cards). Then watch the episode and notice the words in context.

### Step 5: Compare and refine
```bash
python scripts/immersion.py compare ~/Downloads/breaking-bad-subs/ --language en --top 200
```
Words that appear in many episodes are your highest-value targets.

## CEFR Level Estimation

The tool estimates word difficulty based on frequency percentile:

| CEFR | Frequency Rank | Description |
|------|---------------|-------------|
| A1 | Top 100 | Most common words (articles, basic verbs) |
| A2 | 101–500 | Everyday vocabulary |
| B1 | 501–1500 | Intermediate — can follow most dialogue |
| B2 | 1501–4000 | Upper-intermediate — films become accessible |
| C1 | 4000–10000 | Advanced — near-native comprehension |

## Common Pitfalls

1. **Studying every word.** Focus on words that appear 3+ times across a series. One-off words are low ROI.
2. **Ignoring context.** Always study words with their original subtitle sentence — context is what makes them stick.
3. **Starting with hard content.** If you're A2, don't start with medical dramas. Begin with sitcoms and cartoons where speech is slower and vocabulary is everyday.
4. **Forgetting to set the language.** The tool needs `--language` for proper stopword removal. Without it, "the", "a", "is" will dominate your deck.
5. **Using machine-translated subtitles.** Always use native-language subtitles, not auto-translated ones. The vocabulary is authentic.

## Verification Checklist

- [ ] `immersion.py analyze subs/movie.srt --language en` prints word frequency stats
- [ ] `immersion.py export subs/movie.srt --language en --format csv` produces a CSV file
- [ ] `immersion.py build-season subs/ --language es` produces a combined frequency list
- [ ] `immersion.py compare subs/ --top 50` shows cross-episode common words
- [ ] Anki TSV output imports cleanly into Anki (tab-separated: word, context, translation-placeholder)

## References

- `references/methodology.md` — the linguistics and cognitive science of learning from comprehensible input
- `references/cefr-levels.md` — CEFR framework explained, with media recommendations per level
