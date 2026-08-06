"""Shared folder-naming logic for video-downloader providers.

Naming convention: YY_MM_DD_标题摘要_平台_作者
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

# Platform key → Chinese display name
_PLATFORM_CN: dict[str, str] = {
    "douyin": "抖音",
    "bilibili": "B站",
    "youtube": "YouTube",
    "xiaohongshu": "小红书",
}

# Maximum title length in Unicode code points
MAX_TITLE_CHARS = 40


def make_output_folder(
    output_root: Path,
    platform: str,
    date: datetime | None,
    title: str | None,
    author: str | None,
    item_id: str,
) -> Path:
    """Create the output folder with a human-readable name.

    Folder format: ``YY_MM_DD_标题摘要_平台_作者``

    If the folder already exists, the last 5 characters of *item_id* are
    appended to disambiguate.
    """
    date_str = _format_date(date)
    clean_title = _clean_title(title)
    platform_cn = _PLATFORM_CN.get(platform, platform)
    author_str = _safe_author(author)

    base_name = f"{date_str}_{clean_title}_{platform_cn}_{author_str}"
    folder = output_root / base_name

    # Dedup: append last-5 of item_id if folder already exists
    if folder.exists():
        suffix = _safe_id_suffix(item_id)
        folder = output_root / f"{base_name}_{suffix}"

    folder.mkdir(parents=True, exist_ok=True)
    return folder


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _format_date(date: datetime | None) -> str:
    """Format datetime as ``YY_MM_DD``; fall back to today in local time."""
    dt = date or datetime.now()
    return dt.strftime("%y_%m_%d")


def _clean_title(title: str | None) -> str:
    """Clean a video title for use in a folder name.

    Steps:
    1. Remove newlines and carriage returns
    2. Remove leading ``#`` hashtag markers
    3. Strip emoji and other non-CJK / non-ASCII symbols
    4. Collapse consecutive whitespace
    5. Trim to MAX_TITLE_CHARS code points
    """
    if not title:
        return "未命名视频"

    text = title.strip()

    # Drop newlines
    text = text.replace("\n", " ").replace("\r", " ")

    # Remove hashtag markers (keep the word after #)
    text = re.sub(r"#\S+", "", text)

    # Remove @ mentions
    text = re.sub(r"@\S+", "", text)

    # Keep: Chinese (CJK), letters, digits, spaces, and a small set of safe punctuation
    # Remove everything else (emoji, special symbols, etc.)
    text = re.sub(r"[^\u4e00-\u9fff\u3400-\u4dbfa-zA-Z0-9 .\-_()（）【】\[\]《》]", "", text)

    # Collapse consecutive spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Remove leading/trailing junk punctuation
    text = text.strip(" .-_")

    if not text:
        return "未命名视频"

    # Truncate to max chars (preserve trailing CJK boundary when possible)
    if len(text) > MAX_TITLE_CHARS:
        text = text[:MAX_TITLE_CHARS].rstrip(" .-_")

    return text


def _safe_author(author: str | None) -> str:
    """Return the author name or ``未知作者``."""
    if not author:
        return "未知作者"
    # Clean simple cases
    author = author.strip()
    if not author:
        return "未知作者"
    # Remove characters unsafe for folder names
    author = re.sub(r'[\\/:*?"<>|]', "", author)
    return author or "未知作者"


def _safe_id_suffix(item_id: str) -> str:
    """Return last 5 alphanumeric chars of an ID for dedup."""
    cleaned = re.sub(r"[^A-Za-z0-9]", "", item_id)
    return cleaned[-5:] if len(cleaned) >= 5 else cleaned


# ---------------------------------------------------------------------------
# Date extractors (provider-specific)
# ---------------------------------------------------------------------------

def parse_ytdlp_date(upload_date: str | None) -> datetime | None:
    """Parse yt-dlp ``upload_date`` (YYYYMMDD) → datetime."""
    if not upload_date:
        return None
    try:
        return datetime.strptime(str(upload_date)[:8], "%Y%m%d")
    except ValueError:
        return None


def parse_timestamp(ts: int | float | None) -> datetime | None:
    """Parse Unix timestamp (seconds) → UTC datetime."""
    if ts is None:
        return None
    try:
        ts = int(ts)
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    except (ValueError, TypeError, OSError):
        return None
