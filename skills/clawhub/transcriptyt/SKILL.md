---
name: transcriptyt
description: Get the transcript of any public YouTube video (text, JSON with timestamps, SRT or VTT, 150+ languages), summarize a video, list a playlist or channel's videos, or search YouTube, using the TranscriptYT API. Use when the user shares a YouTube link or asks what a video says.
version: 1.0.0
homepage: https://transcript-yt.com
metadata:
  openclaw:
    requires:
      env:
        - TRANSCRIPTYT_API_KEY
      bins:
        - curl
    primaryEnv: TRANSCRIPTYT_API_KEY
    envVars:
      - name: TRANSCRIPTYT_API_KEY
        required: true
        description: API key (starts with ts_live_) from https://transcript-yt.com/dashboard/keys. New accounts include free credits.
---

# TranscriptYT: YouTube transcripts

All requests go to `https://transcript-yt.com` with the header `Authorization: Bearer $TRANSCRIPTYT_API_KEY`. `url` accepts a full YouTube URL or an 11-character video ID.

## Transcript (1 credit)

```bash
curl -s -G "https://transcript-yt.com/v1/transcript" \
  -H "Authorization: Bearer $TRANSCRIPTYT_API_KEY" \
  --data-urlencode "url=https://www.youtube.com/watch?v=VIDEO_ID" \
  --data-urlencode "format=text"
```

- `format`: `text` (plain), `md`, `json` (timestamped segments plus metadata), `srt`, `vtt`, `csv`. Use `text` or `md` when you only need to read it; `json` when timestamps matter.
- `language=de` picks a caption language; `translate_to=es` translates.
- `startTime` / `endTime` (seconds) return only part of a long video.
- Videos without captions are transcribed from audio on paid plans (1 credit per minute). On the Free plan they return `NO_CAPTIONS`.

## Summary (usually 2 credits)

```bash
curl -s -G "https://transcript-yt.com/v1/summary" -H "Authorization: Bearer $TRANSCRIPTYT_API_KEY" --data-urlencode "url=VIDEO_ID"
```

Returns a summary, key points and timestamped notes. Prefer this over a full transcript for long videos when the user only wants the gist.

## Other endpoints

- `GET /v1/languages?url=...`: caption tracks a video has. Free.
- `GET /v1/playlist?url=<playlist or channel>&limit=100`: video IDs, titles, durations.
- `GET /v1/search?q=<query>&limit=20` (optional `channel=@handle`, `upload_date=week`): search YouTube.
- `GET /v1/usage`: plan and remaining credits. Free.

## Errors

- `401`: missing or wrong key; ask the user to set `TRANSCRIPTYT_API_KEY`.
- `402`: out of credits; point the user to https://transcript-yt.com/#pricing.
- `404` with `NO_CAPTIONS`: the video has no captions and the account can't use AI transcription.

Docs: https://transcript-yt.com/docs
