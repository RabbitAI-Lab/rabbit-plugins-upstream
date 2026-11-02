---
name: hookpost
description: Draft, schedule and list social media posts on the channels a user connected in Hookpost, using the hookpost CLI. Use when the user asks to post, schedule, queue or draft something for X, LinkedIn, Threads, Facebook Pages, Discord, Slack or another channel they connected in Hookpost, to see what is scheduled, or to find the next free posting slot.
homepage: https://hookpost.hookstep.in/mcp
metadata:
  {
    "openclaw":
      {
        "emoji": "🪝",
        "requires": { "bins": ["hookpost"], "env": ["HOOKPOST_API_KEY"] },
        "primaryEnv": "HOOKPOST_API_KEY",
        "install":
          [
            {
              "id": "node",
              "kind": "node",
              "package": "hookpost",
              "bins": ["hookpost"],
              "label": "Install the Hookpost CLI (npm)",
            },
          ],
      },
  }
---

# Hookpost

Hookpost is a hosted social media scheduler. This skill drives it through the `hookpost` CLI (npm package `hookpost`, Node.js 18 or later). Every command acts on the user's own Hookpost workspace, identified by the API key in `HOOKPOST_API_KEY`.

## Before the first command

- The user needs a Hookpost workspace on Standard or Pro (both include the API and CLI, and each starts with a 3-day trial) with at least one connected channel. Channels are connected in the Hookpost web app at https://hookpost.hookstep.in, not from the CLI.
- The API key is under Settings > Developers in Hookpost. Never print, echo or log it, and never write it into a file the user did not ask for.
- Check access with `hookpost channels`. Avoid `hookpost auth status` in shared output: it prints the first characters of the key.

## Commands

| Task | Command |
|---|---|
| List channels and their ids | `hookpost channels` |
| Posts in the next N days (default 7) | `hookpost posts --days 14` |
| Save a draft | `hookpost post "text" --channel <id> --draft` |
| Schedule for an exact time | `hookpost post "text" --channel <id> --at 2026-11-03T03:30:00Z` |
| Schedule into the next free slot | `hookpost post "text" --channel <id>` (no `--at`) |
| Publish now | `hookpost post "text" --channel <id> --now` |
| Same post on several channels | `--channel a,b,c`, or repeat `--channel` |
| Network-specific settings | `--settings '<json>'` (one channel per command when used) |
| Next free slot of a channel | `hookpost slot <channelId>` |
| Delete a post | `hookpost delete <postId>` |

## How to work

1. Run `hookpost channels` first and map the user's words ("my LinkedIn") to channel ids. If two channels could match, ask which one.
2. Default to drafts. Use `--draft` unless the user clearly asked to schedule or publish. Before `--now` or a scheduled post, show the exact text, the channel names and the time (in the user's timezone and in UTC), and wait for a yes.
3. Pass `--at` in UTC with a trailing `Z`. Convert from the user's timezone yourself and say the conversion back to them.
4. Write each post for its network: keep it within that network's character limit and adapt tone and hashtags per channel instead of pasting one text everywhere. The limits per network are listed at https://hookpost.hookstep.in/guides/post-to-multiple-social-media-at-once. If Hookpost rejects a post, the error says why; fix the text or settings and try again.
5. The CLI posts text only. For images or video, tell the user to add media in the Hookpost app, or use the Hookpost MCP server, which can import media from a public URL.
6. After creating a post, report its id, state and time, and say it is visible in the Hookpost calendar.
7. There is no edit command. To change a post's text or time, tell the user to edit it in the Hookpost app.
8. Delete only when the user asks to delete a specific post. `hookpost delete` removes the whole post group, including its copies on the other channels, so show the text and channels first and get a yes.

## When something fails

- "Not signed in" or 401: the key is missing, wrong or was rotated. Ask the user to copy a fresh key from Settings > Developers.
- A message about the trial or plan: the workspace has to start its trial or choose a plan at https://hookpost.hookstep.in/billing.
- 429: the hourly limit on creating posts was reached. Wait and try later; do not loop.
- A post in state ERROR in `hookpost posts`: the network refused it at publish time. The reason is shown on the post in the Hookpost calendar.

## MCP alternative

If the agent supports MCP, the hosted server at `https://hookpost.hookstep.in/api/mcp` (header `Authorization: Bearer <key>`) adds per-network rules, media import from a URL and settings updates on queued posts. Setup for each client: https://hookpost.hookstep.in/mcp
