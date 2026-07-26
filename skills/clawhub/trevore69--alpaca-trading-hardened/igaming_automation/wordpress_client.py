#!/usr/bin/env python3
"""WordPress REST API client for igamingreviews.org."""

import json
import re
from pathlib import Path
from urllib.parse import urljoin

import requests

from config import CREDENTIALS_PATH

# All content sections that count when checking for duplicates.
CONTENT_REST_BASES = ["posts", "pages", "sportsbooks", "casinos"]


def load_credentials():
    if not CREDENTIALS_PATH.exists():
        raise FileNotFoundError(f"Credentials not found at {CREDENTIALS_PATH}")
    with open(CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_session():
    creds = load_credentials()
    session = requests.Session()
    session.auth = (creds["username"], creds["app_password"])
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
    })
    return session, creds["site_url"].rstrip("/")


def _api_url(site_url: str, endpoint: str) -> str:
    return urljoin(site_url + "/", f"wp-json/wp/v2/{endpoint}")


def create_post(title: str, content: str, status: str = "draft", **kwargs):
    session, site_url = get_session()
    payload = {"title": title, "content": content, "status": status}
    payload.update(kwargs)
    response = session.post(_api_url(site_url, "posts"), json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def update_post(post_id: int, **kwargs):
    session, site_url = get_session()
    response = session.post(_api_url(site_url, f"posts/{post_id}"), json=kwargs, timeout=30)
    response.raise_for_status()
    return response.json()


def get_post(post_id: int, context: str = "edit"):
    session, site_url = get_session()
    response = session.get(_api_url(site_url, f"posts/{post_id}"), params={"context": context}, timeout=30)
    response.raise_for_status()
    return response.json()


def list_posts(per_page: int = 10, page: int = 1, **kwargs):
    session, site_url = get_session()
    params = {"per_page": per_page, "page": page}
    params.update(kwargs)
    response = session.get(_api_url(site_url, "posts"), params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def list_items(rest_base: str, per_page: int = 100, **kwargs):
    """List items from any rest base (posts, pages, sportsbooks, casinos...)."""
    session, site_url = get_session()
    params = {"per_page": per_page}
    params.update(kwargs)
    response = session.get(_api_url(site_url, rest_base), params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def get_published_titles(rest_bases=None) -> list:
    """Titles of everything published across the main content sections."""
    titles = []
    for rb in (rest_bases or CONTENT_REST_BASES):
        try:
            for p in list_items(rb, per_page=100, status="publish"):
                titles.append(re.sub(r"<[^>]+>", "", p["title"]["rendered"]).strip())
        except Exception:
            continue
    return titles


def normalize(text: str) -> str:
    """Lowercase alphanumeric-only form, for fuzzy title/brand matching."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def title_exists(title: str, rest_bases=None) -> bool:
    """True if a published item already carries this (or a containing) title."""
    norm = normalize(title)
    return any(norm and norm in normalize(t) for t in get_published_titles(rest_bases))


def search_posts(search: str, per_page: int = 20):
    session, site_url = get_session()
    response = session.get(
        _api_url(site_url, "posts"),
        params={"search": search, "per_page": per_page, "status": "publish"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def get_categories():
    session, site_url = get_session()
    response = session.get(_api_url(site_url, "categories"), params={"per_page": 100}, timeout=30)
    response.raise_for_status()
    return response.json()


def get_tags():
    session, site_url = get_session()
    response = session.get(_api_url(site_url, "tags"), params={"per_page": 100}, timeout=30)
    response.raise_for_status()
    return response.json()


def get_users_me():
    session, site_url = get_session()
    response = session.get(_api_url(site_url, "users/me"), timeout=10)
    response.raise_for_status()
    return response.json()
