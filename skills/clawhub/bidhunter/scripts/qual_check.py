#!/usr/bin/env python3
"""
qual_check.py - Qualification matching engine for bidding announcements.
No third-party dependencies. Uses Python standard library only.

Usage:
  python3 qual_check.py <cache_file.jsonl> <rules_file.json>
  Output: JSON lines to stdout, each with qualification verdict.
"""

import json
import sys
import os
import re
from datetime import datetime


def load_rules(rules_path):
    with open(rules_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_announcements(cache_path):
    announcements = []
    if not os.path.exists(cache_path):
        return announcements
    with open(cache_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                announcements.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return announcements


def check_special_rules(title, special_rules):
    """Check special rules first (highest priority)."""
    for rule in special_rules:
        keywords = rule.get("match_keywords", [])
        for kw in keywords:
            if kw in title:
                return {
                    "verdict": rule.get("action", "unknown"),
                    "reason": rule.get("description", ""),
                    "assigned_entity": rule.get("assigned_entity", ""),
                    "rule_id": rule.get("id", ""),
                }
    return None


def check_red_alerts(title, red_alerts):
    """Check if title contains any red-alert keywords."""
    for alert in red_alerts:
        if alert in title:
            return {"verdict": "not_investable", "reason": f"红色预警：{alert}"}
    return None


def match_entity(title, entities):
    """Match title against entity capabilities. Returns best matching entity."""
    best_entity = None
    best_score = 0
    for entity_id, entity_data in entities.items():
        capabilities = entity_data.get("capabilities", [])
        score = 0
        matched_caps = []
        for cap in capabilities:
            if cap in title:
                score += 1
                matched_caps.append(cap)
        if score > best_score:
            best_score = score
            best_entity = {
                "entity_id": entity_id,
                "entity_name": entity_data.get("name", entity_id),
                "matched_capabilities": matched_caps,
                "score": score,
            }
    return best_entity


def check_skip_result(title, skip_keywords):
    """Check if this is a result announcement (not a bid invitation)."""
    for kw in skip_keywords:
        if kw in title:
            return True
    return False


def classify_region(title, region_priority):
    """Check if title mentions a high-priority region."""
    high_regions = region_priority.get("high", [])
    for region in high_regions:
        if region in title:
            return {"is_priority": True, "region": region}
    return {"is_priority": False, "region": ""}


def evaluate_announcement(ann, rules):
    """Main evaluation function. Returns verdict dict."""
    title = ann.get("title", "")

    # Skip result announcements
    if check_skip_result(title, rules.get("skip_keywords_result", [])):
        return {
            **ann,
            "verdict": "skip",
            "reason": "结果/中标公示，非投标公告",
            "assigned_entity": "",
            "matched_capabilities": [],
            "region_info": classify_region(title, rules.get("region_priority", {})),
        }

    # 1. Special rules (highest priority)
    special = check_special_rules(title, rules.get("special_rules", []))
    if special:
        return {
            **ann,
            "verdict": special["verdict"],
            "reason": special["reason"],
            "assigned_entity": special.get("assigned_entity", ""),
            "matched_capabilities": [],
            "region_info": classify_region(title, rules.get("region_priority", {})),
        }

    # 2. Red alerts
    red = check_red_alerts(title, rules.get("red_alerts", []))
    if red:
        return {
            **ann,
            "verdict": red["verdict"],
            "reason": red["reason"],
            "assigned_entity": "",
            "matched_capabilities": [],
            "region_info": classify_region(title, rules.get("region_priority", {})),
        }

    # 3. Entity capability match
    entity = match_entity(title, rules.get("entities", {}))
    if entity:
        return {
            **ann,
            "verdict": "investable",
            "reason": f"主体能力匹配：{', '.join(entity['matched_capabilities'])}",
            "assigned_entity": entity["entity_id"],
            "assigned_entity_name": entity["entity_name"],
            "matched_capabilities": entity["matched_capabilities"],
            "region_info": classify_region(title, rules.get("region_priority", {})),
        }

    # 4. No match - needs confirmation
    return {
        **ann,
        "verdict": "needs_review",
        "reason": "未匹配到主体能力词，需人工研判",
        "assigned_entity": "",
        "matched_capabilities": [],
        "region_info": classify_region(title, rules.get("region_priority", {})),
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 qual_check.py <cache_file.jsonl> <rules_file.json>", file=sys.stderr)
        sys.exit(1)

    cache_path = sys.argv[1]
    rules_path = sys.argv[2]

    rules = load_rules(rules_path)
    announcements = load_announcements(cache_path)

    verdict_map = {
        "investable": "investable",
        "not_investable": "not_investable",
        "needs_review": "needs_review",
        "skip": "skip",
        "unknown": "needs_review",
    }

    stats = {"investable": 0, "not_investable": 0, "needs_review": 0, "skip": 0}

    for ann in announcements:
        result = evaluate_announcement(ann, rules)
        verdict = verdict_map.get(result["verdict"], "needs_review")
        stats[verdict] = stats.get(verdict, 0) + 1
        result["verdict"] = verdict
        print(json.dumps(result, ensure_ascii=False))

    # Summary to stderr
    total = sum(stats.values())
    summary = f"Total: {total} | investable: {stats['investable']} | not_investable: {stats['not_investable']} | needs_review: {stats['needs_review']} | skip: {stats['skip']}"
    print(summary, file=sys.stderr)


if __name__ == "__main__":
    main()
