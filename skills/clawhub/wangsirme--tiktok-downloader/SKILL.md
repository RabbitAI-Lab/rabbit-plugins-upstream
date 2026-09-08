---
name: tiktok-downloader
description: Download TikTok videos without watermark and extract MP3 audio via the free TikTok Download API (tk.seekubo.com). Give it any TikTok URL (www.tiktok.com, vm.tiktok.com, vt.tiktok.com, m.tiktok.com) and it resolves video metadata plus direct, browser-fetchable CDN download links. No API key or subscription required.
version: 2.0.0
metadata:
  openclaw:
    requires:
      bins: [curl]
    emoji: 📹
    homepage: https://tk.seekubo.com
---

# TikTok Downloader (No Watermark)

Resolve any public TikTok video URL into metadata and direct download links:
no-watermark MP4 in multiple quality tiers, or MP3 audio-only. The API is
free and public — no API key, no account, no subscription.

## When to use

The user shares a TikTok link (`www.tiktok.com/@user/video/{id}`,
`vm.tiktok.com/{code}`, `vt.tiktok.com/{code}`, `m.tiktok.com/v/{id}.html`)
and wants to download the video — typically without the watermark — or extract
its audio. Short links are resolved automatically server-side.

## Parse a URL

```bash
curl -s -X POST "https://tk.seekubo.com/api/v2/parse" \
  -H "Content-Type: application/json" \
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
    "thumbnail": "/api/v2/image?e=1788262278&s=...&u=...",
    "duration": 14,
    "filename": "tiktok_6718335390845095173",
    "stats": { "plays": "1.2M", "likes": "340K" },
    "downloads": [
      { "type": "no_watermark_hd", "quality": "1080p · 3.2 MB", "ext": "mp4", "size": "3.2 MB", "url": "https://cdn.../video.mp4" },
      { "type": "no_watermark", "quality": "720p · 1.9 MB", "ext": "mp4", "size": "1.9 MB", "url": "https://cdn.../video.mp4" },
      { "type": "mp3", "quality": "128kbps", "ext": "mp3", "url": "https://cdn.../audio.mp3" }
    ]
  }
}
```

`downloads[]` may contain several quality tiers of the same type. Pick the
best entry — prefer the highest-quality `no_watermark_hd` > `no_watermark` >
`watermark`; use `mp3` when the user wants audio only. The `quality` string
(e.g. `"1080p · 3.2 MB"`) is the quickest way to compare tiers.

Failure:

```json
{ "success": false, "error": { "code": "VIDEO_PRIVATE", "message": "This video is private and can’t be downloaded." } }
```

### Thumbnail note

`data.thumbnail` is often a **relative path** to a signed, expiring proxy
(`/api/v2/image?e=<unix-expiry>&s=<sig>&u=<b64url>`). To show or fetch it,
prepend the base URL:

```bash
curl -L -o cover.jpg "https://tk.seekubo.com${thumbnail}"
```

It stops working after the `e=` expiry — download it in the same session.

## Download the file

Fetch the chosen `downloads[].url` directly. CDN links need no headers or
cookies:

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
| `RATE_LIMITED`     | Fair-use burst limit hit (20 requests/min per IP) — wait ~30–60 s and retry. |
| `UPSTREAM_ERROR`   | TikTok-side failure — retry once after ~30 s.                            |
| `INTERNAL_ERROR`   | Unexpected server error — retry once.                                    |

## Notes

- One request per video: metadata and all download links come back together.
- Repeated parses of the same video within ~60 s return the same buffered
  result without hitting TikTok again.
- The service is rate limited to 20 requests/min per IP — parse one video at
  a time, don't batch-loop URLs.
