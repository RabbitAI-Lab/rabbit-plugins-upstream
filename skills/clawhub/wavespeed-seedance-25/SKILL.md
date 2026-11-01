---
name: wavespeed-seedance-25
description: Generate and edit videos with ByteDance Seedance 2.5 via WaveSpeed AI. Covers text-to-video, image-to-video (first and last frame), reference-to-video (up to 30 images, 10 videos and 10 audios), video edit and video extend, plus faster Turbo variants, with 4-30 second clips at up to 4K and native synchronized audio. Use when the user asks for Seedance 2.5, or wants to create a video from a prompt, animate an image, keep characters or products consistent across references, restyle an existing video, or continue a clip.
metadata:
  author: wavespeedai
  version: "1.0"
---

# WaveSpeedAI Seedance 2.5 Video Generation

Generate and edit videos with ByteDance's Seedance 2.5 on the WaveSpeed AI platform. Text, image and reference inputs produce 4-30 second clips at 480p to 4K with native audio; video edit restyles an existing clip and video extend appends a new segment. Turbo variants offer 720p/1080p at a lower price.

## Setup

Install the open-source CLI once and sign in; the CLI stores the key, so never ask the user to paste an API key into the chat:

```bash
npm install -g @wavespeed/cli
wavespeed login          # opens https://wavespeed.ai/accesskey and stores the key
wavespeed status         # confirms you are signed in
```

For CI or one-off shells, `WAVESPEED_API_KEY` in the environment also works.

Prefer MCP tools over shell commands? The same platform is exposed as an MCP server: hosted at `https://api.wavespeed.ai/mcp` (browser sign-in) or locally with `npx -y @wavespeed/mcp@latest`; every example below maps onto `run_model` with the same model id and input fields.

## Quick Start

The shortcut commands use the same model and pick the endpoint from the inputs: `wavespeed generate video "<prompt>" -m seedance-2.5` (or `-m seedance-2.5-turbo`), and likewise `wavespeed edit video` and `wavespeed extend video`; the MCP tools `generate_video`, `edit_video` and `extend_video` take the same `model` value (confirm the keys with `wavespeed generate video --help`). Add `--estimate --json` first to see the chosen endpoint, final input and price without submitting.

```bash
wavespeed generate video "A paper boat drifting down a rain-soaked street" -m seedance-2.5 --estimate --json
```

### Text-to-Video

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/text-to-video \
  -p "A golden retriever running through a field of sunflowers at sunset, slow tracking shot" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

The `image` parameter accepts an image URL. If you have a local file, pass it with the `@path` marker and the CLI uploads it and substitutes the hosted URL.

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/image-to-video \
  -i image=@./photo.png \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/image-to-video \
  -i image="https://example.com/photo.jpg" \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

Every endpoint has a Turbo twin (`text-to-video-turbo`, `image-to-video-turbo`, `reference-to-video-turbo`, `video-edit-turbo`) with the same fields but `resolution` limited to `720p` or `1080p`. Also in the catalog: `bytedance/seedance-2.5/motion-control` (a character from a picture or description performs the motion of a reference video), `bytedance/seedance-2.5/talking-avatar` (animates a portrait from an audio recording, 480p/720p) and `bytedance/seedance-2.5/image-to-video-spicy`; inspect them with `wavespeed run <id> -h`.

### Text-to-Video

**Model ID:** `bytedance/seedance-2.5/text-to-video` (Turbo: `bytedance/seedance-2.5/text-to-video-turbo`)

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Scene, action, camera movement and mood |
| `aspect_ratio` | string | No | `16:9` | One of: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, `21:9` |
| `duration` | integer | No | `5` | Seconds. Range: 4-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p`, `4k` (Turbo: `720p`, `1080p`) |
| `generate_audio` | boolean | No | `true` | Generate native audio synchronized with the video |
| `reference_images` | string[] | No | -- | Up to 30 image URLs to guide style, characters or composition |
| `reference_videos` | string[] | No | -- | Up to 10 video URLs (total length at most 30 s) |
| `reference_audios` | string[] | No | -- | Up to 10 audio URLs (total length at most 30 s) |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/text-to-video \
  -p "A timelapse of a city skyline transitioning from day to night, cinematic slow pan" \
  -i aspect_ratio="21:9" \
  -i duration=10 \
  -i resolution="1080p" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

**Model ID:** `bytedance/seedance-2.5/image-to-video` (Turbo: `bytedance/seedance-2.5/image-to-video-turbo`)

The output follows the start image's framing; there is no `aspect_ratio` field.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | Start image URL |
| `prompt` | string | Yes | -- | Scene, action, camera movement and mood |
| `last_image` | string | No | -- | Last-frame image URL |
| `duration` | integer | No | `5` | Seconds. Range: 4-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p`, `4k` (Turbo: `720p`, `1080p`) |
| `generate_audio` | boolean | No | `true` | Generate native audio synchronized with the video |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/image-to-video \
  -i image=@./start-frame.png \
  -i last_image=@./end-frame.png \
  -p "Smooth transition from day to night as the lights come on" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')
```

### Reference-to-Video

**Model ID:** `bytedance/seedance-2.5/reference-to-video` (Turbo: `bytedance/seedance-2.5/reference-to-video-turbo`)

Keeps characters, products or scenes consistent with reference media. Provide at least one reference image, video or audio; with none, the request runs as text-to-video. In the prompt, refer to inputs as `@Image 1`, `@Video 1`, `@Audio 1` (in upload order) and say what each is for.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Scene description that names each reference and its role |
| `reference_images` | string[] | No | -- | Up to 30 image URLs (characters, products, scenes, style) |
| `reference_videos` | string[] | No | -- | Up to 10 video URLs for motion, camera work or a character (total at most 30 s) |
| `reference_audios` | string[] | No | -- | Up to 10 audio URLs for voice, music or sound style (total at most 30 s) |
| `aspect_ratio` | string | No | `16:9` | One of: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, `21:9` |
| `duration` | integer | No | `5` | Seconds. Range: 4-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p`, `4k` (Turbo: `720p`, `1080p`) |
| `generate_audio` | boolean | No | `true` | Generate native audio synchronized with the video |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/reference-to-video \
  -i reference_images='["@./character.png", "@./product.png"]' \
  -p "@Image 1 picks up @Image 2 from a cafe table and shows it to the camera, warm morning light" \
  -i aspect_ratio="9:16" \
  --json | jq -r '.outputs[0]')
```

### Video Edit

**Model ID:** `bytedance/seedance-2.5/video-edit` (Turbo: `bytedance/seedance-2.5/video-edit-turbo`)

The input video drives subject identity, composition and motion while the prompt rewrites lighting, style, weather, environment or specific elements. Videos longer than 30 s are trimmed to 30 s; shorter than 4 s are padded to 4 s.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video to edit |
| `prompt` | string | Yes | -- | The edit to apply |
| `reference_images` | string[] | No | -- | Up to 30 image URLs to guide the edit (subject identity, style) |
| `reference_audios` | string[] | No | -- | Up to 10 audio URLs to guide audio generation |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p`, `4k` (Turbo: `720p`, `1080p`) |
| `generate_audio` | boolean | No | `true` | Generate new audio; `false` keeps the input video's audio track |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/video-edit \
  -i video=@./street.mp4 \
  -p "Turn the scene into a snowy winter evening, keep the people and their motion" \
  -i generate_audio=false \
  --json | jq -r '.outputs[0]')
```

### Video Extend

**Model ID:** `bytedance/seedance-2.5/video-extend`

Appends a new segment that continues from the end of the input video (the last 30 s are used as context).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video to extend |
| `prompt` | string | Yes | -- | The continuation: action, camera movement, lighting, mood |
| `duration` | integer | No | `5` | Length of the new segment in seconds. Range: 4-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p`, `4k` |
| `generate_audio` | boolean | No | `true` | Generate native audio for the new segment |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-2.5/video-extend \
  -i video=@./clip.mp4 \
  -p "The camera pulls back to reveal the whole valley as the sun sets" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')
```

## Pricing

Estimates for a 5-second clip at default settings; cost scales with duration (10 s at 720p is $3.60). Turning off `generate_audio` does not change the price. Endpoints that take a video are also priced on the input video, so the edit and extend rows assume a 5-second input; quote exact inputs with `wavespeed price <model-id> ... --upload`. Prices may change; see `https://wavespeed.ai/models/<model-id>` (e.g. [text-to-video](https://wavespeed.ai/models/bytedance/seedance-2.5/text-to-video)).

| Endpoint | 480p | 720p | 1080p | 4k |
|----------|------|------|-------|----|
| text-to-video / image-to-video / reference-to-video (images) | $0.90 | $1.80 | $4.50 | $9.00 |
| text / image / reference-to-video Turbo | -- | $1.00 | $1.10 | -- |
| video-edit (5 s input) | $1.10 | $2.20 | $5.50 | -- |
| video-edit Turbo (5 s input) | -- | $1.20 | $1.30 | -- |
| video-extend (5 s input, 5 s new segment) | $1.10 | $2.20 | $5.50 | -- |

A reference-to-video request with a 5-second reference video is $2.20 at 720p.

## Prompt Tips

- Describe scene, subject action, camera movement and mood; name the camera move explicitly ("slow dolly in", "handheld tracking shot")
- Describe the sound you want (dialogue, ambience, music); audio is generated with the picture by default
- In reference-to-video, name each input by its tag (`@Image 1`, `@Video 1`, `@Audio 1`) and say what it is for ("@Image 1 is the main character", "follow the camera move of @Video 1")
- For video edit, say what must stay ("keep the people and their motion") as well as what changes
- Draft at 480p or with a Turbo endpoint, then render the final take at 1080p or 4K

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run bytedance/seedance-2.5/text-to-video -h

# Estimate the cost (no generation, no charge)
wavespeed price bytedance/seedance-2.5/text-to-video -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run bytedance/seedance-2.5/text-to-video -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run bytedance/seedance-2.5/text-to-video -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

A `run` that fails with a gateway or network error (502/503/504, connection reset, timeout) does NOT mean the task failed, and the submit request is never retried automatically, so re-running can create a duplicate paid task. Do not re-run immediately. If the error contains a task id (`task_id` / prediction id), keep checking it with `wavespeed show <id> --json` until its status is terminal (`completed`, `failed`, `cancelled`, `timeout`, `deleted`). If no id was returned, check recent predictions with `wavespeed history --json` (add `--model <id>`; default window is the last 24h) and re-run once only if none matches. A client-side wait timeout or an interrupted `run` does not mean the task failed: tasks can run for a long time, so do not give up after a fixed time.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
