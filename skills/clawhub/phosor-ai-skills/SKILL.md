---
name: phosor-ai-skills
description: Generate AI videos, images and speech (text-to-video, image-to-video, reference-to-video, speech-to-video, animate, text-to-image, image-to-image, image edit, text-to-speech), bring your own LoRA models, and generate AI product/model photography for e-commerce (Image Studio) via the Phosor AI platform. Use when the user wants to create videos or images from text prompts, animate images, generate lip-synced video from audio, synthesize speech from text, generate images with a custom LoRA, generate product photography or model/clothing photography for e-commerce listings, or manage generation jobs.
license: MIT-0
compatibility: Requires Python 3.7+ and network access to phosor.ai
metadata:
  author: phosor.ai
  version: "1.1.0"
  api_version: "v1.0.0"
  homepage: https://phosor.ai
---

# Phosor AI

Generate AI videos and images (text-to-video, image-to-video, speech-to-video, animate, text-to-image, image-to-image), bring your own LoRA models, and generate AI product/model photography for e-commerce (Image Studio) via the Phosor AI platform.

For detailed API endpoints, parameters, pricing, and limits, see [references/api.md](references/api.md).

## Setup

Set your API key:

```bash
export PHOSOR_API_KEY="your-api-key-here"
```

Get an API key at [phosor.ai](https://phosor.ai) → Settings → API Keys.

The CLI script is at `scripts/phosor_client.py`. All commands output JSON to stdout.

## Environments (dev vs prod — same API, only the base URL differs)

It is **one API**. Endpoints, parameters and payloads are identical across environments — **only the base URL (host:port) and scheme change**. Do not fork the client or the skill per environment; just point the same client at a different base URL.

| Env | Base URL | How to target it |
|-----|----------|------------------|
| **Production** (default) | `https://phosor.ai` (fixed) | nothing to set; key from phosor.ai → Settings → API Keys |
| **Dev** | the current dev machine — **not fixed, it moves with the box** (e.g. `http://54.95.59.4:3000` nginx front, or `http://localhost:8010` gateway when you're on the box) | `--base-url http://<dev-host:port> --allow-http` (or env `PHOSOR_BASE_URL=... PHOSOR_ALLOW_HTTP=1`). `localhost`/`127.0.0.1` needs no flag. Dev key from the dev site. |

```bash
# dev
python3 scripts/phosor_client.py --base-url http://54.95.59.4:3000 --allow-http --api-key <dev-key> check-key
# prod (default — HTTPS enforced)
python3 scripts/phosor_client.py --api-key <prod-key> check-key
```

Dev gotcha: `studio-analyze` / `studio-suite` `--image-url` must be the **full https S3 URL** returned by `upload-image`, not the bare S3 key path — a bare key errors with `unsupported URL scheme`.

## Quick Start

### MiniMax H3 — Text-to-Video

H3 is **duration-based**, not frame-based: it ignores `--num-frames` / `--fps` (output is
always 24fps) and bills per output second. Pick the frame size with
`--resolution-tier` + `--aspect` instead of `--width/--height`.

```bash
python3 scripts/phosor_client.py submit "A cat walking on a beach at sunset" \
  --model minimax/h3/text-to-video \
  --resolution-tier 768p --aspect 16:9 --duration 5
```

### MiniMax H3 — Image-to-Video

```bash
# Upload first (direct URLs are not accepted); then submit with the returned s3_key
python3 scripts/phosor_client.py upload-image /path/to/first-frame.jpg

python3 scripts/phosor_client.py submit "The person starts dancing" \
  --model minimax/h3/image-to-video \
  --image-url "images/img-xxx.jpg" \
  --end-image-url "images/img-yyy.jpg" \
  --resolution-tier 480p --aspect 9:16 --duration 6
```

`--end-image-url` is optional and pins the closing frame.

### MiniMax H3 — Reference-to-Video (Ref2VA)

Feed reference **images**, **videos**, and **audio** together; refer to them positionally in
the prompt as `<Picture 1>`, `<Picture 2>`, … At least one of `--reference-image-urls` /
`--reference-video-urls` is required.

```bash
python3 scripts/phosor_client.py submit \
  "Use <Picture 1> and <Picture 2> as sequential keyframes; slow push-in, cinematic 35mm look." \
  --model minimax/h3/reference-to-video \
  --reference-image-urls "images/a.jpg,images/b.jpg" \
  --reference-audio-urls "audio/voice.mp3" \
  --resolution-tier 768p --aspect 16:9 --duration 5
```

Reference inputs are billed on top of the output — see **Ref2VA Pricing** below, and
**Ref2VA Reference Limits** for the per-tier caps (they differ between 480p and 768p).

### Text-to-Video (Wan)

Wan is frame-based. Add `/turbo` to the model id for the fast, ~3x cheaper variant
(it ignores `--steps` / `--guidance`).

```bash
# Submit T2V job (480p, 81 frames, 16fps)
python3 scripts/phosor_client.py submit "A cat walking on a beach at sunset" \
  --width 854 --height 480 --num-frames 81 --fps 16

# Check status
python3 scripts/phosor_client.py status <request_id>

# Get result (video URL)
python3 scripts/phosor_client.py result <request_id>
```

### Image-to-Video

**Two-step flow**: upload image first, then submit with the returned S3 key.

```bash
# Step 1: Upload image
python3 scripts/phosor_client.py upload-image /path/to/photo.jpg
# Returns: {"file_id": "img-xxx", "s3_key": "images/img-xxx.jpg", ...}

# Step 2: Submit I2V job using the s3_key as image_url
python3 scripts/phosor_client.py submit "The person in the photo starts dancing" \
  --image-url "images/img-xxx.jpg" --width 854 --height 480
```

### Text-to-Image

```bash
# Submit T2I job (1024x1024, default settings)
python3 scripts/phosor_client.py submit "A futuristic city skyline at dusk" \
  --model qwen-image/v2512/text-to-image --width 1024 --height 1024

# Generate multiple images at once (1-4)
python3 scripts/phosor_client.py submit "A futuristic city skyline at dusk" \
  --model z-image/turbo/text-to-image --width 1024 --height 768 --num-images 4

# Check status and get result (image URL)
python3 scripts/phosor_client.py status <request_id>
python3 scripts/phosor_client.py result <request_id>
# Returns: {"data": {"image": {"url": "..."}, "seed": 12345}, ...}
```

### Image-to-Image

**Two-step flow**: upload source image first, then submit with the returned S3 key.

```bash
# Step 1: Upload source image
python3 scripts/phosor_client.py upload-image /path/to/photo.jpg
# Returns: {"file_id": "img-xxx", "s3_key": "images/img-xxx.jpg", ...}

# Step 2: Submit I2I job using the s3_key as image_url
python3 scripts/phosor_client.py submit "Transform into oil painting style" \
  --model z-image/turbo/image-to-image --image-url "images/img-xxx.jpg" \
  --width 1024 --height 1024 --strength 0.7
```

### Image Edit (Multi-image Reference)

**Two-step flow**: upload reference images first, then submit with S3 keys as `image_urls`.

```bash
# Step 1: Upload reference images (up to 3)
python3 scripts/phosor_client.py upload-image /path/to/ref1.jpg
python3 scripts/phosor_client.py upload-image /path/to/ref2.jpg

# Step 2: Submit image-edit job
python3 scripts/phosor_client.py submit \
  "The girl in image 1 is wearing the outfit from image 2" \
  --model qwen-image/v2511/image-edit \
  --image-urls '["images/img-ref1.jpg","images/img-ref2.jpg"]' \
  --width 1024 --height 1024

# Turbo variant (faster, Lightning LoRA built-in)
python3 scripts/phosor_client.py submit \
  "The girl in image 1 is wearing the outfit from image 2" \
  --model qwen-image/v2511/image-edit \
  --image-urls '["images/img-ref1.jpg","images/img-ref2.jpg"]'
```

### Speech-to-Video (S2V)

**Two-step flow**: upload both audio and reference image first, then submit with the returned S3 keys.

```bash
# Step 1: Upload reference image
python3 scripts/phosor_client.py upload-image /path/to/face.jpg
# Returns: {"file_id": "img-xxx", "s3_key": "images/img-xxx.jpg", ...}

# Step 2: Submit S2V job using the s3_key as image_url and audio URL as audio_url
python3 scripts/phosor_client.py submit "A person speaking naturally" \
  --model wan/v2.2-a14b/speech-to-video \
  --image-url "images/img-xxx.jpg" --audio-url "https://example.com/speech.wav" \
  --width 854 --height 480
```

### Animate

**Two-step flow**: upload both source video and reference image first, then submit.

```bash
# Step 1: Upload reference image
python3 scripts/phosor_client.py upload-image /path/to/character.jpg
# Returns: {"file_id": "img-xxx", "s3_key": "images/img-xxx.jpg", ...}

# Step 2: Submit Animate job using the s3_key as image_url and video URL as video_url
python3 scripts/phosor_client.py submit "The character performs the dance moves" \
  --model wan/v2.2-a14b/animate \
  --image-url "images/img-xxx.jpg" --video-url "https://example.com/dance.mp4" \
  --width 854 --height 480
```

### Text-to-Image (GPT Image 2)

Its own resolution set and **always exactly 1 image** (`--num-images` is ignored).

```bash
python3 scripts/phosor_client.py submit "A ceramic mug on a linen cloth, soft window light" \
  --model openai/gpt-image-2/text-to-image --width 1024 --height 1024
```

Allowed sizes: **1024×1024 only**. Any other size is rejected with `400 Invalid parameters`.
It ignores `--num-images`, `--steps` and `--guidance` — the only parameters it accepts are
prompt, model, width, height and seed.

### Text-to-Image (FLUX.2-dev)

FLUX.2-dev has its own resolution whitelist and is **fixed at 1 image per request**
(`--num-images` and `--steps` are ignored).

```bash
python3 scripts/phosor_client.py submit "Editorial product photo, soft window light" \
  --model flux2/dev/text-to-image --width 2048 --height 1536
```

### Image Edit (FLUX.2-dev)

```bash
python3 scripts/phosor_client.py upload-image /path/to/source.jpg

python3 scripts/phosor_client.py submit "Replace the background with a marble surface" \
  --model flux2/dev/image-edit --image-url "images/img-xxx.jpg" \
  --width 1024 --height 1024
```

### Text-to-Speech

TTS takes `text` (not a prompt) and is billed per character with a minimum charge.

```bash
python3 scripts/phosor_client.py submit-tts "Hello, welcome to Phosor AI." \
  --speaker Sohee --language English
```

### LoRA Upload (Custom Pre-trained)

**Video LoRA** requires two .safetensors files (high_noise + low_noise). **Image LoRA** requires a single .safetensors file.

```bash
# Video LoRA: upload two .safetensors files
python3 scripts/phosor_client.py upload-lora high_noise.safetensors low_noise.safetensors --name "My Style"

# Image LoRA: import single .safetensors file via URL
python3 scripts/phosor_client.py import-lora \
  "https://example.com/my_lora.safetensors" \
  --name "My Image Style"

# Video LoRA: import two files via URL
python3 scripts/phosor_client.py import-lora \
  "https://example.com/high_noise.safetensors" \
  "https://example.com/low_noise.safetensors" \
  --name "My Video Style"

# Check status, then use
python3 scripts/phosor_client.py lora-status <lora_id>
python3 scripts/phosor_client.py submit "A person walking" --lora-id <lora_id>
```

## CLI Commands

| Command | Description | Key Arguments |
|---------|-------------|---------------|
| `check-key` | Validate API key | — |
| `submit` | Submit inference job (T2V/I2V/S2V/Animate/T2I/I2I) | `prompt`, `--width`, `--height`, `--num-frames`, `--fps`, `--steps`, `--guidance`, `--image-url`, `--audio-url`, `--video-url`, `--lora-id`, `--lora-scale`, `--loras`, `--seed`, `--negative-prompt`, `--model`, `--num-images`, `--strength`, `--output-format` |
| `status` | Get job status | `request_id` |
| `result` | Get job result (video or image URL) | `request_id` |
| `poll` | Poll all pending jobs | — |
| `list` | List locally tracked pending jobs | — |
| `history` | Get job history | `--limit` |
| `upload-image` | Upload image for I2V or I2I | `file` |
| `import-image` | Import image from URL | `url`, `--filename` |
| `upload-lora` | Upload LoRA (two .safetensors for video) | `high_noise_file`, `low_noise_file`, `--name` |
| `import-lora` | Import LoRA from URLs (one or two files) | `high_noise_url`, `[low_noise_url]`, `--name` |
| `loras` | List LoRA models | `--limit`, `--offset` |
| `lora-status` | Get LoRA upload/import status | `lora_id` |
| `save-lora` | Activate a LoRA (extends expiry to 7 days) | `lora_id`, `--name` |
| `delete-lora` | Delete a LoRA model | `lora_id` |
| `submit-tts` | Submit a text-to-speech job (Qwen3-TTS) — keys off `text`, not a prompt | `text`, `--speaker`, `--language`, `--seed`, `--temperature`, `--top-p`, `--top-k`, `--repetition-penalty` |
| `models` | List available video/image models (static offline reference) | — |
| `studio-features` | List Image Studio endpoints, fields, billing (static offline reference) | — |
| `studio-pricing` | Get live Image Studio pricing | — |
| `studio-analyze` | AI-analyze a product/garment image or reference URL (freemium) | `--target agent\|product\|model\|reference`, `--image-url`, `--url`, `--prompt`, `--language` |
| `studio-layouts` | List the layout template library (query, then select) — static asset on the **web front** (prod phosor.ai / dev `:3000`), not a `/api/v1` endpoint; needs no key; dev auto-falls back `:8010`→`:3000` | `--module` (product\|clothing), `--type` (selling_point\|aplus\|white_bg\|scene\|closeup\|size_chart) |
| `studio-suite` | Generate a product image suite | `--image-url`, `--layout-types`, `--count-per-type`, `--custom-suggestions`, `--template-ids` (ids from `studio-layouts`, auto-expanded to custom_suggestions like the UI's manual pick — use this to get **text-callout selling-point / A+ layouts** and model templates), `--product-info`, `--aspect-ratio`, `--gen-language`, `--model`, `--same-style-reference` |
| `studio-clothing-suite` | Generate a model/garment image suite | `--image-urls`, `--main-image-types`, `--aplus-types`, `--product-info`, `--brand-config`, `--aspect-ratio`, `--gen-language`, `--model`, `--same-style-reference` |
| `studio-status` | Get Image Studio job status (separate id space, same `request_id` key) | `request_id` |
| `studio-cancel` | Cancel a running generation — queued images refunded, already-generating ones charged | `request_id` |
| `studio-my-works` | List past Image Studio generations | `--task-type`, `--limit`, `--offset` |
| `studio-call` | Generic call for any other Image Studio endpoint (remove-bg, replace, inpaint, erase, handheld, translate, outpaint, recolor, enhance, upscale, scene-compose, scene-variation, real-model-swap, mannequin-swap, model-scene-swap, ai-outfit, pose-variation, ai-wearable) | `method`, `path`, `--json` |

## Image Studio (Product & Model Photography)

Image Studio is a separate product surface for e-commerce sellers — AI product photography and model/clothing photography — reached through the **same gateway and API key** as video/LoRA, under the `/api/v1/image-studio` prefix. It has its own async namespace - the same key name `request_id`, but a **separate id space**: an Image Studio `request_id` is not valid on `/api/v1/inference/status/...` and vice versa - and its own pricing (flat per-image rate + freemium analyze quota, not per-frame). Full endpoint/parameter reference: [references/api.md](references/api.md#image-studio-product--model-photography--separate-product-surface).

### Quick Start: Product Suite

```bash
# 1. Upload the product photo
python3 scripts/phosor_client.py upload-image /path/to/product.jpg
# Returns: {"file_id": "img-xxx", "s3_key": "images/img-xxx.jpg", ...}

# 2. (Optional) AI-analyze it first for richer generation context
python3 scripts/phosor_client.py studio-analyze --target product --image-url "images/img-xxx.jpg"

# 3. Generate a product image suite
python3 scripts/phosor_client.py studio-suite --image-url "images/img-xxx.jpg" \
  --layout-types "white_background,lifestyle_scene" --count-per-type 2

# 4. Poll for the result
python3 scripts/phosor_client.py studio-status <request_id>
```

### Quick Start: Clothing/Model Suite

```bash
python3 scripts/phosor_client.py upload-image /path/to/garment.jpg
python3 scripts/phosor_client.py studio-clothing-suite \
  --image-urls "images/img-xxx.jpg" \
  --main-image-types '{"model_shot":2,"selling_point":1}' \
  --aplus-types '{"standard_aplus":1}'
python3 scripts/phosor_client.py studio-status <request_id>
```

### Quick Start: One-off Edits (remove-bg, inpaint, translate, etc.)

The long tail of single-purpose editing endpoints doesn't get a dedicated subcommand — use `studio-call` with the exact field names from [references/api.md](references/api.md#image-studio-product--model-photography--separate-product-surface):

```bash
python3 scripts/phosor_client.py studio-call POST /product/remove-bg \
  --json '{"image_url": "images/img-xxx.jpg", "count": 2}'
python3 scripts/phosor_client.py studio-status <request_id>
```

### Key facts

- **Every Image Studio call requires `X-API-Key`** (`PHOSOR_API_KEY`), including `GET /pricing` — there is no unauthenticated endpoint under this prefix.
- **All generation/analyze endpoints are async**: POST returns `{"request_id": "...", "status": "pending"}`; poll `studio-status <request_id>` until `status` is `"done"`, `"error"` or `"cancelled"`. Earlier revisions of this skill said the key was `job_id` - it is not, and reading it yields `undefined`. Image Studio ids live in a **separate id space** from video/LoRA: `poll`/`status`/`result` will not accept an Image Studio `request_id`.
- **Cancelling**: `POST /jobs/{request_id}/cancel` stops a running generation. Images still queued are refunded; images already generating are charged and cannot be stopped; images already delivered bill once through the normal path. The response reports the split as `refunded_queued`, `charged_running` and `already_done`, and the task then polls as `status: "cancelled"` - not an error.
- **Pricing is per-image, not per-frame**: call `studio-pricing` for the live rate. Partial success (e.g. 3 of 5 images) bills only the successes.
- **Analyze is freemium**: `agent/analyze`, `product/analyze`, `model/analyze` share a daily free quota before per-call billing kicks in.
- **`model_attrs` matters for model-photography endpoints** (real-model-swap, mannequin-swap, ai-outfit, ai-wearable) — pass `{gender, age_group, ethnicity, skin_tone, hair_color}` explicitly; it is not reliably inferred from the source image alone.
- Run `studio-features` for the full offline endpoint/field catalog without leaving the terminal.

## Key Constraints

### Video Resolutions (exact pairs only)

| Preset | Width × Height | Max Frames (turbo) | Max Frames (standard) |
|--------|---------------|-------------------|----------------------|
| 480p landscape | 854 × 480 | 161 | 161 |
| 480p portrait | 480 × 854 | 161 | 161 |
| 720p landscape | 1280 × 720 | 161 | 161 |
| 720p portrait | 720 × 1280 | 161 | 161 |
| 1080p landscape | 1920 × 1080 | 153 | **81** |
| 1080p portrait | 1080 × 1920 | 153 | **81** |

> Standard (non-turbo) mode: 1080p is capped at 81 frames due to generation time limits.

### S2V / Animate Video Resolutions (exact pairs only)

| Preset | Width x Height | Max Frames |
|--------|---------------|------------|
| 480p landscape | 854 x 480 | 161 |
| 480p portrait | 480 x 854 | 161 |
| 512p square | 512 x 512 | 161 |
| 720p landscape | 1280 x 720 | 161 |
| 720p portrait | 720 x 1280 | 161 |

### Image Resolutions (exact pairs only)

| Preset | Width × Height |
|--------|---------------|
| Square small | 512 × 512 |
| Square | 1024 × 1024 |
| Landscape | 1024 × 768 |
| Portrait | 768 × 1024 |
| Wide landscape | 1280 × 768 |
| Tall portrait | 768 × 1280 |

### MiniMax H3 Frame Sizes (`--resolution-tier` + `--aspect`)

| Tier | 16:9 | 4:3 | 1:1 | 3:4 | 9:16 |
|------|------|-----|-----|-----|------|
| 480p | 832 × 480 | 640 × 480 | 480 × 480 | 480 × 640 | 480 × 832 |
| 768p | 1344 × 768 | 1024 × 768 | 768 × 768 | 768 × 1024 | 768 × 1344 |

`duration` is 4–15 seconds (default 5). Output FPS is fixed at 24 and
`frames_per_second` is ignored.

### Ref2VA Reference Limits (`minimax/h3/reference-to-video`)

Caps differ per tier, and the image cap is higher when you send **only** images:

| Limit | 480p | 768p |
|-------|------|------|
| Reference images (with videos/audio present) | 4 | 2 |
| Reference images (images only) | 9 | 4 |
| Reference videos | 3 | 1 |
| Reference audios | 3 | 3 |

| Limit | Value |
|-------|-------|
| Total reference video length | 6.5 s (across all reference videos) |
| Reference video FPS ceiling | 24 |
| Reference audio length | 10 s each |
| Reference image longest edge | 2048 px |
| Reference image aspect ratio | ≤ 4.0 |

### FLUX.2-dev Resolutions (exact pairs only)

| Width × Height |
|---------------|
| 2048 × 1536 · 1536 × 2048 |
| 2048 × 1152 · 1152 × 2048 |
| 2048 × 2048 · 1024 × 1024 |

> FLUX.2-dev does not accept the general image resolution list above, and always
> returns exactly 1 image.

### Frame Alignment (video only)

Frames must follow `1 + 4*k` where `k >= 1` (e.g. 5, 9, 13, ... 81, 85, ...). Server auto-aligns down.

### Video Inference Parameters

| Parameter | Default | Range |
|-----------|---------|-------|
| `frames_per_second` | 16 | 4–60 |
| `num_inference_steps` | 4 | 4–40 |
| `guidance_scale` | 1.0 | 1.0–10.0 |

### Image Inference Parameters

| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| `num_images` | 1 | 1–4 | Number of images to generate |
| `num_inference_steps` | varies | 1–4 (z-image turbo), 1–40 (qwen-image) | Model-dependent max |
| `guidance_scale` | varies | 1.0–20.0 | — |
| `strength` | — | 0.0–1.0 | Image-to-image only: how much to transform the source |
| `output_format` | png | png, jpeg | Output file format |

### Concurrency

Model API inference jobs run concurrently up to a per-account cap; over it the submit
returns `429` and you retry after a job finishes.

| Tier | Plan | Concurrent Model API jobs |
|------|------|---------------------------|
| Free | — | 1 |
| 1 | Starter | 2 |
| 2 | Standard | 4 |
| 3 | Pro | 8 |

Image Studio runs on its own pool and does **not** consume this quota — a suite and a
video generation can run at the same time.

### Multiple LoRAs

```bash
python3 scripts/phosor_client.py submit "A person dancing" \
  --loras '[{"lora_id": "lora-abc", "lora_scale": 0.8}, {"lora_id": "lora-def", "lora_scale": 0.5}]'
```

### Two-Step Upload Rule

Files must be uploaded before use — direct URLs are NOT supported in `submit --image-url`:

1. **Image** → `upload-image` / `import-image` → returns `s3_key` → use as `--image-url`
2. **LoRA** → `upload-lora` / `import-lora` → returns `lora_id` → use as `--lora-id`

## Queue Flow

```
PENDING → PROCESSING → COMPLETED / FAILED
```

The `poll` command checks all locally-tracked pending jobs and removes completed/failed ones.

## MiniMax H3 Pricing (per output second)

| Tier | USD/sec | Credits/sec |
|------|---------|-------------|
| 480p | $0.02 | 0.2 |
| 768p | $0.04 | 0.4 |

### Ref2VA Pricing (`minimax/h3/reference-to-video`)

Billed in two parts — the output **plus** the reference inputs:

```
total = duration x base_rate
      + reference_images x $0.010
      + reference_audios x $0.010
      + reference_video_seconds x base_rate
```

| Tier | Base USD/sec | Reference image | Reference audio | Reference video USD/sec |
|------|--------------|-----------------|-----------------|-------------------------|
| 480p | $0.025 | $0.010 each | $0.010 each | $0.025 |
| 768p | $0.063 | $0.010 each | $0.010 each | $0.063 |

Example — 5s at 768p with 4 reference images: `5 x $0.063 + 4 x $0.010 = $0.355` (3.55 credits).

> Ref2VA's base rate is higher than plain H3 T2V/I2V — do not reuse the table above for it.

## Wan Video Pricing (per frame)

| Tier | Standard | + LoRA | Turbo |
|------|----------|--------|-------|
| 480p | $0.0009375 | $0.00125 | $0.0003125 |
| 512p | $0.0013125 | $0.001625 | $0.0004375 |
| 720p | $0.001875 | $0.0021875 | $0.000625 |
| 1080p | $0.0025 | $0.003 | $0.0010938 |

LoRA multiplier on turbo: 1.2x.

## S2V Pricing (per frame)

| Tier | Cost |
|------|------|
| 480p | $0.0009375 |
| 512p | $0.0013125 |
| 720p | $0.001875 |

## Animate Pricing (per frame)

| Tier | Cost |
|------|------|
| 480p | $0.00125 |
| 512p | $0.00175 |
| 720p | $0.0025 |

## Image Pricing (per image)

| Model | USD | Credits |
|-------|-----|---------|
| GPT Image 2 T2I | $0.03 | 0.3 |
| FLUX.2-dev T2I | $0.006 | 0.06 |
| FLUX.2-dev Image Edit | $0.012 | 0.12 |
| qwen-image T2I | $0.015 | 0.15 |
| qwen-image T2I + LoRA | $0.018 | 0.18 |
| qwen-image-edit | $0.003 | 0.03 |
| z-image turbo (T2I / I2I) | $0.0025 | 0.025 |
| z-image turbo + LoRA | $0.003 | 0.03 |

Flat per image at every resolution. Multiply by `num_images` (1–4) where the model
supports it; FLUX.2-dev is fixed at 1 image per request.

## Audio Pricing

| Item | Cost |
|------|------|
| Qwen3-TTS | $0.00003 per character |
| Minimum charge | $0.003 per request |

Exchange rate: 10 credits = $1 USD. Credits pre-deducted, auto-refunded on failure.
Live rates: `GET /api/v1/pricing/config` — always prefer it over any table here.
