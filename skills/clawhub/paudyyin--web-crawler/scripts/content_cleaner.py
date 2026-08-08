"""
Content cleaner using Readability algorithm.
Extracts main content from HTML, removing navigation, sidebars, footers, ads.
"""

import re
from html import unescape
from typing import Optional


class ContentCleaner:
    """Clean HTML content and extract main text using Readability-like scoring."""

    # Tags that typically contain non-content
    NEGATIVE_PATTERNS = re.compile(
        r"comment|meta|footer|footnote|sidebar|nav|menu|ad-|advert|banner|popup|modal",
        re.IGNORECASE,
    )
    POSITIVE_PATTERNS = re.compile(
        r"article|body|content|entry|main|post|text|blog|story",
        re.IGNORECASE,
    )

    # Tags to remove entirely
    REMOVE_TAGS = {
        "script", "style", "noscript", "iframe", "svg",
        "nav", "footer", "header", "aside",
        "button", "input", "form", "select",
    }

    def __init__(self, min_text_length: int = 100):
        self.min_text_length = min_text_length

    def clean(self, html: str, url: str = "") -> dict:
        """
        Clean HTML and extract content.

        Returns:
            dict with keys: title, text, html, publish_time
        """
        try:
            from readability import Document
            doc = Document(html, url=url)
            title = doc.title()
            content_html = doc.summary()
            text = self._html_to_text(content_html)
            publish_time = self._extract_publish_time(html)
            return {
                "title": title,
                "text": text,
                "html": content_html,
                "publish_time": publish_time,
            }
        except ImportError:
            # Fallback: simple extraction without readability
            return self._simple_extract(html)

    def _simple_extract(self, html: str) -> dict:
        """Fallback extraction without readability library."""
        title = self._extract_title(html)
        # Remove unwanted tags
        cleaned = html
        for tag in self.REMOVE_TAGS:
            cleaned = re.sub(
                rf"<{tag}[^>]*>.*?</{tag}>",
                "",
                cleaned,
                flags=re.DOTALL | re.IGNORECASE,
            )
        text = self._html_to_text(cleaned)
        publish_time = self._extract_publish_time(html)
        return {
            "title": title,
            "text": text,
            "html": cleaned,
            "publish_time": publish_time,
        }

    def _extract_title(self, html: str) -> str:
        """Extract title from HTML."""
        # Try <title> tag
        match = re.search(r"<title[^>]*>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
        if match:
            return unescape(match.group(1).strip())
        # Try <h1>
        match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
        if match:
            return unescape(match.group(1).strip())
        return ""

    def _extract_publish_time(self, html: str) -> Optional[str]:
        """Try to extract publish time from meta tags or common patterns."""
        # Check meta tags
        patterns = [
            r'<meta[^>]*property=["\']article:published_time["\'][^>]*content=["\']([^"\']+)',
            r'<meta[^>]*name=["\']publish_date["\'][^>]*content=["\']([^"\']+)',
            r'<meta[^>]*name=["\']date["\'][^>]*content=["\']([^"\']+)',
            r'<time[^>]*datetime=["\']([^"\']+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

    def _html_to_text(self, html: str) -> str:
        """Convert HTML to plain text."""
        text = html
        # Remove script/style content
        text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
        # Replace block elements with newlines
        text = re.sub(r"<(?:p|div|br|h[1-6]|li|tr)[^>]*>", "\n", text, flags=re.IGNORECASE)
        # Remove remaining tags
        text = re.sub(r"<[^>]+>", "", text)
        # Decode entities
        text = unescape(text)
        # Normalize whitespace
        lines = [line.strip() for line in text.splitlines()]
        text = "\n".join(line for line in lines if line)
        # Collapse multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()
