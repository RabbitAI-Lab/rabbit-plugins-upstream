---
name: meme-maker
description: Search meme templates, suggest formats, and generate local or hosted image memes.
---

# Meme Maker

Generates memes using web APIs or local image tools.

## Quick Start

```bash
# List popular templates
node skills/meme-maker/scripts/list-templates.js

# Generate a meme
node skills/meme-maker/scripts/generate.js --template="Drake Hotline Bling" --top="text 1" --bottom="text 2"
```

## Templates

Popular templates built-in:
- Drake Hotline Bling
- Distracted Boyfriend
- Change My Mind
- Two Buttons
- Expanding Brain
- Is This a Pigeon?
- Blank Nut Button
- Running Away Balloon
- UNO Draw 25 Cards
- Waiting Skeleton
- Boardroom Meeting Suggestion
- Woman Yelling at Cat
- Batman Slapping Robin

## API

Uses imgflip API (free, no key required for basic usage).
For unlimited usage, set `IMGFLIP_USER` and `IMGFLIP_PASS` in `.env`.

## Output

Returns the generated meme image URL. Can be downloaded or shared directly.
