#!/usr/bin/env python3
"""Persistent state for the automation pipeline."""

from datetime import datetime, timezone
from typing import Any

from config import STATE_PATH, load_json, save_json


def load_state() -> dict:
    return load_json(STATE_PATH, {
        "used_topic_indices": [],
        "published_posts": [],
        "last_refresh_check": None,
        "last_social_draft": None,
        "version": 1,
    })


def save_state(state: dict):
    save_json(STATE_PATH, state)


def record_published_post(post_id: int, title: str, url: str, post_type: str = "guide"):
    state = load_state()
    state.setdefault("published_posts", [])
    state["published_posts"].append({
        "id": post_id,
        "title": title,
        "url": url,
        "type": post_type,
        "published_at": datetime.now(timezone.utc).isoformat(),
    })
    save_state(state)


def mark_topic_used(index: int):
    state = load_state()
    used = set(state.get("used_topic_indices", []))
    if index not in used:
        state["used_topic_indices"].append(index)
        save_state(state)


def get_used_topics() -> set:
    return set(load_state().get("used_topic_indices", []))


def get_last_refresh_check() -> str | None:
    return load_state().get("last_refresh_check")


def set_last_refresh_check():
    state = load_state()
    state["last_refresh_check"] = datetime.now(timezone.utc).isoformat()
    save_state(state)
