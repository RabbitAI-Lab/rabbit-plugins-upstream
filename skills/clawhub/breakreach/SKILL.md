---
name: breakreach
description: Schedule and publish social media posts across 12 platforms (X, Instagram, TikTok, LinkedIn, Bluesky, Reddit, Telegram…) via the Breakreach API — with best-time slots, media hosting and unified analytics.
metadata:
  openclaw:
    requires:
      env:
        - BREAKREACH_API_KEY
---

# Breakreach — social media on autopilot

Breakreach (https://www.breakreach.com) connects social accounts to AI agents. This skill lets you create, schedule and publish posts, and read analytics, through the REST API.

## Setup

1. Create an account at https://www.breakreach.com and connect social accounts (Settings → Accounts).
2. Create an API key in Settings → API & MCP (requires a Pro or Agency plan).
3. Export it: `BREAKREACH_API_KEY=br_...`

All requests: `Authorization: Bearer $BREAKREACH_API_KEY`, base URL `https://api.breakreach.com/v1`.

## Endpoints

List connected accounts (get account ids for posting):
```bash
curl -s https://api.breakreach.com/v1/accounts -H "Authorization: Bearer $BREAKREACH_API_KEY"
```

Next free posting slot (from the user's configured schedule):
```bash
curl -s https://api.breakreach.com/v1/next-slot -H "Authorization: Bearer $BREAKREACH_API_KEY"
```

Create a post — schedule at the next free slot:
```bash
curl -s -X POST https://api.breakreach.com/v1/posts \
  -H "Authorization: Bearer $BREAKREACH_API_KEY" -H "Content-Type: application/json" \
  -d '{"content":"Post text here","accountIds":["<id-from-/accounts>"],"useNextSlot":true}'
```
Other options: `"scheduledAt":"2026-08-30T11:00:00"` (workspace timezone), `"publishNow":true`, `"media":["https://..."]` (public URLs — REQUIRED for Instagram, TikTok, YouTube, Pinterest), `"pinterestBoardId"`, `"redditSubreddit"`, `"tiktokSettings":{"privacyLevel":"SELF_ONLY"}`.

Host media permanently before scheduling (returns a stable URL):
```bash
curl -s -X POST https://api.breakreach.com/v1/media \
  -H "Authorization: Bearer $BREAKREACH_API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/image.jpg"}'
```

List posts / delete a post / analytics:
```bash
curl -s "https://api.breakreach.com/v1/posts?status=scheduled" -H "Authorization: Bearer $BREAKREACH_API_KEY"
curl -s -X DELETE https://api.breakreach.com/v1/posts/<postId> -H "Authorization: Bearer $BREAKREACH_API_KEY"
curl -s https://api.breakreach.com/v1/analytics -H "Authorization: Bearer $BREAKREACH_API_KEY"
```

## Workflow tips

- Always call `/accounts` first and use the returned ids in `accountIds`.
- Prefer `useNextSlot: true` over guessing times — it respects the user's posting schedule and skips taken slots.
- Keep X posts under 280 characters. The first line of a Reddit post becomes its title.
- Errors are JSON `{"error": "..."}` with proper HTTP codes; 402 means the plan doesn't include API access.

Docs: https://github.com/samuelrondot/breakreach-mcp · Support: https://www.breakreach.com/support
