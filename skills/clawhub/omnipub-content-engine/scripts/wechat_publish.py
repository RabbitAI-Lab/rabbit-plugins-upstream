"""
Draft creation — create WeChat draft via draft/add API.
"""

import json
import requests
from dataclasses import dataclass
from typing import Optional


@dataclass
class DraftResult:
    media_id: str


def _safe_title(title: str, max_chars: int = 64) -> str:
    if len(title) <= max_chars:
        return title
    return title[:max_chars]


def _safe_digest(digest: str, max_chars: int = 120) -> str:
    if len(digest) <= max_chars:
        return digest
    return digest[:max_chars]


def create_draft(
    access_token: str,
    title: str,
    html: str,
    digest: str,
    thumb_media_id: Optional[str] = None,
    author: Optional[str] = None,
) -> DraftResult:
    """Create a draft in WeChat."""
    safe_title = _safe_title(title, max_chars=64)
    safe_digest = _safe_digest(digest, max_chars=120)
    safe_author = (author or "")[:8]

    article = {
        "title": safe_title,
        "author": safe_author,
        "digest": safe_digest,
        "content": html,
        "show_cover_pic": 0,
    }
    if thumb_media_id:
        article["thumb_media_id"] = thumb_media_id

    body = {"articles": [article]}
    resp = requests.post(
        "https://api.weixin.qq.com/cgi-bin/draft/add",
        params={"access_token": access_token},
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    data = resp.json()
    errcode = data.get("errcode", 0)
    if errcode != 0:
        errmsg = data.get("errmsg", "unknown error")
        raise ValueError(f"create_draft error: errcode={errcode}, errmsg={errmsg}")
    if "media_id" not in data:
        raise ValueError(f"create_draft: missing media_id: {data}")
    return DraftResult(media_id=data["media_id"])
