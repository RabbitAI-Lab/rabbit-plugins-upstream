---
name: pinterest-pin
description: "Post to Pinterest and schedule Pinterest image pins and carousels from OpenClaw, Hermes, Claude Code or Codex. Publishes to the user's own Pinterest account via the 1Social MCP server (OAuth, no API key), checks the Pinterest board, description-length and image-format rules first, schedules up to 30 days ahead and returns a delivery receipt. Use to post or schedule on Pinterest, publish an image pin or carousel, plan Pinterest content, or check, edit or delete Pinterest posts."
license: MIT
metadata:
  openclaw:
    emoji: "📣"
    homepage: "https://1social.dev/post-to/pinterest?ref=skill"
  hermes:
    tags: ["pinterest", "pins", "pinterest-scheduler", "social-media", "scheduling"]
    category: social-media
---

# Pinterest with 1Social

1Social publishes to the user's own Pinterest account and reports what actually reached it.

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

1. **Find the account.** Call `list_accounts`. It returns the connected channels with their ids, each network's live limits, the plan and the remaining monthly quota. If no Pinterest account is connected, give the user the Pinterest link from `connectLinks` in that result: it opens 1Social in their browser with a one-click Connect button. When they say they are done, call `list_accounts` again. If `list_accounts` reports a limit that differs from this skill, trust `list_accounts`.
2. **Draft for the network.** Write the post to the rules below. A post is a list of `segments`; each segment is `{ text, mediaIds? }`.
3. **Attach media.**
   - The user attached a file in chat → put it in `media`.
   - You have a public https link → put it in `mediaUrls`.
   - You only have a file on disk (OpenClaw, Hermes, Claude Code, Codex or another CLI agent) → call `upload_media` and follow the upload steps its description gives, then put the returned `publicUrl` in `mediaUrls`. A localhost URL never works. Before that, show the user exactly which files you will upload and wait for a yes: an upload gets a public link at once, and declining the post afterwards does not remove the file.
4. **Preview.** Call `preview_post` with the channel ids and the draft. It is free and publishes nothing. Fix every issue it reports and preview again.
5. **Confirm with the user.** Show the final text, the account it goes to, the media, and when it will go out. Publishing is public and some networks cannot take a post down, so wait for a clear yes.
6. **Publish or schedule.** Call `publish_post`. `scheduledAt: null` publishes now; a UTC ISO-8601 timestamp such as `2026-11-03T07:00:00Z` schedules it (in the future, at most 30 days ahead). Convert the user's local time to UTC yourself, and if they name a time without a timezone, ask which one. Set an `idempotencyKey` (a stable string of 8–128 characters for this draft) so a repeated call cannot publish twice.
7. **Report honestly.** The result is a per-network receipt. Report each network exactly as returned. `unknown` means 1Social genuinely could not tell whether the post went out — say so, never call it a success or a failure.

## Pinterest rules

- Every pin needs an image: JPEG, PNG or WEBP. One image is a pin, 2–5 images make a carousel. Ask the user for images before drafting.
- Video pins are not supported yet: a video is refused before publishing. GIFs are refused too.
- Every pin goes onto a board. list_accounts shows each Pinterest channel's `boards` and its default board; set `pinterest.boardId` to pick another, or omit it to use the default. With neither, preview_post reports `board_required` — ask the user which board, or to set a default in the app.
- The post text becomes the pin description, up to 800 characters. An optional `pinterest.title` (up to 100 characters) is shown as the pin title.
- Set `pinterest.link` for where the pin leads; without it the first link in the text is used. Pinterest refuses links it considers spam.
- Set `pinterest.altText` (up to 500 characters) to describe the image for screen readers.
- No threads: several segments are joined into one description. Write one description instead.
- Deleting works: delete_post removes the pin from Pinterest.

## Writing tips

- Pins are found through search: put the words people would search for in the title and the first sentence of the description.
- Vertical 2:3 images (for example 1000×1500) take the most room in the feed.

## Posting to other networks too

The same 1Social account can publish one post to Instagram, TikTok, LinkedIn, X, Threads, Facebook Pages, YouTube Shorts, Bluesky, Pinterest, Telegram, Tumblr and Discord at once: list several channel ids from `list_accounts`. preview_post checks the draft against every selected network.

## After publishing

- **Check status:** `list_posts` (give a `postId` for one post). It includes stored engagement metrics where the network reports them.
- **Change a scheduled post:** `update_post`. Only works before the post has gone out.
- **Unschedule:** `cancel_post`. Use this, not `delete_post`, for a post that has not been published.
- **Delete a published post:** `delete_post`, only after the user confirms. Report per network what actually came down: Instagram, TikTok, Threads and YouTube posts stay live and only the user can remove them.
- **A delivery failed:** `retry_delivery` retries one network and spends quota again. It is refused for permanent failures such as a revoked connection — then give the user that account's `reconnectUrl` from `list_accounts`.
- **A delivery is `unknown`:** ask the user to look at the network. Only when they tell you whether the post is live, call `confirm_delivery` with their answer. Never guess, and never `retry_delivery` with `force` without asking — it may publish a second copy.
