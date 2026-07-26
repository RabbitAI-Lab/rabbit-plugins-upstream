#!/usr/bin/env python3
"""HTML cleanup utilities for generated content."""

import re


def clean_html(raw: str) -> str:
    """Remove LLM artifacts and markdown fences from generated HTML."""
    raw = raw.strip()

    # Remove markdown code fences around the whole content
    if raw.startswith("```"):
        raw = re.sub(r"^```[\w]*\n", "", raw)
        raw = re.sub(r"\n```$", "", raw)

    # Remove common LLM preambles before the first HTML tag
    raw = re.sub(
        r"^(Here is(?: the)? (?:full )?article.*?)(?=<h\d|<p|<blockquote|<ul|<ol|<table)",
        "",
        raw,
        flags=re.S | re.I,
    )

    # Remove leading ```html or ``` markers
    raw = re.sub(r"^(`+html?\s*)", "", raw, flags=re.I)
    raw = re.sub(r"(`+\s*)$", "", raw)

    # Remove artifact paragraphs (HTML-wrapped)
    artifact_patterns = [
        r"<p>\s*&#8220;`\s*</p>",
        r"<p>\s*`+\s*</p>",
        r"<p>\s*\*\*Links added:\*\*.*?</p>",
        r"<p>\s*Links added:.*?</p>",
        r"<p>\s*No article is linked more than once.*?</p>",
        r"<p>\s*No disclaimer was added.*?</p>",
    ]
    for pattern in artifact_patterns:
        raw = re.sub(pattern, "", raw, flags=re.S | re.I)

    # Strip trailing code fences after a closing HTML tag or at end of string
    raw = re.sub(r"(</(?:p|blockquote|ul|ol|table|h\d)>)\s*```+\s*$", r"\1", raw, flags=re.S)
    raw = re.sub(r"```+\s*$", "", raw)

    # Strip raw markdown summaries appended after the HTML body
    raw = re.sub(r"\s*```+\s*\n+\s*\*\*Links added:\*\*.*?(?=\Z)", "", raw, flags=re.S | re.I)
    raw = re.sub(r"\s*```+\s*\n+\s*Links added:.*?(?=\Z)", "", raw, flags=re.S | re.I)
    raw = re.sub(r"\s*\*\*Links added:\*\*.*?(?=\Z)", "", raw, flags=re.S | re.I)
    raw = re.sub(r"\s*Links added:.*?(?=\Z)", "", raw, flags=re.S | re.I)
    raw = re.sub(r"\s*No article is linked more than once.*?(?=\Z)", "", raw, flags=re.S | re.I)
    raw = re.sub(r"\s*No disclaimer was added.*?(?=\Z)", "", raw, flags=re.S | re.I)

    return raw.strip()


def clean_review_html(html: str) -> str:
    """Normalize review HTML: remove stray H1, convert div.key-takeaways to blockquote."""
    html = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", html, count=1, flags=re.S | re.I)
    html = re.sub(
        r'<div class="key-takeaways">(.*?</ul>)\s*</div>',
        r'<blockquote class="key-takeaways">\1</blockquote>',
        html,
        count=1,
        flags=re.S | re.I,
    )
    return html.strip()


def ensure_key_takeaways_class(html: str) -> str:
    """Add the site-standard key-takeaways class if the first blockquote contains Key Takeaways."""
    return re.sub(
        r'<blockquote>\s*<strong>Key Takeaways</strong>',
        '<blockquote class="key-takeaways">\n  <strong>Key Takeaways</strong>',
        html,
        count=1,
        flags=re.I,
    )
