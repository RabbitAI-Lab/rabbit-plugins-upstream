"""Xiaohongshu provider backed by yt-dlp.

Download fallback order:
1. Anonymous yt-dlp (no cookies)
2. Public direct URL (from yt-dlp metadata formats)
3. yt-dlp with Chrome cookies (last resort)
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from time import strftime
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from folder_utils import make_output_folder, parse_ytdlp_date

PLATFORM = "xiaohongshu"

MOBILE_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 "
    "Mobile/15E148 Safari/604.1"
)

# Regex patterns for cookie auth failure detection
_COOKIE_FAILURE_PATTERNS = [
    r"keychain",
    r"Keychain",
    r"cannot (access|open|read).*cookie",
    r"permission denied.*cookie",
    r"cookies?.+not found",
    r"failed to decrypt",
    r"无法.*(读取|访问).*cookie",
    r"拒绝",
    r"denied",
]

# Remote assistant marker — set by the agent when running on behalf of a
# remote trigger, so we don't hang waiting for local GUI dialogs.
_IS_REMOTE_ASSISTANT = os.environ.get("VIDEO_DOWNLOADER_REMOTE", "").lower() in ("1", "true", "yes")


def supports(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return any(domain in host for domain in ("xiaohongshu.com", "xhslink.com", "xhslink.cn"))


# ---------------------------------------------------------------------------
# Main fetch entry point
# ---------------------------------------------------------------------------

def fetch(url: str, output_root: Path, *, metadata_only: bool = False, **options) -> dict:
    # Step 1: anonymous metadata only — never trigger cookies just for metadata
    metadata, meta_source = _extract_metadata_anonymous(url)

    item_id = _item_id(metadata)
    folder = make_output_folder(
        output_root,
        platform=PLATFORM,
        date=parse_ytdlp_date(metadata.get("upload_date")),
        title=metadata.get("title"),
        author=metadata.get("uploader") or metadata.get("channel"),
        item_id=item_id,
    )

    caption = _post_caption(metadata)
    post_caption_path = folder / "post_caption.txt"
    post_caption_path.write_text(caption, encoding="utf-8")

    # Download orchestration
    video_path = None
    download_method = None
    cookie_used = False
    direct_url_source = None
    fallback_errors: list[dict] = []
    validation: dict | None = None

    if not metadata_only:
        video_path, download_method, cookie_used, direct_url_source, fallback_errors, validation = (
            _download_with_fallback(url, metadata, folder, _safe_filename(metadata.get("title"), item_id))
        )

    normalized = _normalize_metadata(
        source_url=url,
        metadata=metadata,
        item_id=item_id,
        caption=caption,
        video_path=video_path,
        metadata_only=metadata_only,
        meta_source=meta_source,
        download_method=download_method,
        cookie_used=cookie_used,
        direct_url_source=direct_url_source,
        fallback_errors=fallback_errors,
        validation=validation,
    )

    metadata_path = folder / "metadata.json"
    metadata_path.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return {
        "platform": PLATFORM,
        "id": item_id,
        "output_dir": str(folder),
        "video_path": str(video_path) if video_path else None,
        "post_caption_path": str(post_caption_path),
        "caption_path": str(post_caption_path),
        "metadata_path": str(metadata_path),
        "post_caption": caption,
        "caption": caption,
        "author": normalized.get("author", {}).get("nickname"),
        "duration_seconds": normalized.get("video", {}).get("duration_seconds"),
        "resolution": normalized.get("video", {}).get("resolution"),
        "download_method": download_method,
    }


# ---------------------------------------------------------------------------
# Metadata extraction (anonymous only)
# ---------------------------------------------------------------------------

def _extract_metadata_anonymous(url: str) -> tuple[dict, str]:
    """Extract metadata with anonymous yt-dlp (no cookies).

    Returns (metadata_dict, source_label).
    source_label is one of: "yt_dlp_anonymous", "yt_dlp_anonymous_partial".
    """
    yt_dlp = _require_ytdlp()
    command = [yt_dlp, "--no-playlist", "--dump-single-json", url]
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=240,
        )
        if result.returncode == 0:
            return json.loads(result.stdout), "yt_dlp_anonymous"
        # Anonymous metadata extraction failed — try to get whatever we can
        # by extracting info from the URL redirect / page title
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    except (json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError(f"Anonymous yt-dlp metadata extraction failed: {exc}") from exc


# ---------------------------------------------------------------------------
# Download orchestration
# ---------------------------------------------------------------------------

def _download_with_fallback(
    url: str,
    metadata: dict,
    folder: Path,
    filename: str,
) -> tuple[Path | None, str | None, bool, str | None, list[dict], dict | None]:
    """Try downloading in this order: anonymous yt-dlp → direct URL → Chrome cookies.

    Returns:
        (video_path, method, cookie_used, direct_url_source, fallback_errors, validation)
    """
    fallback_errors: list[dict] = []
    validation: dict | None = None

    # ---- Route 1: anonymous yt-dlp ----
    video_path, err, validation = _try_anonymous_ytdlp_download(url, folder, filename)
    if video_path is not None:
        return video_path, "yt_dlp_anonymous", False, None, fallback_errors, validation
    if err:
        fallback_errors.append({"route": "yt_dlp_anonymous", "error": err})

    # ---- Route 2: public direct URL ----
    video_path, direct_url_source, err, validation = _try_direct_url_download(metadata, folder, filename)
    if video_path is not None:
        return video_path, "public_direct_url", False, direct_url_source, fallback_errors, validation
    if err:
        fallback_errors.append({"route": "public_direct_url", "error": err})

    # ---- Route 3: Chrome cookies ----
    if _IS_REMOTE_ASSISTANT:
        # Don't block remote tasks — report immediately
        raise RuntimeError(
            "Anonymous yt-dlp and public direct URL both failed. "
            "Chrome Cookie auth is required but unavailable in remote mode. "
            "Please run this download from the desktop app."
        )

    video_path, err, cookie_refused, validation = _try_cookie_ytdlp_download(url, folder, filename)
    if video_path is not None:
        return video_path, "yt_dlp_chrome_cookies", True, None, fallback_errors, validation

    if cookie_refused:
        fallback_errors.append({
            "route": "yt_dlp_chrome_cookies",
            "error": err or "Chrome Cookie access was denied or unavailable",
            "cookie_refused": True,
        })
    else:
        fallback_errors.append({"route": "yt_dlp_chrome_cookies", "error": err or "Unknown error"})

    # All routes exhausted
    raise RuntimeError(
        "All download routes for Xiaohongshu failed:\n" +
        "\n".join(f"  [{e['route']}] {e.get('error', '')}" for e in fallback_errors)
    )


# ---------------------------------------------------------------------------
# Video file validation
# ---------------------------------------------------------------------------

def _validate_video_file(path: Path) -> tuple[bool, dict]:
    """Validate that a downloaded file is a real video.

    Checks:
    1. File exists
    2. File size >= 100 KB (102400 bytes)
    3. ffprobe detects at least one video stream (if ffprobe is available)

    Returns: (is_valid, validation_info_dict)
    """
    MIN_SIZE = 100 * 1024  # 100 KB

    info: dict = {
        "file_size_bytes": 0,
        "minimum_size_passed": False,
        "ffprobe_available": False,
        "video_stream_found": False,
        "valid": False,
        "error": None,
    }

    # Check 1: file exists
    if not path.exists():
        info["error"] = f"File does not exist: {path.name}"
        return False, info

    # Check 2: file size
    file_size = path.stat().st_size
    info["file_size_bytes"] = file_size
    if file_size < MIN_SIZE:
        info["error"] = f"File too small ({file_size} bytes, minimum {MIN_SIZE})"
        return False, info
    info["minimum_size_passed"] = True

    # Check 3: ffprobe video stream
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        info["ffprobe_available"] = False
        # ffprobe not available — pass on size check alone, but record honestly
        info["video_stream_found"] = False
        info["valid"] = True
        return True, info

    info["ffprobe_available"] = True
    try:
        result = subprocess.run(
            [
                ffprobe,
                "-v", "error",
                "-select_streams", "v:0",
                "-show_entries", "stream=codec_type",
                "-of", "csv=p=0",
                str(path),
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0 and "video" in result.stdout.strip():
            info["video_stream_found"] = True
            info["valid"] = True
            return True, info
        else:
            error_msg = result.stderr.strip() or result.stdout.strip() or "no video stream found"
            info["error"] = f"ffprobe: {error_msg}"
            return False, info
    except subprocess.TimeoutExpired:
        info["error"] = "ffprobe timed out"
        return False, info


# ---------------------------------------------------------------------------
# Route 1: Anonymous yt-dlp download
# ---------------------------------------------------------------------------

def _try_anonymous_ytdlp_download(url: str, folder: Path, filename: str) -> tuple[Path | None, str | None, dict | None]:
    yt_dlp = _require_ytdlp()
    output_path = folder / filename
    command = [
        yt_dlp,
        "--no-playlist",
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", str(output_path),
        url,
    ]
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=900,
        )
        if completed.returncode == 0:
            found = _find_output_file(output_path, folder)
            is_valid, validation = _validate_video_file(found)
            if is_valid:
                return found, None, validation
            # Invalid file — delete it and report failure so fallback continues
            try:
                found.unlink()
            except OSError:
                pass
            return None, f"yt_dlp_anonymous validation failed: {validation.get('error', 'unknown')}", None
        return None, (completed.stderr.strip() or completed.stdout.strip() or "Unknown yt-dlp error"), None
    except subprocess.TimeoutExpired:
        return None, "Anonymous yt-dlp download timed out", None


# ---------------------------------------------------------------------------
# Route 2: Public direct URL download
# ---------------------------------------------------------------------------

def _try_direct_url_download(
    metadata: dict,
    folder: Path,
    filename: str,
) -> tuple[Path | None, str | None, str | None, dict | None]:
    """Try to download via a direct video URL extracted from yt-dlp metadata.

    Returns: (video_path, source_field, error)
    """
    direct_url, source_field = _extract_best_direct_url(metadata)
    if not direct_url:
        return None, None, "No public direct video URL found in yt-dlp metadata"

    output_path = folder / filename
    webpage_url = metadata.get("webpage_url") or metadata.get("original_url") or ""

    headers = {
        "User-Agent": MOBILE_UA,
        "Referer": webpage_url,
    }

    try:
        _http_download(direct_url, output_path, headers)
        if output_path.exists() and output_path.stat().st_size > 0:
            is_valid, validation = _validate_video_file(output_path)
            if is_valid:
                return output_path, source_field, None, validation
            try:
                output_path.unlink()
            except OSError:
                pass
            return None, source_field, f"public_direct_url validation failed: {validation.get('error', 'unknown')}", None
        return None, source_field, f"Direct URL download produced empty file (source: {source_field})", None
    except RuntimeError as exc:
        return None, source_field, f"Direct URL download failed: {exc}", None


def _extract_best_direct_url(metadata: dict) -> tuple[str | None, str | None]:
    """Extract the highest-quality direct video URL from yt-dlp metadata.

    Checks (in order): formats list, requested_formats, direct url field.

    Returns: (url, source_field_name) or (None, None).
    """
    formats = metadata.get("formats") or []

    # Pick best format: prefer mp4/h264, highest resolution
    best = None
    best_score = -1
    for fmt in formats:
        fmt_url = fmt.get("url")
        if not fmt_url:
            continue
        # Score: prefer video formats, higher resolution
        score = 0
        if fmt.get("vcodec") and fmt.get("vcodec") != "none":
            score += 100
        if fmt.get("acodec") and fmt.get("acodec") != "none":
            score += 10
        height = fmt.get("height") or 0
        score += height
        if score > best_score:
            best_score = score
            best = fmt

    if best:
        return best.get("url"), f"formats[{best.get('format_id', '?')}]"

    # Fallback: direct url field
    direct = metadata.get("url")
    if direct:
        return direct, "url"

    # Fallback: requested_formats
    requested = metadata.get("requested_formats") or []
    for fmt in requested:
        if fmt.get("url"):
            return fmt.get("url"), f"requested_formats[{fmt.get('format_id', '?')}]"

    return None, None


def _http_download(url: str, destination: Path, headers: dict[str, str]) -> None:
    """Download a file via HTTP with atomic temp-file replacement.

    Follows redirects automatically (urllib default).
    """
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=300) as response:
            final_url = response.geturl()
            suffix = destination.suffix or ".mp4"
            with tempfile.NamedTemporaryFile(
                "wb",
                delete=False,
                dir=str(destination.parent),
                suffix=suffix,
            ) as tmp:
                shutil.copyfileobj(response, tmp)
                tmp_path = Path(tmp.name)

        # Atomic replace
        tmp_path.replace(destination)
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} fetching {url}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error fetching {url}: {exc}") from exc


# ---------------------------------------------------------------------------
# Route 3: Chrome cookies yt-dlp (last resort)
# ---------------------------------------------------------------------------

def _try_cookie_ytdlp_download(
    url: str,
    folder: Path,
    filename: str,
) -> tuple[Path | None, str | None, bool, dict | None]:
    """Try yt-dlp with Chrome cookies.

    Returns: (video_path, error, cookie_refused)
    """
    yt_dlp = _require_ytdlp()
    output_path = folder / filename
    command = [
        yt_dlp,
        "--cookies-from-browser", "chrome",
        "--no-playlist",
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", str(output_path),
        url,
    ]
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=900,
        )
        stderr = completed.stderr.strip() or ""
        stdout = completed.stdout.strip() or ""

        if completed.returncode == 0:
            found = _find_output_file(output_path, folder)
            is_valid, validation = _validate_video_file(found)
            if is_valid:
                return found, None, False, validation
            try:
                found.unlink()
            except OSError:
                pass
            return None, f"yt_dlp_chrome_cookies validation failed: {validation.get('error', 'unknown')}", False, None

        combined = f"{stderr}\n{stdout}"
        cookie_refused = _detect_cookie_refusal(combined)
        return None, combined or "Unknown yt-dlp error with cookies", cookie_refused, None

    except subprocess.TimeoutExpired:
        return None, "yt-dlp with Chrome cookies timed out", False, None


def _detect_cookie_refusal(error_text: str) -> bool:
    """Check if the error indicates Chrome cookie access was denied."""
    return any(re.search(pattern, error_text) for pattern in _COOKIE_FAILURE_PATTERNS)


# ---------------------------------------------------------------------------
# Metadata normalization
# ---------------------------------------------------------------------------

def _normalize_metadata(
    source_url: str,
    metadata: dict,
    *,
    item_id: str,
    caption: str,
    video_path: Path | None,
    metadata_only: bool,
    meta_source: str,
    download_method: str | None,
    cookie_used: bool,
    direct_url_source: str | None,
    fallback_errors: list[dict],
    validation: dict | None = None,
) -> dict:
    width = metadata.get("width")
    height = metadata.get("height")

    download_info: dict = {
        "method": download_method,
        "video_path": str(video_path) if video_path else None,
        "metadata_only": metadata_only,
        "cookie_used": cookie_used,
    }
    if direct_url_source:
        download_info["direct_url_source"] = direct_url_source
    if fallback_errors:
        download_info["fallback_errors"] = fallback_errors
    if validation:
        download_info["validation"] = validation

    return {
        "platform": PLATFORM,
        "source_url": source_url,
        "final_url": metadata.get("webpage_url") or metadata.get("original_url"),
        "fetched_at": strftime("%Y-%m-%dT%H:%M:%S%z"),
        "id": item_id,
        "caption": caption,
        "title": metadata.get("title"),
        "description": metadata.get("description"),
        "tags": metadata.get("tags") or [],
        "author": {
            "nickname": metadata.get("uploader") or metadata.get("channel"),
            "id": metadata.get("uploader_id") or metadata.get("channel_id"),
        },
        "video": {
            "width": width,
            "height": height,
            "resolution": _resolution(width, height),
            "duration_seconds": metadata.get("duration"),
            "filesize": metadata.get("filesize"),
            "thumbnail": metadata.get("thumbnail"),
        },
        "download": download_info,
        "raw_ytdlp_metadata": metadata,
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _post_caption(metadata: dict) -> str:
    parts = []
    title = (metadata.get("title") or "").strip()
    description = (metadata.get("description") or "").strip()
    if title:
        parts.append(title)
    if description and description != title:
        parts.append(description)
    return "\n\n".join(parts)


def _item_id(metadata: dict) -> str:
    for key in ("id", "display_id", "webpage_url_basename"):
        value = metadata.get(key)
        if value:
            return _safe_id(str(value))
    return "unknown"


def _safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-") or "unknown"


def _safe_filename(title: str | None, item_id: str) -> str:
    stem = title or item_id
    stem = re.sub(r"[\\/:*?\"<>|\n\r\t]+", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    stem = stem[:80].strip() or item_id
    return f"{stem}-{item_id}.mp4"


def _resolution(width: int | None, height: int | None) -> str | None:
    if width and height:
        return f"{width}x{height}"
    return None


def _require_ytdlp() -> str:
    yt_dlp = shutil.which("yt-dlp")
    if yt_dlp:
        return yt_dlp
    raise RuntimeError(
        "Xiaohongshu provider requires yt-dlp, but yt-dlp is not installed or not on PATH."
    )


def _find_output_file(output_path: Path, folder: Path) -> Path:
    """Find the downloaded file — yt-dlp may append extensions."""
    if output_path.exists():
        return output_path
    matches = sorted(folder.glob(f"{output_path.stem}.*"))
    if matches:
        return matches[0]
    raise RuntimeError("yt-dlp reported success but no downloaded video file was found.")
