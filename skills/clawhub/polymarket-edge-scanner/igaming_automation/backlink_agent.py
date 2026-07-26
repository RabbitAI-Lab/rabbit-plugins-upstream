#!/usr/bin/env python3
"""Backlink outreach agent: drafts comments/replies for manual posting.

This agent does NOT post automatically to forums, Reddit, Quora, or other platforms.
It generates human-reviewable outreach drafts saved to backlink_opportunities.md.
"""

from datetime import datetime, timezone
from pathlib import Path

from llm_client import chat

OPPORTUNITIES_PATH = Path(__file__).parent / "backlink_opportunities.md"


def build_prompt(title: str, url: str, topic: str) -> str:
    return (
        f"Generate 2-3 short, helpful comment/reply drafts that could naturally link to this article.\n\n"
        f"Article title: {title}\n"
        f"URL: {url}\n"
        f"Topic focus: {topic}\n\n"
        "Each draft should:\n"
        "- Be 2-4 sentences.\n"
        "- Genuinely answer a likely question.\n"
        "- Include the URL only where it adds value.\n"
        "- Avoid spammy or promotional language.\n"
        "- Be suitable for Reddit, Quora, or forum replies.\n\n"
        "Return the drafts as a numbered list. No preamble."
    )


def generate_opportunities(title: str, url: str, topic: str) -> list:
    messages = [
        {"role": "system", "content": "You are a careful, white-hat link-building assistant for a South African iGaming site."},
        {"role": "user", "content": build_prompt(title, url, topic)},
    ]
    raw = chat(messages, temperature=0.6)
    drafts = [line.strip() for line in raw.splitlines() if line.strip() and (line.strip()[0].isdigit() or line.strip().startswith("-"))]
    return drafts


def save_opportunities(title: str, url: str, topic: str, drafts: list):
    timestamp = datetime.now(timezone.utc).isoformat()
    with open(OPPORTUNITIES_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n## {title}\n")
        f.write(f"- URL: {url}\n")
        f.write(f"- Topic: {topic}\n")
        f.write(f"- Generated: {timestamp}\n\n")
        for draft in drafts:
            f.write(f"- {draft}\n")
        f.write("\n---\n")


def run(title: str, url: str, topic: str):
    drafts = generate_opportunities(title, url, topic)
    save_opportunities(title, url, topic, drafts)
    print(f"Saved {len(drafts)} backlink outreach drafts to {OPPORTUNITIES_PATH}")
    return drafts
