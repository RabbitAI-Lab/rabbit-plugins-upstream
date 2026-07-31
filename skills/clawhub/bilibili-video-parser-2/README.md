# bilibili-video-parser 🎬

Parse and analyze Bilibili (哔哩哔哩) video content from a URL — metadata, visual frames, and speech transcription, all in one pipeline.

## What It Does

Given a Bilibili video URL, this tool extracts:

- **Metadata** — title, author, duration, views, likes, etc.
- **Visual content** — key frames extracted and analyzed via VLM (Vision Language Model)
- **Speech content** — audio transcribed via ASR (or subtitles if available)
- **Synthesized output** — everything combined into structured JSON

```
Bilibili URL
    │
    ├─ Stage 1: Metadata API ──→ Title, Author, Duration, Views...
    │
    ├─ Stage 2: Subtitle API ──→ (If available, skip ASR)
    │
    ├─ Stage 3: Stream Download ──→ video.m4s + audio.m4s → merged.mp4
    │
    ├─ Stage 4a: Frame Extraction ──→ key frames → VLM visual analysis
    │
    ├─ Stage 4b: Audio Extraction ──→ WAV chunks → ASR transcription
    │
    └─ Stage 5: Synthesis ──→ Metadata + Visual + Audio → JSON output
```

## Quick Start

```bash
# Full pipeline
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC"

# Save result to file
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" -o result.json

# Metadata only (fast, no download)
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" --skip-download

# Skip visual analysis (ASR only)
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" --skip-visual

# Skip audio transcription (visual only)
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" --skip-audio

# Analyze only 5 representative frames (save tokens)
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" --sample-frames 5

# Higher quality video download
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" --quality 64
```

## Prerequisites

| Dependency | Purpose | Install |
|------------|---------|---------|
| **Python 3.8+** | Script runtime | System package |
| **ffmpeg** | Video/audio processing | `apt install ffmpeg` / `brew install ffmpeg` |
| **curl** | API calls & stream download | Usually pre-installed |
| **z-ai CLI** | VLM visual analysis & ASR transcription | `npm install -g z-ai-web-dev-sdk` |

> **Note:** `z-ai CLI` is the command-line tool from [z-ai-web-dev-sdk](https://www.npmjs.com/package/z-ai-web-dev-sdk). If you want to use a different VLM/ASR provider, you can modify the `analyze_frames()` and `transcribe_audio()` functions in the script.

## CLI Options

| Option | Default | Description |
|--------|---------|-------------|
| `url` | (required) | Bilibili video URL |
| `--output, -o` | stdout | Output JSON file path |
| `--work-dir` | temp dir | Working directory for temporary files |
| `--quality` | 16 | Video quality: 16=360p, 32=480p, 64=720p, 80=1080p |
| `--frame-interval` | 5 | Seconds between extracted frames |
| `--sample-frames` | all | Max number of frames to analyze with VLM |
| `--skip-download` | false | Skip stream download (metadata + subtitles only) |
| `--skip-visual` | false | Skip VLM frame analysis |
| `--skip-audio` | false | Skip ASR transcription |
| `--keep-temp` | false | Keep temporary files after processing |

## Output Format

```json
{
  "metadata": {
    "bvid": "BV1q2RhB9EQC",
    "aid": 116530733975077,
    "cid": 38148178055,
    "title": "视频标题",
    "author": "UP主名称",
    "author_mid": 123456,
    "duration_seconds": 101,
    "views": 19441,
    "likes": 409,
    "coins": 7,
    "favorites": 103,
    "shares": 37,
    "danmaku": 1,
    "description": "视频描述",
    "published_at": "2026-05-07 09:39:28"
  },
  "visual_analysis": {
    "frames_analyzed": 5,
    "frame_descriptions": [
      {
        "frame": "frame_001.jpg",
        "description": "画面描述..."
      }
    ]
  },
  "speech": {
    "source": "asr",
    "transcript": "完整语音转录文本..."
  },
  "parsed_at": "2026-05-13T09:30:00"
}
```

## How It Works — Stage by Stage

### Stage 1: Metadata

Calls Bilibili's public API (no auth required):

```
GET https://api.bilibili.com/x/web-interface/view?bvid={BV号}
```

Returns title, author, duration, stats, and the `cid` needed for subsequent stages.

### Stage 2: Subtitles

Checks for available subtitles:

```
GET https://api.bilibili.com/x/player/v2?bvid={BV号}&cid={cid}
```

If subtitles exist, downloads and parses them — no need for ASR in Stage 4b.

### Stage 3: Stream Download

B站 serves video and audio as separate m4s streams. This stage:

1. Gets stream URLs from the playurl API
2. Downloads both streams via CDN (requires `Referer: https://www.bilibili.com` header)
3. Merges them with ffmpeg into a single MP4

**Why not yt-dlp?** B站's anti-scraping returns HTTP 412 for yt-dlp. The API+CDN approach is more reliable.

### Stage 4a: Visual Analysis

1. Extracts key frames at configurable intervals via ffmpeg
2. Sends each frame to VLM for description
3. Parses VLM response to extract clean text descriptions

### Stage 4b: Audio Transcription

1. Extracts audio as 16kHz mono WAV
2. Splits into ≤25-second chunks (ASR has a 30-second limit)
3. Transcribes each chunk via ASR
4. Concatenates all transcripts

### Stage 5: Synthesis

Combines metadata, visual analysis, and speech transcript into a single structured JSON output.

## Adapting for Other AI Providers

The script uses `z-ai CLI` for VLM and ASR. To use other providers:

**VLM (Visual Analysis):** Modify the `analyze_frames()` function. Replace:
```bash
z-ai vision -p "..." -i "frame.jpg"
```
with your provider's image analysis API call.

**ASR (Speech Transcription):** Modify the `transcribe_audio()` function. Replace:
```bash
z-ai asr -f "chunk.wav" -o "transcript.json"
```
with your provider's speech-to-text API call. Note: if your ASR has no 30-second limit, you can skip the chunking step and transcribe the full audio at once.

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| yt-dlp returns 412 | B站 anti-scraping | Use this script's API+CDN approach |
| VLM rejects video file | VLM only accepts images | Frames are extracted automatically |
| ASR "时长限制0-30秒" | Audio too long | Audio is auto-split into 25s chunks |
| CDN download fails | Missing Referer header | Script adds it automatically |
| Stream URLs expired | CDN URLs are time-limited | Re-run the script |
| No subtitles | Video has no CC | Script falls back to ASR automatically |

## Limitations

- B站 API endpoints are **unofficial** — they may change without notice
- CDN stream URLs are **time-limited** — use immediately after fetching
- Very long videos (>10 min) will take significant time for full VLM+ASR analysis
- b23.tv short URLs are not yet supported (needs redirect resolution)
- Some videos may require login cookies for higher quality streams

## License

MIT
