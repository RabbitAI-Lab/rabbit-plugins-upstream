---
name: klingai
version: "2.0.1"
description: Official Kling AI Skill. Call Kling AI for video generation, image generation, subject management, voice management, and account quota inquiry. Use subcommand video / image / element / voice / account by user intent. Use when the user mentions "Kling", "可灵", "文生视频", "图生视频", "参考视频", "视频编辑", "文生图", "图生图", "AI 画图", "视频生成", "图片生成", "主体", "角色", "多镜头", "分镜", "多图", "两张图", "首尾帧", "中间帧", "多关键帧", "可灵4.0", "音色", "组图", "余额", "资源包", "余量", "配额", "text-to-video", "image-to-video", "reference video", "video editing", "text-to-image", "multi-shot", "omni", "4K", "subject", "character", "element", "storyboard", "series", "quota", "balance".
metadata: {"openclaw":{"emoji":"🎬","requires":{"bins":["node"]},"primaryEnv":"KLING_API_KEY","homepage":"https://klingai.com/document-api/"}}
---

> **Language**: Respond in the user's language (detect from their message). Use it for explanations, confirmations, errors, and follow-ups. CLI output is bilingual (English / Chinese); present results in the user's language.

# Kling AI

Video generation, image generation, subject management, voice management, and (read-only) account resource/quota inquiry.
Invoke with subcommand `video` | `image` | `element` | `voice` | `account` by user intent.
Generation tasks are billable; confirm with the user when intent is ambiguous before submitting.

## Invocation

From repository root:

```bash
node skills/klingai/scripts/kling.mjs <video|image|element|voice|account> [options]
```

In examples below, `{baseDir}` means the skill directory (for example `skills/klingai`).

## Routing priority (OpenClaw)

- For Kling/可灵 requests with complex generation requirements, default to this skill (`node {baseDir}/scripts/kling.mjs ...`).
- Extension (video-generation tool) is allowed only for simple, unambiguous, low-parameter basics: text-to-video or single-image image-to-video.
- Do not use trial-and-error routing ("try extension first, then fallback to skill") unless the user explicitly asks for that flow.

## Intent routing (required)

Choose subcommand from user intent first. HTTP API path and default `model_name` are determined by **Route & model**.

| User intent | Subcommand |
| --- | --- |
| Video (t2v, i2v, multi-shot, Omni ref/edit clip via `feature`/`base`, subject-in-video, animation) | `video` |
| Image (text-to-image, image-to-image, 4K, series, AI drawing) | `image` |
| Subject / element (create, manage, list, presets, delete) | `element` |
| Voice library (create, list custom/preset, delete) | `voice` |
| Account resources, packs, remaining quota / balance (read-only) | `account` (`--costs`, default) |
| Credential setup (bind/import) | `account` with `--bind-url` / `--import-env` / `--import-credentials` |

Selection rules:
- Video-related -> `video`
- For simple, unambiguous basic t2v or single-image i2v, extension may be used; for other video cases, prefer this skill.
- Image-only -> `image`
- Subject CRUD -> `element`
- Create / list / delete a voice -> `voice` (then pass the returned `voice_id` to `video --voice_ids`)
- Quota/balance/resource packs -> `account` (default `--costs`)
- Use existing subject in generation -> `video`/`image` + `--element_ids`
- Create subject first -> `element`

Force skill conditions (any hit -> use this skill):
- multi-image input (>=2 images)
- Omni/frame control (`first_frame`/`middle_frame`/`last_frame`/`image_types`)
- any `kling-4.0` request
- reference video (`--video` + `feature`/`base`) or video editing
- subject/element reuse (`--element_ids`)
- storyboard/multi-shot (`--multi_shot`, 分镜)
- image series (`--result_type series`/`--series_amount`, 组图)
- extension parameter gaps or ambiguous/unclear parameter intent

Model name strict rule:
- Video `--model` canonical names: `kling-4.0`, `kling-3.0`, `kling-3.0-turbo`, `kling-2.6`, `kling-2.5-turbo`, `kling-3.0-omni`, `kling-o1`.
- `kling-4.0` is **one** name for text-to-video, image-to-video and Omni (全能参考). There is no `kling-4.0-omni`; the route is chosen by flags (see **Kling 4.0 intent → route**).
- Image `--model` canonical names: `kling-v3`, `kling-v2-1`, `kling-v3-omni`, `kling-image-o1`.
- Do not pass aliases as CLI values.
- Alias disambiguation: `视频O3` -> `kling-3.0-omni`; `图片O3` -> `kling-v3-omni`; only `o1`/`omni1` map to O1 models by intent.

When ambiguous (for example video vs image, or 3.0-omni vs o1), ask user first, then submit.
Use `kling-4.0` only when the user asks for 4.0 / 可灵 4.0 or needs a 4.0-only capability (middle frames / 多关键帧, >15 s, 21:9). Do not switch an existing request to 4.0 silently.

## Preflight checklist (mandatory before submit)

Before any billable submit, pass all checks below. If any check fails, stop and ask user or run `--help`.

1. Subcommand is confirmed: `video` / `image` / `element` / `voice` / `account`.
2. Route is confirmed by flags: basic vs Omni (from **Route & model**).
3. `--model` is canonical (no alias values like `o3`, `omni3`).
4. All params come from this SKILL.md or subcommand `--help`; no undocumented flags.
5. No conflicting combinations (for example `--video_refer_type base` + first/last frame, `--video` feature + `--audio native`/`original`, `--audio original` without `--video`, `kling-4.0` + `--audio` / `--multi_shot`, `--voice_ids` on turbo / 2.5 / o1 / `kling-3.0` / `kling-3.0-omni`, `--voice_ids` on `kling-4.0` text-to-video or image-to-video, `--voice_ids` on `kling-2.6` text-to-video, `--voice_ids` with `--audio off`/`original`, `middle_frame` without `kling-4.0`).
6. Query mode and submit mode are not mixed.

## Anti-fabrication policy (no guessing)

- Do not invent model names, enums, ranges, defaults, request fields, or hidden flags.
- Do not infer unsupported values from older/other skills.
- If value is uncertain, verify with `node {baseDir}/scripts/kling.mjs <subcommand> --help`.
- If user intent is uncertain, ask first; do not submit trial jobs.
- If user uses alias words, map to canonical names and pass canonical only.

## Cost and submission rules

- Every submit is charged; do not submit speculatively.
- Confirm intent first when unclear.
- On timeout/failure/unexpected result, ask user whether to wait or retry.
- Do not auto-resubmit or silently change intent/parameters.

## Agent loop & results

- Entry: only `node {baseDir}/scripts/kling.mjs` with `video`/`image`/`element`/`voice`/`account`.
- Default flow: submit -> poll (~10s interval) -> download to `--output_dir`.
- Keep user updated on long runs (video: `submitted -> processing -> succeeded/failed`; image/element: `succeed/failed`).
- `--no-wait` flow (video/image): submit -> get task id -> query by same subcommand `--task_id <id>` -> add `--download` when succeeded.
- Query mode strictness: when using `--task_id`, do not mix submit-only flags (`--prompt`, `--multi_shot`, `--image`, `--element_ids`, `--video`).
- Never print secrets (`KLING_API_KEY`, `api_key`).

Presenting results:
- Always return task id + local path(s).
- If stdout includes an URL, include markdown link as fallback.

## Prerequisites

- Runtime: Node.js 18+, no extra packages.
- Credential priority: `KLING_API_KEY` (session Bearer as-is) -> stored `api_key` in `.credentials` (same Bearer; **no JWT**). `KLING_TOKEN` is not recognized.
- Official business APIs: `Authorization: Bearer <apiKey>`. Device bind is unchanged Device Flow; `POST /auth/skill/exchange` `ISSUED` returns `credential.apiKey`. See [接口鉴权](https://klingai.com/document-api/api/get-started/authentication.md).
- `KLING_API_KEY` is never read from env files. `--import-env` copies the process env value into credentials. `--bind-url` / `--import-credentials` / `--configure` write credentials, not the env var.
- Permission/auth errors: report the API `message`. Rebind only after user confirmation when the stored API Key itself is invalid. Legacy AK/SK files are ignored — ask the user to rebind.
- Storage root: default `~/.config/kling`, optional `KLING_STORAGE_ROOT`.
- No `KLING_API_KEY` and no stored `api_key`: CLI auto-starts bind flow (writes API Key).
- `account --bind-url`: init -> print URL (manual open) -> poll exchange -> persist `api_key`.
- Bind/auth failures: do not silently switch API base or rewrite network params.
- Forced rebind (requires user confirmation):
  - `node {baseDir}/scripts/kling.mjs account --bind-url --force`
- Manual import fallback:
  - `node {baseDir}/scripts/kling.mjs account --import-env`
  - `node {baseDir}/scripts/kling.mjs account --import-credentials --api_key "<API_KEY>"`
  - `node {baseDir}/scripts/kling.mjs account --configure`
- Mask secret values in user-facing text.
- Optional behavior (API base, media roots): check subcommand `--help`.

## Quick start

```bash
# Show help
node {baseDir}/scripts/kling.mjs --help

# Video
node {baseDir}/scripts/kling.mjs video --prompt "A cat running on the grass" --output_dir ./output
node {baseDir}/scripts/kling.mjs video --image ./photo.jpg --prompt "Wind blowing hair"
node {baseDir}/scripts/kling.mjs video --prompt "Match motion of <<<video_1>>>" --video "https://..." --video_refer_type feature
node {baseDir}/scripts/kling.mjs video --prompt "Change background to ..." --video "https://..." --video_refer_type base
node {baseDir}/scripts/kling.mjs video --multi_shot true --prompt "镜头 1, 5, Sunrise over the hills; 镜头 2, 5, Conflict in the valley;"
node {baseDir}/scripts/kling.mjs video --prompt "A story in three beats: arrival, conflict, resolution"
node {baseDir}/scripts/kling.mjs video --model kling-4.0 --prompt "A train crossing a snowy valley" --duration 20 --aspect_ratio 21:9
node {baseDir}/scripts/kling.mjs video --model kling-4.0 --image a.jpg,b.jpg,c.jpg --image_types first_frame,middle_frame,last_frame --prompt "..."

# Image
node {baseDir}/scripts/kling.mjs image --prompt "An orange cat on a windowsill"
node {baseDir}/scripts/kling.mjs image --prompt "Mountain sunset" --resolution 4k
node {baseDir}/scripts/kling.mjs image --model kling-image-o1 --prompt "<<<element_1>>> on the beach" --element_ids 123456
node {baseDir}/scripts/kling.mjs image --prompt "Character on the beach" --element_ids 123456

# Subject / element
node {baseDir}/scripts/kling.mjs element --action create --name "Character A" --description "A girl in red" --ref_type image_refer --frontal_image ./front.jpg --refer_images ./side.jpg
node {baseDir}/scripts/kling.mjs element --action list
node {baseDir}/scripts/kling.mjs element --action query --task_id <id>

# Account
node {baseDir}/scripts/kling.mjs account --help
node {baseDir}/scripts/kling.mjs account
node {baseDir}/scripts/kling.mjs account --days 90
node {baseDir}/scripts/kling.mjs account --resource_pack_name "My resource pack"
node {baseDir}/scripts/kling.mjs account --bind-url
node {baseDir}/scripts/kling.mjs account --bind-url --force
node {baseDir}/scripts/kling.mjs account --import-env
node {baseDir}/scripts/kling.mjs account --import-credentials --api_key "<API_KEY>"
node {baseDir}/scripts/kling.mjs account --configure

# Query existing task
node {baseDir}/scripts/kling.mjs video --task_id <id> --download
node {baseDir}/scripts/kling.mjs image --task_id <id> --download
```

## Core parameters by subcommand

Do not invent values/ranges/enums/defaults. If unsure, check:
`node {baseDir}/scripts/kling.mjs <subcommand> --help`

### video (video generation)

Official docs: [文生视频 3.0](https://klingai.com/document-api/api/video/3-0-omni/text-to-video.md), [图生视频 3.0](https://klingai.com/document-api/api/video/3-0-omni/image-to-video.md), [Omni 视频](https://klingai.com/document-api/api/video/3-0-omni/video-omni.md), [能力地图](https://klingai.com/document-api/guides/capability-map/video.md). Kling 4.0: internal beta doc (2026.09.22), paths `/text-to-video/kling-4.0`, `/image-to-video/kling-4.0`, `/omni-video/kling-4.0`.

| Parameter | Description | Default |
| --- | --- | --- |
| `--prompt` | T2V/Omni required. Multi-shot format: `镜头 n, m, words;` (half-width separators; n=index 1–6, m=shot seconds ≥1 summing to `--duration`, words ≤512). Omni refs: `@image_1` `@element_1` `@video_1` (`@video_2`, …). | — |
| `--image` | Basic i2v: single first-frame image (`kling-4.0`: up to 10 keyframes, see `--image_types`). Omni: comma-separated list. A first frame, or `kling-4.0` frame-only keyframes, stays on image-to-video unless `--aspect_ratio` is set (then Omni; see `--aspect_ratio`). | — |
| `--image_types` | Per-image type aligned with `--image`: `first_frame` / `middle_frame` / `last_frame` / `refer_image` / empty (`refer_image` when multiple images). `middle_frame` is `kling-4.0` only. `kling-4.0` frame-only types stay on I2V unless `--aspect_ratio` is set (then Omni). Any `refer_image` goes Omni. Other models: Omni only. Do not combine `last_frame` with `--image_tail`. | — |
| `--duration` | Seconds. `kling-4.0`: 3–30. Omitted: not sent. The server reads a duration stated in the prompt; on Omni it then uses `base_video` when present; otherwise the official default is 10. `kling-3.0` / `kling-3.0-turbo` / `kling-3.0-omni`: 3–15. `kling-o1`: 3–10. `kling-2.6` / `kling-2.5-turbo`: `5` or `10`. | `kling-4.0`: omitted; others: 5 |
| `--model` | Path model; see **Route & model**. | route default |
| `--resolution` | `720p` / `1080p` / `4k`. `4k` only on `kling-3.0` and `kling-3.0-omni`. `kling-4.0`: `720p` / `1080p`. | official `1080p` (`kling-4.0`) / `720p` (others) if omitted |
| `--aspect_ratio` | `16:9` / `9:16` / `1:1`; `kling-4.0` adds `21:9` (T2V / Omni) and `adaptive` (Omni). Image-to-video has no aspect_ratio, so `--image` plus this flag (a first frame or `kling-4.0` keyframes included) routes to Omni and submits the value as given. Omni also submits an explicit value with a first frame or base video. If omitted on Omni with no first frame and not a base edit, CLI sends `16:9` (`kling-4.0`: not sent, official default `adaptive`). | T2V `16:9`; Omni `16:9` (`kling-4.0`: omitted) |
| `--audio` | `native` / `off` / `original`. 3.0 T2V/I2V and 2.6: `native\|off`. Omni 3.0: `native\|original\|off`. O1: `original\|off`. Turbo/2.5/`kling-4.0`: not sent (rejected; 4.0 uses `--voice_ids` for 音色, not `--audio`). `original` requires `--video` (keep source audio). Feature video: `off` only. Base video: not `native`. 2.6 native requires `1080p`. | official `off` if omitted |
| `--voice_ids` | Voice IDs (comma-separated). `contents` `type=voice` with `voice_id` and `id` (`1`, `2`, …). Prompt uses `@1`. Does **not** change route. `kling-4.0`: Omni only, max 3, no `settings.audio`; T2V and I2V reject this flag. `kling-2.6`: image-to-video only, max 2; omitted `--audio` is sent as `native` and resolution `1080p`; `--audio off` is rejected. Not on `kling-3.0` / `kling-3.0-omni` / turbo / 2.5 / o1. Get IDs from `voice --action list-presets` / `list` / `create`. | — |
| `--image_tail` | Last-frame image (`contents[].type=last_frame`). Requires `--image`. Do not combine with `--image_types last_frame`. Turbo I2V does not support last_frame. | — |
| `--element_ids` | Subject IDs (comma-separated). Single `--image` + `kling-3.0` I2V: `contents` `type=element` (max 3). Otherwise Omni (`kling-4.0` I2V has no element, so it goes Omni). | — |
| `--video` | Omni reference clip(s): public http(s) URL, comma-separated. `kling-4.0`: up to 5, prompt `@video_1` `@video_2` …. `kling-3.0-omni` / `kling-o1`: one URL. At most one `base_video`. | — |
| `--video_refer_type` | `feature` → `feature_video` / `base` → `base_video`. One value, or a list aligned with `--video`. One URL and omitted type → `base`. Several URLs: list each type, or a single `feature` for every URL. | base for one URL |
| `--multi_shot` | `true` / `false`. Request field only on `kling-3.0` and `kling-3.0-omni` (`settings.multi_shot`); rejected on `kling-4.0`. Turbo: write `镜头 n, m, words;` in `--prompt`; do not pass `--multi_shot`. `false` disables 镜头-format prompts. Base video edit: if omitted, CLI sends `false` (server default `true` would fail). | official `true` if omitted (3.0 / 3.0-omni), except base edit → `false` |
| `--output_dir` | Output directory. | `./output` |
| `--task_id` | Query via `GET /tasks?task_ids=`; pair with `--download`. | — |

Do not pass: `--mode`, `--sound`, `--shot_type`, `--multi_prompt`, `--keep_original_sound`, `--negative_prompt`.

Model aliases (do not pass aliases to `--model`): see **Model catalog**.

Omni `contents` image rules:
- `url` cannot be empty (URL or Base64).
- Types: `first_frame` / `middle_frame` (`kling-4.0` only) / `last_frame` / `refer_image`. Last-frame requires first-frame. No last-frame-only. `kling-3.0-omni`, `kling-o1` and `kling-4.0` support last_frame (o1 has extra limits below).
- `kling-3.0-omni` / `kling-o1`: with `--video` max 4 images; without `--video` max 7.
- `kling-4.0`: max 10 images (with or without `--video`).
- `kling-o1`: when image count > 2, no `last_frame`. First+last: no extra `refer_image`.
- Frame generation cannot combine with `--video_refer_type base`.
- `kling-o1` + `feature_video`: first_frame only, no last_frame.
- `kling-o1` first_frame only (no `refer_image`, no `--video`): `--duration` only `5` or `10`.

Omni `contents` element rules:
- `element_id` cannot be empty; `id` is `element_1`…
- `kling-3.0-omni` / `kling-o1`: frame generation supports up to 3 subjects.
- First+last frame with `kling-o1`: subjects unsupported.
- `kling-3.0-omni` / `kling-o1`: with `--video`: `image_count + element_count <= 4`; otherwise `<= 7`.
- `kling-4.0`: max 7 subjects. Video-character subjects are at most 3, and those subjects plus reference videos total at most 5. An element id does not say which kind of subject it is, so the CLI does not apply that combined cap; the server does. `image_count + video_count + element_count + voice_count <= 15`.

Omni / 4.0 `contents` voice rules:
- Item: `type=voice`, `voice_id`, `id`=`1` (`2`, `3` …); prompt `@1`. Model limits, route, and audio side effects: see `--voice_ids`.

Omni `contents` video rules:
- Counts and type mapping: see `--video` / `--video_refer_type`. On `kling-4.0`, at most one `base_video`; any other clip is `feature_video`. Video-character subjects plus reference videos: see element rules above.
- `feature_video`: `--audio` must be `off`; do not set `--multi_shot false`.
- `base_video`: no first/last frame; no `--multi_shot true`; if `--multi_shot` omitted, CLI sends `false`; `--audio` cannot be `native`.

Compact examples:

```bash
# explicit frame marking by intent
node {baseDir}/scripts/kling.mjs video --model kling-3.0-omni --image a.jpg,b.jpg,c.jpg --image_types first_frame,refer_image,last_frame --prompt "..."

# with reference video: image count <= 4
node {baseDir}/scripts/kling.mjs video --video "https://..." --video_refer_type feature --audio off --image a.jpg,b.jpg --prompt "..."

# kling-4.0 multi-keyframe I2V (frame-only types, max 10 images incl. --image_tail)
node {baseDir}/scripts/kling.mjs video --model kling-4.0 --image a.jpg,b.jpg,c.jpg --image_types first_frame,middle_frame,middle_frame --image_tail d.jpg --prompt "..."

# kling-4.0 Omni (refer image + subject); no --audio / --multi_shot
node {baseDir}/scripts/kling.mjs video --model kling-4.0 --image a.jpg --image_types refer_image --element_ids 123456 --prompt "@element_1 in the style of @image_1"

# kling-4.0 voice is Omni only (prompt uses @1)
node {baseDir}/scripts/kling.mjs video --model kling-4.0 --image a.jpg --image_types refer_image --prompt "A woman says hello in the voice of @1" --voice_ids 850087542757535834

# kling-2.6 voice is image-to-video only (id is 1, prompt uses @1)
node {baseDir}/scripts/kling.mjs video --model kling-2.6 --image a.jpg --prompt "@1 whispers softly" --voice_ids 829826751244537879
```

If the user asks for a voice / 音色 without naming a model, ask which of `kling-4.0` Omni or `kling-2.6` image-to-video to use. Do not invent a `voice_id`. List official voices with `voice --action list-presets`, or create one with `voice --action create` (public `--voice_url` or `--video_id` only).

### image (image generation)

| Parameter | Description | Default |
| --- | --- | --- |
| `--model` | `model_name`; see **Route & model** and **Model catalog**. | route default |
| `--prompt` | Image prompt (required). Omni: `<<<image_1>>>` / `<<<element_1>>>`. | — |
| `--image` | Basic: single image. Omni: image list (comma-separated). | — |
| `--resolution` | `1k` / `2k` / `4k`; `4k` routes to Omni. | 1k |
| `--aspect_ratio` | `16:9` / `9:16` / `1:1` / `auto` (`auto` Omni only, and only with `--image`). | basic: `16:9`; Omni t2i: `16:9`; Omni with `--image`: `auto` |
| `--n` | Result count 1–9 (`result_type=single`). | 1 |
| `--negative_prompt` | Basic API only. | — |
| `--result_type` | `single` / `series` (`series` is Omni and i2i-only). | single |
| `--series_amount` | 2–9 or `auto` for `result_type=series`. `auto` = 智能选择数量. | 4 |
| `--element_ids` | Subject IDs (comma-separated). `kling-v3` generations: `element_list`. Omni: `element_list`. `kling-v2-1` unsupported. | — |
| `--output_dir` | Output directory. | `./output` |
| `--task_id` | Query task id; pair with `--download`. | — |

Notes:
- `n` and `series_amount` apply to different modes.
- `series` is i2i-only, so `--result_type series` requires `--image`.
- `--negative_prompt` is generations-only and cannot combine with `--image`.
- Omni `aspect_ratio=auto` needs `--image`. Text-to-image Omni (no `--image`) defaults to `16:9`; do not pass `auto`.

Omni refs rules (image):
- `image` cannot be empty (URL or Base64).
- `element_id` cannot be empty.
- `image_count + element_count <= 10`.

### element (subject management)

Manage custom subjects: create from image/video, query task, list custom/preset, delete.
Use `element_id` in `video`/`image` with `--element_ids` for reusable subject consistency.

| Parameter | Description |
| --- | --- |
| `--action create` | Create subject; requires `--name` (<=20), `--description` (<=100), `--ref_type` |
| `--ref_type` | `image_refer` (requires `--frontal_image` and `--refer_images`) / `video_refer` (requires `--video`) |
| `--frontal_image` | Front reference image (`image_refer`) |
| `--refer_images` | Other reference images (comma-separated, **required** 1–3). Official API: must differ from the frontal image. |
| `--video` | Reference video (`video_refer`) |
| `--voice_id` | Optional voice bind (image_refer: 人物/类人形象) |
| `--action query --task_id <id>` | Query creation task |
| `--action list` | List custom subjects |
| `--action list-presets` | List preset subjects |
| `--action delete --element_id <id>` | Delete subject |

If the user only provides a frontal image: **ask** whether to (1) add 1–3 other-angle images, or (2) explicitly reuse the frontal file as `--refer_images`. Do not submit without `--refer_images`. The CLI does not silently copy `--frontal_image` into `refer_images`.

### voice (voice management)

Model-independent library. Official paths are the same on the 2.6 and 3.0 Omni voice pages (`/v1/general/custom-voices`). Use the returned `voice_id` in `video --voice_ids` (`kling-4.0` Omni or `kling-2.6` image-to-video).

| Parameter | Description |
| --- | --- |
| `--action create` | Create a custom voice. Requires `--name` (≤20). Exactly one of `--voice_url` or `--video_id`. |
| `--voice_url` | Public http(s) URL (`.mp3` / `.wav` / `.mp4` / `.mov`, one speaker, 5–30 s). Local paths and base64 are rejected. |
| `--video_id` | Existing work ID. Official limit: 2.6 with sound on, avatar, or lip-sync. |
| `--action query --task_id <id>` | Query the creation task; read `task_result.voices[].voice_id`. |
| `--action list` | List custom voices |
| `--action list-presets` | List official preset voices |
| `--action delete --voice_id <id>` | Delete a custom voice |

### account (resource & quota inquiry, optional credential setup)

| Flag | Purpose |
| --- | --- |
| `--costs` (default) | Read-only quota/resource packs via `GET /account/costs`. |
| `--bind-url` | Device bind with polling; prints URL for manual open; optional `--force`. |
| `--import-env` | Read `KLING_API_KEY` and persist. |
| `--import-credentials` | Persist `--api_key`. |
| `--configure` | Interactive API Key input and save credentials. |

All bind/account files persist under storage root (`~/.config/kling` by default, or `KLING_STORAGE_ROOT`).

`--costs` query params:

| Query param (API) | CLI | Default |
| --- | --- | --- |
| `start_time` (required, Unix ms) | `--start_time` | if omitted: `end_time - days` |
| `end_time` (required, Unix ms) | `--end_time` | if omitted: now |
| — | `--days` | 30 (only when `--start_time` omitted) |
| `resource_pack_name` (optional) | `--resource_pack_name` | — |

Run `node {baseDir}/scripts/kling.mjs account --help` for details.
Run `node {baseDir}/scripts/kling.mjs video --help`, `image --help`, `element --help`, or `voice --help` for full params.

## Route & model (CLI: `kling.mjs` + flags -> default `model_name`)

Agents call `node {baseDir}/scripts/kling.mjs <video|image|element|voice|account>` with flags.
`--model` selects the official path/model. Video encodes model in the URL (`/text-to-video/kling-4.0`); image still sends `model_name`. Must be exact canonical spelling.
If `--model` is omitted, route defaults apply.
CLI guardrails reject incompatible model/route and invalid `audio` / frame combinations before submit.

### Routing decision tree (must follow)

1. Choose subcommand from intent: `video` / `image` / `element` / `voice` / `account`.
2. Determine route triggers:
   - any Omni trigger -> Omni route
   - otherwise -> basic route
3. Validate model-route compatibility:
   - Omni route accepts only Omni-capable canonical models
   - basic route rejects Omni-only models
4. Validate strict parameter combos (`audio`, `multi_shot`, frame rules, ref limits).
5. If uncertain, run `--help` or ask user; never guess-submit.

### Video (`video` subcommand)

Omni routing triggers (any of these -> `/omni-video/{model}`):
- `--video`
- comma in `--image` (exception: `kling-4.0` frame-only `--image_types` stays I2V when `--aspect_ratio` is omitted)
- `--image` + `--aspect_ratio` (a first frame or `kling-4.0` frame-only keyframes included; see `--aspect_ratio`)
- `--element_ids` without a single I2V first-frame (or with turbo/2.6/2.5/`kling-4.0`)
- `kling-4.0` + `--image_types` containing `refer_image`
- explicit `--model kling-3.0-omni` or `--model kling-o1` (Omni-only names; `kling-4.0` is **not** an Omni trigger by itself)

Otherwise:
- T2V: no `--image` → `POST /text-to-video/{model}`
- I2V: single `--image` (optional `--image_tail`, optional `--element_ids` on `kling-3.0` max 3) → `POST /image-to-video/{model}`
- I2V (`kling-4.0` only): up to 10 keyframes, every `--image_types` entry is `first_frame` / `middle_frame` / `last_frame` (plus optional `--image_tail`) → `POST /image-to-video/kling-4.0`

#### Kling 4.0 intent → route

`kling-4.0` has three endpoints under one name. Always pass `--model kling-4.0`; pick flags from intent, and the CLI routes:

| User intent (with 4.0) | Flags | Endpoint |
| --- | --- | --- |
| Text only, no media / subject | `--prompt` (`--aspect_ratio` optional) | `/text-to-video/kling-4.0` |
| Animate one image as first frame | `--image x.jpg` (`--image_tail` optional) | `/image-to-video/kling-4.0`. With `--aspect_ratio`: `/omni-video/kling-4.0` |
| Keyframes: first / middle / last frames in order (多关键帧) | `--image a,b,c --image_types first_frame,middle_frame,last_frame` | `/image-to-video/kling-4.0`. With `--aspect_ratio`: `/omni-video/kling-4.0` |
| Style / scene / character reference images (not frames) | `--image a,b` (types empty or `refer_image`) | `/omni-video/kling-4.0` |
| Use subject(s) | `--element_ids ...` (with or without images) | `/omni-video/kling-4.0` |
| Reference video (motion / style) | `--video URL --video_refer_type feature`. Up to 5 URLs on 4.0: `--video u1,u2 --video_refer_type feature` | `/omni-video/kling-4.0` |
| Edit a video | `--video URL --video_refer_type base` | `/omni-video/kling-4.0` |
| Mixed: frames + refer images | `--image_types` mixing frames and `refer_image` | `/omni-video/kling-4.0` |
| Use voice / 音色 | `--voice_ids ...` together with Omni flags (reference image, subject, or video) | `/omni-video/kling-4.0`. Text-only and image-to-video reject `--voice_ids`. Voice alone does not switch route. |

Rules for 4.0:
- If it is unclear whether images are **frames** (where the video starts / passes / ends) or **references** (style, scene, character), ask the user before submitting.
- Text-only 4.0 always goes T2V (there is no "Omni without references") and rejects `--voice_ids`.
- Not on 4.0: `--audio`, `--multi_shot`, `4k`. Voice: `--voice_ids` on Omni only (not `--audio`).
- Duration 3–30 (omitted: see `--duration`). Resolution `720p` / `1080p` (official default `1080p`).

`--multi_shot` does not force Omni; it still follows the routing triggers above.

| Video routing (CLI) | Default if `--model` omitted | Allowed `--model` |
| --- | --- | --- |
| T2V / I2V | `kling-4.0` | `kling-3.0`, `kling-3.0-turbo`, `kling-2.6`, `kling-2.5-turbo`, `kling-4.0` |
| Omni | `kling-4.0` | `kling-4.0` (default), `kling-3.0-omni`, `kling-o1` |

### Image (`image` subcommand)

Omni routing triggers (any of these -> omni-image API route):
- explicit `--model kling-v3-omni` or `--model kling-image-o1`
- `--result_type series`
- `--resolution 4k`
- `--aspect_ratio auto`
- comma in `--image`

`--element_ids` alone stays on `/v1/images/generations` with `kling-v3` `element_list` (`kling-v2-1` rejected). 4k/series/multi-image still go Omni.

Else -> basic generations route (text-to-image / image-to-image).

| Image routing (CLI) | Default if `--model` omitted | Allowed `--model` |
| --- | --- | --- |
| Basic `/v1/images/generations` | `kling-v3` | `kling-v3`, `kling-v2-1` |
| Omni `/v1/images/omni-image` (4k / series) | `kling-v3-omni` | `kling-v3-omni`, `kling-image-o1` |
| Omni `/v1/images/omni-image` (other) | `kling-image-o1` | `kling-image-o1` (official default), `kling-v3-omni` |

### Model catalog (by name)

Common aliases (understanding only; do not pass aliases to `--model`):
- `omni3`, `omni v3`, `视频O3`, `video o3`, `O3`, `o3` -> `kling-3.0-omni` (video) / `kling-v3-omni` (image)
- `o1`, `omni1` -> `kling-o1` (video) or `kling-image-o1` (image)
- `kling-4.0-omni`, `4.0 全能参考`, `4.0 Omni`, `可灵 4.0` -> `kling-4.0` (video)

`--model` input rule: pass only canonical names from this table.

| Model | Valid on | Notes |
| --- | --- | --- |
| `kling-4.0` | T2V / I2V / Omni video | One name, three endpoints (see **Kling 4.0 intent → route**). Duration 3–30; 720p/1080p; no `--audio` / `--multi_shot` / 4k. I2V: up to 10 keyframes, no subjects. Omni: max 10 images, 7 subjects, 5 reference videos (one `base_video`); aspect adds `21:9` (T2V / Omni) and `adaptive` (Omni). Voice: Omni `--voice_ids` only (max 3). |
| `kling-3.0` | T2V / I2V | Video basic. Resolution 720p/1080p/4k; audio native/off; multi_shot. I2V contents may include `element` (max 3). No `--voice_ids`. |
| `kling-3.0-turbo` | T2V / I2V | No audio / `settings.multi_shot`; I2V first_frame only (no last_frame). Multi-shot via prompt `镜头 n, m, words;` only. |
| `kling-2.6` | T2V / I2V | Duration 5 or 10; audio native/off (native needs 1080p). Last-frame: 1080p silent. Voice: I2V `--voice_ids` max 2 (sends `audio=native` and `1080p`). |
| `kling-2.5-turbo` | T2V / I2V | Duration 5 or 10; no audio field. Last-frame: 1080p only. |
| `kling-3.0-omni` | Omni video | Omni video. audio native/original/off (`original` needs `--video`); 4k; first+last frame; feature/base video. No `--voice_ids`. |
| `kling-o1` | Omni video | Duration 3–10; audio original/off; no 4k; no multi_shot field. First-frame-only: 5 or 10s. Feature video: no last_frame. First+last: no extra refs/subjects. |
| `kling-v3` | Basic image | Default basic image. 1k/2k. Supports `element_list`. |
| `kling-v2-1` | Basic image | Official generations `model_name`. No subjects. |
| `kling-v3-omni` | Omni image | 1k/2k/4k; series + `auto`. Default Omni when 4k or series. Text-to-image: no `aspect_ratio=auto` (default `16:9`). |
| `kling-image-o1` | Omni image | Official omni-image default. Capability map: 1k/2k (not 4k, not series). Text-to-image default `16:9`; `auto` only with `--image`. |

Principle:
- Set task flags first (`--image`, `--element_ids`, `--video`, `--multi_shot`, ...).
- Omit `--model` to use route defaults.
- If `--model` is explicit, it must match route implied by flags.

## When to use Omni; element vs image reference

Which route: follow **Route & model** triggers.
Prefer Omni when you need multi-image composition, 4K/series, reference-video edit, or mixed image+element Omni prompts (`<<<image_1>>>` / `@image_1`).
Single-image + subject on `kling-3.0` I2V or `kling-v3` generations stays on the basic route.

Prefer plain image reference for simple tasks.
Create element first only when user explicitly wants reusable subject consistency across outputs.

## Prompt template syntax (video / image Omni)

In Omni video, pass media/subjects by flags; reference in `--prompt` with official `@` ids (`contents[].id`):
- `@image_1` -> first `--image` (`@image_2`, ...)
- `@element_1` -> first `--element_ids` (`@element_2`, ...)
- `@video_1` -> first `--video` (`@video_2`, …)
- `kling-4.0` I2V keyframes also get ids `image_1`, `image_2`, ... in `--image` order (`--image_tail` is the last one).
- `@1` -> first `--voice_ids` (`@2`, `@3` for the rest) on `kling-4.0` Omni and `kling-2.6` image-to-video

Omni image still uses `<<<image_1>>>` / `<<<element_1>>>` in `--prompt` (official `/v1/images/omni-image`). Those placeholders require the Omni route (explicit `--model kling-image-o1` / `kling-v3-omni`, or 4k/series/multi-image). `kling-v3` generations uses `element_list` without `<<<>>>`.

## Notes

- Timing: video ~1–5+ min; image ~20–60 s; subject creation ~30 s–2 min.
- Retention: platform may remove assets after ~30 days; save outputs locally.
- Server checks prompt length and media size; the CLI does not. Users are strongly advised to validate these locally.

| Model | Prompt | Image | Reference video |
| --- | --- | --- | --- |
| `kling-4.0` | English ≤26000, other languages ≤11000 (mixed: English/26000 + other/11000 ≤ 1) | ≤30MB, side ≥300px, aspect 2:5–5:2 | ≤300MB, side 700–4553px, area ≤8294400, aspect 2:5–5:2, 3–30s each and in total (includes video-character subjects), 24–60fps in (24fps out) |
| `kling-3.0` | ≤3072, suggest ≤2500 | ≤50MB, side ≥300px, aspect 1:2.5–2.5:1 | — |
| `kling-3.0-omni` | ≤3072, suggest ≤2500 | ≤50MB, side ≥300px, aspect 1:2.5–2.5:1 | ≤200MB, side 700–4553px, area ≤8294400, aspect 0.4–2, 3–15.5s, 24–60fps in (24fps out) |
| `kling-2.6` | ≤2500 | ≤50MB, side ≥300px, aspect 1:2.5–2.5:1 | — |

## Reference

- Official docs index: https://klingai.com/document-api/llms.txt
- Official docs home: https://klingai.com/document-api/
- API endpoint quick map in this package: `reference.md`
