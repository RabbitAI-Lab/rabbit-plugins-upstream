#!/usr/bin/env python3
"""Check subscribed shipments and emit only changes or errors."""
from __future__ import annotations

import argparse
import json
from datetime import datetime

from kuaidi_common import (SubscriptionDataError, extract_pickup_code, latest_trace_of,
    load_subscriptions, merge_subscription_updates, state_icon, state_text)
from query_tracking import query_tracking

def signature(state, state_ex, latest):
    return {"state": str(state or ""), "state_ex": str(state_ex or ""),
            "latest_trace": latest.get("AcceptStation", "") if latest else "",
            "latest_time": latest.get("AcceptTime", "") if latest else ""}

def previous(item, current):
    old = {"state": str(item.get("last_status") or ""), "state_ex": str(item.get("last_state_ex") or ""),
           "latest_trace": item.get("latest_trace") or "", "latest_time": item.get("latest_trace_time") or ""}
    if not old["latest_time"] and old["latest_trace"] == current["latest_trace"]:
        old["latest_time"] = current["latest_time"]
    return old

def check_changes(dry_run=False, include_first_seen=False):
    snapshot = load_subscriptions()
    changes, errors, updates = [], [], []
    for item in snapshot:
        number = item["tracking_number"]
        result = query_tracking(number, item.get("company_code"), item.get("phone_suffix"))
        checked_at = datetime.now().isoformat()
        if not result.get("Success"):
            error = result.get("Reason", "查询失败")
            errors.append({"tracking_number": number, "error": error})
            updates.append({"tracking_number": number, "last_checked": checked_at, "last_error": error})
            continue
        latest = latest_trace_of(result)
        current = signature(result.get("State"), result.get("StateEx"), latest)
        old = previous(item, current)
        has_previous = any(old.values())
        if (has_previous or include_first_seen) and current != old:
            title = " / ".join(filter(None, [item.get("remark"), item.get("platform")])) or number
            changed_fields = [key for key in current if current[key] != old[key]]
            changes.append({"tracking_number": number, "company_code": item.get("company_code"),
                "company": result.get("ShipperName") or item.get("company_code") or "未知快递",
                "title": title, "state": current["state"], "state_text": state_text(current["state"]),
                "state_ex": current["state_ex"], "changed_fields": changed_fields,
                "previous": old, "current": current, "latest_trace": latest,
                "message": f"{state_icon(current['state'])} {title}：{state_text(current['state'])}\n{result.get('ShipperName') or item.get('company_code') or '未知快递'} - {number}\n{current['latest_trace'] or '暂无最新轨迹'}"})
        update = {"tracking_number": number, "last_checked": checked_at, "last_status": result.get("State"),
                  "last_state_ex": result.get("StateEx", ""), "latest_trace": current["latest_trace"],
                  "latest_trace_time": current["latest_time"], "last_error": None}
        pickup = extract_pickup_code(current["latest_trace"])
        if pickup:
            update["pickup_code"] = pickup
        updates.append(update)
    if not dry_run:
        merge_subscription_updates(updates)
    return {"success": not errors, "total": len(snapshot), "changed": bool(changes),
            "change_count": len(changes), "changes": changes, "error_count": len(errors),
            "errors": errors, "checked_at": datetime.now().isoformat(), "dry_run": dry_run}

def main(argv=None):
    parser = argparse.ArgumentParser(description="检查订阅快递是否发生变化")
    parser.add_argument("--dry-run", action="store_true"); parser.add_argument("--include-first-seen", action="store_true")
    parser.add_argument("--quiet", action="store_true", help="仅在无变化且无错误时静默")
    args = parser.parse_args(argv)
    try:
        result = check_changes(args.dry_run, args.include_first_seen)
    except SubscriptionDataError as exc:
        result = {"success": False, "changed": False, "change_count": 0, "changes": [],
                  "error_count": 1, "errors": [{"error": str(exc)}], "checked_at": datetime.now().isoformat()}
    if not (args.quiet and not result.get("changed") and not result.get("errors")):
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("success") else 1

if __name__ == "__main__":
    raise SystemExit(main())
