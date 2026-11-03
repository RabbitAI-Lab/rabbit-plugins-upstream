---
name: wavespeed-kling-40
description: Generate and edit videos with Kuaishou Kling 4.0 via WaveSpeed AI. Covers text-to-video, image-to-video with first, last and in-between keyframes, reference-to-video (up to 10 images, 5 videos and 3 audios), video edit and video extend, with 3-30 second clips at 720p or 1080p and synchronized stereo audio. Use when the user asks for Kling 4.0, or wants to create a video from a prompt, direct an image animation with keyframes, build a clip from reference media, rewrite an existing video, or continue a clip.
metadata:
  author: wavespeedai
  version: "1.0"
---

# WaveSpeedAI Kling 4.0 Video Generation

Generate and edit videos with Kuaishou's Kling 4.0 on the WaveSpeed AI platform. Text, image and reference inputs produce 3-30 second clips at 720p or 1080p with synchronized stereo audio; video edit rewrites an existing clip and video extend appends a new segment.

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

The shortcut commands use the same model and pick the endpoint from the inputs: `wavespeed generate video "<prompt>" -m kling-4.0`, and likewise `wavespeed edit video` and `wavespeed extend video`; the MCP tools `generate_video`, `edit_video` and `extend_video` take the same `model` value (confirm the keys with `wavespeed generate video --help`). Add `--estimate --json` first to see the chosen endpoint, final input and price without submitting.

```bash
wavespeed generate video "A paper boat drifting down a rain-soaked street" -m kling-4.0 --estimate --json
```

### Text-to-Video

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/text-to-video \
  -p "A golden retriever running through a field of sunflowers at sunset, slow tracking shot" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

The `image` parameter accepts an image URL. If you have a local file, pass it with the `@path` marker and the CLI uploads it and substitutes the hosted URL.

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/image-to-video \
  -i image=@./photo.png \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/image-to-video \
  -i image="https://example.com/photo.jpg" \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

`duration` is an integer from 3 to 30 seconds on every endpoint, and `resolution` is `720p` or `1080p`.

### Text-to-Video

**Model ID:** `kwaivgi/kling-v4.0/text-to-video`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | What to generate |
| `aspect_ratio` | string | No | `16:9` | One of: `16:9`, `9:16`, `1:1`, `21:9` |
| `duration` | integer | No | `5` | Seconds. Range: 3-30 |
| `resolution` | string | No | `720p` | One of: `720p`, `1080p` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/text-to-video \
  -p "A timelapse of a city skyline transitioning from day to night, cinematic slow pan" \
  -i aspect_ratio="21:9" \
  -i duration=10 \
  -i resolution="1080p" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

**Model ID:** `kwaivgi/kling-v4.0/image-to-video`

Animates a first frame, optionally toward a last frame and through ordered in-between keyframes.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | First-frame image URL (.jpg/.jpeg/.png) |
| `prompt` | string | No | -- | Motion description (may be empty) |
| `last_image` | string | No | -- | Last-frame image URL |
| `keyframes` | string[] | No | -- | Middle frames in order, up to 9; `image`, `last_image` and `keyframes` together are at most 10 |
| `aspect_ratio` | string | No | -- | One of: `16:9`, `9:16`, `1:1`, `21:9`. Leave out to follow the first frame |
| `duration` | integer | No | `5` | Seconds. Range: 3-30 |
| `resolution` | string | No | `720p` | One of: `720p`, `1080p` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/image-to-video \
  -i image=@./sketch-1.png \
  -i keyframes='["@./sketch-2.png", "@./sketch-3.png"]' \
  -i last_image=@./sketch-4.png \
  -p "A seed sprouts, grows into a sapling and blossoms, steady camera" \
  -i duration=10 \
  --json | jq -r '.outputs[0]')
```

### Reference-to-Video

**Model ID:** `kwaivgi/kling-v4.0/reference-to-video`

Builds a new clip that follows the subjects, motion and camera you point to. In the prompt, refer to inputs as `@Image1`, `@Image2`, ..., `@Video1`, ... and `@Audio1`, ... in array order.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Scene description that names each reference |
| `images` | string[] | No | -- | Up to 10 reference image URLs |
| `videos` | string[] | No | -- | Up to 5 reference video URLs for motion, camera and pacing (up to 30 s used in total) |
| `audios` | string[] | No | -- | Up to 3 reference audio URLs, 5-30 s each, to guide voice and sound |
| `keep_original_sound` | boolean | No | `false` | Keep the reference video's sound instead of generating new audio. Requires `videos` |
| `aspect_ratio` | string | No | `auto` | One of: `auto`, `16:9`, `9:16`, `1:1`, `21:9`. `auto` follows the references |
| `duration` | integer | No | `5` | Seconds. Range: 3-30 |
| `resolution` | string | No | `720p` | One of: `720p`, `1080p` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/reference-to-video \
  -i images='["@./character.png", "@./product.png"]' \
  -p "@Image1 picks up @Image2 from a cafe table and shows it to the camera, warm morning light" \
  -i aspect_ratio="9:16" \
  --json | jq -r '.outputs[0]')
```

### Video Edit

**Model ID:** `kwaivgi/kling-v4.0/video-edit`

Keeps the scene, subject and motion of a 3-30 second video and changes what you describe (longer videos are trimmed to 30 s). Refer to the video as `@Video1`, to images as `@Image1`, ... and audios as `@Audio1`, ...

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video to edit |
| `prompt` | string | Yes | -- | The edit: subject, setting, weather or style |
| `images` | string[] | No | -- | Up to 10 reference image URLs for a subject, object or style |
| `audios` | string[] | No | -- | Up to 3 reference audio URLs, 5-30 s each |
| `keep_original_sound` | boolean | No | `true` | Keep the input video's sound; `false` generates new synchronized audio |
| `aspect_ratio` | string | No | -- | One of: `16:9`, `9:16`, `1:1`, `21:9`. Follows the input if not set |
| `duration` | integer | No | -- | Seconds, 3-30. Follows the input length if not set |
| `resolution` | string | No | `720p` | One of: `720p`, `1080p` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/video-edit \
  -i video=@./street.mp4 \
  -i images='["@./red-jacket.png"]' \
  -p "Dress the man in @Video1 in the jacket from @Image1, keep everything else unchanged" \
  --json | jq -r '.outputs[0]')
```

### Video Extend

**Model ID:** `kwaivgi/kling-v4.0/video-extend`

Generates a new segment from the input video's last frame and returns the original and the new segment joined; audio is generated with the picture.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video to extend |
| `prompt` | string | Yes | -- | The continuation: action, camera movement, lighting and sound |
| `last_image` | string | No | -- | Target last-frame image URL for the new segment |
| `duration` | integer | No | `5` | Length of the new segment in seconds. Range: 3-30 |
| `resolution` | string | No | `720p` | One of: `720p`, `1080p` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run kwaivgi/kling-v4.0/video-extend \
  -i video=@./clip.mp4 \
  -p "The camera pulls back to reveal the whole valley as the sun sets" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')
```

## Pricing

Estimates for a 5-second clip; cost scales with duration (10 s at 720p is $1.57). Video edit and reference-to-video with a reference video are also priced on the input video, so those rows assume a 5-second input; quote exact inputs with `wavespeed price <model-id> ... --upload`. Prices may change; see `https://wavespeed.ai/models/<model-id>` (e.g. [text-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0/text-to-video)).

| Endpoint | 720p | 1080p |
|----------|------|-------|
| text-to-video / image-to-video | $0.785 | $1.175 |
| reference-to-video (images only) | $0.785 | $1.175 |
| reference-to-video (5 s reference video) | $0.94 | $1.41 |
| video-edit (5 s input) | $0.94 | $1.41 |
| video-extend (5 s new segment) | $0.785 | $1.175 |

## Prompt Tips

- Describe subject, action, camera movement and the sound you want; audio is generated with the picture
- Use `keyframes` and `last_image` in image-to-video to direct a sequence of story beats in order
- Name every reference by its tag (`@Image1`, `@Video1`, `@Audio1`) and say what each contributes
- For video edit, state what must stay unchanged; set `keep_original_sound: false` only when the new scene needs new audio
- Use `21:9` for ultrawide cinematic shots and `9:16` for vertical social video

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run kwaivgi/kling-v4.0/text-to-video -h

# Estimate the cost (no generation, no charge)
wavespeed price kwaivgi/kling-v4.0/text-to-video -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run kwaivgi/kling-v4.0/text-to-video -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run kwaivgi/kling-v4.0/text-to-video -i <field>=@./local-file.png --json

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
