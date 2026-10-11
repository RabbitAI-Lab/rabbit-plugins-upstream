---
name: "video-understanding"
description: "Watch and analyze video URLs or files using Gemini native agentic video understanding for summaries, timestamped answers, transcripts, and visual reconstruction."
metadata:
  openclaw:
    emoji: "🎬"
    requires:
      bins: ["uv"]
    primaryEnv: "GEMINI_API_KEY"
    install:
      - id: "uv-brew"
        kind: "brew"
        formula: "uv"
        bins: ["uv"]
        label: "Install uv (brew)"
      - id: "yt-dlp-brew"
        kind: "brew"
        formula: "yt-dlp"
        bins: ["yt-dlp"]
        label: "Install yt-dlp (brew)"
      - id: "ffmpeg-brew"
        kind: "brew"
        formula: "ffmpeg"
        bins: ["ffmpeg"]
        label: "Install ffmpeg (brew)"
---

# Video Understanding

Analyze video URLs or files, including casual requests to watch or react. All cloud analysis uses Gemini 3.7 Flash and native `processing: agentic`. No static fallback.

## Procedure

1. Identify the video, requested output, sensitivity, and intended audience. Before sending any video or prompt to Google Gemini, confirm the user authorized that cloud processing. A generic “watch this” request alone is not permission to upload private/local material. Use `--allow-cloud` only to record actual authorization, never to bypass asking. Public-video analysis explicitly requested through this Gemini skill is authorized.
2. Check `uv` and the configured Gemini credential path. Download workflows also require `yt-dlp` and `ffmpeg` (macOS: `brew install yt-dlp ffmpeg`). Never put credentials or signed URLs in commands, chat, or logs. For authentication, destinations, and retention, read [references/privacy.md](references/privacy.md).
3. Inspect `scripts/analyze_video.py --help`. Default output is a summary/visual overview; `--question` requests a focused answer and timestamped evidence. `--mode full` requests a transcript and full visual coverage, not guaranteed completeness.
4. Run the smallest sufficient analysis. Local videos upload to Gemini, YouTube URLs go directly to Gemini, and other credential-free HTTPS videos download first. Confirm a valid result or explicit failure.
5. Check timestamps, visible text, speaker attribution, chronology, and critical claims against evidence. Mark uncertainty and distinguish observation from inference. Return only the requested material to the intended audience; transcripts can contain sensitive information.
6. Retain uploads only when authorized using `--reuse-file-cache`. A `--session-key` identifies reuse but does not save chat history. Add `--save-history --continue-chat` only with authorization to retain questions/outputs locally; YouTube follow-ups resubmit the URL.
7. Use `--purge-cache` with the same source/session to delete retained remote handles and local history. Cleanup failures return nonzero and preserve minimal handles for retry; confirm deletion rather than assuming it.

## Commands

After cloud authorization:

```bash
uv run <skill_dir>/scripts/analyze_video.py "<video-url-or-path>" --allow-cloud
uv run <skill_dir>/scripts/analyze_video.py "<video-url-or-path>" --allow-cloud --question "What product is shown?"
uv run <skill_dir>/scripts/analyze_video.py "<video-url-or-path>" --allow-cloud --mode full
uv run <skill_dir>/scripts/analyze_video.py "<video-url-or-path>" --allow-cloud --session-key "<stable-key>" --reuse-file-cache --save-history --continue-chat --question "What happens after that screen?"
uv run <skill_dir>/scripts/analyze_video.py "<video-url-or-path>" --session-key "<stable-key>" --purge-cache
```

## Gotchas and boundaries

- `--prompt` replaces built-in evidence instructions, ignores `--mode`, and bypasses `--continue-chat` context. Include required evidence and uncertainty instructions yourself; it cannot accompany `--question`.
- Supported models: `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash-lite`. Optional `--fallback-model` stays agentic and applies only to transient errors. Missing access is a blocker, not permission to switch providers.
- SDK is pinned and resolved by `uv`. `--use-context-cache` is rejected; legacy `--cache-ttl-seconds` does not control File API expiry. Purge supports legacy CachedContent.
- No history is saved by default. `--output` deliberately writes analysis to a mode-0600 file; stdout may be captured by the caller. Do not post private transcripts to a shared channel merely because processing was authorized.
- Diagnostics omit source URLs/paths and raw provider/downloader errors. Usage, model, processing mode, and elapsed time go to stderr. Timestamps and duration are model estimates, not frame-exact measurements.
- Any HTTP(S) video source supported by yt-dlp is eligible; there is no domain whitelist. Normal query parameters are supported. Use only sources the user authorized. This local downloader is not an SSRF isolation boundary: deployments accepting untrusted jobs must enforce network egress policy outside the skill, including redirects and extractor/CDN requests.
- Never put signed URLs or credentials into commands; use an authorized local file instead. The downloader ignores ambient configuration.
