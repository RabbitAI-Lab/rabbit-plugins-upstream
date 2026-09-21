#!/usr/bin/env python3
"""
Publish image(s) to Instagram via the Graph API.

Single image (1 URL):
  1. GET  /me?fields=id,username              -> validate token, fetch IG_USER_ID
  2. POST /{ig_user_id}/media                 -> create media container
  3. POST /{ig_user_id}/media_publish         -> publish the container

Carousel (2-10 URLs):
  1. GET  /me?fields=id,username              -> validate token, fetch IG_USER_ID
  2a. POST /{ig_user_id}/media   (per URL)    -> create is_carousel_item containers
  2b. POST /{ig_user_id}/media   (media_type=CAROUSEL, children=id1,id2,...)
                                            -> create carousel container
  3.  POST /{ig_user_id}/media_publish        -> publish the carousel container

Reads ACCESS_TOKEN (and optionally IG_USER_ID) from .env.
Requires Python 3.7+; uses only stdlib (urllib, json, argparse).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_VERSION = "v24.0"
GRAPH_BASE = "https://graph.instagram.com"

CAROUSEL_MIN = 2
CAROUSEL_MAX = 10


# ---------------------------------------------------------------------------
# .env loading (stdlib only — no python-dotenv needed)
# ---------------------------------------------------------------------------

def load_env(path: Path) -> dict[str, str]:
    """Minimal .env parser. Skips blank lines and `#` comments."""
    env: dict[str, str] = {}
    if not path.exists():
        return env
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        env[key] = value
    return env


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def http_get(url: str) -> dict:
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_post(url: str, data: dict) -> dict:
    encoded = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def explain_error(err: urllib.error.HTTPError) -> str:
    body = err.read().decode("utf-8", errors="replace")
    try:
        parsed = json.loads(body)
        return json.dumps(parsed, indent=2, ensure_ascii=False)
    except json.JSONDecodeError:
        return body


def media_download_hint(body: str) -> str:
    if "Media download has failed" in body:
        return (
            "\n  Hint: Meta's servers cannot reach the image_url.\n"
            "        Use a public URL (S3/OSS/GitHub Raw/CDN), not localhost."
        )
    if "Unsupported post request" in body:
        return (
            "\n  Hint: token permissions are incomplete.\n"
            "        Go to App dashboard → Use cases → Customize → API setup with Instagram login,\n"
            "        then regenerate the token."
        )
    return ""


# ---------------------------------------------------------------------------
# Graph API steps
# ---------------------------------------------------------------------------

def validate_token_and_get_user_id(access_token: str, cached_user_id: str | None) -> tuple[str, str]:
    """Step 1: confirm token works and return (ig_user_id, username)."""
    url = f"{GRAPH_BASE}/me?fields=id,username&access_token={urllib.parse.quote(access_token)}"
    try:
        result = http_get(url)
    except urllib.error.HTTPError as e:
        raise SystemExit(
            f"✗ Token validation failed (HTTP {e.code}).\n"
            f"  Body: {explain_error(e)}\n"
            f"  Likely cause: expired token or wrong value in ACCESS_TOKEN."
        )
    user_id = result.get("id")
    username = result.get("username", "?")
    if not user_id:
        raise SystemExit(f"✗ /me returned no id. Full response: {result}")
    if cached_user_id and cached_user_id != user_id:
        print(f"  note: .env IG_USER_ID={cached_user_id} but token resolves to {user_id}; using token's value")
    return user_id, username


def create_container(ig_user_id: str, image_url: str, caption: str, access_token: str, api_version: str = API_VERSION) -> str:
    """Single-image mode: upload the image, return creation_id."""
    url = f"{GRAPH_BASE}/{api_version}/{ig_user_id}/media"
    try:
        result = http_post(url, {
            "image_url": image_url,
            "caption": caption,
            "access_token": access_token,
        })
    except urllib.error.HTTPError as e:
        body = explain_error(e)
        raise SystemExit(f"✗ Container creation failed (HTTP {e.code}).\n  Body: {body}{media_download_hint(body)}")
    creation_id = result.get("id")
    if not creation_id:
        raise SystemExit(f"✗ Container creation returned no id. Full response: {result}")
    return creation_id


def create_carousel_item_container(ig_user_id: str, image_url: str, access_token: str, api_version: str = API_VERSION) -> str:
    """Carousel mode (per item): create an is_carousel_item container, return creation_id."""
    url = f"{GRAPH_BASE}/{api_version}/{ig_user_id}/media"
    try:
        result = http_post(url, {
            "image_url": image_url,
            "is_carousel_item": "true",
            "access_token": access_token,
        })
    except urllib.error.HTTPError as e:
        body = explain_error(e)
        raise SystemExit(f"✗ Carousel item container failed (HTTP {e.code}).\n  Body: {body}{media_download_hint(body)}")
    creation_id = result.get("id")
    if not creation_id:
        raise SystemExit(f"✗ Carousel item container returned no id. Full response: {result}")
    return creation_id


def create_carousel_container(ig_user_id: str, item_ids: list[str], caption: str, access_token: str, api_version: str = API_VERSION) -> str:
    """Carousel mode (parent): combine 2-10 is_carousel_item ids into a CAROUSEL container, return creation_id."""
    url = f"{GRAPH_BASE}/{api_version}/{ig_user_id}/media"
    try:
        result = http_post(url, {
            "media_type": "CAROUSEL",
            "children": ",".join(item_ids),
            "caption": caption,
            "access_token": access_token,
        })
    except urllib.error.HTTPError as e:
        body = explain_error(e)
        raise SystemExit(f"✗ Carousel container failed (HTTP {e.code}).\n  Body: {body}{media_download_hint(body)}")
    creation_id = result.get("id")
    if not creation_id:
        raise SystemExit(f"✗ Carousel container returned no id. Full response: {result}")
    return creation_id


def publish_container(ig_user_id: str, creation_id: str, access_token: str, dry_run: bool) -> str:
    """Step 3: convert container to a live post. Returns post id."""
    if dry_run:
        return "(dry-run, not published)"
    url = f"{GRAPH_BASE}/{API_VERSION}/{ig_user_id}/media_publish"
    try:
        result = http_post(url, {
            "creation_id": creation_id,
            "access_token": access_token,
        })
    except urllib.error.HTTPError as e:
        raise SystemExit(
            f"✗ Publish failed (HTTP {e.code}).\n"
            f"  Body: {explain_error(e)}"
        )
    post_id = result.get("id")
    if not post_id:
        raise SystemExit(f"✗ Publish returned no id. Full response: {result}")
    return post_id


def get_permalink(post_id: str, access_token: str, api_version: str = API_VERSION) -> str | None:
    """Step 4: resolve a numeric media id to its public shortcode URL."""
    url = f"{GRAPH_BASE}/{api_version}/{post_id}?fields=permalink&access_token={urllib.parse.quote(access_token)}"
    try:
        result = http_get(url)
    except urllib.error.HTTPError as e:
        print(f"  (warning) permalink lookup failed (HTTP {e.code}): {explain_error(e)}")
        return None
    return result.get("permalink")


# ---------------------------------------------------------------------------
# Orchestrators
# ---------------------------------------------------------------------------

def publish_single(ig_user_id: str, image_url: str, caption: str, access_token: str, dry_run: bool, api_version: str) -> str:
    """Single-image path: one container, one publish."""
    creation_id = create_container(ig_user_id, image_url, caption, access_token, api_version)
    print(f"✓ Container created: {creation_id}")
    return publish_container(ig_user_id, creation_id, access_token, dry_run)


def publish_carousel(ig_user_id: str, image_urls: list[str], caption: str, access_token: str, dry_run: bool, api_version: str) -> str:
    """Carousel path: N item containers, one parent CAROUSEL container, one publish."""
    item_ids: list[str] = []
    for idx, url in enumerate(image_urls, start=1):
        item_id = create_carousel_item_container(ig_user_id, url, access_token, api_version)
        print(f"✓ Carousel item {idx}/{len(image_urls)} container: {item_id}")
        item_ids.append(item_id)

    creation_id = create_carousel_container(ig_user_id, item_ids, caption, access_token, api_version)
    print(f"✓ Carousel container created: {creation_id}")
    return publish_container(ig_user_id, creation_id, access_token, dry_run)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    global API_VERSION
    parser = argparse.ArgumentParser(
        description="Publish image(s) to Instagram via the Graph API. "
                    "1 URL = single post, 2-10 URLs = carousel.",
    )
    parser.add_argument(
        "--image-urls",
        nargs="+",
        required=True,
        metavar="URL",
        help="One or more public image URLs. Pass 1 URL for a single post, "
             "or 2-10 URLs for a carousel. Each URL must be reachable by Meta's servers.",
    )
    parser.add_argument("--caption", default="", help="Caption text (hashtags OK)")
    parser.add_argument("--env", default=".env", help="Path to .env file (default: ./env)")
    parser.add_argument("--api-version", default=API_VERSION, help=f"Graph API version (default: {API_VERSION})")
    parser.add_argument("--dry-run", action="store_true", help="Validate token and build container, but skip publish")
    args = parser.parse_args()

    API_VERSION = args.api_version
    image_urls = args.image_urls

    if not image_urls:
        raise SystemExit("✗ --image-urls requires at least one URL.")
    if len(image_urls) > CAROUSEL_MAX:
        raise SystemExit(
            f"✗ Instagram carousels accept at most {CAROUSEL_MAX} items, got {len(image_urls)}.\n"
            f"  Split into multiple posts, or stitch images into one and use a single URL."
        )
    for url in image_urls:
        if not url.startswith(("http://", "https://")):
            raise SystemExit(f"✗ --image-urls entries must be http(s) URLs, got: {url}")

    env_path = Path(args.env)
    env = load_env(env_path)
    # Allow real env vars to override .env
    access_token = os.environ.get("ACCESS_TOKEN") or env.get("ACCESS_TOKEN", "")
    ig_user_id = os.environ.get("IG_USER_ID") or env.get("IG_USER_ID") or None
    ig_username = os.environ.get("IG_USERNAME") or env.get("IG_USERNAME") or None

    if not access_token:
        raise SystemExit(
            f"✗ ACCESS_TOKEN not found.\n"
            f"  Put it in {env_path} or export ACCESS_TOKEN=... in your shell."
        )

    # Step 1: validate token
    if not ig_user_id:
        print("  (IG_USER_ID not set — fetching from /me)")
    resolved_id, username = validate_token_and_get_user_id(access_token, ig_user_id)
    label = ig_username or username
    print(f"✓ Token valid — user: @{label} (id: {resolved_id})")

    # Step 2 + 3: build container(s), then publish
    is_carousel = len(image_urls) >= CAROUSEL_MIN
    if is_carousel:
        print(f"→ Carousel mode ({len(image_urls)} images)")
        post_id = publish_carousel(resolved_id, image_urls, args.caption, access_token, args.dry_run, API_VERSION)
    else:
        print("→ Single-image mode")
        post_id = publish_single(resolved_id, image_urls[0], args.caption, access_token, args.dry_run, API_VERSION)

    if args.dry_run:
        print(f"✓ Dry-run complete — would publish post_id={post_id}")
    else:
        print(f"✓ Published: {post_id}")
        permalink = get_permalink(post_id, access_token, api_version=API_VERSION)
        if permalink:
            print(f"  {permalink}")
        else:
            print(f"  https://www.instagram.com/p/{post_id}  (fallback — permalink lookup failed)")


if __name__ == "__main__":
    main()