#!/usr/bin/env python3
"""
qual_check.py - Qualification matching engine for BidHunter v1.1.
No third-party dependencies. Uses Python standard library only.

Usage:
  python3 qual_check.py <cache_file.jsonl> <rules_file.json>
  Output: JSON lines to stdout, each with qualification verdict.

  python3 qual_check.py --validate-rules <rules_file.json>
  Output: rule health check result to stderr.
"""

import json
import sys
import os
import re
from datetime import datetime


def log(msg):
    """Print log message to stderr with timestamp."""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", file=sys.stderr)


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


def _is_cjk(char):
    """Check if a character is a CJK (Chinese) character."""
    cp = ord(char)
    # CJK Unified Ideographs + Extension + Compatibility
    return 0x4E00 <= cp <= 0x9FFF or \
           0x3400 <= cp <= 0x4DBF or \
           0x20000 <= cp <= 0x2A6DF


def smart_match(text, keyword, exclude_context=None):
    """
    Boundary-aware keyword match for Chinese text.
    - Left boundary: keyword must not be preceded by a CJK character
      (avoids matching '电气' as a substring of '新电气石')
    - Right boundary: if the keyword is followed by a CJK character,
      the CJK run must be >= 2 chars (keyword is standalone, not a 1-char suffix compound)
      (avoids matching '电气' in '电气石' (suffix '石'=1char), but allows '电气设备' (suffix '设备'>=2))
    - exclude_context: if any exclude pattern appears anywhere in the text, reject match
    Returns True if matched, False otherwise.
    """
    if not keyword or not text:
        return False

    escaped = re.escape(keyword)
    pattern = re.compile(escaped)
    m = pattern.search(text)
    if not m:
        return False

    start, end = m.start(), m.end()

    # Left boundary check: preceding char must not be CJK
    if start > 0 and _is_cjk(text[start - 1]):
        return False

    # Right boundary check: if next char is CJK, count the full CJK run
    if end < len(text) and _is_cjk(text[end]):
        # Count how many consecutive CJK chars follow
        run = 0
        for i in range(end, len(text)):
            if _is_cjk(text[i]):
                run += 1
            else:
                break
        # If CJK run is exactly 1 char, keyword is a 1-char suffix compound → block
        if run == 1:
            return False
        # run >= 2: keyword is followed by a word (e.g. "电气设备"), allow

    # Context exclusion: if any exclude pattern found in text, reject
    if exclude_context:
        for ctx in exclude_context:
            if ctx in text:
                return False

    return True


def validate_rules(rules_path):
    """
    Check rule library health.
    Prints issues to stderr. Returns True if passed, False if issues found.
    """
    log(f"Validating rules: {rules_path}")
    issues = []

    try:
        rules = load_rules(rules_path)
    except Exception as e:
        issues.append(f"Failed to load rules: {e}")
        for issue in issues:
            print(f"ERROR: {issue}", file=sys.stderr)
        return False

    # 1. Check each entity has non-empty capabilities
    entities = rules.get("entities", {})
    if not entities:
        issues.append("No entities defined.")
    else:
        for eid, edata in entities.items():
            caps = edata.get("capabilities", [])
            if not caps:
                issues.append(f"Entity '{eid}' has empty capabilities list.")
            # Check for duplicate keywords
            if len(caps) != len(set(caps)):
                seen = set()
                dupes = []
                for c in caps:
                    if c in seen:
                        dupes.append(c)
                    seen.add(c)
                issues.append(f"Entity '{eid}' has duplicate capability keywords: {dupes}")

    # 2. Check capability keywords vs red_alerts conflict
    red_alerts = set(rules.get("red_alerts", []))
    if entities:
        for eid, edata in entities.items():
            caps = set(edata.get("capabilities", []))
            conflict = caps & red_alerts
            if conflict:
                issues.append(
                    f"Entity '{eid}': capability keywords conflict with red_alerts: {sorted(conflict)}"
                )

    # 3. Check special_rules have required fields
    for rule in rules.get("special_rules", []):
        if not rule.get("match_keywords"):
            issues.append(f"Special rule '{rule.get('id', '?')}' has empty match_keywords.")
        if not rule.get("action"):
            issues.append(f"Special rule '{rule.get('id', '?')}' missing action.")

    # 4. Check red_alerts no duplicates
    if len(rules.get("red_alerts", [])) != len(red_alerts):
        issues.append("red_alerts list contains duplicate entries.")

    if issues:
        for issue in issues:
            print(f"WARNING: {issue}", file=sys.stderr)
        log(f"Rule validation FAILED ({len(issues)} issue(s) found)")
        return False
    else:
        log("Rule validation passed.")
        return True


def check_special_rules(title, special_rules):
    """Check special rules first (highest priority)."""
    for rule in special_rules:
        keywords = rule.get("match_keywords", [])
        for kw in keywords:
            if smart_match(title, kw):
                return {
                    "verdict": rule.get("action", "unknown"),
                    "reason": rule.get("description", ""),
                    "assigned_entity": rule.get("assigned_entity", ""),
                    "rule_id": rule.get("id", ""),
                }
    return None


def check_red_alerts(title, red_alerts, exclude_contexts=None):
    """
    Check if title contains any red-alert keywords (boundary-aware).
    exclude_contexts: dict mapping alert -> list of disqualifying context patterns
    """
    if exclude_contexts is None:
        exclude_contexts = {}

    for alert in red_alerts:
        ctx = exclude_contexts.get(alert)
        if smart_match(title, alert, exclude_context=ctx):
            return {"verdict": "not_investable", "reason": f"红色预警：{alert}"}
    return None


def match_entity(title, entities, exclude_contexts=None):
    """
    Match title against entity capabilities (boundary-aware).
    Returns best matching entity.
    """
    if exclude_contexts is None:
        exclude_contexts = {}

    best_entity = None
    best_score = 0
    for entity_id, entity_data in entities.items():
        capabilities = entity_data.get("capabilities", [])
        score = 0
        matched_caps = []
        for cap in capabilities:
            ctx = exclude_contexts.get(cap)
            if smart_match(title, cap, exclude_context=ctx):
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
        if smart_match(title, kw):
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

    # Load exclude contexts if present in rules
    exclude_contexts = rules.get("_exclude_contexts", {})

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

    # 2. Red alerts (boundary-aware)
    red = check_red_alerts(title, rules.get("red_alerts", []), exclude_contexts=exclude_contexts)
    if red:
        return {
            **ann,
            "verdict": red["verdict"],
            "reason": red["reason"],
            "assigned_entity": "",
            "matched_capabilities": [],
            "region_info": classify_region(title, rules.get("region_priority", {})),
        }

    # 3. Entity capability match (boundary-aware)
    entity = match_entity(title, rules.get("entities", {}), exclude_contexts=exclude_contexts)
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
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  python3 qual_check.py --validate-rules <rules_file.json>", file=sys.stderr)
        print("  python3 qual_check.py <cache_file.jsonl> <rules_file.json>", file=sys.stderr)
        sys.exit(1)

    if sys.argv[1] == "--validate-rules":
        if len(sys.argv) < 3:
            print("Usage: python3 qual_check.py --validate-rules <rules_file.json>", file=sys.stderr)
            sys.exit(1)
        ok = validate_rules(sys.argv[2])
        sys.exit(0 if ok else 1)

    if len(sys.argv) < 3:
        print("Usage: python3 qual_check.py <cache_file.jsonl> <rules_file.json>", file=sys.stderr)
        sys.exit(1)

    cache_path = sys.argv[1]
    rules_path = sys.argv[2]

    log(f"Loading rules from {rules_path}")
    rules = load_rules(rules_path)
    log(f"Loading announcements from {cache_path}")
    announcements = load_announcements(cache_path)
    log(f"Processing {len(announcements)} announcements")

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
    log(f"Done. Total: {total} | can: {stats['investable']} | cannot: {stats['not_investable']} | review: {stats['needs_review']} | skip: {stats['skip']}")


if __name__ == "__main__":
    main()
