#!/usr/bin/env python3
"""Update agent: flag and optionally refresh stale posts."""

from datetime import datetime, timezone, timedelta

from config import SITE_URL
from llm_client import chat
from humanizer import humanize_html
from state import get_last_refresh_check, set_last_refresh_check
from wordpress_client import get_post, list_posts, update_post


def is_stale(post: dict, days: int = 30) -> bool:
    """Check if a post is older than `days`."""
    modified = post.get("modified") or post.get("date")
    if not modified:
        return False
    modified_dt = datetime.fromisoformat(modified.replace("Z", "+00:00"))
    if modified_dt.tzinfo is None:
        modified_dt = modified_dt.replace(tzinfo=timezone.utc)
    return datetime.now(timezone.utc) - modified_dt > timedelta(days=days)


def fetch_stale_posts(days: int = 30, per_page: int = 100) -> list:
    """Fetch published posts older than `days`."""
    posts = list_posts(per_page=per_page, status="publish")
    return [p for p in posts if is_stale(p, days)]


def build_refresh_prompt(content: str, title: str) -> str:
    return (
        f"Title: {title}\n\n"
        f"Article HTML:\n{content}\n\n"
        "Review this article for outdated South African iGaming information. Identify:\n"
        "1. Outdated bonus terms or wagering requirements.\n"
        "2. Dead or changed operator names/brands.\n"
        "3. Stale timeframes, laws, or regulations.\n"
        "4. Missing internal links or FAQs.\n\n"
        "Return a concise list of issues and a refreshed version of the HTML. "
        "Format:\n"
        "---ISSUES---\n"
        "- issue 1\n"
        "- issue 2\n"
        "---REFRESHED---\n"
        "<article html>\n\n"
        "No preamble, no markdown code fences."
    )


def analyze_post(post_id: int) -> dict:
    """Analyze a post and return issues + refreshed content (without saving)."""
    post = get_post(post_id, context="edit")
    content = post["content"]["raw"]
    title = post["title"]["raw"]
    messages = [
        {"role": "system", "content": "You are a South African iGaming content editor."},
        {"role": "user", "content": build_refresh_prompt(content, title)},
    ]
    raw = chat(messages, temperature=0.4)

    issues = []
    refreshed = content
    if "---ISSUES---" in raw and "---REFRESHED---" in raw:
        parts = raw.split("---REFRESHED---", 1)
        issues_text = parts[0].split("---ISSUES---", 1)[1]
        issues = [line.strip("- ").strip() for line in issues_text.splitlines() if line.strip().startswith("-")]
        refreshed = parts[1].strip()

    return {
        "id": post_id,
        "title": title,
        "url": post["link"],
        "issues": issues,
        "refreshed_content": refreshed,
    }


def run_refresh_check(dry_run: bool = True, max_posts: int = 5):
    """Check stale posts and optionally update them."""
    stale = fetch_stale_posts()[:max_posts]
    if not stale:
        print("No stale posts found.")
        set_last_refresh_check()
        return []

    results = []
    for post in stale:
        analysis = analyze_post(post["id"])
        results.append(analysis)
        print(f"\n[{post['id']}] {analysis['title']}")
        print(f"URL: {analysis['url']}")
        print("Issues:")
        for issue in analysis["issues"]:
            print(f"  - {issue}")

        if not dry_run and analysis["issues"]:
            update_post(post["id"], content=humanize_html(analysis["refreshed_content"]))
            print("  → Updated.")
        else:
            print("  → Skipped (dry run or no issues).")

    set_last_refresh_check()
    return results
