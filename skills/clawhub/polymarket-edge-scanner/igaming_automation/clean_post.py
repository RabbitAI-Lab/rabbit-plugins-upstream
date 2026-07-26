#!/usr/bin/env python3
"""Clean artifacts from an existing published post."""
import re
from wordpress_publisher import update_post

POST_ID = 107628


def clean_content(content: str) -> str:
    # Remove preamble artifact
    content = re.sub(r"^(Here is the full article with \d+ internal links added using natural anchor text\.)\s*", "", content, flags=re.I)
    content = re.sub(r"^&#8220;`html\s*", "", content)
    content = re.sub(r"^`+html\s*", "", content, flags=re.I)
    content = re.sub(r"`+\s*$", "", content)
    content = content.strip()
    return content


if __name__ == "__main__":
    import requests
    from wordpress_publisher import get_session

    session, site_url = get_session()
    url = f"{site_url}/wp-json/wp/v2/posts/{POST_ID}?context=edit"
    response = session.get(url, timeout=20)
    response.raise_for_status()
    post = response.json()

    cleaned = clean_content(post["content"]["raw"])
    update_post(POST_ID, content=cleaned)
    print(f"Cleaned post {POST_ID}: {post['link']}")
