---
name: story-spark
description: "Generate creative writing prompts from your own life. Scans personal photos metadata, journal entries, and notes to find emotionally resonant moments, then transforms them into fiction seeds across multiple genres. Use when experiencing writer's block or wanting to fictionalize real experiences."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [creative-writing, writing-prompts, fiction, storytelling, journaling, creativity]
---

# Story Spark

## Overview

Story Spark cures writer's block by mining your own life for fiction-worthy moments. Instead of generic prompts ("write about a rainy day"), it analyzes your photos, journal entries, and notes to find specific, emotionally charged moments — then transforms them into fiction seeds across genres from literary fiction to sci-fi to thriller.

The core idea: **the best fiction grows from real emotional truth**. Your photo from a lonely train station, your journal entry about a strange conversation, your half-finished note about a weird dream — these are the raw materials of compelling stories.

## When to Use

- You have writer's block and need a prompt that feels personally meaningful
- You want to write fiction inspired by your own experiences
- You have a library of photos or journal entries and want creative uses for them
- You're teaching creative writing and want a prompt-generation tool
- **Don't use for:** memoir/journal writing directly (this is for fiction, not diary entries)

## How It Works

1. **Source Scan** — Extract moments from EXIF photo metadata (date, location, captions) and/or text files (journal entries, notes)
2. **Moment Extraction** — Identify emotionally interesting elements: unusual locations, solitary times, evocative words, seasonal moods
3. **Genre Transformation** — Apply genre lenses (mystery, romance, sci-fi, horror, literary) to each moment
4. **Prompt Generation** — Produce specific, detailed story prompts with character, setting, conflict, and twist suggestions
5. **Export** — Save prompts as text, markdown, or JSON for your writing workflow

## Quick Start

```bash
# Generate prompts from a folder of photos (EXIF data)
python scripts/story_spark.py photos ~/Pictures/vacation-2025/ --count 5

# Generate prompts from journal/text files
python scripts/story_spark.py text ~/journal/ --count 5

# Generate from both sources
python scripts/story_spark.py mixed --photos ~/Pictures/ --texts ~/journal/ --count 10

# Generate prompts in a specific genre
python scripts/story_spark.py photos ~/Pictures/ --genre mystery --count 3

# Use the built-in demo source (no files needed)
python scripts/story_spark.py demo --count 5
```

## Genre Lenses

Story Spark applies these genre transformations to your moments:

| Genre | Transformation Pattern |
|-------|----------------------|
| **Literary Fiction** | Focus on internal conflict, character growth, quiet revelations |
| **Mystery/Thriller** | Introduce a secret, a disappearance, an unanswered question |
| **Science Fiction** | Add a speculative element: time shift, technology, alternate reality |
| **Horror** | Find the uncanny in the mundane: something is slightly wrong |
| **Romance** | Introduce an unexpected connection or missed encounter |
| **Historical** | Shift the moment to a different era with period-appropriate detail |

## Workflow: From Photo to Story

### Step 1: Scan your sources
```bash
python scripts/story_spark.py photos ~/Pictures/2025/ --count 10 --output prompts.json
```

### Step 2: Review generated prompts
Each prompt includes:
- **Source moment**: What was extracted (location, time, mood)
- **Genre lens**: How it was transformed
- **Story seed**: A 2-3 sentence premise
- **Character suggestion**: Who could the protagonist be?
- **Conflict hook**: What goes wrong or creates tension?
- **Twist idea**: An unexpected turn for the ending

### Step 3: Pick one and write
Choose the prompt that resonates most and free-write for 15 minutes. Don't edit — just follow the spark.

## Common Pitfalls

1. **Expecting finished stories.** Story Spark generates *prompts*, not complete narratives. The writing is still yours.
2. **Using only happy photos.** The best fiction comes from complex emotions — loneliness, confusion, nostalgia, not just joy.
3. **Sticking to one genre.** Try the same moment across multiple genres — a vacation photo becomes very different stories as mystery vs. romance vs. sci-fi.
4. **Ignoring the "boring" moments.** A photo of an empty parking lot at 3 AM is often a better story seed than a beautiful sunset.
5. **Overthinking the prompt.** The prompt is a spark, not a blueprint. Let the story go where it wants.

## Verification Checklist

- [ ] `story_spark.py demo --count 5` generates 5 story prompts without any input files
- [ ] `story_spark.py photos ~/Pictures/ --count 3` reads EXIF data from JPEGs
- [ ] `story_spark.py text ~/journal/ --count 3` extracts prompts from text files
- [ ] Each prompt includes: source moment, genre, premise, character, conflict, twist
- [ ] `--genre` flag filters to a specific genre lens

## References

- `references/creative-process.md` — the craft of turning real moments into fiction
- `references/genre-transformations.md` — detailed breakdown of each genre lens
