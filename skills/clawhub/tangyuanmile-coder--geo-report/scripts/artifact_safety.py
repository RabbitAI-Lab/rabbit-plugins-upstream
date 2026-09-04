#!/usr/bin/env python3
"""Detect API schema names and internal platform codes in user-facing text."""

from __future__ import annotations

import re
from html.parser import HTMLParser


PLATFORM_CODES = (
    "DB",
    "DOUBA",
    "DP",
    "DPA",
    "TXYB",
    "TXYBA",
    "TYQW",
    "TYQWA",
    "BDAI",
    "WXYY",
    "KIMI",
    "DYAI",
    "XHSA",
)
RAW_FIELD_NAMES = (
    "reqId",
    "thinking_enabled",
    "rich_media_block",
    "search_word",
    "fetch_time",
    "published_at",
    "site_name",
    "site_icon",
    "task_id",
    "quto_id",
    "seller_name",
    "image_url",
    "jump_url",
    "source_seq_id",
    "context_raw",
    "context_text",
    "raw_data_custom_html",
    "direct_report",
)
GENERIC_API_FIELDS = (
    "code",
    "msg",
    "data",
    "result",
    "prompt",
    "name",
    "status",
    "context",
    "think",
    "quote",
    "suggestions",
    "url",
    "title",
    "snippet",
    "index",
    "platform",
    "text",
    "pid",
)

PLATFORM_CODE_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:" + "|".join(map(re.escape, PLATFORM_CODES)) + r")(?![A-Za-z0-9_])"
)
RAW_FIELD_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:" + "|".join(map(re.escape, RAW_FIELD_NAMES)) + r")(?![A-Za-z0-9_])"
)
GENERIC_FIELD_LABEL_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:"
    + "|".join(map(re.escape, GENERIC_API_FIELDS))
    + r")(?![A-Za-z0-9_])\s*[=:：]"
)


class _VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_text_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"style", "script", "template"}:
            self.hidden_text_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"style", "script", "template"} and self.hidden_text_depth:
            self.hidden_text_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_text_depth and data.strip():
            self.parts.append(data)


def extract_visible_text(document: str) -> str:
    parser = _VisibleTextParser()
    parser.feed(document)
    parser.close()
    return " ".join(parser.parts)


def find_user_facing_leaks(text: str) -> list[str]:
    leaks: list[str] = []
    for pattern in (PLATFORM_CODE_RE, RAW_FIELD_RE, GENERIC_FIELD_LABEL_RE):
        for match in pattern.finditer(text):
            token = match.group(0).strip()
            if token and token not in leaks:
                leaks.append(token)
    return leaks
