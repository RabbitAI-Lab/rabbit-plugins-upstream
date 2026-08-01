---
name: seedance
description: Generate videos with the doubao-seedance-2.0 model (text-to-video, image-to-video, first/last-frame-to-video). Use when the user asks to "generate a video", mentions "seedance", or wants AI video generation from text and/or images. Wraps the asynchronous Volcengine Ark / OpenAI-style video API behind one synchronous call.
allowed-tools: Bash, Read, Write, AskUserQuestion
---

# seedance — doubao-seedance-2.0 video generation

This skill generates a video with the **doubao-seedance-2.0** model by running
`scripts/seedance.py` (paths below are relative to this skill's directory, i.e.
the folder containing this `SKILL.md`). The script is synchronous: it creates a
task, polls until completion, and prints the result (including the video URL).

## When to use

Trigger this skill when the user's request mentions **"seedance"** or asks to
**"generate a video"** / produce AI video from text, an image, or first/last
frames. Also trigger on explicit `/seedance`.

Do **not** trigger for image-only generation, audio, or general chat.

## Prerequisites (check before running)

- **Python 3.11+**. The entrypoint wrapper (`scripts/seedance`) auto-selects
  `python3.11`/`python3.12` when available (some proxies' TLS cert chain is
  rejected by Python 3.14; `python3` is fine for the raw Ark API), so you do not
  pick the interpreter by hand.
- The same wrapper creates an isolated virtualenv at `<skill_dir>/.venv` on
  first run and installs `requirements.txt` there automatically. The only Python
  dependency is `alibabacloud_oss_v2` — pulled in only when the user supplies
  **local image files** (uploaded to Alibaba OSS as a signed URL), but harmless
  to install regardless. No manual `pip install` is needed.
- **`ARK_API_KEY`** is required. It may be a real env var or stored in a `.env`
  file (in the skill dir or the user's cwd). If absent, ask the user for it and
  offer to write it to `<skill_dir>/.env` (never print the value back).
- Optional env overrides: `ARK_API_TYPE` (`ark`/`openai-video`/`openai`),
  `ARK_MODEL` (model id), `ARK_ENDPOINT`. All are lower priority than their CLI
  flags (`--api-type`, `-m`, `--endpoint`). For **local images** also:
  `OSS_ACCESS_KEY_ID`, `OSS_ACCESS_KEY_SECRET` (required), and optionally
  `OSS_ENDPOINT`, `OSS_BUCKET` (default `jiangsier`), `OSS_KEY_PREFIX` (default `dev/`).

## Extract options from the user's query

Map the user's natural-language request to these CLI options:

| User intent | CLI option |
|---|---|
| The video prompt / description | `-t` / `--text` (required) |
| A local reference image file | `-i` / `--image` |
| An online reference image URL | `--image-url` |
| A local first-frame image | `-f` / `--first-frame` |
| An online first-frame URL | `--first-frame-url` |
| A local last-frame image | `-l` / `--last-frame` |
| An online last-frame URL | `--last-frame-url` |
| "5 seconds", "10s", duration | `--duration` (default 5) |
| "16:9", "vertical/9:16", "square/1:1", "follow the image" | `--ratio` (default 16:9; use `adaptive` when an image is provided and the user wants the output to match it) |
| "720p", "1080p", "4k" | `--resolution` (default 720p) |
| A specific model id | `-m` / `--model` (or `ARK_MODEL` env) |
| Which backend protocol | `--api-type` (default `ark`; or `ARK_API_TYPE` env). `ark` = raw Volcengine Ark (audio). `openai-video` = openai-video endpoint, `doubao-seedance-2.0-mini` (silent). `openai` = openai chat-mirror entry, `doubao-seedance-2.0` full (silent). |
| Reproducible result | `--seed` (ark/openai only; openai-video ignores it) |
| Save the mp4 locally | `--save <path>` |

Rules (enforced by the script; surface them to the user when relevant):
- `--image` and `--image-url` are mutually exclusive (same for first/last frame).
- A reference image (`--image`/`--image-url`) cannot be combined with explicit
  first/last frames.
- `--last-frame` requires `--first-frame`.
- `--ratio adaptive` requires an image input.

## Ask proactively, then confirm

1. **Prompt**: if the user's request does not contain a usable video prompt,
   ask for one (it is required).
2. **API key**: if `ARK_API_KEY` is not in the environment or a `.env`, ask the
   user for it (offer to store it in `<skill_dir>/.env`).
3. **Ambiguous image role**: if the user gives an image without saying whether
   it is a reference, first frame, or last frame, ask.
4. **Confirm before running** — generation costs quota and runs for minutes.
   Summarize the resolved options and use `AskUserQuestion` (or just ask) to get
   explicit confirmation, including: prompt, image inputs, duration, ratio,
   resolution, model, api-type. Proceed only after the user confirms.

## Invocation

Resolve `<skill_dir>` (this directory). Load secrets from `<skill_dir>/.env` if
present via `--env-file`. Run the skill through the **`scripts/seedance`** wrapper
— it provisions an isolated venv (with `requirements.txt` installed) and forwards
every argument to `scripts/seedance.py`, picking `python3.11`/`python3.12` for the
proxy-TLS-safe interpreter automatically. The same wrapper serves all three
`--api-type` values; no interpreter switch is needed between them.

```bash
# Ark (default) — also covers openai-video / openai; just pass --api-type
<skill_dir>/scripts/seedance --env-file <skill_dir>/.env \
  -t "<prompt>" [-i ./local.png | --image-url <url>] [-f ./first.png -l ./last.png] \
  [--duration 5] [--ratio 16:9] [--resolution 720p] [-m <model>] [--save out.mp4]

<skill_dir>/scripts/seedance --api-type openai-video --env-file <skill_dir>/.env -t "<prompt>" ...
<skill_dir>/scripts/seedance --api-type openai      --env-file <skill_dir>/.env -t "<prompt>" ...
```

The script prints the full task result as JSON on stdout and the `video_url` on
stderr. On success, report the video URL to the user; if `--save` was given,
confirm the saved path.

To run the test suite (offline, no key needed): `<skill_dir>/scripts/seedance test_seedance.py`.
The wrapper reuses the same venv for any script in `scripts/` — pass its filename
as the first argument.

## Examples

- "Generate a 5s video of a daisy field under a blue sky, camera pushing in"
  → `scripts/seedance -t "a daisy field under a blue sky, camera pushing in" --duration 5`
- "Make a video from this image ./fox.png — the camera slowly pulls out, hair blowing in the wind"
  → `scripts/seedance -t "camera slowly pulls out, hair blowing in the wind" -i ./fox.png --ratio adaptive`
- "Animate between these two frames: ./first.jpeg and ./last.jpeg, 360° orbit"
  → `scripts/seedance -t "360 degree orbit" -f ./first.jpeg -l ./last.jpeg --ratio adaptive`
- "Generate a vertical 1080p 10s clip of waves at sunset"
  → `scripts/seedance -t "waves at sunset" --ratio 9:16 --resolution 1080p --duration 10`

## Notes

- Fixed per-spec params (ark + openai): `generate_audio=true`, `watermark=false`
  (not exposed). The openai-video body omits these. Both `openai-video` and
  `openai` yield **silent video** on this backend — only `ark` produces audio.
- Three API protocols (`--api-type`, or `ARK_API_TYPE` env): `ark` (default;
  Volcengine Ark, `POST /contents/generations/tasks`, audio), `openai-video`
  (`POST /video/generations`, OpenAI-video body `seconds`/`size`/`input_reference`,
  model `doubao-seedance-2.0-mini`, silent), and `openai` (`POST /video/generations`,
  Ark-shaped body, model `doubao-seedance-2.0` full, silent — the proxy's chat-mirror
  entry; `/v1/chat/completions` returns `unsupported_model_endpoint` here). The script
  normalizes all three into `{id, status, video_url, error, raw}`.
- Default model id: `doubao-seedance-2-0-260128` (ark) / `doubao-seedance-2.0-mini`
  (openai-video) / `doubao-seedance-2.0` (openai). Override with `-m` or `ARK_MODEL`.
- `reference.md` (in this skill's directory) is the upstream Volcengine Ark
  video-generation doc; consult it for advanced/parameter details.
- Local images are uploaded to Alibaba OSS with a 10-minute signed URL, then
  that URL is used as the model input.
