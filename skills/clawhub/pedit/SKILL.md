---
name: pedit
description: Edit photos with a real layered editor — layers, masks, blend modes, adjustments, background removal, generative fill and upscaling — by driving pedit over MCP. Local, or with your own API key.
version: 1.0.0
metadata:
  openclaw:
    emoji: "🖼️"
    homepage: https://github.com/metiutek/editorimage-ai
    requires:
      bins:
        - uv
    install:
      - kind: uv
        package: pedit-mcp[ai]
        bins: [pedit, pedit-mcp]
    envVars:
      - name: OPENAI_API_KEY
        required: false
        description: Optional, for generative edits with OpenAI models.
      - name: GEMINI_API_KEY
        required: false
        description: Optional, for generative edits with Gemini.
      - name: STABILITY_API_KEY
        required: false
        description: Optional, for Stability AI models.
      - name: OPENROUTER_API_KEY
        required: false
        description: Optional, for models via OpenRouter.
      - name: REPLICATE_API_TOKEN
        required: false
        description: Optional, for models on Replicate.
---

# pedit — photo editing an agent can drive

[pedit](https://github.com/metiutek/editorimage-ai) is an open-source layered image editor
(a Photoshop / GIMP alternative): layers, groups, masks, clipping masks, blend modes, adjustment
layers, clone stamp and healing, plus generative fill and expand, image-to-image, text-to-image,
background removal and upscaling. Every operation is also an MCP tool. MIT licensed.

## Use this skill when

- the user asks to remove or replace a background, retouch, recolor or crop a photo;
- they want something added, removed or extended in an image ("extend the sky", "remove the person");
- they need a thumbnail, cover or social image built from layers.

## Setup (once)

```bash
uv tool install "pedit-mcp[ai]"
pedit doctor                  # says what is missing and how to fix it
```

Register the MCP server with your agent (stdio):

```json
{ "mcpServers": { "pedit": { "command": "pedit-mcp" } } }
```

To let the user watch, start the editor with `pedit ui` (<http://127.0.0.1:8770>); the running
editor is itself an MCP server at `http://127.0.0.1:8770/mcp/`.

Generative features run locally (e.g. through a local ComfyUI) or with an API key the user
provides. Never ask the user to paste keys into chat; they can set them in pedit's *AI models*
panel or as environment variables.

## How to work

1. Open the user's image as a project; keep edits non-destructive (new layers, masks).
2. After each step, check the result before the next one.
3. Export only when the user confirms. The original file is never overwritten unless they ask.

---

By [Mattia Cibin (Metiu)](https://metiu.xyz) · source: https://github.com/metiutek/editorimage-ai
