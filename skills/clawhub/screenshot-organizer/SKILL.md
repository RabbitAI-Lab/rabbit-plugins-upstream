---
name: screenshot-organizer
description: "OCR, tag, search, deduplicate, and organize screenshots. Makes screenshots searchable by content, detects and removes duplicates, groups by topic, and generates a searchable index. Use when a user has hundreds of unorganized screenshots and needs to find, clean, or categorize them."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [screenshots, ocr, organization, deduplication, search, digital-life]
---

# Screenshot Organizer

## Overview

Screenshots accumulate fast — error reports, memes, recipes, payment confirmations, chat conversations — and they pile up in a single folder with useless filenames like `Screenshot_2026-08-13-094231.png`. This skill uses image hashing for deduplication, OCR text extraction to make screenshots searchable, content-based tagging to categorize them, and folder organization to sort them by topic. Turn a folder of 500 anonymous images into a searchable, categorized library.

## When to Use

- A user has **hundreds of screenshots** and needs to find a specific one
- A user wants to **delete duplicates** and reclaim storage space
- A user needs to **search screenshots by text content** ("find the screenshot with the confirmation number")
- A user wants screenshots **organized into folders** by category
- A user is **running out of storage** due to screenshot accumulation
- **Don't use for:** organizing photos from a camera (different workflow), or live screen capture automation

## Core Features

### 1. Deduplication Engine (`scripts/dedup_scanner.py`)
Finds exact and near-duplicate screenshots using perceptual hashing:
- Exact duplicates: identical files (same MD5 hash)
- Near-duplicates: visually similar (same screenshot taken twice, minor cropping differences)
- Generates a deletion plan with confidence scores

### 2. OCR Text Extractor (`scripts/ocr_extractor.py`)
Extracts text from screenshots using Tesseract OCR:
- Identifies text content for searchability
- Detects URLs, email addresses, phone numbers, dates
- Generates a searchable text index
- Tags screenshots by content keywords

### 3. Organizer (`scripts/screenshot_organizer.py`)
The main orchestrator that:
- Scans a directory for screenshots
- Runs dedup analysis
- Runs OCR extraction
- Categorizes by content
- Proposes folder organization
- Generates a searchable index

## Numbered Workflow

1. **Scan** — Identify all screenshot files in the target directory
2. **Deduplicate** — Find exact and near-duplicates, flag for deletion
3. **Extract text** — Run OCR on each unique screenshot
4. **Categorize** — Classify by detected content (receipt, chat, error, meme, code, etc.)
5. **Organize** — Propose folder structure and move/rename files
6. **Index** — Generate a searchable JSON index of all screenshots

## Common Pitfalls

1. **Deleting near-duplicates without review.** A "near-duplicate" might be a cropped version with different content. Always review before deleting.

2. **OCR quality varies by screenshot resolution.** Low-resolution or small-text screenshots may have poor OCR results. Check confidence scores.

3. **Filename patterns vary by platform.** macOS uses `Screenshot 2026-01-01 at 10.00.00.png`, Android uses `Screenshot_20260101_100000.png`, Windows uses `Screenshot (1).png`. The scanner detects all patterns.

4. **Large collections take time.** OCR on 500+ images can take 10-30 minutes. The tool processes in batches and can resume.

5. **Privacy concern with OCR.** Screenshots may contain passwords, private messages, financial info. The extracted text index is stored locally and should be treated as sensitive.

## Verification Checklist

- [ ] All screenshot files detected and counted
- [ ] Exact duplicates identified and flagged
- [ ] Near-duplicates identified with confidence scores
- [ ] OCR text extracted for all unique images
- [ ] Content categories assigned
- [ ] Searchable index generated
- [ ] Folder organization plan reviewed before executing moves

## Example Session

**User:** "I have 847 screenshots in my Pictures folder and I can never find anything. Help me organize them."

**Agent:**
```
📊 SCREENSHOT ORGANIZATION REPORT
═══════════════════════════════════════
Total screenshots scanned: 847

DEDUPLICATION:
  Exact duplicates: 43 (saving ~127 MB)
  Near-duplicates: 28 pairs (flagged for review)
  Total reclaimable: ~340 MB

CONTENT CATEGORIES:
  💬 Chat/Social: 234 (28%)
  🧾 Receipt/Payment: 156 (18%)
  🐛 Error/Bug Report: 89 (11%)
  📄 Document/Text: 78 (9%)
  🎭 Meme/Image: 67 (8%)
  💻 Code/Technical: 54 (6%)
  🗺️ Map/Location: 43 (5%)
  📱 App Screenshot: 38 (4%)
  ❓ Unclassified: 88 (10%)

SEARCH INDEX:
  804 unique images indexed
  12,456 words extracted via OCR
  89 URLs detected
  34 email addresses found
  23 phone numbers found

⏱️ ESTIMATED TIME: 15 minutes to organize
```
