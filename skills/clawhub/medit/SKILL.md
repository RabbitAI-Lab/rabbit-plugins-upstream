---
name: medit
description: Write and produce music in a real DAW — chords, beats, bass, melodies, lyrics and vocals, then mix and master — by driving medit over MCP. Free and local.
version: 1.0.0
metadata:
  openclaw:
    emoji: "🎹"
    homepage: https://github.com/metiutek/editormusic-ai
    requires:
      bins:
        - uv
    install:
      - kind: uv
        package: medit-mcp
        bins: [medit, medit-mcp]
---

# medit — music production an agent can drive

[medit](https://github.com/metiutek/editormusic-ai) is an open-source DAW with built-in synths,
drum kits and 31 effects. Every operation is an MCP tool, so you can write the song for the user
— chords, beats, bass lines, melodies, lyrics and vocals — then mix and master it, while they
can open it in the DAW and change anything by hand. MIT licensed, runs locally.

## Use this skill when

- the user asks for a beat, a song, a chord progression or a melody in a given style or key;
- they want an existing track mixed, mastered or exported (mixdown or stems);
- they want to import audio or MIDI and build on it.

## Setup (once)

```bash
uv tool install medit-mcp
medit doctor                  # says what is missing and how to fix it
```

Register the MCP server with your agent (stdio):

```json
{ "mcpServers": { "medit": { "command": "uvx", "args": ["medit-mcp"] } } }
```

To work on the song open in the user's browser, start `medit ui` (<http://127.0.0.1:8780>) and
use the live endpoint `http://127.0.0.1:8780/mcp/` instead.

## How to work

1. Agree on style, tempo and key with the user, then build the arrangement track by track.
2. Listen-check by rendering short previews before mixing.
3. Mix and master at the end; export only when the user is happy.

---

By [Mattia Cibin (Metiu)](https://metiu.xyz) · source: https://github.com/metiutek/editormusic-ai
