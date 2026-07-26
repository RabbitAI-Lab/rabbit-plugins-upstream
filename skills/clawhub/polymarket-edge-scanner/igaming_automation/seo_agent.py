#!/usr/bin/env python3
"""SEO agent: internal linking, meta verification, sitemap helper."""

import re
from datetime import datetime, timezone

from llm_client import chat
from humanizer import humanize_html
from wordpress_client import get_post, list_posts, update_post


def extract_internal_links(content: str) -> list:
    """Find relative internal links in HTML content."""
    return re.findall(r'href="(/[^"]+)"', content)


def fetch_existing_posts_for_links(per_page: int = 100):
    """Return list of {title, link, slug} for published posts."""
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


def build_link_prompt(content: str, title: str, existing_posts: list) -> str:
    link_context = "\n".join(f"- {p['title']}: {p['link']}" for p in existing_posts[:30])
    return (
        f"Title: {title}\n\n"
        f"Article HTML:\n{content}\n\n"
        "Existing site articles you can link to:\n"
        f"{link_context}\n\n"
        "Add 2-4 relevant internal links using natural anchor text and the relative URLs above. "
        "Preserve all existing content and styling. Only add links where they fit naturally. "
        "Return ONLY the updated HTML article. No preamble, no markdown code fences, no explanation."
    )


def add_internal_links(post_id: int, dry_run: bool = False) -> dict:
    """Add internal links to a published post and update it."""
    post = get_post(post_id, context="edit")
    content = post["content"]["raw"]
    title = post["title"]["raw"]

    existing_links = extract_internal_links(content)
    if len(existing_links) >= 3:
        print(f"Post {post_id} already has {len(existing_links)} internal links. Skipping.")
        return post

    existing_posts = fetch_existing_posts_for_links()
    messages = [
        {"role": "system", "content": "You are an SEO editor for a South African iGaming site."},
        {"role": "user", "content": build_link_prompt(content, title, existing_posts)},
    ]
    updated_content = chat(messages, temperature=0.4)

    if dry_run:
        print(f"DRY RUN — would update post {post_id} with added internal links.")
        return post

    return update_post(post_id, content=humanize_html(updated_content))


def generate_sitemap_list() -> list:
    """Return list of published post URLs for sitemap/manual submission."""
    posts = list_posts(per_page=100, status="publish")
    return [p["link"] for p in posts]


def save_sitemap(path: str = "sitemap_urls.txt"):
    urls = generate_sitemap_list()
    with open(path, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")
    print(f"Saved {len(urls)} URLs to {path}")
