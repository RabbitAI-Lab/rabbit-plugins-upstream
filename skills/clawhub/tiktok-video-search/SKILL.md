---
name: tiktok-video-search
version: 1.1.35
description: Search TikTok videos by keyword with the official Gecho Bridge MCP tool and return video metadata, creators, engagement metrics, and links.
author: Gecho AI
metadata:
  openclaw:
    os: ["darwin", "linux", "win32"]
    requires:
      bins: ["node", "npx"]
  hermes:
    tags: [tiktok, video-search, search, gecho, mcp]
    category: social-media
    os: [darwin, linux, windows]
---

# TikTok Video Search

Use the official Gecho Bridge MCP tool `tiktok_search` to search TikTok videos for a keyword or phrase.

## Tool

### `tiktok_search`

Parameters:

- `query` string, required: the keyword or phrase to search.
- `save_dir` string, optional: an absolute directory for saving the raw result JSON. Pass a directory, not a JSON filename.

## Workflow

1. Pass the user's keyword or phrase to `tiktok_search`.
2. When results are returned, summarize the top 3 to 5 videos with title, creator, engagement metrics, and URL.
3. Include the saved file path when the tool returns one.
4. If no results are returned, report that the query had no results.
5. If the tool reports an error, report the error without fabricating results.

## Runtime

The Skill provides the instruction layer for the Gecho Bridge MCP tool. Runtime services and their configuration are managed by the MCP host. The Skill package contains no credentials or account data.
