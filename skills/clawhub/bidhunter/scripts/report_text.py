#!/usr/bin/env python3
"""
report_text.py - Generate plain text briefing report.
Suitable for IM push (WeChat, DingTalk, Feishu, Email).

Usage:
  python3 report_text.py <qual_file.jsonl> <date>
  Output: text report to stdout.
"""

import json
import sys
from collections import defaultdict


VERDICT_EMOJI = {
    "investable": "[can]",
    "not_investable": "[cannot]",
    "needs_review": "[review]",
    "skip": "[skip]",
}


def load_results(path):
    results = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return results


def format_item(item):
    """Format a single item for text output."""
    title = item.get("title", "")
    rid = item.get("id", "")
    url = item.get("url", "")
    verdict = item.get("verdict", "needs_review")
    reason = item.get("reason", "")
    entity = item.get("assigned_entity_name", item.get("assigned_entity", ""))
    caps = item.get("matched_capabilities", [])
    region_info = item.get("region_info", {})
    is_priority = region_info.get("is_priority", False)
    region = region_info.get("region", "")

    emoji = VERDICT_EMOJI.get(verdict, "[?]")
    caps_str = f" | matched: {', '.join(caps)}" if caps else ""
    entity_str = f" | entity: {entity}" if entity else ""
    region_str = f" | region: {region}" if region else ""
    priority_str = " [PRIORITY]" if is_priority else ""

    lines = [
        f"- {title}({rid}){region_str}{priority_str}",
        f"  {emoji} {reason}{caps_str}{entity_str}",
    ]
    if url:
        lines.append(f"  link: {url}")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 report_text.py <qual_file.jsonl> <date>", file=sys.stderr)
        sys.exit(1)

    qual_path = sys.argv[1]
    date_str = sys.argv[2]

    results = load_results(qual_path)

    # Filter out skip items
    active = [r for r in results if r.get("verdict") != "skip"]

    stats = defaultdict(int)
    for r in active:
        stats[r.get("verdict", "needs_review")] += 1

    total = len(active)

    # Group by verdict
    investable = [r for r in active if r.get("verdict") == "investable"]
    not_investable = [r for r in active if r.get("verdict") == "not_investable"]
    needs_review = [r for r in active if r.get("verdict") == "needs_review"]

    # Priority items
    priority_items = [r for r in active if r.get("region_info", {}).get("is_priority", False)]

    lines = []
    lines.append("=" * 50)
    lines.append(f"[Bid Briefing - {date_str}] Total: {total} | can: {stats['investable']} | cannot: {stats['not_investable']} | review: {stats['needs_review']}")
    lines.append("=" * 50)

    if priority_items:
        lines.append("")
        lines.append("--- Priority Region Items ---")
        for item in priority_items:
            lines.append(format_item(item))
            lines.append("")

    if investable:
        lines.append("")
        lines.append("--- Investable (Core Capability Match) ---")
        for item in investable:
            if not item.get("region_info", {}).get("is_priority", False):
                lines.append(format_item(item))
                lines.append("")

    if needs_review:
        lines.append("")
        lines.append("--- Needs Review ---")
        for item in needs_review:
            lines.append(format_item(item))
            lines.append("")

    if not_investable:
        lines.append("")
        lines.append("--- Not Investable (Red Alert) ---")
        for item in not_investable:
            lines.append(format_item(item))
            lines.append("")

    if total == 0:
        lines.append("No new announcements today.")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
