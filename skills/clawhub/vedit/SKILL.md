---
name: vedit
description: Edit videos with a real timeline editor — cut, trim, speed up, add transitions, color, audio, subtitles and export — by driving vedit over MCP. Runs locally on FFmpeg.
version: 1.0.0
metadata:
  openclaw:
    emoji: "🎬"
    homepage: https://github.com/metiutek/editorvideo-ai
    requires:
      bins:
        - uv
    install:
      - kind: uv
        package: vedit-mcp
        bins: [vedit, vedit-mcp]
---

# vedit — video editing an agent can drive

[vedit](https://github.com/metiutek/editorvideo-ai) is an open-source timeline video editor
(tracks, clips, cuts, transitions, color, audio, subtitles). Every operation the buttons do is
also an MCP tool, so you can do the edit for the user while they watch it happen in the editor
and fix anything by hand. Rendering is local and deterministic (FFmpeg). MIT licensed.

## Use this skill when

- the user asks to cut, trim, merge, speed up or reorder video clips;
- they want silences removed, b-roll on the beat, titles or burned-in subtitles;
- they want a vertical (9:16) or square version of a video, or an export for YouTube / TikTok.

## Setup (once)

```bash
uv tool install vedit-mcp     # installs the `vedit` and `vedit-mcp` commands
vedit install-ffmpeg          # only if ffmpeg is not already on PATH
vedit doctor                  # says what is missing and how to fix it
```

Register the MCP server with your agent (stdio):

```json
{ "mcpServers": { "vedit": { "command": "vedit-mcp", "args": [] } } }
```

To let the user watch the edit live, start the editor with `vedit ui`
(opens <http://127.0.0.1:8760>).

## How to work

1. Create or open a project, then add the user's media files.
2. Make the edit with vedit's tools; after each step, check the timeline state before moving on.
3. Tell the user what you changed. Everything can be undone in the editor (Ctrl+Z).
4. Export only when the user is happy with the result.

Do not delete or overwrite the user's source files: vedit works on a project, the originals stay
untouched.

---

By [Mattia Cibin (Metiu)](https://metiu.xyz) · source: https://github.com/metiutek/editorvideo-ai
