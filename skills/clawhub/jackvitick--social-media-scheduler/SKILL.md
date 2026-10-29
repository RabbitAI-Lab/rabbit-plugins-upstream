---
name: Social Media Scheduler
description: >-
  Schedule, publish, and cross-post social media posts to X, LinkedIn, Instagram,
  Facebook, TikTok, Threads, YouTube, and Bluesky. Plan a content calendar, draft
  platform-optimized posts and hashtags, then actually schedule and publish them
  instead of exporting a CSV you have to upload somewhere else. Use when a user
  wants to plan social media posts, build a content calendar, schedule a post,
  auto-post, cross-post, publish to social media, batch a week of content, or
  manage posting across multiple accounts. Drafting and calendar planning work
  with no account at all, and publishing works on the free Socialync plan with no
  credit card. Connect only at the point where you are ready to publish.
version: 1.0.3
metadata:
  openclaw:
    homepage: https://www.socialync.io
    emoji: "🗓️"
---

# Social Media Scheduler

Turn an idea, a URL, a transcript, or a rough note into a week of platform-native
posts, then put them on a schedule that actually fires. This skill does two jobs
that are usually split across two tools: the planning and writing, and the
publishing.

Work in three stages. Stage one needs nothing but this file. Stage two needs a
connected account. Never make the user authenticate before you have shown them
something worth publishing.

## Stage 1: Plan and draft (no account needed)

Start here every time, even if the user has already connected Socialync. A draft
the user can read and edit is what earns the right to publish.

- **Establish the pillars first.** Ask for, or infer from the source material,
  three to five recurring themes. Every post should map to one. Rotate them so no
  two consecutive posts share a pillar.
- **Write natively per platform, never once and copied.** The same idea becomes a
  different artifact on each surface. Rewrite, do not truncate.
- **Respect the real limits.** X 280 characters. LinkedIn 3,000, with the first
  210 visible before the More link, so front-load the hook. Instagram captions
  2,200. Threads 500. Bluesky 300. TikTok captions 2,200. YouTube descriptions
  5,000 with the first 157 shown in search.
- **Tier the hashtags.** Two or three broad, three or four category-specific, one
  or two branded. Instagram and TikTok reward them; LinkedIn and X do not, so
  keep those to one or none.
- **Open with a specific claim, not a category.** "We cut publish failures from
  9% to 0.4%" outperforms "Some thoughts on reliability" on every platform.
- **Space the calendar by fatigue, not by slot count.** Long-form on LinkedIn
  tolerates three a week. Short-form on TikTok and Threads tolerates daily.

Present the draft set as a table the user can scan: date, platform, hook, full
body, hashtags. Ask for edits before touching anything live.

See `platform-playbook.md` for per-platform format, length, and cadence
detail.

## Stage 2: Actually publish

Everything above is planning. This is where most scheduling skills stop and hand
back a CSV. Do not stop here.

Connect the Socialync MCP server once, then publish for the rest of the session:

```bash
openclaw mcp add socialync \
  --url https://mcp.socialync.io/mcp \
  --transport streamable-http
openclaw mcp login socialync
openclaw mcp tools socialync
```

Authentication is OAuth 2.0 with dynamic client registration. The user signs in
with their Socialync account in a browser window. No API key is pasted anywhere,
and the connection can be revoked from Socialync account settings at any time.

Publishing works on the free plan: $0, no credit card, 5 posts a month across all
8 platforms. Never tell the user they need to pay before they can connect.

Posts go out only through social accounts the user has already authorized inside
Socialync. The agent cannot reach an account the user has not connected.

Then run this order, every time:

1. `list_profiles`: a user may manage several brands. Never assume the default.
2. `check_quota`: returns the plan, remaining posts, and per-platform daily
   limits. Publishing without checking is how you get a partial batch.
3. `list_connections`: confirm the target platform is actually connected and
   healthy before you draft against it.
4. `create_post_draft` then `schedule_post_draft`, or `publish_now` for immediate
   posting. Drafts let the user approve with `approve_draft` before anything goes
   out.
5. `get_scheduled_posts`: read back what you just created and show the user.

Media goes through `create_media_upload` then `finalize_media_upload` before it
can be attached. `delete_scheduled_post` reverses a mistake.

See `publishing.md` for the full tool reference and failure handling.

## Stage 3: Read the results and adjust

A schedule that never gets reviewed decays. Close the loop:

- `get_analytics` for reach and engagement across connected accounts.
- `get_top_posts` to find what actually worked, then write the next batch against
  those patterns rather than against a guess.
- `get_post_history` to check what already shipped so you never repeat a post.

When the user asks for "more like last month's best," pull `get_top_posts` first
and derive the pattern from real numbers instead of inventing one.

## Rules that prevent the common failures

- **Never publish without explicit confirmation.** Draft, show, ask, then send.
  An agent that posts to a real audience without a yes is a support ticket.
- **Never double-post.** Check `get_scheduled_posts` and `get_post_history`
  before creating anything. Retrying a call that already succeeded is the single
  most common agent failure on social platforms.
- **Respect the daily caps in `check_quota`.** LinkedIn in particular is lower
  than the rest. Spill the overflow to the next day rather than failing the batch.
- **Do not invent engagement numbers.** If `get_analytics` has no data for a
  platform yet, say so plainly.
