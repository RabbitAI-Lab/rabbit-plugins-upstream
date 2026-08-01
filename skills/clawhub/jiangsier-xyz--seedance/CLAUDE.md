# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An agent **skill** (standard `SKILL.md`; runs on Claude Code, OpenClaw, and compatible runtimes) that generates videos with the **doubao-seedance-2.0** model. `SKILL.md` defines the skill (triggers on "generate video"/"seedance"); `README.md`/`README.zh-CN.md` document it. The synchronous video wrapper is `scripts/seedance.py` (stdlib-only Python); the entrypoint `scripts/seedance` is a venv wrapper that provisions an isolated `.venv/` (installing `requirements.txt`), auto-picks `python3.11`/`python3.12` for proxy-TLS safety, and forwards all args to `scripts/seedance.py`. The only third-party dep is the Alibaba OSS SDK, and only when local image files are used. Video generation is async on every backend this targets (POST a task → poll GET until terminal), so the wrapper hides that behind one blocking call returning the final result (with the video URL).

## Commands

```bash
# offline unit tests (no network, no key needed) — the main feedback loop
scripts/seedance test_seedance.py
cd scripts && ../.venv/bin/python -m unittest test_seedance.OpenaiTransportTests -v   # one class
cd scripts && ../.venv/bin/python -m unittest test_seedance.GenerateVideoSyncTests.test_text_to_video_polls_until_succeeded  # one test

# run the CLI against the Ark API (default api-type; interpreter chosen for you)
scripts/seedance -t "prompt"                                  # text-to-video
scripts/seedance -t "prompt" -i ./fox.png                     # image-to-video (local → OSS)
scripts/seedance -t "prompt" -f ./first.png -l ./last.png     # first+last frame
scripts/seedance -t "prompt" --image-url https://.../x.png    # online image URL
scripts/seedance --api-type openai-video -t "prompt"          # openai-video (mini); see interpreter note
scripts/seedance --api-type openai      -t "prompt"            # openai (full, Ark-shaped body)

# live integration tests (real API calls — costs quota; skips unless ARK_API_KEY set)
# (the one-off runs below drive the venv interpreter created by the first `scripts/seedance` run)
.venv/bin/python -c "import sys; sys.path.insert(0,'scripts'); import seedance, unittest; seedance.load_dotenv('.env'); unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromName('test_seedance.LiveTests'))"          # openai-video (mini)
.venv/bin/python -c "import sys; sys.path.insert(0,'scripts'); import seedance, unittest; seedance.load_dotenv('.env'); unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromName('test_seedance.OpenaiLiveTests.test_text_to_video'))"  # openai (full)
```

Tests do **not** auto-load `.env` (so offline runs never accidentally hit the network). Live tests need `ARK_API_KEY` either in the real env or loaded via the one-liner above.

## Three API types (`--api-type`, default `ark`; also `ARK_API_TYPE`)

The wrapper speaks three protocols, selected by `--api-type` / `ArkVideoClient(api_type=...)` (priority: CLI > `ARK_API_TYPE` env > default). `openai-video` and `openai` share the `/video/generations` transport + `{code, data:{…}}` response; they differ only in **body shape** and **default model**. `ark` is a separate protocol.

| | `openai-video` | `openai` | `ark` |
|---|---|---|---|
| create | `POST /video/generations` | `POST /video/generations` | `POST /contents/generations/tasks` |
| request body | `{model, prompt, seconds(str,4/8/12), size(WxH), input_reference?(comma-joined URLs)}` | `{model, prompt, generate_audio, ratio, duration, watermark, resolution, image?, first_frame?, last_frame?, seed?}` | `{model, content:[{type:text},{type:image_url,role}], generate_audio, ratio, duration, watermark, resolution, seed?}` |
| poll | `GET /video/generations/{id}` | `GET /video/generations/{id}` | `GET /contents/generations/tasks/{id}` |
| status values | `queued`/`IN_PROGRESS`/`SUCCESS` | `queued`/`IN_PROGRESS`/`SUCCESS` | `queued`/`running`/`succeeded` |
| video URL | `data.result_url` (wrapped `{code, data:{…}}`) | `data.result_url` (wrapped `{code, data:{…}}`) | `content.video_url` |
| default model | `doubao-seedance-2.0-mini` | `doubao-seedance-2.0` | `doubao-seedance-2-0-260128` |
| audio | **no** | **no** | yes (`generate_audio=true`) |
| `--seed` | dropped (stderr warning) | sent | sent |

`reference.md` is the Volcengine Ark doc — the **`ark`** path follows it. The **`openai-video`** path targets the openai-video endpoint with an OpenAI-video-style body. The **`openai`** path is the proxy's "openai" (chat-mirror) entry: the marketplace lists it at `/v1/chat/completions`, but that path returns `unsupported_model_endpoint` on this account, so the full `doubao-seedance-2.0` is reached via `/video/generations` with the Ark-shaped body (the original openai implementation). All three were confirmed by live probing. Branching lives in `build_request_body`/`_build_openai_video_body`/`_build_openai_body`, `create_task`, `get_task`, and `_normalize_task`. `get_task` always returns a **normalized** dict `{id, status, video_url, error, raw}` so `wait_for_task` and `video_url()` are api-agnostic.

openai-video body-field quirks (probed): **`seconds` must be a string** (the endpoint rejects a JSON number: `cannot unmarshal number into …seconds of type string`), snapped from `--duration` to `{4,8,12}`; **`input_reference` is a string** — a comma-joined list of image URLs (one = reference image / first frame; two = first+last frame). `--ratio`+`--resolution` map to `size` (`WxH`). The `openai` (Ark-shaped) body uses `OPENAI_FIELD_IMAGE`/`OPENAI_FIELD_FIRST_FRAME`/`OPENAI_FIELD_LAST_FRAME` (= `image`/`first_frame`/`last_frame`) and supports `seed`. Both `openai-video` and `openai` yield **silent video** on this backend; audio requires the `ark` path.

## Architecture

- **`ArkVideoClient`** — the core. `__init__` (reads `ARK_API_KEY`/`ARK_ENDPOINT`/`ARK_INSECURE`; resolves **api_type** = CLI > `ARK_API_TYPE` env > `DEFAULT_API_TYPE`, and **model** = CLI > `ARK_MODEL` env > `_DEFAULT_MODEL_FOR_TYPE[api_type]`, so a bare `ArkVideoClient()` yields a valid request for the default `ark`), `_http_request` (single low-level HTTP method — mock this in tests), `validate_params` (conflict/dependency checks, called from `build_request_body`), `build_request_body`/`_build_openai_video_body`/`_build_openai_body`, `create_task`/`get_task`/`wait_for_task`/`generate_video`. `generate_video` is the sync entry: build body → create → poll until terminal.
- **`load_dotenv`** — tiny stdlib `.env` parser (no python-dotenv). Real env takes precedence over the file. `--env-file` selects the path.
- **`OSSUploader`** — uploads local image files to Alibaba OSS, returns 10-min signed URLs. `alibabacloud_oss_v2` is imported **lazily** (only when a local image is used), so the dep is optional. Credentials come from `OSS_ACCESS_KEY_ID`/`OSS_ACCESS_KEY_SECRET` via a `StaticCredentialsProvider` (not the SDK's env provider). `OSS_ENDPOINT` may be a region (`cn-beijing`) **or** a full host (`oss-cn-beijing.aliyuncs.com`); `_resolve_region_endpoint` handles both by deriving the region from the host.
- **`_resolve_image_inputs`** — the CLI pre-flight: enforces per-slot exclusivity (`--image` vs `--image-url`, etc.) and cross-slot conflicts (image vs first/last, last-needs-first, `adaptive` ratio needs an image) **before** any OSS upload, then resolves local files to signed URLs.
- **CLI** (`build_arg_parser` + `main`) — `--image/-i`, `--first-frame/-f`, `--last-frame/-l` = local files (→ OSS); `--image-url`/`--first-frame-url`/`--last-frame-url` = online URLs (no abbreviations). `-m/--model` sets the model for the actual call.

Fixed parameters per spec: `generate_audio=True`, `watermark=False` (constants `FIXED_GENERATE_AUDIO`/`FIXED_WATERMARK`, not CLI-exposed).

## Testing approach

`scripts/test_seedance.py` mocks `_http_request` (or `urllib.request.urlopen` for the error-wrapping tests) and injects a fake OSS client + fake `alibabacloud_oss_v2` module, so the offline suite needs **no network, no API key, no OSS SDK installed**. `make_client()` defaults to `api_type="ark"`; `make_openai_video_client()` for openai-video-shape tests; `make_openai_client()` for openai (Ark-shaped) tests. Two live classes, both skipped without `ARK_API_KEY`: `LiveTests` (forces `openai-video` / mini) and `OpenaiLiveTests` (forces `openai` / full).

## Interpreter note (important, environment-specific)

The OpenAI-style proxy is load-balanced across backend nodes; some intermittently serve a cert chain whose intermediate CA lacks the `keyUsage` extension. **CPython 3.14 rejects those nodes** (stricter CA verification); **3.11 accepts them all**. The wrapper has SSL retry logic (`http_retries`) to ride through it under 3.14, but `python3.11` is the reliable choice for the `openai-video` / `openai` paths. For the `ark` path (Volcengine, `ark.cn-beijing.volces.com`), `python3` is fine. `--insecure`/`ARK_INSECURE` disables cert verification but the proxy's WAF 403s unverified-TLS handshakes, so it does **not** help for that proxy.

## Env vars (`.env`)

`ARK_API_KEY` (required), `ARK_ENDPOINT` (default `https://ark.cn-beijing.volces.com/api/v3`), `ARK_API_TYPE` (ark/openai-video/openai; lower priority than `--api-type`), `ARK_MODEL` (lower priority than `-m`), `ARK_INSECURE`. For local images: `OSS_ACCESS_KEY_ID`, `OSS_ACCESS_KEY_SECRET`, `OSS_ENDPOINT`, `OSS_BUCKET` (default `jiangsier`), `OSS_KEY_PREFIX` (default `dev/`). **Never print the `.env` contents** — it holds live API keys; check presence/masked only.
