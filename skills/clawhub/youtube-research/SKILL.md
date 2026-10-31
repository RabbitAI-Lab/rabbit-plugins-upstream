---
name: youtube-research
description: Pulls structured YouTube data — video and channel details, transcripts/captions, comments, playlists, and search — via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping. Use when the user provides a YouTube URL or asks for a transcript, comments, channel/video metadata, or video search results.
---

# YouTube research

Resolve YouTube videos and channels, and pull transcripts, comments, playlists,
and search results as normalized JSON from the Crawlora API — no `yt-dlp`, no
browser, no scraping.

## When to use this skill

- The user pastes a YouTube URL and wants its transcript, summary, or stats.
- "Get the comments on this video" / "what are people saying?"
- "List this channel's recent videos / shorts / playlists."
- "Search YouTube for …" or "what videos exist about …".
- Building a transcript-based summary, sentiment, or research pipeline.
- Comparing a bounded set of videos with timestamped transcript evidence.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- Set `CRAWLORA_API_KEY` in the environment before running the helper.
- The helper reads `CRAWLORA_API_KEY` from the environment and sends requests to `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Resolve the id.** A YouTube watch URL `https://www.youtube.com/watch?v=<ID>`
   (or `https://youtu.be/<ID>`) gives the **video id**; channel URLs give a
   **channel id**. Extract the id before calling.
2. **Transcript:** `/youtube/transcript/{id}` (use
   `/youtube/transcript/{id}/languages` first if you need a specific language).
3. **Metadata / comments:** `/youtube/video/{id}`, `/youtube/comments/{id}`.
4. **Channel:** `/youtube/channel/{id}/videos`, `/channel/{id}/shorts`,
   `/channel/{id}/playlists`, `/youtube/profile/{id}`.
5. **Discovery:** `/youtube/search?q=...` to find videos by keyword.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Transcript-backed topic research

For a topic brief, search first, deduplicate by video ID, and choose a bounded
sample that reflects the requested date, language, and video types. Discover
available transcript languages before fetching captions. Request JSON with
timestamps for evidence extraction; tie each theme or claim to the actual
caption segment and video URL. A caption or translation may mishear speech and
does not independently verify factual claims. Report unavailable transcripts
and keep search rank, view counts, and comment samples separate from demand.

For a wider map of topic and format coverage across videos or channels, use
youtube-content-gap-analysis when installed.

~~~sh
scripts/crawlora.sh /youtube/search q="home energy storage" type=video sort_by=relevance
scripts/crawlora.sh /youtube/transcript/dQw4w9WgXcQ/languages
scripts/crawlora.sh /youtube/transcript/dQw4w9WgXcQ format=json timestamps=true
~~~

## Calling the API

```sh
# Transcript for a video id (GET):
scripts/crawlora.sh /youtube/transcript/dQw4w9WgXcQ | jq '.'

# Video metadata + comments:
scripts/crawlora.sh /youtube/video/dQw4w9WgXcQ | jq '.data'
scripts/crawlora.sh /youtube/comments/dQw4w9WgXcQ | jq '.data'

# Search:
scripts/crawlora.sh /youtube/search q="web scraping tutorial" | jq '.'
```

Use `scripts/crawlora.sh` for all requests; it keeps the API key out of command-line arguments.


## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every YouTube endpoint
this skill uses (method, path, params, description).

## Examples

- **Summarize a video:** extract the id from the URL → `/youtube/transcript/{id}`
  → concatenate transcript segments → summarize.
- **Comment sentiment:** `/youtube/comments/{id}` → bucket comments by sentiment
  and surface common themes.
- **Channel digest:** `/youtube/channel/{id}/videos` → list recent uploads with
  view counts and publish dates.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public YouTube pages; respect YouTube's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- Not every video has captions; check `/youtube/transcript/{id}/languages` when a
  transcript request returns empty.
