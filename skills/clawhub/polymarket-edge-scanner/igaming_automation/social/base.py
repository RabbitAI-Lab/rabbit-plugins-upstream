#!/usr/bin/env python3
"""Base utilities for social media post generation."""

import json
from datetime import datetime, timezone
from pathlib import Path

DRAFTS_PATH = Path(__file__).parent.parent / "social_drafts.json"


def format_post(title: str, url: str, platform: str = "x") -> str:
    """Generate a platform-appropriate social post."""
    hashtags = "#SouthAfrica #iGaming #BettingTips"
    if platform == "x":
        body = f"{title}\n\n{url}\n\n{hashtags}"
        if len(body) > 280:
            body = f"{title[:100]}...\n\n{url}\n\n{hashtags}"
        return body
    elif platform == "linkedin":
        return (
            f"{title}\n\n"
            f"New on the site: a straight-up guide for South African players. "
            f"Worth a read if you bet online.\n\n"
            f"{url}\n\n"
            f"{hashtags}"
        )
    return f"{title}\n{url}"


def save_draft(post_id: int, title: str, url: str, platforms: list):
    drafts = []
    if DRAFTS_PATH.exists():
        with open(DRAFTS_PATH, "r", encoding="utf-8") as f:
            drafts = json.load(f)

    for platform in platforms:
        drafts.append({
            "post_id": post_id,
            "title": title,
            "url": url,
            "platform": platform,
            "body": format_post(title, url, platform),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "posted": False,
        })

    with open(DRAFTS_PATH, "w", encoding="utf-8") as f:
        json.dump(drafts, f, indent=2)
