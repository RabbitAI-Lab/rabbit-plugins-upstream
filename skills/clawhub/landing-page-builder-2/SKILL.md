---
name: social-media-kit
version: 1.0.0
author: Denis Voronin
license: MIT
description: >-
  Generate a complete week of social media content for all platforms from a single
  topic or brand. Produces platform-optimized posts, a beautiful shareable HTML
  content calendar, hashtag suggestions, posting-time recommendations, and JSON
  export for scheduling tools.
categories:
  - social-media
  - content-creation
  - marketing
tags:
  - social-media
  - content-calendar
  - twitter
  - instagram
  - linkedin
  - marketing
---

# Social Media Kit

Generate a **complete week of social media content** for all major platforms from
a single topic, brand name, or URL.

## Quick Start

```bash
# Generate a week of content for a brand
python scripts/social_kit.py generate --topic 'sustainable fashion' --brand 'EcoThreads'

# Generate 14 days for specific platforms only
python scripts/social_kit.py generate --topic 'AI productivity' --days 14 --platforms twitter,linkedin

# Build an HTML calendar from a previous JSON export
python scripts/social_kit.py calendar content.json --output calendar.html

# Auto-detect topic from any text snippet via stdin
echo 'organic coffee roastery in Brooklyn' | python scripts/social_kit.py --auto
```

## What It Produces

| Output | Description |
|--------|-------------|
| `content.json` | All posts in structured JSON — ready for scheduling tools |
| `calendar.html` | Beautiful, shareable, print-friendly weekly content calendar |
| Console summary | Quick overview of the week's content strategy |

## Output Structure

```
output/
├── content.json     # Machine-readable: 21+ posts with full metadata
└── calendar.html    # Visual weekly grid: 7 days × N platforms
```

## Features

- **21 posts by default** (7 days × 3 platforms), fully customizable
- **Platform optimization**: Twitter (280 chars + hashtags), Instagram (caption + image suggestions), LinkedIn (professional, longer form)
- **Content mix**: follows the 70-20-10 rule — Educational (70%), Promotional (20%), Engaging (10%) — plus behind-the-scenes and UGC
- **Hashtag suggestions** tailored per platform
- **Best posting time** recommendations per platform per day
- **Engagement hooks** and CTAs baked into every post
- **Weekly theme/storyline** that ties all posts together
- **Color-coded HTML calendar**: educational = blue, promo = green, engaging = orange
- **Print-friendly** layout for physical planning
- **JSON export** for Buffer, Hootsuite, Later, and other scheduling tools

## Content Strategy

See [`references/content-strategy.md`](references/content-strategy.md) for the 70-20-10
rule and content pillar framework.

See [`references/platform-guide.md`](references/platform-guide.md) for character limits,
hashtag strategies, and best practices per platform.

## CLI Reference

### `generate`

```bash
python scripts/social_kit.py generate \
  --topic 'sustainable fashion' \
  --brand 'EcoThreads' \
  --days 7 \
  --platforms twitter,instagram,linkedin \
  --output-dir ./output
```

| Flag | Default | Description |
|------|---------|-------------|
| `--topic` | required | The topic, niche, or description |
| `--brand` | topic | Brand or product name |
| `--days` | 7 | Number of days to generate |
| `--platforms` | twitter,instagram,linkedin | Comma-separated platform list |
| `--output-dir` | ./output | Where to write files |

### `calendar`

```bash
python scripts/social_kit.py calendar content.json --output calendar.html
```

### `--auto` (stdin)

```bash
echo 'AI fitness app called FitAI' | python scripts/social_kit.py --auto
```
