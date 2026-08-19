#!/usr/bin/env python3
"""Manage local tracking subscriptions."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime

from kuaidi_common import (SubscriptionDataError, extract_pickup_code, latest_trace_of,
    load_subscriptions, merge_subscription_updates, mutate_subscriptions, state_icon, state_text)
from query_tracking import query_tracking, format_result

def summary(sub):
    status = sub.get("last_status")
    return {**sub, "last_status_text": "未查询" if status is None else state_text(status),
            "last_status_icon": "" if status is None else state_icon(status)}

def emit(payload, json_output=False, text=None):
    if json_output:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif text:
        print(text)

def add(args):
    remark, platform, phone = args.remark, args.platform, args.phone_suffix
    legacy = list(args.legacy)
    if legacy:
        if len(legacy) > 3:
            raise ValueError("旧式位置参数最多为：备注、平台、手机尾号；含空格备注请加引号")
        remark = remark or legacy.pop(0)
        if legacy:
            candidate = legacy.pop(0)
            if candidate.isdigit() and len(candidate) == 4 and not phone:
                phone = candidate
            else:
                platform = platform or candidate
        if legacy:
            phone = phone or legacy.pop(0)
    if phone and (not phone.isdigit() or len(phone) != 4):
        raise ValueError("手机尾号必须是 4 位数字")
    now = datetime.now().isoformat()
    created = {"tracking_number": args.tracking_number.strip(), "company_code": args.company_code,
               "remark": remark, "platform": platform, "phone_suffix": phone,
               "subscribed_at": now, "last_status": None, "last_checked": None,
               "latest_trace": None, "pickup_code": None}
    def mutate(items):
        if any(item.get("tracking_number") == created["tracking_number"] for item in items):
            return False
        items.append(created)
        return True
    added = mutate_subscriptions(mutate)
    payload = {"success": added, "action": "add", "subscription": summary(created)}
    if not added:
        payload["error"] = f"快递单号 {created['tracking_number']} 已订阅"
    emit(payload, args.json, "✅ 已添加订阅" if added else f"⚠️ {payload['error']}")
    return 0 if added else 1

def remove(args):
    def mutate(items):
        before = len(items)
        items[:] = [item for item in items if item.get("tracking_number") != args.tracking_number]
        return len(items) != before
    removed = mutate_subscriptions(mutate)
    payload = {"success": removed, "action": "remove", "tracking_number": args.tracking_number}
    if not removed:
        payload["error"] = f"未找到订阅的单号：{args.tracking_number}"
    emit(payload, args.json, "✅ 已取消订阅" if removed else f"❌ {payload['error']}")
    return 0 if removed else 1

def list_items(args):
    items = [summary(item) for item in load_subscriptions()]
    payload = {"success": True, "total": len(items), "subscriptions": items}
    if args.json:
        emit(payload, True)
    elif not items:
        print("📭 暂无订阅的快递")
    else:
        print(f"📦 订阅的快递（{len(items)} 个）")
        for item in items:
            title = item.get("remark") or item["tracking_number"]
            platform = f"（{item['platform']}）" if item.get("platform") else ""
            print(f"- {item['last_status_icon']} {title}{platform}：{item['last_status_text']}｜{item.get('latest_trace') or '暂无轨迹'}")
    return 0

def check(args):
    snapshot = load_subscriptions()
    if args.tracking_number:
        snapshot = [item for item in snapshot if item.get("tracking_number") == args.tracking_number]
        if not snapshot:
            payload = {"success": False, "error": f"未找到订阅的单号：{args.tracking_number}"}
            emit(payload, args.json, f"❌ {payload['error']}")
            return 1
    checked, updates, errors = [], [], []
    for item in snapshot:
        result = query_tracking(item["tracking_number"], item.get("company_code"), item.get("phone_suffix"))
        now = datetime.now().isoformat()
        if not result.get("Success"):
            errors.append({"tracking_number": item["tracking_number"], "error": result.get("Reason", "查询失败")})
            updates.append({"tracking_number": item["tracking_number"], "last_checked": now, "last_error": result.get("Reason", "查询失败")})
            checked.append({**summary(item), "success": False, "error": result.get("Reason", "查询失败")})
            continue
        latest = latest_trace_of(result)
        desc = latest.get("AcceptStation", "") if latest else ""
        update = {"tracking_number": item["tracking_number"], "last_checked": now,
                  "last_status": result.get("State"), "last_state_ex": result.get("StateEx", ""),
                  "latest_trace": desc, "latest_trace_time": latest.get("AcceptTime", "") if latest else "",
                  "last_error": None}
        pickup = extract_pickup_code(desc)
        if pickup:
            update["pickup_code"] = pickup
        merged = {**item, **update}
        checked.append({**summary(merged), "success": True,
                        "message": format_result(result, item["tracking_number"], item.get("company_code"))})
        updates.append(update)
    merge_subscription_updates(updates)
    payload = {"success": not errors, "total": len(checked), "subscriptions": checked,
               "error_count": len(errors), "errors": errors, "checked_at": datetime.now().isoformat()}
    if args.json:
        emit(payload, True)
    else:
        for item in checked:
            print(item.get("message") or f"❌ {item['tracking_number']}：{item.get('error')}")
    return 0 if not errors else 1

def build_parser():
    parser = argparse.ArgumentParser(description="管理快递订阅")
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("add", help="添加订阅")
    p.add_argument("tracking_number"); p.add_argument("company_code", nargs="?"); p.add_argument("legacy", nargs="*")
    p.add_argument("--remark"); p.add_argument("--platform"); p.add_argument("--phone-suffix"); p.add_argument("--json", action="store_true")
    p.set_defaults(handler=add)
    p = sub.add_parser("remove", help="取消订阅"); p.add_argument("tracking_number"); p.add_argument("--json", action="store_true"); p.set_defaults(handler=remove)
    p = sub.add_parser("list", help="列出订阅"); p.add_argument("--json", action="store_true"); p.set_defaults(handler=list_items)
    p = sub.add_parser("check", help="刷新订阅"); p.add_argument("tracking_number", nargs="?"); p.add_argument("--json", action="store_true"); p.set_defaults(handler=check)
    return parser

def main(argv=None):
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
        return args.handler(args)
    except (SubscriptionDataError, ValueError) as exc:
        json_output = "--json" in (argv if argv is not None else sys.argv[1:])
        emit({"success": False, "error": str(exc)}, json_output, f"❌ {exc}")
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
