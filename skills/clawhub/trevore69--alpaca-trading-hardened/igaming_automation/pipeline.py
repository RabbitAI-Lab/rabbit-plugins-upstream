#!/usr/bin/env python3
"""Main automation pipeline for igamingreviews.org.

Coordinates content calendar, review generation, updates, SEO, and social drafting.
"""

import argparse
import os
from datetime import datetime, timezone

from config import DRY_RUN
from content_calendar import next_topic
from content_generator import generate_and_publish
from review_generator import publish_next_review
from seo_agent import add_internal_links
from social.scheduler import draft_for_post
from update_agent import run_refresh_check


def log(message: str):
    print(f"[{datetime.now(timezone.utc).isoformat()}] {message}")


def run(mode: str = "auto", status: str = "publish", dry_run: bool = False):
    dry_run = dry_run or DRY_RUN
    log(f"Starting pipeline mode={mode} status={status} dry_run={dry_run}")

    published = None

    if mode in ("guide", "auto"):
        topic = next_topic(dry_run=dry_run)
        if topic:
            published = generate_and_publish(
                title=topic["title"],
                keywords=topic["keywords"],
                post_type="guide",
                status=status,
                dry_run=dry_run,
            )
        else:
            log("No guide topics available.")

    if not published and mode in ("review", "auto"):
        published = publish_next_review(status=status, dry_run=dry_run)
        if not published:
            log("No operator reviews available.")

    if published and not dry_run and published.get("id"):
        try:
            log(f"Running SEO link pass on post {published['id']}...")
            add_internal_links(published["id"], dry_run=False)
        except Exception as exc:
            log(f"SEO link pass failed: {exc}")

        try:
            log("Creating social media drafts...")
            title_text = published.get("title", {}).get("rendered") if isinstance(published.get("title"), dict) else published.get("title")
            draft_for_post(published["id"], title_text, published["link"], dry_run=True)
        except Exception as exc:
            log(f"Social drafting failed: {exc}")

    if mode == "refresh":
        log("Running refresh check (dry-run by default)...")
        run_refresh_check(dry_run=True, max_posts=3)
        return

    if mode == "social":
        log("Social mode: no new article to promote.")

    log("Pipeline completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="igamingreviews.org automation pipeline")
    parser.add_argument(
        "--mode",
        default=os.environ.get("PIPELINE_MODE", "auto"),
        choices=["auto", "guide", "review", "refresh", "social"],
        help="Pipeline mode",
    )
    parser.add_argument("--status", default="publish", help="WordPress post status")
    parser.add_argument("--dry-run", action="store_true", help="Generate without publishing")
    args = parser.parse_args()

    run(mode=args.mode, status=args.status, dry_run=args.dry_run)
