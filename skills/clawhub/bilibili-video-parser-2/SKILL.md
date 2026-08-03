---
name: bilibili-video-parser
description: Parse and analyze Bilibili (哔哩哔哩) video content from a URL. Use this skill whenever the user shares a Bilibili video link (bilibili.com/video/BV... or b23.tv/...) and wants to understand its content, extract key information, transcribe speech, or analyze visual frames. Also use when the user asks to "watch", "analyze", "read", "understand", or "extract" content from a B站/bilibili video. This skill handles the full pipeline: metadata extraction via Bilibili public API, video/audio stream download, key frame extraction, VLM visual analysis, and ASR speech transcription.
license: MIT
---

# Bilibili Video Parser Skill

Parse and analyze Bilibili video content through a multi-stage pipeline: metadata → stream download → frame extraction + audio extraction → VLM analysis + ASR transcription → synthesized output.

## Skill Location

`{project_path}/skills/bilibili-video-parser`

## Prerequisites

- **ffmpeg** — must be installed and available in PATH (for video/audio processing)
- **curl** — for downloading streams and calling APIs
- **z-ai CLI** — for VLM (visual analysis) and ASR (speech transcription)
- **Python 3** — for JSON parsing and orchestration

## Quick Start

The simplest way to use this skill is to run the bundled script:

```bash
python3 {Skill Location}/scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC"
```

This runs the full pipeline and outputs a structured JSON result. See `scripts/bilibili_parser.py` for details.

## Pipeline Overview

```
Bilibili URL
    │
    ├─ Stage 1: Metadata ──→ Title, UP主, Duration, Views, etc.
    │
    ├─ Stage 2: Subtitles ──→ (If available, skip Stage 3-5 for speech)
    │
    ├─ Stage 3: Stream Download ──→ video.m4s + audio.m4s → merged.mp4
    │
    ├─ Stage 4a: Frame Extraction ──→ key frames → VLM analysis
    │
    ├─ Stage 4b: Audio Extraction ──→ WAV chunks → ASR transcription
    │
    └─ Stage 5: Synthesis ──→ Metadata + Visual + Audio → Final output
```

## Stage 1: Extract Video Metadata

Use Bilibili's public API. No authentication required.

### Get video info from BV number

```bash
curl -s "https://api.bilibili.com/x/web-interface/view?bvid=BV1q2RhB9EQC" \
  -H "User-Agent: Mozilla/5.0" | python3 -c "
import json, sys
from datetime import datetime
data = json.load(sys.stdin)
if data.get('code') == 0:
    info = data['data']
    print('标题:', info.get('title'))
    print('UP主:', info.get('owner', {}).get('name'))
    print('时长:', info.get('duration'), '秒')
    print('播放量:', info.get('stat', {}).get('view'))
    print('点赞:', info.get('stat', {}).get('like'))
    print('投币:', info.get('stat', {}).get('coin'))
    print('收藏:', info.get('stat', {}).get('favorite'))
    print('描述:', info.get('desc'))
    print('CID:', info.get('cid'))
    pubdate = datetime.fromtimestamp(info.get('pubdate', 0))
    print('发布时间:', pubdate.strftime('%Y-%m-%d %H:%M:%S'))
else:
    print('API错误:', data)
"
```

**Key fields:**
- `data.title` — Video title
- `data.owner.name` — UP主 name
- `data.duration` — Duration in seconds
- `data.cid` — Required for stream URL and subtitles
- `data.stat.view` — View count
- `data.stat.like` — Likes

**URL parsing:** Extract BV number from various URL formats:
- `https://www.bilibili.com/video/BV1q2RhB9EQC`
- `https://www.bilibili.com/video/BV1q2RhB9EQC?t=4.6`
- `https://b23.tv/xxxxx` (short URL, needs redirect resolution)

## Stage 2: Check for Subtitles

Bilibili videos may have community or auto-generated subtitles. If available, this is the fastest way to get speech content — no need for ASR.

```bash
curl -s "https://api.bilibili.com/x/player/v2?bvid=BV1q2RhB9EQC&cid=<CID>" \
  -H "User-Agent: Mozilla/5.0" | python3 -c "
import json, sys
data = json.load(sys.stdin)
subtitle = data.get('data', {}).get('subtitle', {})
subtitles = subtitle.get('subtitles', [])
if subtitles:
    for s in subtitles:
        print(f'Language: {s.get(\"lan_doc\")}, URL: {s.get(\"subtitle_url\")}')
else:
    print('No subtitles available')
"
```

If subtitles exist, download the subtitle URL (prepend `https:` if it starts with `//`) and parse the JSON. Each entry has `from`, `to` (timestamps) and `content` (text).

**If subtitles are available, you can skip Stages 4b (audio extraction + ASR) for speech content.**

## Stage 3: Download Video Stream

B站 videos have separate audio and video streams (m4s format). You need to download both and merge them.

### Step 3a: Get stream URLs

```bash
curl -s "https://api.bilibili.com/x/player/playurl?bvid=BV1q2RhB9EQC&cid=<CID>&qn=16&fnver=0&fnval=16&fourk=0" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Referer: https://www.bilibili.com" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if data.get('code') == 0:
    d = data['data']
    videos = d.get('dash', {}).get('video', [])
    audios = d.get('dash', {}).get('audio', [])
    if videos:
        print('VIDEO_URL:', videos[0].get('baseUrl', videos[0].get('base_url', '')))
    if audios:
        print('AUDIO_URL:', audios[0].get('baseUrl', audios[0].get('base_url', '')))
"
```

**Quality parameter `qn`:**
- `16` — 360p (smallest, fastest download)
- `32` — 480p
- `64` — 720p
- `80` — 1080p

Use `qn=16` for analysis purposes — smaller file, faster processing.

### Step 3b: Download streams

```bash
# Download video stream
curl -L -o video.m4s "$VIDEO_URL" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Referer: https://www.bilibili.com"

# Download audio stream
curl -L -o audio.m4s "$AUDIO_URL" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Referer: https://www.bilibili.com"
```

**Critical:** The `Referer: https://www.bilibili.com` header is required. Without it, CDN requests will be rejected.

### Step 3c: Merge video and audio

```bash
ffmpeg -i video.m4s -i audio.m4s -c copy output.mp4 -y
```

## Stage 4a: Visual Analysis (Key Frames + VLM)

VLM cannot process video files directly. Extract key frames as images, then analyze each frame.

### Extract frames at regular intervals

```bash
# One frame every 5 seconds (adjust fps for density)
ffmpeg -i output.mp4 -vf "fps=1/5" -q:v 2 frames/frame_%03d.jpg -y
```

**Frame rate guidance:**
- `fps=1/5` — 1 frame per 5 seconds (good for talks/presentations)
- `fps=1/2` — 1 frame per 2 seconds (for fast-cut videos)
- `fps=1` — 1 frame per second (for detailed analysis)

### Analyze frames with VLM

```bash
z-ai vision -p "请用中文描述这张图片的内容，包括人物、场景、屏幕上的文字等所有细节" -i frames/frame_001.jpg
```

**Optimization tips:**
- Don't analyze every frame — sample strategically (first, middle, last, plus any scene changes)
- For long videos, analyze 5-10 representative frames rather than all frames
- Ask specific questions about what you're looking for rather than generic descriptions

## Stage 4b: Audio Transcription (ASR)

### Step 4b-1: Extract audio from video

```bash
ffmpeg -i output.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav -y
```

Parameters: 16kHz sample rate, mono channel, 16-bit PCM — the format ASR expects.

### Step 4b-2: Split audio into ≤25-second chunks

The ASR API has a 30-second limit. Split into 25-second segments to be safe.

```bash
ffmpeg -i audio.wav -f segment -segment_time 25 -c copy audio_chunk_%03d.wav -y
```

### Step 4b-3: Transcribe each chunk

```bash
for chunk in audio_chunk_*.wav; do
  z-ai asr -f "$chunk" -o "transcript_$(basename $chunk .wav).json"
done
```

### Step 4b-4: Combine transcripts

```python
import json, glob

full_text = ""
for f in sorted(glob.glob("transcript_*.json")):
    with open(f) as fh:
        data = json.load(fh)
        text = data.get("text", "")
        full_text += text + " "

print(full_text.strip())
```

## Stage 5: Synthesize Results

Combine all extracted information into a structured output:

```json
{
  "metadata": {
    "title": "...",
    "author": "...",
    "duration_seconds": 101,
    "views": 19441,
    "likes": 409,
    "published_at": "2026-05-07 09:39:28"
  },
  "visual_analysis": {
    "scenes": ["..."],
    "people": ["..."],
    "on_screen_text": ["..."],
    "key_frames_analyzed": 5
  },
  "speech_transcript": "Full transcribed text...",
  "summary": "Synthesized summary combining visual and audio content..."
}
```

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| yt-dlp returns 412 | B站 anti-scraping | Use the API+CDN approach in Stage 3 instead |
| VLM rejects video file | VLM only accepts images | Extract frames first (Stage 4a) |
| ASR returns "时长限制0-30秒" | Audio too long | Split into 25-second chunks (Stage 4b-2) |
| CDN download fails | Missing Referer header | Add `-H "Referer: https://www.bilibili.com"` |
| playurl API returns error | Missing or invalid CID | Get CID from Stage 1 API first |
| No subtitles available | Video has no CC | Fall back to ASR (Stage 4b) |
| Stream URLs expired | CDN URLs are time-limited | Re-fetch from playurl API |

## Important Notes

- B站 API endpoints are **unofficial public APIs** — they may change without notice
- CDN stream URLs are **time-limited** — use them immediately after fetching
- The `Referer` header is **mandatory** for CDN downloads
- Video and audio streams are **always separate** (m4s format) — they must be merged
- For very long videos (>10 min), consider analyzing only specific time segments rather than the full video
- Respect B站's terms of service — this is for content analysis, not mass scraping

## Cleanup

After analysis, clean up temporary files:

```bash
rm -f video.m4s audio.m4s audio.wav output.mp4
rm -rf frames/
rm -f audio_chunk_*.wav transcript_*.json
```
