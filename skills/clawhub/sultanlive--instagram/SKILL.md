---
name: instagram-post
description: "Post to Instagram and schedule Instagram posts, Reels and carousels from OpenClaw, Hermes, Claude Code or Codex. Publishes to the user's own Instagram account via the 1Social MCP server (OAuth, no API key), checks the Instagram caption, hashtag, aspect-ratio and media rules first, schedules up to 30 days ahead and returns a delivery receipt. Use to post or schedule on Instagram, publish a photo, Reel or carousel, plan Instagram content, or check, edit or delete Instagram posts."
license: MIT
metadata:
  openclaw:
    emoji: "📣"
    homepage: "https://1social.dev/post-to/instagram?ref=skill"
  hermes:
    tags: ["instagram", "instagram-scheduler", "reels", "social-media", "scheduling"]
    category: social-media
---

# Instagram with 1Social

1Social publishes to the user's own Instagram account and reports what actually reached it.

## Setup (once)

These steps drive the 1Social MCP server. If tools such as `list_accounts` are not available, connect it first. Sign-in is OAuth in the browser; there is no API key to store. Ask the user before running these commands — the login step opens a page where they sign in to 1Social themselves.

- **OpenClaw:** `openclaw mcp set 1social '{"url":"https://mcp.1social.dev/mcp","transport":"streamable-http","auth":"oauth"}'`, then `openclaw mcp login 1social`. Check with `openclaw mcp doctor 1social --probe`.
- **Hermes:** add to `~/.hermes/config.yaml`:
  ```yaml
  mcp_servers:
    1social:
      url: "https://mcp.1social.dev/mcp"
      auth: oauth
  ```
  then `hermes mcp login 1social` (on a headless host: `hermes mcp login 1social --flow device`).
- **Claude Code:** `claude mcp add --transport http 1social https://mcp.1social.dev/mcp`
- **Any other client:** https://1social.dev/mcp lists the setup for each one.

The user needs a 1Social account. New accounts start with a free trial; publishing after it needs a paid plan (https://1social.dev/pricing).

## Workflow

1. **Find the account.** Call `list_accounts`. It returns the connected channels with their ids, each network's live limits, the plan and the remaining monthly quota. If no Instagram account is connected, tell the user to connect one at https://1social.dev/app — connecting needs a browser and cannot be done from chat. If `list_accounts` reports a limit that differs from this skill, trust `list_accounts`.
2. **Draft for the network.** Write the post to the rules below. A post is a list of `segments`; each segment is `{ text, mediaIds? }`.
3. **Attach media.**
   - The user attached a file in chat → put it in `media`.
   - You have a public https link → put it in `mediaUrls`.
   - You only have a file on disk (OpenClaw, Hermes, Claude Code, Codex or another CLI agent) → call `upload_media` and follow the upload steps its description gives, then put the returned `publicUrl` in `mediaUrls`. A localhost URL never works. Before that, show the user exactly which files you will upload and wait for a yes: an upload gets a public link at once, and declining the post afterwards does not remove the file.
4. **Preview.** Call `preview_post` with the channel ids and the draft. It is free and publishes nothing. Fix every issue it reports and preview again.
5. **Confirm with the user.** Show the final text, the account it goes to, the media, and when it will go out. Publishing is public and some networks cannot take a post down, so wait for a clear yes.
6. **Publish or schedule.** Call `publish_post`. `scheduledAt: null` publishes now; a UTC ISO-8601 timestamp such as `2026-11-03T07:00:00Z` schedules it (in the future, at most 30 days ahead). Convert the user's local time to UTC yourself, and if they name a time without a timezone, ask which one. Set an `idempotencyKey` (a stable string of 8–128 characters for this draft) so a repeated call cannot publish twice.
7. **Report honestly.** The result is a per-network receipt. Report each network exactly as returned. `unknown` means 1Social genuinely could not tell whether the post went out — say so, never call it a success or a failure.

## Instagram rules

- Every post needs an image or a video. A caption on its own is rejected — ask the user for media before drafting.
- Caption limit: 2,200 characters. Up to 30 hashtags; 3–5 relevant ones usually do better than a wall of tags.
- Image aspect ratio must be between 4:5 (portrait) and 1.91:1 (landscape). Square 1:1 is safe. Wide banners are rejected by Instagram with an "aspect ratio" error.
- PNG and JPEG both work.
- No threads: if the draft has several segments, 1Social joins them into one caption. Write one caption instead.
- Links in captions are not clickable on Instagram. If the user wants traffic, suggest "link in bio" wording instead of a raw URL.
- A published Instagram post cannot be deleted through 1Social — Instagram has no delete API for it. Make sure the user is happy with the caption before publishing.

## Writing tips

- Lead with a hook in the first 125 characters — that is what shows before "more".
- Put hashtags at the end of the caption, after a line break.

## Posting to other networks too

The same 1Social account can publish one post to Instagram, TikTok, LinkedIn, X, Threads, Facebook Pages, YouTube Shorts and Bluesky at once: list several channel ids from `list_accounts`. preview_post checks the draft against every selected network.

## After publishing

- **Check status:** `list_posts` (give a `postId` for one post). It includes stored engagement metrics where the network reports them.
- **Change a scheduled post:** `update_post`. Only works before the post has gone out.
- **Unschedule:** `cancel_post`. Use this, not `delete_post`, for a post that has not been published.
- **Delete a published post:** `delete_post`, only after the user confirms. Report per network what actually came down: Instagram, TikTok, Threads and YouTube posts stay live and only the user can remove them.
- **A delivery failed:** `retry_delivery` retries one network and spends quota again. It is refused for permanent failures such as a revoked connection — then the user must reconnect at https://1social.dev/app.
- **A delivery is `unknown`:** ask the user to look at the network. Only when they tell you whether the post is live, call `confirm_delivery` with their answer. Never guess, and never `retry_delivery` with `force` without asking — it may publish a second copy.
