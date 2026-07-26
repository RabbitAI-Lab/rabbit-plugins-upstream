---
name: social-media-scheduler
description: Schedule and publish social media posts to Facebook, Instagram, Threads, LinkedIn, LinkedIn Pages, X/Twitter, TikTok, Pinterest, and YouTube through WoopSocial's remote MCP server. A social media scheduler, auto-publisher, cross-poster, and content-calendar tool for AI agents. Use whenever the user wants to post, schedule, queue, cross-post, bulk-schedule, draft, or auto-publish social content — "post this," "schedule for 9am," "publish this reel to Instagram and TikTok," "fan this out to all platforms," or "build my content calendar."
homepage: https://woopsocial.com

---

# WoopSocial

Docs: [https://docs.woopsocial.com](https://docs.woopsocial.com)

## Prerequisites

To use this skill, you must have a WoopSocial account. Sign up for one [here](https://woopsocial.com/).

## MCP Setup

Ensure that OpenClaw is connected to the WoopSocial remote MCP server. There are two methods to do this: 

### Method 1: OAuth

```sh
openclaw mcp add woopsocial \
  --url https://api.woopsocial.com/mcp \
  --transport streamable-http \
  --auth oauth

openclaw mcp login woopsocial
openclaw mcp doctor woopsocial --probe
```

If OAuth prints an authorization URL but cannot receive its localhost callback, approve access in the browser and pass the returned code directly to the CLI:

```sh
openclaw mcp login woopsocial --code <code>
```

Use `openclaw mcp probe woopsocial --json` to inspect exposed tools when troubleshooting.

### Method 2: API key in MCP URL

As an alternative to OAuth, API-key based authentication is also possible. Generate an API key in the [WoopSocial dashboard API page](https://app.woopsocial.com/api-access). Then you can add the generated MCP URL to OpenClaw like this:

```sh
openclaw mcp add woopsocial \
  --url https://api.woopsocial.com/mcp?api_key=YOUR_API_KEY \
  --transport streamable-http
```

## Posting Workflow

1. Use `projects_list` to identify the project.
2. Use `social_accounts_list` to resolve the requested accounts. Only accounts with `status: CONNECTED` can publish, and **all accounts for one post must belong to the same project**. If a requested platform isn't connected, say so plainly, never skip it silently.

3. Use `social_accounts_get_platform_inputs` when a platform requires current account-specific options, such as a Pinterest board or TikTok privacy setting.
4. Reuse existing media returned by `media_list` when appropriate. For new media, use the `media_uploads_*` session tools, upload every returned part exactly as instructed, complete the session, and wait until the media is ready.
5. Build the post request from the user's content, accounts, platform-specific fields, and schedule.
6. Call `posts_create` only after the target accounts, content, and schedule are unambiguous.
7. Return the post ID and requested schedule. For delivery results, use `posts_get` or `social_account_posts_list` and distinguish pending, scheduled, published, and failed states.

## Action Boundaries

Treat an explicit request to publish or schedule as authorization for that action. Ask before creating the post only when its target accounts, content, schedule, or publish-versus-draft intent is ambiguous.

Require explicit user intent before calling delete tools for posts, account posts, projects, social accounts, media, or webhooks.

Never claim that a post was published merely because creation succeeded. Report the delivery state returned by WoopSocial.
