#!/usr/bin/env python3
"""Priority Coach local record management.

默认写入 ~/.openclaw/data/priority-coach/records.json，兼容读取旧版
~/.workbuddy/priority-coach/records.json。

用法：
  python3 scripts/record.py add --data '<json>'
  python3 scripts/record.py list
  python3 scripts/record.py latest
  python3 scripts/record.py get [--date YYYY-MM-DD | --index N]
  python3 scripts/record.py delete [--date YYYY-MM-DD | --index N | --all]
  python3 scripts/record.py export
  python3 scripts/record.py path
  python3 scripts/record.py migrate
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

OPENCLAW_HOME = Path(os.environ.get("OPENCLAW_HOME", "~/.openclaw")).expanduser()
PRIMARY_DIR = OPENCLAW_HOME / "data" / "priority-coach"
PRIMARY_STORE = PRIMARY_DIR / "records.json"
LEGACY_DIR = Path("~/.workbuddy/priority-coach").expanduser()
LEGACY_STORE = LEGACY_DIR / "records.json"
SCHEMA_VERSION = 2


def empty_store() -> dict[str, Any]:
    return {"schemaVersion": SCHEMA_VERSION, "records": []}


def detect_existing_store() -> Path | None:
    if PRIMARY_STORE.exists():
        return PRIMARY_STORE
    if LEGACY_STORE.exists():
        return LEGACY_STORE
    return None


def load_store() -> tuple[dict[str, Any], Path | None]:
    store_path = detect_existing_store()
    if store_path is None:
        return empty_store(), None
    try:
        with store_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return empty_store(), store_path

    if not isinstance(data, dict):
        return empty_store(), store_path
    records = data.get("records")
    if not isinstance(records, list):
        data["records"] = []
    data["schemaVersion"] = SCHEMA_VERSION
    return data, store_path


def write_store(data: dict[str, Any]) -> None:
    PRIMARY_DIR.mkdir(parents=True, exist_ok=True)
    data["schemaVersion"] = SCHEMA_VERSION
    with PRIMARY_STORE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def normalize_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_list(value: Any, *, limit: int | None = None) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        items = [value]
    elif isinstance(value, list):
        items = value
    else:
        items = [str(value)]

    cleaned: list[str] = []
    for item in items:
        text = normalize_string(item)
        if text:
            cleaned.append(text)
    if limit is not None:
        cleaned = cleaned[:limit]
    return cleaned


def normalize_record(raw: dict[str, Any]) -> dict[str, Any]:
    now = dt.datetime.now().isoformat(timespec="seconds")
    record = {
        "schemaVersion": SCHEMA_VERSION,
        "date": normalize_string(raw.get("date")) or dt.date.today().isoformat(),
        "createdAt": normalize_string(raw.get("createdAt")) or now,
        "state": normalize_string(raw.get("state")),
        "topPriorities": normalize_list(raw.get("topPriorities"), limit=3),
        "smallestActionToday": normalize_string(raw.get("smallestActionToday")),
        "notNow": normalize_list(raw.get("notNow")),
        "candidates": normalize_list(raw.get("candidates"), limit=7),
        "weeklyFocus": normalize_list(raw.get("weeklyFocus"), limit=3),
        "energyPattern": normalize_string(raw.get("energyPattern")),
        "supportPreference": normalize_string(raw.get("supportPreference")),
    }

    raw_answers = raw.get("rawAnswers")
    if raw_answers is not None:
        record["rawAnswers"] = raw_answers

    if not record["topPriorities"]:
        raise ValueError("topPriorities 不能为空")
    if not record["smallestActionToday"]:
        raise ValueError("smallestActionToday 不能为空")
    return record


def cmd_add(args: argparse.Namespace) -> int:
    try:
        raw = json.loads(args.data)
    except Exception as exc:
        print(f"ERROR: --data 必须是合法 JSON: {exc}", file=sys.stderr)
        return 1
    if not isinstance(raw, dict):
        print("ERROR: 记录必须是 JSON 对象", file=sys.stderr)
        return 1
    try:
        record = normalize_record(raw)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    data, _ = load_store()
    data["records"].insert(0, record)
    write_store(data)
    print(f"已保存。当前共 {len(data['records'])} 条记录。")
    print(json.dumps(record, ensure_ascii=False, indent=2))
    return 0


def iter_records() -> tuple[list[dict[str, Any]], Path | None]:
    data, store_path = load_store()
    return data.get("records", []), store_path


def cmd_list(_: argparse.Namespace) -> int:
    records, store_path = iter_records()
    if not records:
        print("（暂无记录）")
        return 0
    print(f"当前数据源：{store_path or PRIMARY_STORE}")
    for idx, record in enumerate(records, start=1):
        date = record.get("date", "?")
        tops = " / ".join(record.get("topPriorities", []))
        action = record.get("smallestActionToday", "")
        print(f"{idx}. {date} | {tops} | 最小行动：{action}")
    return 0


def cmd_latest(_: argparse.Namespace) -> int:
    records, _ = iter_records()
    if not records:
        print("（暂无记录）")
        return 0
    print(json.dumps(records[0], ensure_ascii=False, indent=2))
    return 0


def find_record(records: list[dict[str, Any]], *, date: str | None, index: int | None) -> dict[str, Any]:
    if not records:
        raise IndexError("暂无记录")
    if date:
        for record in records:
            if record.get("date") == date:
                return record
        raise IndexError(f"未找到日期 {date}")
    idx = index or 1
    if not 1 <= idx <= len(records):
        raise IndexError("索引越界")
    return records[idx - 1]


def cmd_get(args: argparse.Namespace) -> int:
    records, _ = iter_records()
    if not records:
        print("（暂无记录）")
        return 0
    try:
        record = find_record(records, date=args.date, index=args.index)
    except IndexError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(record, ensure_ascii=False, indent=2))
    return 0


def cmd_delete(args: argparse.Namespace) -> int:
    data, _ = load_store()
    records = data.get("records", [])
    if not records:
        print("（暂无记录）")
        return 0

    if args.all:
        data["records"] = []
        write_store(data)
        print("已清空所有记录。")
        return 0

    if args.date:
        before = len(records)
        data["records"] = [record for record in records if record.get("date") != args.date]
        removed = before - len(data["records"])
        write_store(data)
        print(f"删除了 {removed} 条。")
        return 0

    idx = args.index or 1
    if not 1 <= idx <= len(records):
        print("索引越界", file=sys.stderr)
        return 1
    removed = records[idx - 1]
    data["records"].pop(idx - 1)
    write_store(data)
    print(f"已删除：{removed.get('date', '?')}")
    return 0


def cmd_export(_: argparse.Namespace) -> int:
    data, _ = load_store()
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return 0


def cmd_path(_: argparse.Namespace) -> int:
    current = detect_existing_store()
    print(str(current or PRIMARY_STORE))
    return 0


def cmd_migrate(_: argparse.Namespace) -> int:
    if PRIMARY_STORE.exists():
        print(f"已使用新路径：{PRIMARY_STORE}")
        return 0
    if not LEGACY_STORE.exists():
        PRIMARY_DIR.mkdir(parents=True, exist_ok=True)
        write_store(empty_store())
        print(f"未发现旧数据，已初始化新路径：{PRIMARY_STORE}")
        return 0
    PRIMARY_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(LEGACY_STORE, PRIMARY_STORE)
    print(f"已迁移：{LEGACY_STORE} -> {PRIMARY_STORE}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="优先级教练本地记录")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add")
    add.add_argument("--data", required=True)

    sub.add_parser("list")
    sub.add_parser("latest")

    get = sub.add_parser("get")
    get.add_argument("--date")
    get.add_argument("--index", type=int)

    delete = sub.add_parser("delete")
    delete.add_argument("--date")
    delete.add_argument("--index", type=int)
    delete.add_argument("--all", action="store_true")

    sub.add_parser("export")
    sub.add_parser("path")
    sub.add_parser("migrate")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == "add":
        return cmd_add(args)
    if args.cmd == "list":
        return cmd_list(args)
    if args.cmd == "latest":
        return cmd_latest(args)
    if args.cmd == "get":
        return cmd_get(args)
    if args.cmd == "delete":
        return cmd_delete(args)
    if args.cmd == "export":
        return cmd_export(args)
    if args.cmd == "path":
        return cmd_path(args)
    if args.cmd == "migrate":
        return cmd_migrate(args)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
