#!/usr/bin/env python3
"""LinkedIn client via the linkedin-api skill / Maton gateway.

Drafts posts by default; live posting requires a Maton API key and an
active LinkedIn OAuth connection.
"""

import json
import os

import requests

from config import SOCIAL_CREDENTIALS_PATH
from social.base import format_post, save_draft

MATON_GATEWAY = "https://api.maton.ai"


def load_credentials():
    if not SOCIAL_CREDENTIALS_PATH.exists():
        return None
    with open(SOCIAL_CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        return json.load(f).get("linkedin")


def get_maton_api_key(credentials: dict) -> str | None:
    return os.environ.get("MATON_API_KEY") or credentials.get("maton_api_key")


def maton_headers(credentials: dict) -> dict:
    api_key = get_maton_api_key(credentials)
    if not api_key:
        raise RuntimeError("MATON_API_KEY not set. Sign up at maton.ai and add your key.")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "LinkedIn-Version": "202502",
    }


def get_organization_urn(credentials: dict) -> str:
    """The iGamingReviews org page URN — the ONLY author we ever post as."""
    urn = credentials.get("organization_urn")
    if not urn:
        raise RuntimeError("linkedin.organization_urn missing from social_credentials.json")
    return urn


def post_share(text: str, credentials: dict):
    """Create a LinkedIn text post via Maton, AS THE ORGANIZATION.

    Posts must never go to a personal profile feed (Trevor's rule). The author
    is always urn:li:organization:126833959 (iGamingReviews); the token is the
    page admin's, which is how LinkedIn org posting works.
    """
    org_urn = get_organization_urn(credentials)
    headers = maton_headers(credentials)
    payload = {
        "author": org_urn,
        "lifecycleState": "PUBLISHED",
        "visibility": "PUBLIC",
        "commentary": text,
        "distribution": {"feedDistribution": "MAIN_FEED"},
    }
    response = requests.post(
        f"{MATON_GATEWAY}/linkedin/rest/posts",
        headers=headers,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return {"ok": True, "location": response.headers.get("location")}


def publish_or_draft(post_id: int, title: str, url: str, dry_run: bool = True):
    credentials = load_credentials()
    text = format_post(title, url, platform="linkedin")

    if dry_run or not credentials or not get_maton_api_key(credentials):
        save_draft(post_id, title, url, platforms=["linkedin"])
        print(f"[LinkedIn] Draft saved for post {post_id}")
        return {"draft": True, "body": text}

    result = post_share(text, credentials)
    print(f"[LinkedIn] Posted share for post {post_id}")
    return result
