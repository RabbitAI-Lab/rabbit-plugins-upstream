---
name: video-content-analyzer
description: Analyze video content by extracting keyframes, searching the web for references, storing results in Supabase, and publishing reports to Feishu Wiki. Supports single-video and batch (whole-directory) processing with category-grouped Wiki publishing. Use when a user wants to analyze one video or many videos at once and turn them into searchable documentation.
tags: ['video', 'analysis', 'wiki', 'search', 'supabase']
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": ["python3", "ffmpeg"] },
      },
  }
---

# Video Content Analyzer

Process video content into structured, searchable documentation. The workflow
extracts keyframes with ffmpeg, searches the web for related references, stores
all metadata and results in Supabase, and publishes analysis reports to Feishu
Wiki.

## When to use

- Analyze a single video and publish a report to Feishu Wiki.
- Batch-analyze every video in a directory in one run, with results stored in
  Supabase and reports grouped by category under per-category Wiki nodes.

## Setup

1. Install dependencies: `pip install -r requirements.txt` (requires `ffmpeg`).
2. Copy `.env.example` to `.env` and fill in Supabase, Google Custom Search,
   and Feishu OpenAPI credentials.
3. Apply the Supabase schema: `supabase db push`.

## Usage

Single video:

```bash
python src/main.py path/to/video.mp4 --user-id <uuid> --space-id <feishu-wiki-space-id>
```

Batch process a directory (results stored in Supabase, reports grouped by
category in Feishu Wiki):

```bash
python src/main.py path/to/videos/ --batch --user-id <uuid> --space-id <space-id>
```

Optional keyword-based categories (override the default sub-folder grouping):

```bash
python src/main.py path/to/videos/ --batch --user-id <uuid> --space-id <space-id> \
  --category-rules '{"webinar": "events", "tutorial": "learning"}'
```

### Batch flags

- `--batch` — treat the path as a directory and process all videos inside.
- `--no-recursive` — only scan the top level of the directory.
- `--category-rules` — JSON map of path-keyword → category (takes priority over
  the sub-folder name).
- `--stop-on-error` — abort on the first failing video (default: continue and
  report per-video failures).

## How categorization works

Each video's category is resolved in this order:

1. Keyword rules matched against the video's relative path.
2. The first sub-directory under the scanned root (folder-based grouping).
3. `uncategorized`.

Pages sharing a category are published under one Feishu Wiki node, which is
created once per category and reused across runs.

## Outputs

- `video_assets`, `video_frames`, `search_results`, `wiki_pages` rows in Supabase.
- A `batch_runs` summary row per directory run (totals + success/failure counts).
- Category-grouped report pages in the target Feishu Wiki space.
