# seedance

An agent skill that generates videos with the **doubao-seedance-2.0** model (text-to-video, image-to-video, first/last-frame-to-video). It triggers when you ask to "generate a video" or mention "seedance", extracts the options from your request, confirms them with you, then runs a synchronous wrapper that creates the task, polls until it finishes, and returns the video URL.

It is a standard `SKILL.md` skill and runs on any compatible agent runtime (Claude Code, OpenClaw, and others).

Video generation on the backend is asynchronous (submit a task → poll status until done). This skill hides that behind one call.

## Layout

```
seedance/
├── SKILL.md            # skill definition + agent instructions
├── scripts/
│   ├── seedance        # venv entrypoint wrapper (provisions .venv, runs seedance.py)
│   ├── seedance.py     # the synchronous wrapper (stdlib-only Python)
│   └── test_seedance.py
├── reference.md        # upstream Volcengine Ark video-generation doc
├── requirements.txt    # alibabacloud_oss_v2 (only for local image upload)
├── README.md           # this file
└── README.zh-CN.md     # Chinese README
```

All script paths in the skill are relative to the skill directory (the folder containing `SKILL.md`).

## Dependencies

- **Python 3.11+**. You don't pick the interpreter yourself: the `scripts/seedance` wrapper auto-selects `python3.11`/`python3.12` when available (some OpenAI-style proxies serve a TLS chain that Python 3.14 rejects via a stricter CA key-usage check) and only falls back to `python3` if those are missing.
- The wrapper provisions an isolated virtualenv at `.venv/` (next to `SKILL.md`) on first run and installs `requirements.txt` into it automatically — no manual `pip install` is needed. `alibabacloud_oss_v2` is the only third-party dependency, required solely when you pass **local image files** (`-i`/`-f`/`-l`, uploaded to Alibaba OSS as a short-lived signed URL). Text-to-video and online image URLs need no third-party package.
- Override the venv location with `SKILL_VENV_DIR=<path>`. The generated `.venv/` is a build artifact — gitignore it, don't commit it.

## Environment variables

Set in the real environment or a `.env` file (loaded automatically; real env wins over the file):

| Variable | Required | Description |
|---|---|---|
| `ARK_API_KEY` | yes | API key for the model |
| `ARK_ENDPOINT` | no | endpoint; default `https://ark.cn-beijing.volces.com/api/v3` |
| `ARK_API_TYPE` | no | `ark` / `openai-video` / `openai` (lower priority than `--api-type`) |
| `ARK_MODEL` | no | model id (lower priority than `-m`) |
| `ARK_INSECURE` | no | `1` to skip TLS verification (see TLS note) |
| `OSS_ACCESS_KEY_ID` | for local images | Alibaba Cloud AccessKey ID |
| `OSS_ACCESS_KEY_SECRET` | for local images | Alibaba Cloud AccessKey Secret |
| `OSS_ENDPOINT` | no | OSS region or full host, e.g. `cn-beijing` or `oss-cn-beijing.aliyuncs.com` |
| `OSS_BUCKET` | no | bucket (default `jiangsier`) |
| `OSS_KEY_PREFIX` | no | object key prefix (default `dev/`) |

Never commit `.env` — it holds live keys (it's gitignored).

## Using the skill

Just ask in natural language, e.g.:

- "Generate a 5-second video of a daisy field under a blue sky, camera pushing in"
- "Make a video from ./fox.png — camera slowly pulls out, hair blowing in the wind"
- "Animate between ./first.jpeg and ./last.jpeg with a 360° orbit"

The skill extracts the options, asks for anything missing or ambiguous, and confirms with you before running (generation costs quota and runs for minutes).

## CLI reference

You can also run it directly through the `scripts/seedance` wrapper, which provisions its own isolated venv (interpreter chosen for you — see TLS note):

```bash
# text-to-video (Ark, default)
scripts/seedance -t "a daisy field, camera pushing in"

# image-to-video (local image → uploaded to OSS)
scripts/seedance -t "camera pulls out" -i ./fox.png --ratio adaptive

# first + last frame
scripts/seedance -t "360 orbit" -f ./first.jpeg -l ./last.jpeg --ratio adaptive

# online image URL
scripts/seedance -t "camera pulls out" --image-url https://example.com/fox.png

# openai-video (mini) — same wrapper, just pass --api-type
scripts/seedance --api-type openai-video -t "a daisy field, camera pushing in"

# openai (full, Ark-shaped body)
scripts/seedance --api-type openai -t "a daisy field, camera pushing in"
```

### Options

| Option | Description | Default |
|---|---|---|
| `-t` / `--text` | prompt (required) | — |
| `-i` / `--image` | local reference image file | — |
| `--image-url` | online reference image URL (mutually exclusive with `--image`) | — |
| `-f` / `--first-frame` | local first-frame image file | — |
| `--first-frame-url` | online first-frame image URL | — |
| `-l` / `--last-frame` | local last-frame image file (requires `--first-frame`) | — |
| `--last-frame-url` | online last-frame image URL | — |
| `--duration` | duration in seconds | `5` |
| `--ratio` | aspect ratio (`16:9`/`9:16`/`1:1`/…; `adaptive` follows the input image) | `16:9` |
| `--resolution` | `480p`/`720p`/`1080p`/`4k` | `720p` |
| `-m` / `--model` | model id (CLI > `ARK_MODEL` env > per-type default) | ark → `doubao-seedance-2-0-260128`; openai-video → `doubao-seedance-2.0-mini`; openai → `doubao-seedance-2.0` |
| `--api-type` | `ark` / `openai-video` / `openai` (CLI > `ARK_API_TYPE` env > `ark`) | `ark` |
| `--seed` | reproducibility seed (ark/openai only; openai-video ignores) | — |
| `--save` | download the generated mp4 to this path | — |
| `--poll-interval` | seconds between status polls | `10` |
| `--timeout` | max seconds to wait | `1800` |
| `--endpoint` | override `ARK_ENDPOINT` | — |
| `--insecure` | skip TLS verification | off |
| `--env-file` | path to a `.env` file | `.env` |

Fixed per spec (ark + openai paths): `generate_audio=true`, `watermark=false`. The openai-video body omits these (it has no such params). Both `openai-video` and `openai` produce **silent video** on this backend — use `ark` for audio.

### Conflict rules (validated before running)

- `--image` vs `--image-url` (and `--first-frame` vs `--first-frame-url`, `--last-frame` vs `--last-frame-url`) cannot both be given.
- A reference image (`--image`/`--image-url`) cannot combine with explicit first/last frames.
- `--last-frame` requires `--first-frame`.
- `--ratio adaptive` requires an image input.

## Three API types (`--api-type`, default `ark`)

| | `openai-video` | `openai` | `ark` |
|---|---|---|---|
| create | `POST /video/generations` | `POST /video/generations` | `POST /contents/generations/tasks` |
| request body | `{model, prompt, seconds(str,4/8/12), size(WxH), input_reference?(comma-joined URLs)}` | `{model, prompt, generate_audio, ratio, duration, watermark, resolution, image?, first_frame?, last_frame?, seed?}` | `{model, content:[{type:text},{type:image_url,role}], …}` |
| poll | `GET /video/generations/{id}` | `GET /video/generations/{id}` | `GET /contents/generations/tasks/{id}` |
| status values | `queued` / `IN_PROGRESS` / `SUCCESS` | `queued` / `IN_PROGRESS` / `SUCCESS` | `queued` / `running` / `succeeded` |
| video URL | `data.result_url` | `data.result_url` | `content.video_url` |
| default model | `doubao-seedance-2.0-mini` | `doubao-seedance-2.0` | `doubao-seedance-2-0-260128` |
| audio | no | no | yes |

`reference.md` is the upstream Volcengine Ark doc; the `ark` path follows it. `openai-video` and `openai` share the `/video/generations` transport and `{code, data:{…}}` response; they differ only in body shape and default model.

- **`openai-video`** — OpenAI-video-style body (`seconds`/`size`/`input_reference`); model `doubao-seedance-2.0-mini`. **`seconds` must be a string** (snapped from `--duration` to `{4,8,12}`); **`input_reference` is a comma-joined URL string** (one = reference image / first frame, two = first+last frame). `--ratio`/`--resolution` map to `size`; `--seed` is ignored.
- **`openai`** — the proxy's "openai" (chat-mirror) entry, Ark-shaped body (`image`/`first_frame`/`last_frame`/`generate_audio`/`ratio`/`duration`/`watermark`/`resolution`/`seed`); model `doubao-seedance-2.0` (full). The marketplace lists this at `/v1/chat/completions`, but that path returns `unsupported_model_endpoint` here, so the full model is reached via `/video/generations`. `--seed` is supported.
- **`ark`** — raw Volcengine Ark API; the only path that produces **audio**.

## TLS note (environment-specific)

Some OpenAI-style proxies are load-balanced across backend nodes that intermittently serve a certificate chain whose intermediate CA lacks the `keyUsage` extension. CPython 3.14 rejects those nodes; 3.11 accepts them all. The wrapper has retry logic to ride through it under 3.14, but `python3.11` is the reliable choice for the `openai-video` / `openai` paths. For the `ark` path, `python3` is fine. The `scripts/seedance` wrapper prefers `python3.11`/`python3.12` automatically, so you don't manage this by hand. `--insecure`/`ARK_INSECURE` disables verification but many proxies' WAFs 403 unverified-TLS handshakes, so it does not help there.

## Tests

```bash
scripts/seedance test_seedance.py                                                  # offline suite (no key/network)
cd scripts && ../.venv/bin/python -m unittest test_seedance.OpenaiTransportTests   # one class
cd scripts && ../.venv/bin/python -m unittest test_seedance.GenerateVideoSyncTests.test_text_to_video_polls_until_succeeded  # one test
```

`scripts/seedance test_seedance.py` runs the full offline suite inside the wrapper's venv (the first run creates `.venv/`); the single-class/test forms drive that venv's interpreter directly with `python -m unittest`. The offline suite mocks the HTTP layer and injects a fake OSS client + fake `alibabacloud_oss_v2` module, so it needs no network, API key, or OSS SDK. Live tests (real calls, cost quota) are skipped unless `ARK_API_KEY` is set.
