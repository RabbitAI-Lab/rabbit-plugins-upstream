#!/usr/bin/env python3
"""Normalize a single-session CTR diagnosis into the public report contract."""

import json
import sys


DIMENSIONS = [
    "search_intent",
    "main_image",
    "title_completeness",
    "price_benefit",
    "decision_trust",
]
STATUSES = {"gap", "parity", "candidate_higher", "unknown"}
PRIORITIES = {"high", "medium", "low"}


def as_string(value, fallback=""):
    return value if isinstance(value, str) else fallback


def parse_report(value):
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else ""
            if text.rstrip().endswith("```"):
                text = text.rstrip()[:-3].rstrip()
        return json.loads(text)
    raise ValueError("report must be a JSON object or JSON string")


def normalize_suggestion(value):
    if not isinstance(value, dict):
        return None
    action = as_string(value.get("action")).strip()
    reason = as_string(value.get("reason")).strip()
    priority = as_string(value.get("priority")).lower().strip()
    if not action or not reason or priority not in PRIORITIES:
        return None
    return {"action": action, "reason": reason, "priority": priority}


def normalize_dimension(value, dimension):
    value = value if isinstance(value, dict) else {}
    status = as_string(value.get("status"), "unknown")
    if status not in STATUSES:
        status = "unknown"
    return {
        "dimension": dimension,
        "status": status,
        "evidence": as_string(value.get("evidence"), "unknown"),
        "suggestion": normalize_suggestion(value.get("suggestion")),
    }


def normalize_items(session, report):
    source_items = report.get("item_diagnostics", [])
    if not isinstance(source_items, list):
        source_items = []
    by_id = {
        str(item.get("item_id")): item
        for item in source_items
        if isinstance(item, dict) and item.get("item_id") is not None
    }
    clicked_id = str(session.get("clicked_item_id", ""))
    output = []
    for item in session.get("items", []):
        if not isinstance(item, dict):
            continue
        item_id = str(item.get("item_id", ""))
        if not item_id or item.get("clicked") is True or item_id == clicked_id:
            continue
        draft = by_id.get(item_id, {})
        raw_dimensions = draft.get("dimension_diagnoses", []) if isinstance(draft, dict) else []
        dimension_by_name = {
            entry.get("dimension"): entry
            for entry in raw_dimensions
            if isinstance(entry, dict) and entry.get("dimension") in DIMENSIONS
        }
        output.append({
            "item_id": item_id,
            "position": item.get("position"),
            "dimension_diagnoses": [
                normalize_dimension(dimension_by_name.get(name), name)
                for name in DIMENSIONS
            ],
        })
    return output


def normalize_merchant_suggestions(values, candidate_ids):
    if not isinstance(values, list):
        return []
    output = []
    for value in values:
        if not isinstance(value, dict):
            continue
        item_id = str(value.get("item_id", ""))
        suggestion = normalize_suggestion(value)
        if item_id in candidate_ids and suggestion:
            output.append({"item_id": item_id, **suggestion})
    return output


def normalize_platform_suggestions(values):
    if not isinstance(values, list):
        return []
    return [suggestion for value in values if (suggestion := normalize_suggestion(value))]


def normalize(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("session"), dict):
        raise ValueError("session must be an object")
    session = payload["session"]
    report = parse_report(payload.get("report"))
    if not isinstance(report, dict):
        raise ValueError("report must resolve to an object")
    diagnostics = normalize_items(session, report)
    candidate_ids = {item["item_id"] for item in diagnostics}
    limitations = report.get("limitations", [])
    return {
        "query": as_string(session.get("query")),
        "clicked_item_id": str(session.get("clicked_item_id", "")),
        "item_diagnostics": diagnostics,
        "merchant_suggestions": normalize_merchant_suggestions(
            report.get("merchant_suggestions"), candidate_ids
        ),
        "platform_suggestions": normalize_platform_suggestions(
            report.get("platform_suggestions")
        ),
        "limitations": [value for value in limitations if isinstance(value, str)],
    }


def main():
    try:
        payload = json.load(sys.stdin)
        print(json.dumps(normalize(payload), ensure_ascii=False, separators=(",", ":")))
    except (ValueError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({"error": {"code": "invalid_draft_json", "message": str(error)}}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
