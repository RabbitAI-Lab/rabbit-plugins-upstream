---
name: batchedits-video-editor
description: Autonomously edit videos, add captions, and remove silences via BatchEdits.
metadata:
  openclaw:
    primaryEnv: BATCHEDITS_API_KEY
    requirements:
    mcp:
      - batchedits
---

Turn your OpenClaw into an autonomous video editor using BatchEdits. Use when you need to add captions, remove silences, or apply custom styles to videos. Covers creating styles, uploading local videos, processing, and checking video status directly from WhatsApp, Telegram, or the CLI.

## Setup
1. Create an account at your BatchEdits instance.
2. Choose one connection method.

### Option A: Easiest — API key in URL
```bash
openclaw config set mcp.servers.batchedits '{"type": "sse", "url": "https://batchedits.com/api/mcp/PASTE_YOUR_API_KEY_HERE"}'
```

### Option B: Header-based
```bash
export BATCHEDITS_API_KEY="PASTE_YOUR_API_KEY_HERE"
openclaw config set mcp.servers.batchedits '{"type": "sse", "url": "https://batchedits.com/api/mcp"}'
```

### Option C: OAuth DCR (Dynamic Client Registration)
```bash
CLIENT_RESPONSE=$(curl -sS -X POST https://batchedits.com/api/oauth/register \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"OpenClaw Local","redirect_uris":["http://localhost/callback"]}')
CLIENT_ID=$(echo "$CLIENT_RESPONSE" | jq -r '.client_id')
CLIENT_SECRET=$(echo "$CLIENT_RESPONSE" | jq -r '.client_secret')

AUTH_URL="https://batchedits.com/api/oauth/authorize?client_id=$CLIENT_ID&redirect_uri=http://localhost/callback&response_type=code"
echo "Open this URL and approve:"
echo "$AUTH_URL"

# After approval, copy the ?code=... value:
CODE="PASTE_CODE_HERE"
TOKEN_RESPONSE=$(curl -sS -X POST https://batchedits.com/api/oauth/token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=authorization_code&code=$CODE&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&redirect_uri=http://localhost/callback")
ACCESS_TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.access_token')
export BATCHEDITS_ACCESS_TOKEN="$ACCESS_TOKEN"
openclaw config set mcp.servers.batchedits '{"type": "sse", "url": "https://batchedits.com/api/mcp"}'
```

## Tools
- `list_actions`
- `create_style`
- `get_styles`
- `upload_videos`
- `process_video`
- `list_videos`
- `download_video`

## Recommended Workflow for Video Editing
1. Identify the local video file provided by the user.
2. Determine the requested edits.
3. Connect using one of the setup options above.
4. Check `get_styles` to see if a matching style already exists. If not, use `list_actions` and `create_style` to make one.
5. Call `upload_videos` to get the upload command.
6. Execute the upload command and extract the `videoId`.
7. Call `process_video` with `videoId` and `styleId`.
8. Call `list_videos` to check when the video reaches `completed` status.
9. Optionally call `download_video` to get the result.

## Tips
- Always check `get_styles` first. Reusing existing styles is faster than creating a new one every time.
- Uploading videos is handled via `curl` because OpenClaw needs to stream large local binaries to the remote server efficiently.
- You can queue multiple videos to the same style or apply different styles for bulk processing.
