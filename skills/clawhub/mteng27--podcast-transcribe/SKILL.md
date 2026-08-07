---
name: podcast-transcribe
description: "Download podcast audio from RSS feeds and transcribe to text using AuralWise API. This skill should be used when the user wants to download podcast episodes, convert podcast audio to text transcripts, or batch-process a podcast library for searchable content. Triggers include downloading podcasts, podcast transcription, audio-to-text conversion, RSS feed downloading, or any request involving podcast audio acquisition and speech-to-text conversion. Covers RSS feed discovery, audio downloading, AuralWise API transcription, and AI-generated content overviews with book references, key concepts, and searchable keywords."
agent_created: true
---

# Podcast Transcribe

## Overview

Automate the full pipeline of podcast content acquisition: discover RSS feed, download all episodes, transcribe audio to text via AuralWise API, and generate structured content overviews for each episode. Output includes audio files, Show Notes, full transcripts (.txt / .md / .srt), and AI-generated episode summaries with extracted books, concepts, and keywords.

## Workflow

### Step 1: Discover RSS Feed

Determine the podcast's RSS Feed URL. Use one of these methods in priority order:

1. **User provides URL directly** — proceed to Step 2.
2. **Apple iTunes Search API** — search by podcast name:
   ```
   GET https://itunes.apple.com/search?term={podcast_name}&media=podcast&limit=5
   ```
   Extract `feedUrl` from results. See `references/rss_discovery.md` for details.
3. **Platform-specific patterns** — e.g., Ximalaya albums use `https://www.ximalaya.com/album/{id}.xml`.

Verify the RSS Feed is accessible by fetching it and confirming episode count.

### Step 2: Configure AuralWise API Key

The transcription service requires an AuralWise API Key. Handle this interactively:

1. **Check if API Key is already configured** — look for a `.env` file in the working directory containing `AURALWISE_API_KEY=asr_...`. If found and valid, skip to Step 3.
2. **If no API Key** — ask the user:
   > "语音转写需要 AuralWise API Key。请到 https://auralwise.cn/refid=asgbifle 注册并获取 API Key（在 Settings → API Key 管理页面生成，格式为 `asr_` 开头）。"
3. **Write the Key to `.env`** — create `{working_dir}/.env` with:
   ```
   AURALWISE_API_KEY=asr_user_provided_key
   ```
4. **Verify the Key** — call `GET https://api.auralwise.cn/v1/account` with header `X-API-Key: {key}` to confirm balance and concurrency.
5. **If user only wants downloads (no transcription)** — use `--download-only` flag, skip API Key requirement.

See `references/auralwise_api.md` for full API documentation.

### Step 3: Run the Pipeline

Execute the bundled pipeline script. The script handles RSS parsing, audio downloading, transcription submission/polling, and multi-format output saving.

**Prerequisites:**
- Python 3 with `requests` installed
- The pipeline script: `scripts/podcast_pipeline.py`

**Basic command:**
```bash
python3 scripts/podcast_pipeline.py \
  --rss-url "https://example.com/feed.xml" \
  --podcast-name "播客名称" \
  --env-file .env
```

**Test mode (recommended first run) — process 2 shortest episodes:**
```bash
python3 scripts/podcast_pipeline.py \
  --rss-url "https://example.com/feed.xml" \
  --podcast-name "播客名称" \
  --env-file .env \
  --test 2
```

**Download only (no API Key needed):**
```bash
python3 scripts/podcast_pipeline.py \
  --rss-url "https://example.com/feed.xml" \
  --podcast-name "播客名称" \
  --download-only
```

**Key CLI parameters:**

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--rss-url` | Yes | Podcast RSS Feed URL |
| `--podcast-name` | No | Podcast name (default: "播客") |
| `--output-dir` | No | Output root dir (default: ~/Desktop/{name}合集) |
| `--api-key` | No | AuralWise API Key directly |
| `--env-file` | No | Path to .env file containing API Key |
| `--test N` | No | Test mode: process N shortest episodes |
| `--download-only` | No | Download audio only, skip transcription |
| `--transcribe-only` | No | Transcribe only, skip download |
| `--language` | No | Transcription language (default: zh) |
| `--diarize` | No | Enable speaker diarization (+0.2 CNY/hour) |

**Output directory structure:**
```
{output_dir}/
├── 音频/              # Downloaded audio files (.m4a)
├── 文稿/              # Show Notes (.md)
├── 文字稿/            # Transcripts
│   ├── EP01-xxx.txt          # Plain text
│   ├── 带时间戳_EP01-xxx.md  # Markdown with timestamps
│   └── EP01-xxx.srt          # SRT subtitles
├── pipeline_state.json  # Resume state
└── pipeline.log         # Run log
```

**Cost estimation:** AuralWise optimize tier = 0.27 CNY/hour. For a podcast with ~170 hours of audio, total cost is ~46 CNY.

### Step 4: Generate Content Overviews

After transcripts are generated, create a structured overview Markdown file for each episode. This is an AI-generated summary — read the `.txt` transcript and produce a `概览_{filename}.md` file in the same `文字稿/` directory.

**Overview file format:**

```markdown
# {Episode Title}

## 播客信息

| 字段 | 内容 |
|------|------|
| 播客 | {Podcast name} |
| 期号 | EP{number} |
| 时长 | {duration} |
| 发布日期 | {date} |

## 内容摘要

{3-5 paragraph summary of what this episode covers}

## 提到的书籍

| 书名 | 作者 | 在本期中的角色 |
|------|------|----------------|
| {Book title} | {Author} | {How it's referenced} |

## 核心概念速查

| 概念 | 一句话解释 |
|------|-----------|
| {Concept} | {Brief explanation} |

## 关键案例

| 案例 | 说明 | 对应理论 |
|------|------|----------|
| {Case} | {Description} | {Related concept} |

## 金句提炼

> {Notable quote 1}
> {Notable quote 2}

## 检索关键词

`keyword1` `keyword2` `keyword3` ...
```

**Overview generation guidelines:**
- Read the full `.txt` transcript file to understand the episode content
- Extract all book titles mentioned (look for patterns like "《书名》", "the book", author names)
- Identify 5-15 core concepts discussed in depth
- Pull 2-5 memorable quotes verbatim from the transcript
- Generate 10-20 searchable keywords wrapped in backticks for easy full-text search
- Keep summaries concise but information-dense — the goal is fast retrieval, not replacement of the original transcript
- Save as `概览_{original_txt_filename_without_ext}.md` in the same `文字稿/` directory

### Step 5: Resume / Batch Processing

The pipeline supports **断点续传 (resume)**. If interrupted:
- Re-run the same command — completed episodes are automatically skipped
- State is tracked in `pipeline_state.json`
- If AuralWise balance runs out mid-run, remaining episodes are downloaded but transcription is skipped
- After recharging, re-run to process remaining episodes

## Important Notes

- **Audio URL accessibility**: AuralWise transcribes by fetching the audio URL directly — no need to download then upload. Verify URLs are publicly accessible.
- **Ximalaya feeds**: Audio URLs from Ximalaya RSS feeds are publicly accessible and work directly with AuralWise.
- **Xiaoyuzhou (小宇宙)**: Their API requires login tokens. Use the iTunes Search API to find the same podcast's RSS feed on Ximalaya or Apple Podcasts instead.
- **Rate limiting**: AuralWise has a default concurrency limit of 3. The script handles 429 responses with retry.
- **Encoding**: All output files are UTF-8 encoded. Filenames are sanitized to avoid OS-level issues.

## Resources

- `scripts/podcast_pipeline.py` — Main pipeline script (parameterized, supports any RSS feed)
- `scripts/.env.example` — Template for API Key configuration
- `references/auralwise_api.md` — Full AuralWise API documentation
- `references/rss_discovery.md` — Methods for discovering podcast RSS feeds
