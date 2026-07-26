---
name: mailchimp-to-ghost
description: Sync Mailchimp newsletter posts to a Ghost blog. Fetches newsletter content from RSS, converts HTML to clean markdown with horizontal rules, uploads images to Ghost, and publishes as Lexical-format posts with proper formatting.
homepage: https://github.com/nickludlam/mailchimp-to-ghost-skill
caption: Sync Mailchimp newsletter posts to Ghost blog
metadata:
  openclaw:
    emoji: "📰"
    homepage: "https://github.com/nickludlam/mailchimp-to-ghost-skill"
    requires:
      bins: ["python3", "ghst"]
      env: ["GHOST_URL", "GHOST_STAFF_ACCESS_TOKEN"]
    primaryEnv: "GHOST_URL"
---

# Sync Newsletter Skill

Fetch newsletter posts from a Mailchimp RSS feed and sync them to a Ghost blog as properly formatted posts with uploaded images and horizontal rules.

## Overview

This skill automates the complete workflow of:
1. **Fetching** newsletter content from Mailchimp's RSS feed
2. **Converting** HTML email content to clean markdown (preserving horizontal rules, links, formatting)
3. **Downloading** images from Mailchimp CDN
4. **Uploading** images to Ghost
5. **Publishing** to Ghost as Lexical-format posts with local images

## Requirements

- **Python 3** with packages: `beautifulsoup4`, `requests`, `feedparser`, `markdownify`, `lxml`
- **ghst CLI** for Ghost publishing (see [ghst skill](../ghst/SKILL.md))
- **Environment variables:**
  - `GHOST_URL` - Your Ghost instance URL
  - `GHOST_STAFF_ACCESS_TOKEN` - Ghost Admin API token

## Installation

### Python Dependencies

```bash
cd skills/sync-newsletter
pip install beautifulsoup4 requests feedparser markdownify lxml
```

### Ghost CLI (ghst)

Install globally via npm:
```bash
npm install -g @tryghost/ghst
```

## Configuration

Set up your Ghost credentials in `~/.openclaw/.env`:

```env
GHOST_URL="https://myghostblog.com"
GHOST_STAFF_ACCESS_TOKEN="your-token-id:secret"
```

## Usage

### ⚠️ CRITICAL: Always Re-fetch First

**You MUST re-fetch the RSS feed every time before syncing** to ensure you're working with the latest newsletter data. The cache may contain stale or previously-processed entries.

```bash
# 1. Clear any stale cache and fetch fresh from RSS (ALWAYS DO THIS FIRST)
rm -rf cache/ && python3 scripts/fetch_markdown.py

# 2. Sync to Ghost (downloads images, uploads them, creates draft post)
python3 scripts/sync_to_ghost.py
```

**Why this matters:** The RSS feed only shows the most recent newsletter(s). If you sync without re-fetching, you may:
- Create duplicate posts (Ghost will add `-2`, `-3` suffixes to slugs)
- Miss new newsletters entirely
- Process outdated content

### Cache Management

All cached data is stored in the `cache/` folder:
- `cache/feed_cache.xml` — RSS feed cache
- `cache/newsletter_markdown_1.md` — Generated markdown

To force a fresh fetch, delete the cache:
```bash
rm -rf cache/
```

### Deduplication

The sync script checks Ghost for existing posts with similar titles before creating. If a match is found, it warns you and exits. Use `--force` to create anyway:

```bash
python3 scripts/sync_to_ghost.py --force
```

## What Gets Converted

### From Mailchimp HTML

The fetch script extracts and converts:
- **Text content** — Paragraphs, headings, lists
- **Formatting** — Bold, italic, links
- **Images** — With filtering for social icons and spacers
- **Horizontal rules** — `mceDividerBlockContainer` → `---`
- **Boilerplate removal** — Unsubscribe links, preview text, social icons

### To Ghost Lexical Format

The sync script creates Lexical JSON with:
- **Paragraphs** with inline formatting (bold, italic, links)
- **Line breaks** preserved within paragraphs
- **Headings** (H2, H3)
- **Images** uploaded to Ghost (not hotlinked)
- **Horizontal rules** — `---` → `horizontalrule` nodes
- **Blockquotes**
- **Buttons** — Call-to-action links → Lexical `button` nodes (center-aligned by default)

### Button Handling

Mailchimp button blocks are converted to Ghost's native Lexical button nodes:

**Markdown pattern:** `[button: text](url)`

**Lexical output:**
```json
{
  "type": "button",
  "version": 1,
  "buttonText": "Read More",
  "alignment": "center",
  "buttonUrl": "https://example.com"
}
```

**Configuration:**
- Buttons are **center-aligned** by default (can be changed in `sync_to_ghost.py`)
- Button text is extracted from the Mailchimp button link
- URL is cleaned of Mailchimp tracking parameters

## Script Reference

### `scripts/fetch_markdown.py`

Fetches Mailchimp RSS and converts to clean markdown.

**Features:**
- Strips Mailchimp boilerplate (social icons, unsubscribe links, preview text)
- Detects `mceDividerBlockContainer` elements and converts to `---` horizontal rules
- Removes tiny spacer images and layout tables
- Deduplicates repeated content blocks
- Preserves actual newsletter content, images, and formatting

**Configuration:**
- `RSS_URL` — The Mailchimp feed URL (hardcoded in script)
- `limit` — Number of entries to process (default: 1)
- Output: `cache/newsletter_markdown_N.md`

### `scripts/sync_to_ghost.py`

Complete sync workflow: downloads images, uploads to Ghost, creates Lexical-format draft post.

**Features:**
- **Deduplication** — Checks for existing posts by title
- **Image handling** — Downloads from Mailchimp CDN, uploads to Ghost via `ghst image upload`
- **URL mapping** — Replaces external image URLs with Ghost-hosted URLs
- **Lexical conversion** — Full markdown → Lexical JSON with:
  - Paragraphs with inline bold/italic/link formatting
  - Line breaks within paragraphs (preserves `<br>`-style breaks)
  - Headings (H2, H3; skips H1 as it's the post title)
  - Images with alt text
  - Horizontal rules (`---` → `horizontalrule` nodes)
  - Blockquotes
  - **Buttons** — `[button: text](url)` pattern → center-aligned Lexical `button` nodes
- **Draft creation** — Creates post with `newsletter` tag as draft

**Command-line options:**
- `--force` — Bypass deduplication check

## Example: Manual Workflow

```bash
# Navigate to skill directory
cd ~/.openclaw/workspace/skills/sync-newsletter

# Fetch latest newsletter
python3 scripts/fetch_markdown.py

# Review the markdown
cat cache/newsletter_markdown_1.md

# Sync to Ghost (creates draft)
python3 scripts/sync_to_ghost.py

# Publish via Ghost admin when ready
```

## Troubleshooting

### Duplicate posts created (slug has `-2`, `-3` suffix)

**Cause:** You synced without re-fetching the RSS feed first. The cache contained an already-published newsletter.

**Fix:** Always clear cache and re-fetch before syncing:
```bash
rm -rf cache/
python3 scripts/fetch_markdown.py
python3 scripts/sync_to_ghost.py
```

### No horizontal rules in output

Delete cache and re-fetch:
```bash
rm -rf cache/
python3 scripts/fetch_markdown.py
```

### Images not uploading

Check Ghost API is accessible:
```bash
ghst site info --json
```

### Duplicate posts created

The deduplication should prevent this. If it fails, check the existing post title matches exactly.

### Buttons not rendering as styled buttons

**Cause:** The markdown may contain plain links instead of the button pattern.

**Fix:** Check the generated markdown has `[button: text](url)` pattern (not just `[text](url)`). If buttons aren't detected, the Mailchimp HTML structure may have changed.

## Notes

- The conversion is tuned for Mailchimp's HTML structure; other newsletter platforms may need adjustments
- Images are uploaded to Ghost and replaced in the content (no hotlinking)
- Horizontal rules from Mailchimp dividers are preserved as `---` in markdown and converted to Ghost's `horizontalrule` nodes
- The script preserves the conversational formatting with line breaks within paragraphs
- **Buttons** — Mailchimp button blocks are converted to center-aligned Ghost Lexical button nodes using the `[button: text](url)` pattern
