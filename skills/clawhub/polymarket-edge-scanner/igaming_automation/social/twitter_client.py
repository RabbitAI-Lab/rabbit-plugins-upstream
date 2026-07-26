#!/usr/bin/env python3
"""X (Twitter) client. Drafts posts by default; live posting via the twitter-post skill."""

import json
import subprocess
from pathlib import Path

from config import SOCIAL_CREDENTIALS_PATH
from social.base import format_post, save_draft

TWITTER_POST_SKILL = Path(__file__).parent.parent.parent / "skills" / "twitter-post" / "scripts" / "tweet.js"


def load_credentials():
    if not SOCIAL_CREDENTIALS_PATH.exists():
        return None
    with open(SOCIAL_CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        return json.load(f).get("twitter")


def has_oauth1_credentials(credentials: dict) -> bool:
    return all(
        credentials.get(k)
        for k in ["consumer_key", "consumer_secret", "access_token", "access_token_secret"]
    )


def post_tweet(text: str, credentials: dict):
    """Post a tweet using the installed twitter-post skill."""
    if not TWITTER_POST_SKILL.exists():
        raise RuntimeError("twitter-post skill not installed. Run: openclaw skills install twitter-post")

    env = {
        "TWITTER_CONSUMER_KEY": credentials["consumer_key"],
        "TWITTER_CONSUMER_SECRET": credentials["consumer_secret"],
        "TWITTER_ACCESS_TOKEN": credentials["access_token"],
        "TWITTER_ACCESS_TOKEN_SECRET": credentials["access_token_secret"],
    }
    result = subprocess.run(
        ["node", str(TWITTER_POST_SKILL), text],
        capture_output=True,
        text=True,
        env={**dict(__import__("os").environ), **env},
        timeout=60,
        check=False,
    )
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        data = {"ok": False, "stdout": result.stdout, "stderr": result.stderr}
    if not data.get("ok"):
        raise RuntimeError(f"Twitter post failed: {data.get('error') or result.stderr}")
    return data


def publish_or_draft(post_id: int, title: str, url: str, dry_run: bool = True):
    credentials = load_credentials()
    text = format_post(title, url, platform="x")

    if dry_run or not credentials or not has_oauth1_credentials(credentials):
        save_draft(post_id, title, url, platforms=["x"])
        print(f"[Twitter] Draft saved for post {post_id}")
        return {"draft": True, "body": text}

    result = post_tweet(text, credentials)
    print(f"[Twitter] Posted tweet for post {post_id}: {result.get('url')}")
    return result
