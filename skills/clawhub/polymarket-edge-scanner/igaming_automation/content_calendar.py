#!/usr/bin/env python3
"""Content calendar agent: pick the next article topic from the topic bank."""

import json
from pathlib import Path

from config import TOPICS_PATH
from state import get_used_topics, mark_topic_used
from wordpress_client import list_items, list_posts


def load_topics() -> dict:
    if not TOPICS_PATH.exists():
        return {"guide_topics": [], "seed_keywords": []}
    with open(TOPICS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_topics(data: dict):
    with open(TOPICS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_existing_slugs() -> set:
    """Slugs from posts AND pages: guides have been published as both."""
    slugs = set()
    for rb in ("posts", "pages"):
        try:
            for p in list_items(rb, per_page=100, status="publish"):
                slugs.add(p["slug"])
        except Exception:
            continue
    return slugs


def slugify(title: str) -> str:
    return "-".join(title.lower().replace("?", "").replace(":", "").replace("&", "and").split())


def score_topic(topic: dict, existing_slugs: set, used: set) -> int:
    score = 100
    slug = slugify(topic["title"])
    if slug in existing_slugs or any(slug in s for s in existing_slugs):
        score -= 50
    return score


def next_topic(force_new: bool = False, dry_run: bool = False) -> dict | None:
    """Return the next guide topic to write. Returns None if none available."""
    data = load_topics()
    topics = data.get("guide_topics", [])
    used = get_used_topics()
    existing_slugs = get_existing_slugs()

    # Topics whose slug is already live are duplicates: mark used, never pick.
    for i, t in enumerate(topics):
        slug = slugify(t["title"])
        if i not in used and (slug in existing_slugs or any(slug in s for s in existing_slugs)):
            print(f"Topic already live, marking used: {t['title']}")
            mark_topic_used(i)
            used.add(i)

    available = [
        (i, t) for i, t in enumerate(topics)
        if i not in used and t.get("type", "guide") == "guide"
    ]

    if not available:
        # Reset used topics if all consumed, but never re-pick live slugs.
        used = set()
        available = [
            (i, t) for i, t in enumerate(topics)
            if t.get("type", "guide") == "guide"
            and slugify(t["title"]) not in existing_slugs
            and not any(slugify(t["title"]) in s for s in existing_slugs)
        ]

    if not available:
        return None

    # Score and pick best
    scored = [(score_topic(t, existing_slugs, used), i, t) for i, t in available]
    scored.sort(key=lambda x: x[0], reverse=True)
    _, index, topic = scored[0]
    if not dry_run:
        mark_topic_used(index)
    return {"index": index, **topic, "type": "guide"}


def generate_topic_ideas(count: int = 5) -> list:
    """Generate new topic ideas from seed keywords (placeholder for LLM-driven research)."""
    data = load_topics()
    seeds = data.get("seed_keywords", [])
    ideas = []
    for i, kw in enumerate(seeds[:count]):
        ideas.append({
            "title": f"{kw.replace('?', '').title()} Guide",
            "keywords": [kw],
        })
    return ideas


def add_topic(title: str, keywords: list):
    data = load_topics()
    data["guide_topics"].append({"title": title, "keywords": keywords})
    save_topics(data)
