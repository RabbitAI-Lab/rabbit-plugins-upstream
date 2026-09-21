# Image with ComfyUI

Call a local ComfyUI instance for **text-to-image**, **image-to-image/edit**, and **image-to-video** generation. Supports Z-Image, SD3.5 Medium, Qwen Image Edit, and Wan2.2 models.

## Quick Start

1. **Ensure ComfyUI is running** on your local machine.
2. **Set the URL** (via environment variable or `config.json`). The bundled default is loopback-only (`http://127.0.0.1:8188`); point `COMFYUI_URL` at a remote server only if you control and trust it — a data-flow warning is printed on every run for non-loopback hosts:
   ```bash
   export COMFYUI_URL=http://comfyui.host:api-port
   ```
3. **Test a workflow** (see [Testing](#testing) below).

## Configuration

Read `config.json` at the skill root. All values can be overridden by environment variables:

| Env Variable | Overrides | Default |
|---|---|---|
| `COMFYUI_URL` | `comfyui_url` | `http://localhost:8188` |
| `COMFYUI_TIMEOUT` | `timeout_seconds` | `120` |
| `COMFYUI_POLL_INTERVAL` | `poll_interval_seconds` | `3` |
| `COMFYUI_OUTPUT_DIR` | `output_dir` | `media/comfyui` |

**Priority:** Environment variables > `config.json`

### Data & Privacy

- **Transmitted to the endpoint**: prompts and workflow JSON (all modes); **full source images** for I2I and I2V.
- **Default endpoint** is loopback-only (`http://127.0.0.1:8188`); a non-loopback `COMFYUI_URL` prints a warning on every run. Use HTTPS for remote servers and never put credentials in the URL or logs.
- **Written to disk**: generated media is saved under `output_dir` (config) or `COMFYUI_OUTPUT_DIR` in your workspace; delivery staging copies live in `~/.openclaw/media/outbound/` and are removed after a successful send. If your content is sensitive, review the endpoint and output location before running.

## Models & Custom Nodes

This skill uses the **existing** ComfyUI installation — it does not ship models or nodes. Before using, ensure your ComfyUI has:

### Required Models
| Model | Expected Location |
|---|---|
| Z-Image (SVD XT) | `ComfyUI/models/checkpoints/` |
| SD3.5 Medium | `ComfyUI/models/checkpoints/` |
| Qwen Image Edit Plus | `ComfyUI/models/checkpoints/` |
| Wan2.2 1.3B | `ComfyUI/models/checkpoints/` |
| Wan2.2 VAEMODEL | `ComfyUI/models/vae/` |
| Wan2.2 Audio Model | `ComfyUI/models/audio_encoders/` |
| T5XXL & FluxFill | `ComfyUI/models/clip/` |
| RIFE (for video interpolation) | `ComfyUI/models/frameworks/` |

### Required Custom Nodes

Install **pinned at reviewed commits** (as of 2026-09-20). Check out the exact commit rather than a mutable default branch, and install dependencies in an isolated venv under a non-privileged user — never `pip install` as root:

| Node | Package (repo) | Pinned commit |
|---|---|---|
| Impact Pack | [ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) | `429d0159a` |
| WAS Nodes | [WASasquatch/was-node-suite-comfyui](https://github.com/WASasquatch/was-node-suite-comfyui) *(repo renamed from `ComfyUI-WAS-Nodes`)* | `9934caa92` |
| ComfyUI-Manager | [Comfy-Org/ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) *(migrated from `comfyanonymous/`)* | `946ef8fe6` |

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack.git
cd ComfyUI-Impact-Pack && git checkout --detach 429d0159ad429e64d2b3916e6e7be9c22d025c3c
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

Repeat the same pin-and-checkout pattern for the other two repositories (use their pinned commits above). Review dependency lists before installing, and re-check upstream commits before upgrading a pin.

When a missing node or model is detected, the script reports the package name and a manual install hint — it never executes `git clone` itself (ComfyUI may run on another host).

## Testing

Use the built-in test script:

```bash
# Health check
python3 image_with_comfyui.py test

# Test each workflow individually
python3 image_with_comfyui.py t2i --prompt "A cat on a windowsill"

# Run the health check before each batch of jobs
python3 image_with_comfyui.py test
```

### Manual Workflow Testing

You can also test workflows directly in the ComfyUI web UI. Copy any workflow file from `workflows/` into ComfyUI, load it, and run:

- **Z-Image T2I**: `workflows/z-image_t2i_api.json`
- **SD3.5 Medium T2I**: `workflows/sd3.5-med_t2i_api.json`
- **Qwen Image Edit**: `workflows/qwen_image-edit_api.json`
- **Wan2.2 I2V**: `workflows/wan2.2_i2v_api.json`

## Important Notes

### Local Skill — No Automatic Installation

This skill **does not install anything automatically**. It connects to your existing ComfyUI instance via API calls; the workflows, models, and custom nodes must already be configured in your ComfyUI setup. If a node is missing, the skill only *reports* the package and a pinned manual install hint (it never runs `git clone` itself, since ComfyUI may be on another host). The manual commands in [Required Custom Nodes](#required-custom-nodes) are optional setup steps for your own ComfyUI — review and pin them before running.

### VRAM Release After Generation

This skill uses the `UnloadAllModels` node (bypassed automatically if unavailable) to free VRAM after each generation. This prevents VRAM exhaustion during repeated tasks. The original node may not be present in your ComfyUI installation — the system will detect and skip it transparently.

### Workflow Modifications

All workflow files in the `workflows/` directory are **adapted versions** of original ComfyUI workflows. The original author information and credits are preserved within each JSON file. Modifications include:
- API-ready output node placement
- Parameter exposure for external control
- Auto-enhance and preprocessing pipeline integration

### Error Handling

The system handles three categories of errors automatically:

1. **Missing nodes** — Reports which node is missing, provides package name, install command, and GitHub URL.
2. **Missing models** — Attempts to substitute a compatible model (e.g., SD3.5 medium variants → SD3.5 large).
3. **Non-critical utility nodes** — Automatically bypasses nodes like `UnloadAllModels` without interrupting generation.

## CLI Reference

```bash
# Generate image from text
python3 image_with_comfyui.py t2i --prompt "Your description" --aspect 16:9

# Generate image with SD3.5
python3 image_with_comfyui.py t2i --model sd35 --prompt "Your description" --negative "blurry"

# Edit an image
python3 image_with_comfyui.py i2i --prompt "Replace background" --image /path/to/image.png

# Generate video from image
python3 image_with_comfyui.py wan2.2 --prompt "Camera pans left" --image /path/to/image.png

# Test ComfyUI connection
python3 image_with_comfyui.py test
```

## Timeout Reference

| Mode | Timeout |
|---|---|
| T2I (Z-Image) | 100s |
| T2I (SD3.5) | 100s |
| I2I (Qwen) | 600s |
| I2V (Wan2.2) | 1000s |
