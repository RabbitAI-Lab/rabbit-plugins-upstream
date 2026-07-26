#!/usr/bin/env python3
"""
Sync wrapper for the Volcengine "doubao-seedance-2.0" video-generation model.

Video generation is asynchronous on every targeted backend: you POST a task,
receive a task id, then poll GET until status is terminal. This script hides
that behind one synchronous call: create the task, poll until it finishes, and
hand back the result (including the generated video URL).

Reference: https://docs.volcengine.com/docs/82379/2298881
           (local copy: reference.md — the `ark` path follows it)

Three API protocols (--api-type), each with its own default model:
    ark          raw Volcengine Ark API            doubao-seedance-2-0-260128
    openai-video openai-video endpoint (sora-style) doubao-seedance-2.0-mini
    openai       openai (chat-mirror) entry         doubao-seedance-2.0 (full)

See the "Two/three API types" section of the README for the request/response
shape of each.

Usage
-----
    export ARK_API_KEY=...
    python3 seedance.py -t "a daisy field under a blue sky, camera pushing in"
    python3 seedance.py -t "girl holding a fox, camera pulls out" -i https://.../fox.png
    python3 seedance.py -t "360 orbit around the girl" -f https://.../first.jpeg -l https://.../last.jpeg

Options
    --text/-t            input prompt                          (required)
    --image/-i           local reference image file            (optional)
    --image-url          online reference image URL            (optional)
    --first-frame/-f     local first-frame image file          (optional)
    --first-frame-url    online first-frame image URL           (optional)
    --last-frame/-l      local last-frame image file          (optional)
    --last-frame-url     online last-frame image URL            (optional)
    --duration           video duration in seconds            (default 5)
    --ratio              aspect ratio, e.g. 16:9 / 9:16 / 1:1  (default "16:9")
    --resolution         480p / 720p / 1080p / 4k              (default "720p")
    --model/-m           model id  (CLI > ARK_MODEL env > per-api-type default)
    --api-type           ark / openai-video / openai  (CLI > ARK_API_TYPE env > ark)
    --seed               reproducibility seed (ark/openai only; openai-video ignores)
    --save               optional path to download the mp4     (optional)
    --poll-interval      seconds between status polls         (default 10)
    --timeout            max seconds to wait for completion   (default 1800)
    --endpoint           override ARK_ENDPOINT                (default from env)
    --env-file           path to .env file                    (default .env)

Local images are uploaded to Alibaba OSS (signed URL, 10-minute validity) and the
signed URL is used as the actual image input. Online `*-url` options are used
directly. A local file and a `*-url` for the same slot cannot both be given.

Environment (real env wins over the .env file)
    ARK_API_KEY     required
    ARK_ENDPOINT    optional, default https://ark.cn-beijing.volces.com/api/v3
    ARK_API_TYPE    optional — ark / openai-video / openai (lower priority than --api-type)
    ARK_MODEL       optional — model id (lower priority than -m)
    ARK_INSECURE    optional — 1 to skip TLS verification

Alibaba OSS (only needed when using local image files)
    OSS_ACCESS_KEY_ID     Alibaba Cloud ACCESS_KEY_ID       (required for local images)
    OSS_ACCESS_KEY_SECRET Alibaba Cloud ACCESS_KEY_SECRET   (required for local images)
    OSS_ENDPOINT     region, e.g. cn-beijing           (optional, default cn-beijing)
    OSS_BUCKET       bucket name                       (optional, default jiangsier)
    OSS_KEY_PREFIX   key prefix                        (optional, default dev/)

Fixed parameters (per spec; ark + openai paths)
    generate_audio = True
    watermark = False
    (openai-video has no such fields; it yields silent video on this backend.)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

DEFAULT_MODEL_OPENAI_VIDEO = "doubao-seedance-2.0-mini"  # openai-video endpoint
DEFAULT_MODEL_OPENAI = "doubao-seedance-2.0"  # openai (chat-mirror) endpoint, full model
DEFAULT_ENDPOINT = "https://ark.cn-beijing.volces.com/api/v3"
DEFAULT_ENV_FILE = ".env"
DEFAULT_DURATION = 5
DEFAULT_RATIO = "16:9"
DEFAULT_RESOLUTION = "720p"
DEFAULT_POLL_INTERVAL = 10
DEFAULT_TIMEOUT = 1800
DEFAULT_HTTP_RETRIES = 6  # retries on transient network/SSL/5xx errors
HTTP_TIMEOUT = 30  # per-request connect/read timeout (seconds), for API JSON calls
DOWNLOAD_TIMEOUT = 180  # per-read timeout for downloading generated mp4s (larger than API JSON)

DEFAULT_MODEL_ARK = "doubao-seedance-2-0-260128"  # raw Volcengine Ark API

# API types (three protocols):
# - "openai-video": openai-video endpoint (POST /video/generations) speaking an
#   OpenAI-video-style body (seconds/size/input_reference); model doubao-seedance-2.0-mini.
# - "openai": the proxy's OpenAI chat-mirror entry (POST /video/generations) with an
#   Ark-shaped body (image/first_frame/last_frame/generate_audio/ratio/duration/
#   watermark/resolution); model doubao-seedance-2.0 (full). Audio is not produced
#   on this backend.
# - "ark": raw Volcengine Ark API (POST /contents/generations/tasks).
API_TYPE_OPENAI_VIDEO = "openai-video"
API_TYPE_OPENAI = "openai"
API_TYPE_ARK = "ark"
DEFAULT_API_TYPE = API_TYPE_ARK
_API_TYPES = (API_TYPE_OPENAI_VIDEO, API_TYPE_OPENAI, API_TYPE_ARK)
_DEFAULT_MODEL_FOR_TYPE = {
    API_TYPE_ARK: DEFAULT_MODEL_ARK,
    API_TYPE_OPENAI_VIDEO: DEFAULT_MODEL_OPENAI_VIDEO,
    API_TYPE_OPENAI: DEFAULT_MODEL_OPENAI,
}

# openai-video body constraints. `seconds` must be a STRING whose value is one
# of 4/8/12 (the endpoint rejects a number); `size` is a "WxH" string. The
# openai-video body has no generate_audio / watermark / ratio / duration /
# resolution / seed params — those are Ark-only. Image inputs are passed as
# `input_reference` entries (comma-joined URLs).
OPENAI_VIDEO_ALLOWED_SECONDS = (4, 8, 12)
_OPENAI_VIDEO_SIZE_BASE = {  # resolution -> short-side pixel count
    "480p": 480, "720p": 720, "1080p": 1080, "4k": 2160, "2160p": 2160,
}

# openai (Ark-shaped) body field names for image inputs.
OPENAI_FIELD_IMAGE = "image"          # single reference image (image-to-video)
OPENAI_FIELD_FIRST_FRAME = "first_frame"
OPENAI_FIELD_LAST_FRAME = "last_frame"

# Fixed input parameters requested by the spec (Ark path only).
FIXED_GENERATE_AUDIO = True
FIXED_WATERMARK = False

# Terminal task states returned by the Ark/openai-video APIs.
SUCCEEDED = "succeeded"
FAILED = "failed"


class ArkVideoError(Exception):
    """Raised when the Ark video-generation workflow fails."""


def load_dotenv(path: str = DEFAULT_ENV_FILE, override: bool = False) -> bool:
    """Load KEY=VALUE pairs from a .env file into os.environ.

    This is a small, dependency-free reader (no python-dotenv required).

    - Only sets a variable if it is not already present in the environment,
      unless ``override=True`` (real environment wins over the file, matching
      the usual .env convention).
    - Supports an optional leading ``export `` prefix, inline ``#`` comments,
      and single- or double-quoted values (quotes are stripped).
    - Returns True if the file was loaded, False if it did not exist.
    """
    if not os.path.isfile(path):
        return False

    try:
        with open(path, "r", encoding="utf-8") as fh:
            for lineno, raw in enumerate(fh, 1):
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("export "):
                    line = line[len("export "):].lstrip()
                if "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                if not key or not key.replace("_", "").isalnum():
                    continue
                value = value.strip()
                if value and value[0] in ("'", '"'):
                    # quoted value: take content up to the matching closing
                    # quote; a trailing comment after it is ignored.
                    quote = value[0]
                    end = value.find(quote, 1)
                    if end != -1:
                        value = value[1:end]
                else:
                    # unquoted: strip a trailing inline comment
                    hash_pos = _find_unquoted_hash(value)
                    if hash_pos != -1:
                        value = value[:hash_pos].rstrip()
                if not override and key in os.environ:
                    continue
                os.environ[key] = value
    except OSError as e:
        raise ArkVideoError(f"failed to read env file {path}: {e}") from None
    return True


def _find_unquoted_hash(s: str) -> int:
    """Index of the first '#' not inside quotes, or -1."""
    quote = None
    for i, ch in enumerate(s):
        if quote:
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
        elif ch == "#":
            return i
    return -1


class ArkVideoClient:
    """Minimal synchronous client for Ark content-generation (video) tasks."""

    def __init__(
        self,
        api_key: str | None = None,
        endpoint: str | None = None,
        model: str | None = None,
        poll_interval: int = DEFAULT_POLL_INTERVAL,
        timeout: int = DEFAULT_TIMEOUT,
        api_type: str | None = None,
        insecure: bool | None = None,
        http_retries: int = DEFAULT_HTTP_RETRIES,
    ) -> None:
        self.api_key = api_key or os.environ.get("ARK_API_KEY")
        if not self.api_key:
            raise ArkVideoError(
                "ARK_API_KEY is required. Set it in the environment or pass api_key=..."
            )
        self.endpoint = (endpoint or os.environ.get("ARK_ENDPOINT") or DEFAULT_ENDPOINT)
        self.endpoint = self.endpoint.rstrip("/")
        # api_type priority: explicit arg > ARK_API_TYPE env > DEFAULT_API_TYPE.
        api_type = api_type or os.environ.get("ARK_API_TYPE") or DEFAULT_API_TYPE
        if api_type not in _API_TYPES:
            raise ArkVideoError(
                f"unknown api_type {api_type!r}; expected one of {_API_TYPES}"
            )
        self.api_type = api_type
        # Model priority: explicit arg > ARK_MODEL env > per-api-type default.
        # A bare ArkVideoClient() thus yields a valid request for the default
        # api_type.
        self.model = model or os.environ.get("ARK_MODEL") or _DEFAULT_MODEL_FOR_TYPE[api_type]
        self.poll_interval = poll_interval
        self.timeout = timeout
        self.http_retries = http_retries
        # Allow disabling TLS verification (some proxies serve a cert chain
        # that Python 3.14's stricter checks reject). Default from ARK_INSECURE.
        self.insecure = bool(insecure) if insecure is not None else (
            os.environ.get("ARK_INSECURE", "").lower() in ("1", "true", "yes")
        )
        self._ssl_ctx = None
        if self.insecure:
            import ssl

            self._ssl_ctx = ssl.create_default_context()
            self._ssl_ctx.check_hostname = False
            self._ssl_ctx.verify_mode = ssl.CERT_NONE

    # ------------------------------------------------------------------ #
    # Low-level HTTP. Kept as a single method so tests can monkeypatch it
    # without touching real sockets.
    # ------------------------------------------------------------------ #
    def _http_request(self, method: str, path: str, body: dict | None = None) -> dict:
        url = f"{self.endpoint}{path}"
        data = None
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers, method=method)

        # Retry transient network/SSL errors: some proxies
        # load-balance across backend nodes whose TLS cert chains intermittently
        # fail Python 3.14's stricter verification. A handshake-level failure
        # means the request never reached the server, so retrying POSTs is safe
        # (no duplicate side effects). 5xx responses are also retried.
        last_err: Exception | None = None
        for attempt in range(self.http_retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT, context=self._ssl_ctx) as resp:
                    raw = resp.read().decode("utf-8")
                    status = resp.status
                break  # success
            except urllib.error.HTTPError as e:
                raw = e.read().decode("utf-8", errors="replace")
                if 500 <= e.code < 600 and attempt < self.http_retries:
                    last_err = ArkVideoError(f"HTTP {e.code} {e.reason} from {method} {url}: {raw}")
                    self._sleep_backoff(attempt)
                    continue
                raise ArkVideoError(
                    f"HTTP {e.code} {e.reason} from {method} {url}: {raw}"
                ) from None
            except urllib.error.URLError as e:
                if attempt < self.http_retries:
                    last_err = e
                    self._sleep_backoff(attempt)
                    continue
                raise ArkVideoError(f"network error calling {method} {url}: {e}") from None
        else:
            # loop exhausted without break (all retries failed on network/5xx)
            raise ArkVideoError(
                f"{method} {url} failed after {self.http_retries + 1} attempts: {last_err}"
            ) from None

        if not raw:
            return {}
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            raise ArkVideoError(f"non-JSON response (HTTP {status}) from {url}: {raw}")
        # Ark/proxy may surface an error object even with a 200.
        if isinstance(parsed, dict) and parsed.get("error") and not parsed.get("data"):
            err = parsed["error"]
            raise ArkVideoError(
                f"API error from {method} {url}: {err}"
            )
        return parsed

    @staticmethod
    def _sleep_backoff(attempt: int) -> None:
        time.sleep(min(1.0 * (2 ** attempt), 8.0))

    # ------------------------------------------------------------------ #
    # Parameter conflict / dependency validation
    # ------------------------------------------------------------------ #
    @staticmethod
    def validate_params(
        *,
        text: str,
        image_url: str | None = None,
        first_frame: str | None = None,
        last_frame: str | None = None,
        duration: int = DEFAULT_DURATION,
        ratio: str = DEFAULT_RATIO,
        resolution: str = DEFAULT_RESOLUTION,
    ) -> None:
        """Raise ArkVideoError for conflicting or incomplete parameter combos.

        Rules (derived from the Seedance 2.0 docs):

        - text is required.
        - --image-url (a plain reference image = implicit first frame) is
          mutually exclusive with --first-frame/--last-frame (explicit role'd
          frame constraints). Mixing them is an ambiguous conditioning image.
        - --last-frame requires --first-frame; a last frame is only valid paired
          with a first frame.
        - ratio "adaptive" makes the output ratio follow the input image's
          aspect ratio, so it requires an image input. Use an explicit ratio
          (e.g. 16:9) for text-to-video.
        - duration must be a positive number of seconds.
        """
        if not text:
            raise ArkVideoError("text prompt is required (--text/-t)")

        if image_url and (first_frame or last_frame):
            raise ArkVideoError(
                "--image-url cannot be combined with --first-frame/--last-frame: "
                "a plain reference image and explicit frame constraints are mutually "
                "exclusive. Use either --image-url (image-to-video), "
                "--first-frame (image-to-video), or --first-frame + --last-frame."
            )

        if last_frame and not first_frame:
            raise ArkVideoError(
                "--last-frame requires --first-frame: a last frame is only valid "
                "together with a first frame."
            )

        if str(ratio).strip().lower() == "adaptive" and not (
            image_url or first_frame or last_frame
        ):
            raise ArkVideoError(
                'ratio "adaptive" requires an image input '
                "(--image-url / --first-frame): there is no input aspect ratio to "
                "adapt to for text-to-video. Pass an explicit ratio such as 16:9."
            )

        if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration <= 0:
            raise ArkVideoError(
                f"duration must be a positive number of seconds, got {duration!r}"
            )

    # ------------------------------------------------------------------ #
    # Request construction
    # ------------------------------------------------------------------ #
    @staticmethod
    def build_content(
        text: str,
        image_url: str | None = None,
        first_frame: str | None = None,
        last_frame: str | None = None,
    ) -> list[dict]:
        """Build the `content` array.

        - A single reference image (--image-url, no first/last frame) is sent as a
          plain image_url block, which the model treats as the first frame
          (standard image-to-video, matching the doc's first-frame example).
        - --first-frame / --last-frame add image blocks with explicit roles, used
          together for first-and-last-frame interpolation.
        """
        if not text:
            raise ArkVideoError("text prompt is required")
        content: list[dict] = [{"type": "text", "text": text}]
        if first_frame:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": first_frame},
                    "role": "first_frame",
                }
            )
        if last_frame:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": last_frame},
                    "role": "last_frame",
                }
            )
        if image_url:
            content.append(
                {"type": "image_url", "image_url": {"url": image_url}}
            )
        return content

    def build_request_body(
        self,
        *,
        text: str,
        image_url: str | None = None,
        first_frame: str | None = None,
        last_frame: str | None = None,
        duration: int = DEFAULT_DURATION,
        ratio: str = DEFAULT_RATIO,
        resolution: str = DEFAULT_RESOLUTION,
        seed: int | None = None,
    ) -> dict:
        # Fail fast on conflicting / incomplete parameter combinations before
        # constructing the request body.
        self.validate_params(
            text=text,
            image_url=image_url,
            first_frame=first_frame,
            last_frame=last_frame,
            duration=duration,
            ratio=ratio,
            resolution=resolution,
        )
        if self.api_type == API_TYPE_OPENAI_VIDEO:
            return self._build_openai_video_body(
                text=text,
                image_url=image_url,
                first_frame=first_frame,
                last_frame=last_frame,
                duration=duration,
                ratio=ratio,
                resolution=resolution,
                seed=seed,
            )
        if self.api_type == API_TYPE_OPENAI:
            return self._build_openai_body(
                text=text,
                image_url=image_url,
                first_frame=first_frame,
                last_frame=last_frame,
                duration=duration,
                ratio=ratio,
                resolution=resolution,
                seed=seed,
            )
        body: dict = {
            "model": self.model,
            "content": self.build_content(text, image_url, first_frame, last_frame),
            "generate_audio": FIXED_GENERATE_AUDIO,
            "ratio": ratio,
            "duration": duration,
            "watermark": FIXED_WATERMARK,
            "resolution": resolution,
        }
        if seed is not None:
            body["seed"] = seed
        return body

    def _build_openai_video_body(
        self,
        *,
        text: str,
        image_url: str | None = None,
        first_frame: str | None = None,
        last_frame: str | None = None,
        duration: int = DEFAULT_DURATION,
        ratio: str = DEFAULT_RATIO,
        resolution: str = DEFAULT_RESOLUTION,
        seed: int | None = None,
    ) -> dict:
        """Build an openai-video request body for POST /video/generations.

        Shape (openai-video protocol):
            {model, prompt, seconds, size, input_reference?}

        `seconds` is a string snapped to {4,8,12} (the endpoint rejects a
        number); `size` is derived from (ratio, resolution) as "WxH". Image
        inputs become a single `input_reference` string — a comma-joined list
        of URLs (one for a reference image, two for first+last frame).
        `generate_audio` / `watermark` / `ratio` / `duration` / `resolution` /
        `seed` are not part of the openai-video body and are omitted.
        """
        body: dict = {
            "model": self.model,
            "prompt": text,
            "seconds": self._seconds_for_duration(duration),
            "size": self._size_for(ratio, resolution),
        }
        refs: list[str] = []
        if image_url:
            refs.append(image_url)
        if first_frame:
            refs.append(first_frame)
        if last_frame:
            refs.append(last_frame)
        if refs:
            body["input_reference"] = ",".join(refs)
        return body

    def _build_openai_body(
        self,
        *,
        text: str,
        image_url: str | None = None,
        first_frame: str | None = None,
        last_frame: str | None = None,
        duration: int = DEFAULT_DURATION,
        ratio: str = DEFAULT_RATIO,
        resolution: str = DEFAULT_RESOLUTION,
        seed: int | None = None,
    ) -> dict:
        """Build an Ark-shaped request body for the openai (chat-mirror) endpoint.

        Shape (POST /video/generations, Ark-style params — the proxy's OpenAI
        chat-mirror entry accepts these for doubao-seedance-2.0):
            {model, prompt, generate_audio, ratio, duration, watermark,
             resolution, image?, first_frame?, last_frame?, seed?}

        `prompt` is the top-level text; image inputs are top-level URL fields.
        Unlike openai-video, this path supports `seed` and the Ark-style
        ratio/duration/resolution/generate_audio/watermark params. Audio is not
        produced on this backend.
        """
        body: dict = {
            "model": self.model,
            "prompt": text,
            "generate_audio": FIXED_GENERATE_AUDIO,
            "ratio": ratio,
            "duration": duration,
            "watermark": FIXED_WATERMARK,
            "resolution": resolution,
        }
        if image_url:
            body[OPENAI_FIELD_IMAGE] = image_url
        if first_frame:
            body[OPENAI_FIELD_FIRST_FRAME] = first_frame
        if last_frame:
            body[OPENAI_FIELD_LAST_FRAME] = last_frame
        if seed is not None:
            body["seed"] = seed
        return body

    @staticmethod
    def _seconds_for_duration(duration: int) -> str:
        """Snap an arbitrary second count to openai-video's allowed {4,8,12}.

        Returns a STRING — the endpoint's `seconds` field rejects a JSON number
        ("cannot unmarshal number into ... of type string").
        """
        d = int(duration)
        return str(min(OPENAI_VIDEO_ALLOWED_SECONDS, key=lambda s: (abs(s - d), s)))

    @staticmethod
    def _size_for(ratio: str, resolution: str) -> str:
        """Map seedance (ratio, resolution) to an OpenAI Videos `size` ("WxH").

        `resolution` gives the short-side pixel count; the ratio orients it:
        landscape/square -> height=base, width scaled; portrait -> width=base,
        height scaled. `adaptive` (no OpenAI equivalent) falls back to a
        landscape default.
        """
        base = _OPENAI_VIDEO_SIZE_BASE.get(str(resolution).lower(), 720)
        if ratio == "adaptive":
            width, height = base * 16 // 9, base  # landscape default
            return f"{width}x{height}"
        try:
            ws, hs = str(ratio).split(":")
            w, h = int(ws), int(hs)
        except Exception:
            return f"{base * 16 // 9}x{base}"
        if w >= h:  # landscape or square
            height = base
            width = round(base * w / h)
        else:  # portrait
            width = base
            height = round(base * h / w)
        return f"{width}x{height}"

    # ------------------------------------------------------------------ #
    # API operations
    # ------------------------------------------------------------------ #
    def create_task(self, body: dict) -> str:
        """POST a task; return its id."""
        if self.api_type != API_TYPE_ARK:
            path = "/video/generations"
        else:
            path = "/contents/generations/tasks"
        resp = self._http_request("POST", path, body)
        task_id = resp.get("id") or resp.get("task_id")
        if not task_id:
            raise ArkVideoError(f"create-task response did not contain an id: {resp}")
        return task_id

    def get_task(self, task_id: str) -> dict:
        """GET the current status/result of a task; return a normalized dict:
        {id, status, video_url, error, raw}."""
        if not task_id:
            raise ArkVideoError("task_id is required")
        if self.api_type != API_TYPE_ARK:
            path = f"/video/generations/{task_id}"
        else:
            path = f"/contents/generations/tasks/{task_id}"
        raw = self._http_request("GET", path)
        return self._normalize_task(raw)

    def _normalize_task(self, raw: dict) -> dict:
        """Normalize an api-specific task response into a common shape."""
        if self.api_type != API_TYPE_ARK:
            # openai / openai-video poll response: {code, message, data:{task_id,
            # status, result_url, fail_reason, ...}}. The video URL is a presigned
            # TOS URL inside data.result_url (no separate content endpoint).
            data = raw.get("data") or {}
            raw_status = str(data.get("status") or "").strip()
            status = raw_status.lower()
            if status in ("success", "succeeded"):
                status = SUCCEEDED
            elif status in ("fail", "failed", "error"):
                status = FAILED
            err = data.get("fail_reason") or None
            if not err and raw.get("code") and raw.get("code") != "success":
                err = raw.get("message") or raw.get("code")
                if not status:
                    status = FAILED
            return {
                "id": data.get("task_id") or data.get("id") or raw.get("id"),
                "status": status,
                "video_url": data.get("result_url"),
                "error": err,
                "raw": raw,
            }
        # ark
        content = raw.get("content") or {}
        return {
            "id": raw.get("id"),
            "status": raw.get("status"),
            "video_url": content.get("video_url"),
            "error": raw.get("error"),
            "raw": raw,
        }

    def wait_for_task(self, task_id: str) -> dict:
        """Poll until the task reaches a terminal state. Returns the final result."""
        deadline = time.monotonic() + self.timeout
        while True:
            result = self.get_task(task_id)
            status = result.get("status")
            if status == SUCCEEDED:
                return result
            if status == FAILED:
                raise ArkVideoError(f"task {task_id} failed: {result.get('error')}")
            # non-terminal (queued / running / IN_PROGRESS / None): keep polling
            if time.monotonic() >= deadline:
                raise ArkVideoError(
                    f"task {task_id} timed out after {self.timeout}s (last status: {status})"
                )
            time.sleep(self.poll_interval)

    def generate_video(
        self,
        *,
        text: str,
        image_url: str | None = None,
        first_frame: str | None = None,
        last_frame: str | None = None,
        duration: int = DEFAULT_DURATION,
        ratio: str = DEFAULT_RATIO,
        resolution: str = DEFAULT_RESOLUTION,
        seed: int | None = None,
    ) -> dict:
        """Synchronous entry point: create the task and block until it finishes.

        Returns the final task result dict (containing content.video_url).
        """
        body = self.build_request_body(
            text=text,
            image_url=image_url,
            first_frame=first_frame,
            last_frame=last_frame,
            duration=duration,
            ratio=ratio,
            resolution=resolution,
            seed=seed,
        )
        task_id = self.create_task(body)
        return self.wait_for_task(task_id)

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    @staticmethod
    def video_url(result: dict) -> str | None:
        # get_task/generate_video return normalized dicts with a "video_url" key.
        url = result.get("video_url")
        if url:
            return url
        # tolerate raw ark-style responses too.
        content = result.get("content")
        if isinstance(content, dict):
            return content.get("video_url")
        return None

    def download_video(self, video_url: str, dest_path: str) -> str:
        """Download the generated mp4 to dest_path. Returns dest_path.

        Robust to flaky links: verifies the byte count against Content-Length
        and resumes via HTTP Range on truncation, retrying transient stalls /
        timeouts (TimeoutError is not a URLError, so it is caught explicitly).
        Presigned TOS URLs (both api-types) need no auth header. Video files
        are larger than the API JSON `HTTP_TIMEOUT` is tuned for, so a longer
        per-read timeout (`DOWNLOAD_TIMEOUT`) is used.
        """
        last_err: Exception | None = None
        for attempt in range(self.http_retries + 1):
            have_before = os.path.getsize(dest_path) if os.path.isfile(dest_path) else 0
            headers: dict[str, str] = {"Accept": "*/*"}
            if have_before:
                headers["Range"] = f"bytes={have_before}-"
            try:
                req = urllib.request.Request(video_url, headers=headers)
                with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT, context=self._ssl_ctx) as resp:
                    ranged = resp.status == 206  # Range honored (resume)
                    if not ranged:
                        have_before = 0  # server sent full content from 0; discard partial
                    mode = "ab" if (ranged and have_before) else "wb"
                    written = 0
                    with open(dest_path, mode) as out:
                        while True:
                            chunk = resp.read(1 << 16)  # 64 KiB
                            if not chunk:
                                break
                            out.write(chunk)
                            written += len(chunk)
                    cl = resp.headers.get("Content-Length")
                    if cl is not None:
                        # For 206 this is the remaining bytes; for 200 the total.
                        expected = have_before + int(cl)
                        if have_before + written < expected:
                            last_err = ArkVideoError(
                                f"truncated: {have_before + written}/{expected} bytes"
                            )
                            if attempt < self.http_retries:
                                self._sleep_backoff(attempt)
                                continue
                            raise ArkVideoError(
                                f"download truncated after {self.http_retries + 1} attempts: "
                                f"{have_before + written}/{expected} bytes for {video_url}"
                            ) from None
                return dest_path
            except urllib.error.HTTPError as e:
                if e.code == 416:  # Range Not Satisfiable -> file already complete
                    return dest_path
                raise ArkVideoError(
                    f"failed to download {video_url}: HTTP {e.code} {e.reason}"
                ) from None
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last_err = e
                if attempt < self.http_retries:
                    self._sleep_backoff(attempt)
                    continue
                raise ArkVideoError(
                    f"failed to download {video_url} after {self.http_retries + 1} attempts: {last_err}"
                ) from None
        raise ArkVideoError(
            f"failed to download {video_url} after {self.http_retries + 1} attempts: {last_err}"
        ) from None


# ---------------------------------------------------------------------- #
# Alibaba OSS uploader (only used for local image files)
# ---------------------------------------------------------------------- #
# OSS env vars (see module docstring). Defaults match the spec.
OSS_ACCESS_KEY_ID_ENV = "OSS_ACCESS_KEY_ID"
OSS_ACCESS_KEY_SECRET_ENV = "OSS_ACCESS_KEY_SECRET"
OSS_REGION_ENV = "OSS_ENDPOINT"  # spec calls it "endpoint" but value is a region
OSS_BUCKET_ENV = "OSS_BUCKET"
OSS_PREFIX_ENV = "OSS_KEY_PREFIX"
DEFAULT_OSS_REGION = "cn-beijing"
DEFAULT_OSS_BUCKET = "jiangsier"
DEFAULT_OSS_PREFIX = "dev/"
OSS_SIGNED_URL_MINUTES = 10  # per spec


class OSSUploader:
    """Upload local image files to Alibaba OSS and return short-lived signed URLs.

    Uses the alibabacloud_oss_v2 SDK (imported lazily, so the dependency is only
    required when local images are actually used). Credentials come from
    OSS_ACCESS_KEY_ID / OSS_ACCESS_KEY_SECRET — the standard names the SDK's
    EnvironmentVariableCredentialsProvider also reads. We still read them
    explicitly to give a clear error up front, and build a
    StaticCredentialsProvider from them.
    """

    def __init__(
        self,
        access_key_id: str,
        access_key_secret: str,
        region: str = DEFAULT_OSS_REGION,
        bucket: str = DEFAULT_OSS_BUCKET,
        key_prefix: str = DEFAULT_OSS_PREFIX,
        signed_url_minutes: int = OSS_SIGNED_URL_MINUTES,
        oss_client=None,  # injectable for tests
    ) -> None:
        if not access_key_id or not access_key_secret:
            raise ArkVideoError(
                "OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET are required to upload local images. "
                "Set them in the environment or .env."
            )
        self.ak = access_key_id
        self.sk = access_key_secret
        self.region = region or DEFAULT_OSS_REGION
        self.bucket = bucket or DEFAULT_OSS_BUCKET
        self.key_prefix = key_prefix if key_prefix is not None else DEFAULT_OSS_PREFIX
        self.signed_url_minutes = signed_url_minutes
        self._oss_client = oss_client  # may be None; built lazily

    @classmethod
    def from_env(cls) -> "OSSUploader":
        return cls(
            access_key_id=os.environ.get(OSS_ACCESS_KEY_ID_ENV, ""),
            access_key_secret=os.environ.get(OSS_ACCESS_KEY_SECRET_ENV, ""),
            region=os.environ.get(OSS_REGION_ENV) or DEFAULT_OSS_REGION,
            bucket=os.environ.get(OSS_BUCKET_ENV) or DEFAULT_OSS_BUCKET,
            key_prefix=os.environ.get(OSS_PREFIX_ENV) or DEFAULT_OSS_PREFIX,
        )

    # ------------------------------------------------------------------ #
    def _key_for(self, local_path: str) -> str:
        """Object key: ${OSS_KEY_PREFIX}<filename>.

        Normalizes the prefix to end with a single '/' so that a prefix like
        "dev" produces "dev/foo.png" rather than "devfoo.png".
        """
        prefix = self.key_prefix or ""
        prefix = prefix.lstrip("/")
        if prefix and not prefix.endswith("/"):
            prefix += "/"
        filename = os.path.basename(local_path)
        if not filename:
            raise ArkVideoError(f"cannot derive object key from path: {local_path!r}")
        return f"{prefix}{filename}"

    @staticmethod
    def _resolve_region_endpoint(value: str) -> tuple[str, str | None]:
        """Given an OSS_ENDPOINT value, return (region, endpoint_host_or_None).

        Accepts either a region (e.g. 'cn-beijing') or a full endpoint host
        (e.g. 'oss-cn-beijing.aliyuncs.com'). When a host is given, the region
        is derived from the first label (stripping a leading 'oss-').
        """
        v = (value or "").strip()
        if not v:
            return DEFAULT_OSS_REGION, None
        host = v.split("://")[-1]  # strip scheme if present
        if "." in host or "aliyuncs" in host:
            first_label = host.split(".")[0]
            region = first_label[len("oss-"):] if first_label.startswith("oss-") else first_label
            return region, host
        return v, None

    def _oss(self):
        """Build (once) and return the OSS v2 client. Lazy import."""
        if self._oss_client is None:
            import alibabacloud_oss_v2 as oss

            provider = oss.credentials.StaticCredentialsProvider(self.ak, self.sk)
            cfg = oss.config.load_default()
            cfg.credentials_provider = provider
            region, endpoint = self._resolve_region_endpoint(self.region)
            cfg.region = region
            if endpoint:
                cfg.endpoint = endpoint
            self._oss_client = oss.Client(cfg)
        return self._oss_client

    def upload_and_sign(self, local_path: str) -> str:
        """Upload a local file to OSS and return a 10-minute signed download URL.

        The object key is ``${OSS_KEY_PREFIX}<basename>``. Returns the signed
        URL to use as the actual image input for the Seedance model.
        """
        if not os.path.isfile(local_path):
            raise ArkVideoError(f"local image not found: {local_path}")

        import datetime

        import alibabacloud_oss_v2 as oss

        key = self._key_for(local_path)
        client = self._oss()
        try:
            with open(local_path, "rb") as fh:
                client.put_object(
                    oss.PutObjectRequest(
                        bucket=self.bucket,
                        key=key,
                        body=fh,
                    )
                )
            presign = client.presign(
                oss.GetObjectRequest(bucket=self.bucket, key=key),
                expires=datetime.timedelta(minutes=self.signed_url_minutes),
            )
        except ArkVideoError:
            raise
        except Exception as e:
            raise ArkVideoError(f"OSS upload/sign failed for {local_path}: {e}") from None
        url = getattr(presign, "url", None)
        if not url:
            raise ArkVideoError(f"OSS presign returned no URL for {local_path}")
        return url


# ---------------------------------------------------------------------- #
# CLI
# ---------------------------------------------------------------------- #
def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="seedance",
        description="Synchronously generate a video with the doubao-seedance-2.0 model.",
    )
    p.add_argument("-t", "--text", required=True, help="Input prompt (required).")
    p.add_argument(
        "-i",
        "--image",
        help="Local reference image file (image-to-video). Uploaded to OSS. Optional.",
    )
    p.add_argument(
        "--image-url",
        dest="image_url",
        help="Online reference image URL (image-to-video). Optional. Mutually exclusive with --image.",
    )
    p.add_argument(
        "-f",
        "--first-frame",
        dest="first_frame",
        help="Local first-frame image file. Uploaded to OSS. Optional. Use with --last-frame.",
    )
    p.add_argument(
        "--first-frame-url",
        dest="first_frame_url",
        help="Online first-frame image URL. Optional. Mutually exclusive with --first-frame.",
    )
    p.add_argument(
        "-l",
        "--last-frame",
        dest="last_frame",
        help="Local last-frame image file. Uploaded to OSS. Optional. Use with --first-frame.",
    )
    p.add_argument(
        "--last-frame-url",
        dest="last_frame_url",
        help="Online last-frame image URL. Optional. Mutually exclusive with --last-frame.",
    )
    p.add_argument("--duration", type=int, default=DEFAULT_DURATION, help="Video duration in seconds (default 5).")
    p.add_argument("--ratio", default=DEFAULT_RATIO, help='Aspect ratio, e.g. 16:9 (default "16:9").')
    p.add_argument("--resolution", default=DEFAULT_RESOLUTION, help="480p/720p/1080p/4k (default 720p).")
    p.add_argument("-m", "--model", default=None, help=f"Model id for the actual API call (default {DEFAULT_MODEL_OPENAI_VIDEO} for openai-video, {DEFAULT_MODEL_OPENAI} for openai, {DEFAULT_MODEL_ARK} for ark). Lower priority than this flag; falls back to ARK_MODEL env, then the per-api-type default.")
    p.add_argument("--seed", type=int, default=None, help="Reproducibility seed. Optional.")
    p.add_argument("--save", help="If set, download the generated mp4 to this path.")
    p.add_argument("--poll-interval", type=int, default=DEFAULT_POLL_INTERVAL, help="Seconds between status polls (default 10).")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Max seconds to wait (default 1800).")
    p.add_argument("--endpoint", default=None, help="Override ARK_ENDPOINT.")
    p.add_argument(
        "--api-type",
        dest="api_type",
        choices=list(_API_TYPES),
        default=None,
        help=f"API protocol: 'openai-video' (doubao-seedance-2.0-mini), 'openai' (doubao-seedance-2.0 full, Ark-shaped body), or 'ark' (raw Volcengine Ark). Default {DEFAULT_API_TYPE}. Lower priority than this flag; falls back to ARK_API_TYPE env, then the default.",
    )
    p.add_argument(
        "--insecure",
        action="store_true",
        help="Disable TLS certificate verification (for proxies whose cert chain Python 3.14 rejects). Also ARK_INSECURE=1.",
    )
    p.add_argument(
        "--env-file",
        default=DEFAULT_ENV_FILE,
        help=f"Path to a .env file to load ARK_API_KEY/ARK_ENDPOINT and OSS_* from (default {DEFAULT_ENV_FILE}). Set to empty string to skip.",
    )
    return p


def _resolve_image_inputs(args) -> dict:
    """Resolve --image*/--first-frame*/--last-frame* options into URLs.

    Validates that a local file and a `*-url` for the same slot are not both
    given, then uploads any local files to OSS and returns the resolved URLs.

    Returns a dict with keys: image_url, first_frame, last_frame (each a URL
    string or None).
    """
    # Per-slot exclusivity: a local file and an online URL cannot both be given.
    def _exclusive(local, url, name):
        if local and url:
            raise ArkVideoError(
                f"--{name} (local file) and --{name}-url (online URL) cannot both be specified"
            )

    _exclusive(args.image, args.image_url, "image")
    _exclusive(args.first_frame, args.first_frame_url, "first-frame")
    _exclusive(args.last_frame, args.last_frame_url, "last-frame")

    # Presence flags (only truthiness is used by validate_params, so passing the
    # raw local path here as a placeholder is safe and lets us fail fast on
    # cross-slot conflicts before doing any OSS upload).
    ArkVideoClient.validate_params(
        text=args.text,
        image_url=args.image or args.image_url,
        first_frame=args.first_frame or args.first_frame_url,
        last_frame=args.last_frame or args.last_frame_url,
        duration=args.duration,
        ratio=args.ratio,
        resolution=args.resolution,
    )

    resolved = {
        "image_url": args.image_url,
        "first_frame": args.first_frame_url,
        "last_frame": args.last_frame_url,
    }
    locals_to_upload = {
        "image_url": args.image,
        "first_frame": args.first_frame,
        "last_frame": args.last_frame,
    }
    if any(locals_to_upload.values()):
        uploader = OSSUploader.from_env()
        for slot, local_path in locals_to_upload.items():
            if local_path:
                resolved[slot] = uploader.upload_and_sign(local_path)
    return resolved


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)

    # Load .env first so ARK_API_KEY / ARK_ENDPOINT are available; the real
    # environment always takes precedence over the file.
    if args.env_file:
        load_dotenv(args.env_file)

    # Model id is resolved per api-type inside ArkVideoClient when not given.
    try:
        client = ArkVideoClient(
            endpoint=args.endpoint,
            model=args.model,
            poll_interval=args.poll_interval,
            timeout=args.timeout,
            api_type=args.api_type,
            insecure=args.insecure or None,
        )
        if args.seed is not None and client.api_type == API_TYPE_OPENAI_VIDEO:
            print(
                "warning: --seed is not supported by the openai-video endpoint "
                "and will be ignored (use --api-type ark for reproducible seeds).",
                file=sys.stderr,
            )
        # Resolve local image files (upload to OSS) and online URLs into the
        # actual image URLs the model consumes. Validates conflicts up front.
        resolved = _resolve_image_inputs(args)
    except ArkVideoError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    try:
        result = client.generate_video(
            text=args.text,
            image_url=resolved["image_url"],
            first_frame=resolved["first_frame"],
            last_frame=resolved["last_frame"],
            duration=args.duration,
            ratio=args.ratio,
            resolution=args.resolution,
            seed=args.seed,
        )
    except ArkVideoError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))

    url = ArkVideoClient.video_url(result)
    if url:
        print(f"\nvideo_url: {url}", file=sys.stderr)
        if args.save:
            try:
                client.download_video(url, args.save)
                print(f"saved: {args.save}", file=sys.stderr)
            except ArkVideoError as e:
                print(f"error downloading video: {e}", file=sys.stderr)
                return 1
    else:
        print("warning: task succeeded but no video_url found", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
