---
name: tiktok-downloader
description: Download TikTok videos without watermark and extract MP3 audio via the TikTok Video Downloader API on RapidAPI. Give it any TikTok URL (www.tiktok.com, vm.tiktok.com, vt.tiktok.com, m.tiktok.com) and it resolves video metadata plus direct, browser-fetchable CDN download links. Requires a RapidAPI subscription key.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env: [RAPIDAPI_KEY]
      bins: [curl]
    primaryEnv: RAPIDAPI_KEY
    envVars:
      - name: RAPIDAPI_KEY
        required: true
        description: RapidAPI key from subscribing at https://rapidapi.com/fwelljson/api/tiktok-video-download-no-watermark2 (free tier available)
    emoji: 📹
    homepage: https://rapidapi.com/fwelljson/api/tiktok-video-download-no-watermark2
---

# TikTok Downloader (No Watermark)

Resolve any public TikTok video URL into metadata and direct download links:
no-watermark MP4 (HD/SD tiers), watermarked MP4, or MP3 audio-only.

## When to use

The user shares a TikTok link (`www.tiktok.com/@user/video/{id}`,
`vm.tiktok.com/{code}`, `vt.tiktok.com/{code}`, `m.tiktok.com/v/{id}.html`)
and wants to download the video — typically without the watermark — or extract
its audio. Short links are resolved automatically server-side.

## Setup (once)

1. Subscribe at
   <https://rapidapi.com/fwelljson/api/tiktok-video-download-no-watermark2>
   (free BASIC plan: 10 requests/month; paid plans for more).
2. Copy your key from the RapidAPI dashboard and export it:

```bash
export RAPIDAPI_KEY="your-rapidapi-key"
```

## Parse a URL

```bash
curl -s -X POST "https://tiktok-video-download-no-watermark2.p.rapidapi.com/api/v2/parse" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: tiktok-video-download-no-watermark2.p.rapidapi.com" \
  -d '{"url":"https://www.tiktok.com/@scout2015/video/6718335390845095173"}'
```

Every response is HTTP 200 — branch on the body `success` field, never on the
HTTP status code.

Success:

```json
{
  "success": true,
  "data": {
    "id": "6718335390845095173",
    "title": "Cat does a backflip",
    "author": "scout2015",
    "author_name": "Scout",
    "thumbnail": "https://.../cover.jpeg",
    "duration": 14,
    "filename": "tiktok_6718335390845095173",
    "stats": { "plays": "1.2M", "likes": "340K" },
    "downloads": [
      { "type": "no_watermark_hd", "quality": "HD", "ext": "mp4", "size": "8.1 MB", "url": "https://cdn.../video.mp4" },
      { "type": "no_watermark", "quality": "SD", "ext": "mp4", "size": "2.4 MB", "url": "https://cdn.../video.mp4" },
      { "type": "mp3", "quality": "128kbps", "ext": "mp3", "url": "https://cdn.../audio.mp3" }
    ]
  }
}
```

Failure:

```json
{ "success": false, "error": { "code": "VIDEO_PRIVATE", "message": "This video is private and can’t be downloaded." } }
```

## Download the file

Pick the best entry from `downloads[]` — prefer `no_watermark_hd` >
`no_watermark` > `watermark`; use `mp3` when the user wants audio only — then
fetch it directly. CDN links need no headers or cookies:

```bash
curl -L -o "tiktok_6718335390845095173.mp4" "https://cdn.../video.mp4"
```

Suggested filename is `data.filename` + `.` + `ext`. Download promptly — CDN
links have a limited lifetime.

## Error codes

| code               | meaning / action                                                        |
| ------------------ | ----------------------------------------------------------------------- |
| `INVALID_URL`      | Not a TikTok URL — check the link.                                      |
| `VIDEO_NOT_FOUND`  | Deleted or nonexistent video.                                            |
| `VIDEO_PRIVATE`    | Private / age-restricted; cannot be downloaded.                          |
| `UNSUPPORTED_MEDIA`| Resolved but not a downloadable video (e.g. a photo post).               |
| `RATE_LIMITED`     | Plan quota or burst limit hit — wait (see `Retry-After` header), or suggest upgrading the RapidAPI plan. |
| `UPSTREAM_ERROR`   | TikTok-side failure — retry once after ~30 s.                            |
| `INTERNAL_ERROR`   | Unexpected server error — retry once.                                    |

## Notes

- One request per video: metadata and all download links come back together.
- Quotas are enforced by RapidAPI per subscription plan (BASIC free 10/month,
  PRO 10,000/month, ULTRA unlimited).
- Never log, echo, or embed the `RAPIDAPI_KEY` value anywhere.
