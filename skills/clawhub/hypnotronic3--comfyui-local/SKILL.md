---
name: comfyui-local
description: "Generate images using a local ComfyUI instance with hardcoded server address and allowlisted workflows. Secure by design — no arbitrary file reads, no arbitrary server connections, no shell injection. Requires a running ComfyUI server on the local network."
metadata:
  {
    "openclaw":
      {
        "emoji": "🎨",
        "requires": { "env": ["COMFYUI_SERVER_ADDRESS"] },
      },
  }
---

# ComfyUI Local — Secure Image Generation

Generate images using your local ComfyUI instance. Designed with security as a priority:

- **Server address is configured, not passed as argument** — no connecting to arbitrary servers
- **Workflows are allowlisted** — only files in the `workflows/` directory can be used
- **No shell injection surface** — prompts are passed as JSON, never interpolated into shell commands
- **Path traversal blocked** — `../` and absolute paths are rejected

## Setup

1. **Server address:** Set the `COMFYUI_SERVER_ADDRESS` environment variable (e.g., `http://192.168.1.10:8188` or `http://127.0.0.1:8188`).
2. **ComfyUI API mode:** Ensure "Enable Dev mode" is turned on in your ComfyUI settings.

## Usage

### Generate an image with a prompt
```bash
python3 {skillDir}/scripts/comfy_gen.py --prompt "a serene mountain lake at sunset"
```

### Generate with a specific allowlisted workflow
```bash
python3 {skillDir}/scripts/comfy_gen.py --prompt "a cyberpunk cityscape" --workflow z-image-turbo
```

### Generate with custom dimensions
```bash
python3 {skillDir}/scripts/comfy_gen.py --prompt "a cat in a spacesuit" --width 768 --height 512
```

### Generate with negative prompt
```bash
python3 {skillDir}/scripts/comfy_gen.py --prompt "a portrait photo" --negative "blurry, distorted, low quality"
```

## Available Workflows

Place API-format workflow JSON files in the `workflows/` directory. They are automatically available by filename (without .json extension).

The included workflows:

| Workflow | Description |
|----------|-------------|
| `z-image-turbo` | Fast generation, 10 steps, Euler sampler |
| `z-image-biglove` | Higher quality, more steps |

## Security Design

This skill fixes the three vulnerabilities found in other ComfyUI skills:

### 1. No arbitrary file reads
The original skill accepted `--workflow /any/path/on/disk.json`, allowing an agent to read any JSON file on the system. This version only allows workflows from the `workflows/` directory within the skill folder. Paths with `..`, `/`, or `\` are rejected.

### 2. No arbitrary server connections
The original skill accepted the server address as a command-line argument, allowing connections to any server. This version reads `COMFYUI_SERVER_ADDRESS` from the environment only. No command-line override.

### 3. No shell injection
The original skill constructed shell commands with user-provided arguments. This version uses `argparse` and passes all data as structured JSON over HTTP — no shell interpolation.

## How It Works

1. Reads `COMFYUI_SERVER_ADDRESS` from environment (required)
2. Validates the workflow name against allowlisted files in `workflows/`
3. Loads the workflow, injects the prompt and seed
4. Sends the workflow to ComfyUI via HTTP API
5. Polls for completion, downloads the result image
6. Saves to `{skillDir}/output/` and prints a `MEDIA:` path
