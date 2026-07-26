#!/usr/bin/env python3
"""Operator review generator."""

import json

from config import OPERATOR_BLACKLIST, REVIEWS_PATH
from content_generator import generate_and_publish
from wordpress_client import get_published_titles, normalize

BLACKLIST_NORM = [normalize(b) for b in OPERATOR_BLACKLIST]


def load_reviews() -> dict:
    if not REVIEWS_PATH.exists():
        return {"operators": []}
    with open(REVIEWS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_reviews(data: dict):
    with open(REVIEWS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def is_blacklisted(name: str) -> bool:
    norm = normalize(name)
    return any(b in norm for b in BLACKLIST_NORM)


def already_live(name: str, live_titles: list) -> bool:
    """Brand is covered if its first token appears in a published review title."""
    brand = normalize(name.split()[0])
    return any(brand and brand in normalize(t) for t in live_titles)


def next_operator() -> dict | None:
    data = load_reviews()
    live_titles = None
    changed = False
    for op in data.get("operators", []):
        if op.get("reviewed", False):
            continue
        if op.get("no_affiliate", False):
            # No affiliate account (Trevor, 15/07/2026): a review earns nothing yet.
            continue
        if is_blacklisted(op["name"]):
            print(f"Skipping blacklisted operator: {op['name']}")
            op["reviewed"] = True
            op["blacklisted"] = True
            changed = True
            continue
        if live_titles is None:
            live_titles = get_published_titles(["sportsbooks", "casinos"])
        if already_live(op["name"], live_titles):
            print(f"Already live, marking reviewed: {op['name']}")
            op["reviewed"] = True
            changed = True
            continue
        if changed:
            save_reviews(data)
        return op
    if changed:
        save_reviews(data)
    return None


def mark_reviewed(name: str):
    data = load_reviews()
    for op in data.get("operators", []):
        if op["name"] == name:
            op["reviewed"] = True
            break
    save_reviews(data)


def publish_next_review(status: str = "publish", dry_run: bool = False):
    op = next_operator()
    if not op:
        print("No operators left to review.")
        return None

    post = generate_and_publish(
        title=f"{op['name']} Review",
        keywords=op["keywords"],
        post_type="review",
        status=status,
        dry_run=dry_run,
    )
    if not dry_run and post and post.get("id"):
        mark_reviewed(op["name"])
    return post
