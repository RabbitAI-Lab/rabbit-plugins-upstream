---
name: video-downloader-enhanced
description: Download videos and extract original post captions, audio transcripts, and metadata from video platform links. Use when the user provides Douyin, Bilibili, WeChat Channels, Xiaohongshu, or YouTube links and asks to save the original video, capture the post text/caption, transcribe the spoken in-video script/copy, archive source material, or prepare video material for downstream analysis or skill creation. Douyin is implemented with an H5 primary route and yt-dlp fallback; Bilibili, YouTube, and Xiaohongshu are implemented through yt-dlp; WeChat Channels is not implemented yet and should currently be handled via the WeChat mini program kg百宝箱.
---

# Video Downloader

## Overview

Use this skill to turn a video-platform URL into a local source-material folder containing the video file, `post_caption.txt`, `audio.wav` / `audio.m4a` / `audio.mp3`, `transcript.txt`, `transcript.srt` (whisper.cpp only), and `metadata.json`.

Terminology:

- `post_caption.txt`: platform publish text, title, description, and hashtags.
- `transcript.txt`: spoken in-video script generated from audio ASR.
- `metadata.json`: normalized platform metadata plus download and ASR status.

## Output Folder Naming

Each download creates a folder with a human-readable name:

```
YY_MM_DD_标题摘要_平台_作者
```

Example: `26_07_27_AI做PPT零基础终极教程_抖音_木子不写代码`

Rules:
- **Date** — video publish date preferred, falls back to download date. Format: `YY_MM_DD`.
- **标题摘要** — title trimmed to ≤40 characters; newlines, hashtags (`#`), mentions (`@`), emoji removed.
- **平台** — Chinese display name: `抖音` / `B站` / `YouTube` / `小红书`.
- **作者** — falls back to `未知作者` when unavailable.
- **Dedup** — if the folder already exists, appends the last 5 characters of the video ID.
- Internal file names (`post_caption.txt`, `metadata.json`, etc.) are **not** affected.

The current implemented providers are Douyin, Bilibili, YouTube, and Xiaohongshu. WeChat Channels is an explicit extension point; do not claim that provider works until its provider module has been implemented and tested. For WeChat Channels links, tell the user to first use the WeChat mini program `kg百宝箱` to download the video from the 视频号 link, then continue with local ASR or downstream processing on the downloaded file.

## Quick Start

Run the bundled CLI from this skill directory:

```bash
python3 scripts/download_video.py "https://v.douyin.com/..." --output-dir ./downloads
```

For metadata/post-caption extraction without downloading the video:

```bash
python3 scripts/download_video.py "https://v.douyin.com/..." --output-dir ./downloads --metadata-only
```

For download without ASR:

```bash
python3 scripts/download_video.py "https://v.douyin.com/..." --output-dir ./downloads --asr none
```

For Chinese speech with local whisper.cpp (recommended):

```bash
python3 scripts/download_video.py "https://v.douyin.com/..." --output-dir ./downloads --asr whisper_cpp --asr-language Chinese
```

For Chinese speech with cloud ASR:

```bash
SILICONFLOW_API_KEY="..." python3 scripts/download_video.py "https://v.douyin.com/..." --output-dir ./downloads --asr siliconflow --asr-language Chinese
```

To bias ASR toward domain terms or a specific script:

```bash
python3 scripts/download_video.py "https://v.douyin.com/..." --output-dir ./downloads --asr-language Chinese --asr-prompt "请使用简体中文转写。关键词：丧尸清道夫、Shotlab、Midjourney、GPT Image、AI生图。"
```

## Workflow

1. Identify the platform from the URL.
2. Use `scripts/download_video.py` as the single entrypoint.
3. Inspect the output folder and report:
   - video path, when downloaded
   - post caption path
   - audio path
   - transcript path
   - SRT path (whisper.cpp and openai-whisper)
   - metadata path
   - platform, item ID, author, duration, resolution, and any provider caveats

## ASR Transcript

After a video is downloaded, the CLI extracts audio with `ffmpeg` and transcribes it. Four backends are available, selected via `--asr`.

### Backend Options

| Backend | Description |
|---------|-------------|
| `auto` (default) | Auto-detect: whisper.cpp > openai-whisper > SiliconFlow |
| `whisper_cpp` | Local whisper.cpp (`whisper-cli`), fastest on Apple Silicon |
| `whisper` | Local openai-whisper Python CLI |
| `siliconflow` | Cloud API via SiliconFlow SenseVoiceSmall |
| `none` | Skip audio extraction and transcription entirely |

### `--asr auto` Priority

When `--asr auto` (the default) is used, the backend is selected in this order:

1. **whisper.cpp** — if `WHISPER_CPP_BIN` points to an executable file, or `whisper-cli` is available on PATH, and `WHISPER_CPP_MODEL` points to an existing model file.
2. **openai-whisper** — if the `whisper` CLI is available on PATH.
3. **SiliconFlow** — if `SILICONFLOW_API_KEY` is set in the environment.
4. If none of the above are available, an error is returned. **No software is auto-installed.**

### whisper.cpp (`--asr whisper_cpp`)

The recommended local backend for best performance on Apple Silicon.

Environment variables:

- `WHISPER_CPP_BIN` — optional explicit path to `whisper-cli`; when unset, search PATH
- `WHISPER_CPP_MODEL` — required path to a local GGML model file

```bash
export WHISPER_CPP_BIN="/path/to/whisper-cli"
export WHISPER_CPP_MODEL="/path/to/ggml-large-v3-turbo.bin"
```

Do not assume a platform-specific default path. No software is installed automatically.

Output artifacts:
- `audio.wav` (16 kHz PCM)
- `transcript.txt`
- `transcript.srt` (subtitles with timestamps)
- `transcript.whisper_cpp.json` (metadata)

The model is always the file path, not a model name — `--asr-model` is ignored for whisper_cpp.

### openai-whisper (`--asr whisper`)

Output artifacts:
- `audio.m4a`
- `transcript.txt`
- `transcript.srt`
- `transcript.whisper.json`

### SiliconFlow (`--asr siliconflow`)

Requires `SILICONFLOW_API_KEY`. Calls `https://api.siliconflow.cn/v1/audio/transcriptions`.

Output artifacts:
- `audio.mp3`
- `transcript.txt`
- `transcript.siliconflow.json`

SiliconFlow does not currently provide an SRT file; `srt_path` is returned as `null`.

### Result Contract

Every ASR result includes `status`, `backend`, `model`, `language`, `audio_path`,
`transcript_path`, `srt_path`, `raw_json_path`, and `error`. A selected backend
that fails returns `status: failed`; `auto` does not silently retry another
backend after transcription has started.

### Common Options

- `--asr-language` — Language for transcription, e.g. `Chinese`, `zh`, `English`, `auto`. Default: `auto`.
- `--asr-model` — Model name. Default: `auto` (whisper.cpp ignores this; openai-whisper defaults to `base`; SiliconFlow maps to `FunAudioLLM/SenseVoiceSmall`).
- `--asr-prompt` — Initial prompt passed to the ASR engine. Use it to request Simplified Chinese output and provide domain terms.
- `--asr-max-seconds` — Debug limit: transcribe only the first N seconds of audio.

## Douyin Provider

The Douyin provider uses the H5 share page as the primary route. It follows the share URL, parses the server-rendered `window._ROUTER_DATA`, extracts the original post text and video resource ID, then downloads through the non-`playwm` endpoint.

If the H5 route fails, or if metadata extraction succeeds but direct media download fails, use `yt-dlp` as a fallback. The fallback first tries a normal `yt-dlp` download, then retries with Chrome cookies.

Important behavior:

- Prefer the non-watermark `aweme/v1/play/` endpoint over the share-page `playwm` endpoint.
- Treat `yt-dlp` as a backup route, not the primary Douyin route.
- Store the original Douyin publish text in `post_caption.txt`.
- Store raw and normalized metadata in `metadata.json`.
- Use `--metadata-only` for fast tests or when the user only needs copy/caption.
- Use `--no-yt-dlp-fallback` only when debugging the H5 route itself.

## Bilibili Provider

The Bilibili provider uses `yt-dlp` as the primary route for both metadata extraction and media download.

Important behavior:

- Support `bilibili.com` and `b23.tv` links.
- Store the Bilibili title plus description in `post_caption.txt`.
- Store `yt-dlp` raw metadata and normalized fields in `metadata.json`.
- Download with `bv*+ba/b` and merge to mp4 when possible.
- Retry with Chrome cookies when anonymous metadata extraction or download fails.
- Use `--metadata-only` for fast tests or when the user only needs title/description metadata.

## YouTube Provider

The YouTube provider uses `yt-dlp` as the primary route for both metadata extraction and media download.

Important behavior:

- Support `youtube.com` and `youtu.be` links.
- Store the YouTube title plus description in `post_caption.txt`.
- Store `yt-dlp` raw metadata and normalized fields in `metadata.json`.
- Download with `bv*+ba/b` and merge to mp4 when possible.
- Use local Node as the yt-dlp JavaScript runtime when available.
- Retry with `--remote-components ejs:github` or Chrome cookies when the basic route fails.
- Use `--metadata-only` for fast tests or when the user only needs title/description metadata.

## Xiaohongshu Provider

The Xiaohongshu provider uses a three-tier download fallback:

1. **Anonymous yt-dlp** — public download without any authentication (no cookies).
2. **Public direct URL** — if metadata is available but anonymous yt-dlp can't download, extracts the highest-quality video stream URL from yt-dlp's formats metadata and downloads it via plain HTTP.
3. **Chrome cookies yt-dlp** — last resort; requires local Chrome browser access.

Metadata extraction is always anonymous — cookies are never triggered just to get author info or metadata.

Important behavior:

- Support `xiaohongshu.com`, `xhslink.com`, and `xhslink.cn` links.
- Store the Xiaohongshu title plus note body in `post_caption.txt`.
- Store `yt-dlp` raw metadata and normalized fields in `metadata.json`.
- Author nickname is taken from anonymous metadata; falls back to `未知作者` when unavailable.
- **Remote assistant**: if both public routes fail, reports "需要在电脑端授权 Chrome Cookie" immediately instead of hanging.
- **Safety**: no `cookies.txt` is saved; cookie contents are never logged or included in output.
- `metadata.json` records `download.method`, `download.cookie_used`, `download.direct_url_source`, and `download.fallback_errors` for full traceability.
- Use `--metadata-only` for fast tests or when the user only needs title/note metadata.

## WeChat Channels Provider

WeChat Channels is recognized but not implemented yet.

Current finding:

- `yt-dlp` does not support the tested `weixin.qq.com/sph/...` share link.
- The public web page can expose text, cover image, and QR-code flow, but did not expose a playable video URL in the tested case.
- Do not claim that this skill can directly download WeChat Channels videos until a provider has been implemented and tested.

Temporary workflow:

- Ask the user to open WeChat and search for the mini program `kg百宝箱`.
- In `kg百宝箱`, paste the 视频号 video link and download the video there.
- After the user has the downloaded video file locally, this skill can still be used for local ASR/transcript work if the file is passed through the ASR helper or a future local-file entrypoint.

## Provider Extension Contract

Add new platforms by creating a module under `scripts/providers/` and registering it in `scripts/providers/__init__.py`.

Each provider should expose:

- `PLATFORM`: stable provider name
- `supports(url: str) -> bool`
- `fetch(url: str, output_root: Path, *, metadata_only: bool = False, **options) -> dict`

Output folders should include the same artifact contract whenever possible:

- `metadata.json`
- `post_caption.txt`
- `audio.wav` / `audio.m4a` / `audio.mp3` and `transcript.txt` when ASR is enabled
- `transcript.srt` when whisper.cpp ASR is enabled
- video file when download is enabled

Reserved providers:

- `wechat_channels`

When a reserved provider is detected but not implemented, say so plainly and do not fabricate a download result.

## Safety

Download only material the user owns, has permission to download, or can lawfully archive for their intended use. Do not bypass DRM, paid access controls, private permissions, or platform restrictions for unauthorized redistribution.
