# TikTok Video Search by Gecho

Search TikTok videos by keyword through the official Gecho Bridge MCP workflow.

## Features

- Search videos for an exact keyword or phrase.
- Return titles, creators, engagement metrics, and links.
- Save raw result data to a local directory when requested.

## Requirements

- An agent that supports Skills and MCP.
- Node.js 18 or later, with `npx` available.
- The Gecho Bridge MCP service configured in the agent.

## Use

Ask the agent to search TikTok for a keyword, for example:

> Search TikTok for portable blender and show the most liked videos.

The agent calls `tiktok_search` with the required `query` parameter. The optional `save_dir` parameter specifies an absolute directory for the raw JSON result.

## Permissions and data configuration

The Skill package contains no credentials or account data. Runtime services and configuration are managed by the MCP host. No API key, cookie, or token is embedded in the package.

## Results

The response includes the searched keyword, result count when available, video titles, creators, engagement metrics, URLs, and the local saved-file path when available.
