#!/usr/bin/env python3
"""Content generator for igamingreviews.org.

Generates SEO-optimized iGaming articles or operator reviews and publishes them to WordPress.
"""

import argparse
import json
import re
from datetime import datetime, timezone

from config import DRY_RUN, SEO_PASSES
from content.cleaners import clean_html, clean_review_html, ensure_key_takeaways_class
from content.templates import (
    GUIDE_SYSTEM_PROMPT,
    SEO_EDIT_SYSTEM_PROMPT,
    guide_user_prompt,
    multi_pass_prompt,
    review_user_prompt,
)
from llm_client import chat
from humanizer import humanize_html
from state import get_used_topics, mark_topic_used, record_published_post
from wordpress_client import create_post, list_posts, normalize, title_exists
from config import OPERATOR_BLACKLIST

SEO_PASSES_INSTRUCTIONS = {
    1: "Structure and keyword placement: ensure primary keyword is in intro and H2s.",
    2: "Readability and engagement: shorten paragraphs, improve flow, add transitions.",
    3: "Depth and intent: expand thin sections, add FAQ if missing, answer follow-up questions.",
    4: "Internal links and entities: verify links are natural and relevant.",
    5: "Final polish: remove keyword stuffing, fix awkward phrasing, ensure consistent tone.",
}


def log(message: str):
    print(f"[{datetime.now(timezone.utc).isoformat()}] {message}")


def fetch_existing_posts(per_page: int = 50):
    """Fetch published posts for internal linking."""
    try:
        posts = list_posts(per_page=per_page, status="publish")
        return [
            {
                "id": p["id"],
                "title": re.sub(r"<[^>]+>", "", p["title"]["rendered"]),
                "link": p["link"].replace("https://igamingreviews.org", "").replace("http://igamingreviews.org", ""),
                "slug": p["slug"],
            }
            for p in posts
        ]
    except Exception as exc:
        log(f"Warning: could not fetch existing posts: {exc}")
        return []


def generate_guide(title: str, keywords: list, existing_posts: list) -> str:
    messages = [
        {"role": "system", "content": GUIDE_SYSTEM_PROMPT},
        {"role": "user", "content": guide_user_prompt(title, keywords, existing_posts)},
    ]
    return chat(messages, temperature=0.6)


def generate_review(operator: str, keywords: list, existing_posts: list) -> str:
    from content.templates import REVIEW_SYSTEM_PROMPT
    messages = [
        {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
        {"role": "user", "content": review_user_prompt(operator, keywords, existing_posts)},
    ]
    return chat(messages, temperature=0.6)


def parse_seo_output(raw: str, title: str, primary: str) -> tuple:
    """Split SEO output into HTML and meta JSON."""
    if "---META---" in raw:
        parts = raw.split("---META---", 1)
        content_part = parts[0].strip()
        meta_part = re.sub(r"^```json\s*|\s*```$", "", parts[1].strip())
        try:
            meta = json.loads(meta_part)
        except json.JSONDecodeError:
            meta = default_meta(title, primary)
    else:
        content_part = raw.strip()
        meta = default_meta(title, primary)
    return content_part, meta


def default_meta(title: str, primary: str) -> dict:
    return {
        "meta_title": title[:60],
        "meta_description": f"Learn about {primary} in South Africa. Honest, compliant guide for SA players."[:160],
        "focus_keyword": primary,
    }


def seo_optimize(content: str, title: str, keywords: list) -> tuple:
    from content.templates import seo_edit_user_prompt
    primary = keywords[0]
    messages = [
        {"role": "system", "content": SEO_EDIT_SYSTEM_PROMPT},
        {"role": "user", "content": seo_edit_user_prompt(content, title, keywords)},
    ]
    raw = chat(messages, temperature=0.4)
    return parse_seo_output(raw, title, primary)


def run_seo_passes(content: str, title: str, keywords: list) -> str:
    for i in range(1, SEO_PASSES + 1):
        log(f"  SEO pass {i}/{SEO_PASSES}")
        instruction = SEO_PASSES_INSTRUCTIONS.get(i, "Final SEO and readability polish.")
        messages = [
            {"role": "system", "content": GUIDE_SYSTEM_PROMPT},
            {"role": "user", "content": multi_pass_prompt(content, title, keywords, i, instruction)},
        ]
        content = chat(messages, temperature=0.4)
        content = clean_html(content)
    return content


def build_wp_meta(keywords: list, meta: dict) -> dict:
    return {
        "keywords": ", ".join(keywords),
        "_yoast_wpseo_title": meta["meta_title"],
        "_yoast_wpseo_metadesc": meta["meta_description"],
        "_yoast_wpseo_focuskw": meta["focus_keyword"],
        "rank_math_title": meta["meta_title"],
        "rank_math_description": meta["meta_description"],
        "rank_math_focus_keyword": meta["focus_keyword"],
    }


def generate_and_publish(
    title: str,
    keywords: list,
    post_type: str = "guide",
    status: str = "publish",
    dry_run: bool = False,
):
    log(f"Generating {post_type}: {title}")

    # Pre-generation guards: never publish blacklisted brands or duplicates.
    norm_title = normalize(title)
    if any(normalize(b) in norm_title for b in OPERATOR_BLACKLIST):
        log(f"SKIP: '{title}' matches the operator blacklist. Not generating.")
        return None
    if title_exists(title):
        log(f"SKIP: '{title}' already exists on the site. Not generating a duplicate.")
        return None

    existing_posts = fetch_existing_posts(per_page=50)

    if post_type == "review":
        content = generate_review(title, keywords, existing_posts)
        content = clean_review_html(content)
        content = clean_html(content)
    else:
        content = generate_guide(title, keywords, existing_posts)

    content = clean_html(content)
    content = ensure_key_takeaways_class(content)

    if SEO_PASSES > 1:
        log(f"Running {SEO_PASSES} SEO optimization passes...")
        content = run_seo_passes(content, title, keywords)

    log("Running final SEO pass + meta generation...")
    content, meta = seo_optimize(content, title, keywords)
    content = clean_html(content)
    content = ensure_key_takeaways_class(content)

    log("Running humanizer pass...")
    content = humanize_html(content)
    content = clean_html(content)
    content = ensure_key_takeaways_class(content)

    wp_meta = build_wp_meta(keywords, meta)

    if dry_run:
        log("DRY RUN — would publish:")
        print(f"  Title: {title}")
        print(f"  Type: {post_type}")
        print(f"  Status: {status}")
        print(f"  Meta: {json.dumps(meta, indent=2)}")
        print(f"  Content preview:\n{content[:600]}...")
        return {"link": "DRY_RUN", "status": "draft", "id": 0, "title": title}

    post = create_post(
        title=title,
        content=content,
        status=status,
        meta=wp_meta,
    )
    record_published_post(post["id"], title, post["link"], post_type=post_type)
    log(f"Created post: {post['link']} (status: {post['status']})")
    log(f"Meta title: {meta['meta_title']}")
    log(f"Meta description: {meta['meta_description']}")
    return post


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and publish iGaming content")
    parser.add_argument("--title", default=None, help="Article/review title")
    parser.add_argument("--keywords", default=None, help="Comma-separated keywords")
    parser.add_argument("--type", default="guide", choices=["guide", "review"], help="Content type")
    parser.add_argument("--status", default="publish", help="WordPress post status")
    parser.add_argument("--dry-run", action="store_true", help="Generate without publishing")
    args = parser.parse_args()

    dry_run = args.dry_run or DRY_RUN

    if args.title and args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
        generate_and_publish(
            title=args.title,
            keywords=keywords,
            post_type=args.type,
            status=args.status,
            dry_run=dry_run,
        )
    else:
        print("Usage: python3 content_generator.py --title '...' --keywords 'kw1, kw2' [--type guide|review] [--dry-run]")
