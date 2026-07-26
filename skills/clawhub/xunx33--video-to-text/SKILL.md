---
name: video-to-text
description: "从视频链接下载视频，并将口播文案转录为文字。依赖 yt-dlp 和 openai-whisper，全部开源免费本地部署。"
user-invocable: true
---

# Video Transcribe

Extract text from video links (Douyin, Bilibili, YouTube, Kuaishou, etc.) with timestamps.

## Dependencies

```bash
pip install yt-dlp openai-whisper
winget install ffmpeg  # Windows
# brew install ffmpeg  # macOS
# sudo apt install ffmpeg  # Linux
```

## First-time Setup

### Model cache directory (recommended: non-system drive)

Whisper large-v3 model is ~2.9GB. Set cache to a non-system drive:

```bash
# Windows PowerShell (permanent, User-level):
[Environment]::SetEnvironmentVariable("WHISPER_DOWNLOAD_ROOT", "X:\whisper_cache", "User")

# macOS/Linux (~/.zshrc or ~/.bashrc):
export WHISPER_DOWNLOAD_ROOT="~/whisper_cache"
```

### Video download directory (optional)

```bash
# Windows PowerShell:
[Environment]::SetEnvironmentVariable("VIDEO_DOWNLOAD_DIR", "X:\video_downloads", "User")

# macOS/Linux:
export VIDEO_DOWNLOAD_DIR="~/video_downloads"
```

### yt-dlp global config (optional)

```bash
# Windows: Create %APPDATA%\yt-dlp\config (one line):
-o X:\video_downloads\%(title)s.%(ext)s

# macOS/Linux: Create ~/.config/yt-dlp/config (one line):
-o ~/video_downloads/%(title)s.%(ext)s
```

## Usage

### Agent call

```bash
python transcribe.py "<video_url>" [model] [prompt]
```

- `model`: `large-v3` (default, best quality) or `turbo` (faster)
- `prompt`: optional context hint for better recognition

### Manual use

```bash
python transcribe.py "<video_url>"
```

## Output

- **Segmented text**: with timestamps for editing
  ```
  [0.0s-8.0s] Text here...
  [8.0s-20.0s] More text...
  ```
- **Full text**: plain text for copying
- **Video file**: saved to download directory

## Supported Platforms

yt-dlp supports 1000+ sites: Douyin, TikTok, Bilibili, YouTube, Kuaishou, Weibo, Xiaohongshu, Xigua Video, etc.

## Notes

- CPU-only, no GPU required
- large-v3: ~77s per minute of video on CPU
- Chinese text optimized with punctuation
- Models stored in `WHISPER_DOWNLOAD_ROOT` directory
- If env vars not set, defaults to script directory
