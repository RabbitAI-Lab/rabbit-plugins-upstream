# Image with ComfyUI

Call a local ComfyUI instance for **text-to-image**, **image-to-image/edit**, and **image-to-video** generation. **Qwen-Image 2.1** is the default model for both T2I and image editing (including multi-image reference composition); Z-Image, SD3.5 Medium, Qwen Image Edit (2511), and Wan2.2 are available as options.

> **New here?** Qwen-Image 2.1 needs a one-time ComfyUI setup — see [Qwen-Image 2.1 ComfyUI Setup](#qwen-image-21-comfyui-setup).

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
| `COMFYUI_POLL_INTERVAL` | `poll_interval_seconds` | `1` |
| `COMFYUI_KEEP_MODELS_RESIDENT` | `keep_models_resident` | `false` |
| `COMFYUI_OUTPUT_DIR` | `output_dir` | `media/comfyui` |

**Priority:** Environment variables > `config.json`

### Data & Privacy

- **Transmitted to the endpoint**: prompts and workflow JSON (all modes); **full source images** for I2I and I2V.
- **Default endpoint** is loopback-only (`http://127.0.0.1:8188`); a non-loopback `COMFYUI_URL` prints a warning on every run. Use HTTPS for remote servers and never put credentials in the URL or logs.
- **Written to disk**: generated media is saved under `output_dir` (config) or `COMFYUI_OUTPUT_DIR` in your workspace; delivery staging copies live in `~/.openclaw/media/outbound/` and are removed after a successful send. If your content is sensitive, review the endpoint and output location before running.

## Models & Custom Nodes

This skill uses the **existing** ComfyUI installation — it does not ship models or nodes. Before using, ensure your ComfyUI has:

### Required Models

Every model below has a **verified download source** in [`MODEL_URL.txt`](MODEL_URL.txt) — open that file for the exact HuggingFace repo, folder, and filename. Our server currently runs a **UC/NSFW-merged set** (Qwen-Image 2.1 = uncensored, Wan2.2 = NSFW creator merges); `MODEL_URL.txt` lists **SFW/official equivalents** for a clean setup.

| Model | Expected Location | Source |
|---|---|---|
| Z-Image (SVD XT) | `ComfyUI/models/checkpoints/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| SD3.5 Medium | `ComfyUI/models/checkpoints/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| Qwen Image Edit Plus | `ComfyUI/models/checkpoints/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| **Qwen-Image 2.1** (default T2I + edit) | see [Qwen-Image 2.1 ComfyUI Setup](#qwen-image-21-comfyui-setup) | [`MODEL_URL.txt`](MODEL_URL.txt) |
| Wan2.2 1.3B | `ComfyUI/models/checkpoints/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| Wan2.2 VAEMODEL | `ComfyUI/models/vae/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| Wan2.2 Audio Model | `ComfyUI/models/audio_encoders/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| T5XXL & FluxFill | `ComfyUI/models/clip/` | [`MODEL_URL.txt`](MODEL_URL.txt) |
| RIFE (for video interpolation) | `ComfyUI/models/frameworks/` | [`MODEL_URL.txt`](MODEL_URL.txt) |

### Required Custom Nodes

Install **pinned at reviewed commits** (as of 2026-09-20). Check out the exact commit rather than a mutable default branch, and install dependencies in an isolated venv under a non-privileged user — never `pip install` as root:

| Node | Package (repo) | Pinned commit |
|---|---|---|
| Impact Pack | [ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) | `429d0159a` |
| WAS Nodes | [WASasquatch/was-node-suite-comfyui](https://github.com/WASasquatch/was-node-suite-comfyui) *(repo renamed from `ComfyUI-WAS-Nodes`)* | `9934caa92` |
| ComfyUI-Manager | [Comfy-Org/ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) *(migrated from `comfyanonymous/`)* | `946ef8fe6` |
| rgthree | [rgthree/rgthree-comfy](https://github.com/rgthree/rgthree-comfy) | — (required by the Qwen-Image 2.1 workflow's LoRA pass-through node) |

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack.git
cd ComfyUI-Impact-Pack && git checkout --detach 429d0159ad429e64d2b3916e6e7be9c22d025c3c
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

Repeat the same pin-and-checkout pattern for the other two repositories (use their pinned commits above). Review dependency lists before installing, and re-check upstream commits before upgrading a pin.

When a missing node or model is detected, the script reports the package name and a manual install hint — it never executes `git clone` itself (ComfyUI may run on another host).

## Qwen-Image 2.1 ComfyUI Setup

**Qwen-Image 2.1** (model id `qwen21`) is the **default** model for both `t2i` and `i2i`. One workflow covers text-to-image, single-image edit, and multi-image reference composition. It is a distilled model — **CFG must stay at 1.0** (the script enforces this; raising it burns the image).

### Prerequisites
- **ComfyUI ≥ 0.37.0** (frontend 1.53.6). The workflow uses core nodes that only exist in recent builds:
  - `TextEncodeQwenImage21` (`comfy_extras.nodes_qwen`)
  - `ResolutionSelector` (`comfy_extras.nodes_resolution`)
  - `ComfySwitchNode` / `If/Else Switch` (`comfy_extras.nodes_logic`)
  - `PrimitiveBoolean` (`comfy_extras.nodes_primitive`)
  
  If any show up as a red *missing node*, **update ComfyUI** — they are core, not a custom pack. (`If/Else Switch` is experimental and may be hidden from node search until you enable experimental nodes; loading the workflow works either way.)

### Model files (3)
Place each in the folder shown, under your ComfyUI install. These are the exact filenames the workflow expects:

| File | Destination folder |
|---|---|
| `QWEN_Image/qwen-image-2.1-UC-int8_convrot.safetensors` | `ComfyUI/models/diffusion_models/` (keep the `QWEN_Image/` subfolder; older builds may use `models/unet/`) |
| `qwen3vl_8b_int8_convrot.safetensors` | `ComfyUI/models/text_encoders/` (Qwen3-VL 8B int8; loaded with `type: qwen_image`) |
| `qwen_image_2.1_vae_bf16.safetensors` | `ComfyUI/models/vae/` |

> Unlike the original foprc workflow (which used a GGUF Q8 model + ComfyUI-GGUF), this workflow loads the diffusion model via **`UNETLoader`** with `weight_dtype: fp8_e4m3fn_fast`. That **removes the ComfyUI-GGUF dependency** — the only custom node needed is **rgthree**.

If you use a different quantization/filename, update `unet_name` in `workflows/qwen_image_2.1_api.json` (node `17`) to match what's on disk.

### Custom nodes
- **rgthree-comfy** (for the `Power Lora Loader` node) — install via ComfyUI Manager or `git clone https://github.com/rgthree/rgthree-comfy` into `custom_nodes/`, then restart.
- All other nodes are core ComfyUI.
- *Optional:* the LoRA stack is off by default and passes the model/CLIP straight through. If you don't have rgthree, you can instead delete node `10` and rewire `17 → 6` (model) and `2 → 5` (clip).

### Verifying your setup
```bash
python3 image_with_comfyui.py test          # server reachable?
python3 image_with_comfyui.py t2i --prompt "A red fox in snow" --aspect 1:1
python3 image_with_comfyui.py i2i --prompt "Change the sky to sunset" --image /path/in.jpg
```
If a loader dropdown is blank in the web UI, the file isn't where ComfyUI is looking — check the folder above. If a node reports *missing*, update ComfyUI (see Prerequisites).

### How the dual-mode switch works
Node `12` (`PrimitiveBoolean`) is the master switch:
- **OFF** (`false`) → pure **T2I**: the sampler starts from an empty latent sized by `ResolutionSelector` (aspect ratio + megapixels).
- **ON** (`true`) → **edit / multi-image**: reference image(s) feed `TextEncodeQwenImage21`, whose output latent is sampled instead. The script wires 1 image to `image_1`, and extra images to `image_2 … image_N` (up to 16).

### Multi-image prompt format
With 2+ reference images, the model sees them in **slot order** (`image_1`, `image_2`, …). Reference each by index in the prompt so it knows which is which:
```
Put the garment from <image2> onto the person in <image1>, keep <image1>'s pose and lighting.
Combine both photos into one scene: subject of <image1> on the left, subject of <image2> on the right.
```
Keep the instruction concise and in the user's language; the skill passes it through verbatim. `--image` accepts multiple paths (order = slot order = `<image1>`, `<image2>` …).

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

### Output filename scheme

Generated files use a short mode prefix + timestamp (`YYYYMMDD_HHMMSS`) + ComfyUI's counter:

| Mode | Prefix | Example (JPG) |
|---|---|---|
| Qwen-Image 2.1 T2I | `qt2i` | `qt2i_20260928_050328_00001.jpg` |
| Qwen-Image 2.1 I2I | `qi2i` | `qi2i_20260928_050328_00001.jpg` |
| Qwen Image Edit (2511) | `qei2i` | `qei2i_20260928_050328_00001.jpg` |
| Z-Image T2I | `zt2i` | `zt2i_20260928_050328_00001.jpg` |
| SD3.5 Medium T2I | `st2i` | `st2i_20260928_050328_00001.jpg` |

The trailing underscore ComfyUI appends is stripped, so names never end in `_`.

### Manual Workflow Testing

You can also test workflows directly in the ComfyUI web UI. Copy any workflow file from `workflows/` into ComfyUI, load it, and run:

- **Qwen-Image 2.1 (T2I + edit + multi-image, default)**: `workflows/qwen_image_2.1_api.json`
- **Z-Image T2I**: `workflows/z-image_t2i_api.json`
- **SD3.5 Medium T2I**: `workflows/sd3.5-med_t2i_api.json`
- **Qwen Image Edit (2511)**: `workflows/qwen_image-edit_api.json`
- **Wan2.2 I2V**: `workflows/wan2.2_i2v_api.json`

## Important Notes

### Local Skill — No Automatic Installation

This skill **does not install anything automatically**. It connects to your existing ComfyUI instance via API calls; the workflows, models, and custom nodes must already be configured in your ComfyUI setup. If a node is missing, the skill only *reports* the package and a pinned manual install hint (it never runs `git clone` itself, since ComfyUI may be on another host). The manual commands in [Required Custom Nodes](#required-custom-nodes) are optional setup steps for your own ComfyUI — review and pin them before running.

### VRAM Release vs. Speed Tradeoff

By default this skill uses the `UnloadAllModels` node (and `UnloadModel` in the Qwen edit branch) to free VRAM after each generation, preventing VRAM exhaustion during repeated tasks. The unload nodes are stripped only when `keep_models_resident` is explicitly set to `true` (config or `COMFYUI_KEEP_MODELS_RESIDENT`); otherwise they run and release VRAM on every run. The unload nodes are bypassed automatically if a given ComfyUI instance doesn't have them — the system detects and skips them transparently.

> **The slow part of a “5-minute” run is almost never inference.** It's model reload *or* agent-side overhead before the run, not the sampling. See the skill's **Execution Discipline — Fast Path** section for how the run is expected to be invoked.

### Workflow Modifications

All workflow files in the `workflows/` directory are **adapted versions** of original ComfyUI workflows. They are repackaged into self-contained HTTP-API graphs — the original source is **not** kept inside the JSON. The original source for each workflow plus exactly what was changed is documented in [references/attribution.md](references/attribution.md). Known modifications include:
- API-ready output node placement + timestamped output filenames
- Parameter exposure (aspect, steps, CFG, seed, neg, etc.) for external control
- Prompt auto-routing (e.g. Qwen Edit routes to the positive prompt node)
- A standard **safetensors** model load replacing the original GGUF load (Qwen-Image 2.1), dropping the ComfyUI-GGUF dependency
- VRAM-cleanup nodes (`UnloadAllModels`, `UnloadModel`) added, auto-bypassed when absent
- The SD3.5 double-`.safetensors` suffix bug fixed; Wan2.2 pointed at 4-step Lightspeed weights

### Error Handling

The system handles three categories of errors automatically:

1. **Missing nodes** — Reports which node is missing, provides package name, install command, and GitHub URL.
2. **Missing models** — Attempts to substitute a compatible model (e.g., SD3.5 medium variants → SD3.5 large).
3. **Non-critical utility nodes** — Automatically bypasses nodes like `UnloadAllModels` without interrupting generation.

## CLI Reference

```bash
# Generate image from text (default: Qwen-Image 2.1)
python3 image_with_comfyui.py t2i --prompt "Your description" --aspect 1:1

# Generate with an explicit model
python3 image_with_comfyui.py t2i --model z-image --prompt "Your description"
python3 image_with_comfyui.py t2i --model sd35 --prompt "Your description" --negative "blurry"

# Edit an image (default: Qwen-Image 2.1)
python3 image_with_comfyui.py i2i --prompt "Replace background" --image /path/to/image.png

# Multi-image reference (2+ images; order = <image1>, <image2>, ...)
python3 image_with_comfyui.py i2i \
  --prompt "Put the shirt from <image2> on the person in <image1>" \
  --image /path/person.jpg /path/shirt.jpg

# Generate video from image
python3 image_with_comfyui.py wan2.2 --prompt "Camera pans left" --image /path/to/image.png

# Test ComfyUI connection
python3 image_with_comfyui.py test
```

## Timeout Reference

| Mode | Timeout |
|---|---|
| T2I (Qwen-Image 2.1) | 300s |
| T2I (Z-Image) | 100s |
| T2I (SD3.5) | 100s |
| I2I (Qwen-Image 2.1, incl. multi-image) | 600s |
| I2I (Qwen 2511) | 600s |
| I2V (Wan2.2) | 1000s |
