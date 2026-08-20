#!/usr/bin/env python3
"""Shared helpers for kuaidi-query scripts."""
from __future__ import annotations

import contextlib
import json
import os
import re
import tempfile
from datetime import datetime
from pathlib import Path

try:
    import fcntl
except ImportError:  # Windows 无 fcntl；单进程场景退化为无锁，原子替换仍保证文件完整
    fcntl = None

SUBSCRIBE_FILE = Path(os.path.expanduser(os.environ.get(
    "KUAIDI_SUBSCRIBE_FILE", "~/.openclaw/subscribe/kuaidi.json"
)))

STATE_TEXT = {"0": "查无信息", "1": "已揽收", "2": "运输中", "3": "已签收", "4": "问题件", "5": "转寄"}
STATE_ICON = {"0": "❓", "1": "🚚", "2": "🚚", "3": "✅", "4": "⚠️", "5": "🚚"}

class SubscriptionDataError(RuntimeError):
    pass

def state_text(state):
    return STATE_TEXT.get(str(state), f"未知状态 ({state})")

def state_icon(state):
    return STATE_ICON.get(str(state), "📦")

def parse_trace_time(value: str):
    if not value:
        return datetime.min
    normalized = value.strip().replace("T", " ").replace("/", "-")
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(normalized[:19], fmt)
        except ValueError:
            continue
    return datetime.min

def sorted_traces(result):
    traces = result.get("Traces") or []
    return sorted(traces, key=lambda item: parse_trace_time(str(item.get("AcceptTime", ""))))

def latest_trace_of(result):
    traces = sorted_traces(result)
    return traces[-1] if traces else None

def extract_pickup_code(desc):
    if not desc:
        return None
    patterns = (
        r"(?:取件码|取货码|提货码|验证码)\s*[：:\s]\s*([A-Z0-9-]{2,12})",
        r"凭\s*([A-Z0-9-]{2,12})\s*(?:取件|取货)",
    )
    for pattern in patterns:
        match = re.search(pattern, desc, re.IGNORECASE)
        if match:
            return match.group(1)
    return None

def _read_unlocked(path=SUBSCRIBE_FILE):
    if not path.exists():
        return []
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SubscriptionDataError(f"订阅文件无法读取或 JSON 已损坏：{path}") from exc
    if not isinstance(value, list):
        raise SubscriptionDataError(f"订阅文件顶层必须是数组：{path}")
    return value

def _write_unlocked(subscriptions, path=SUBSCRIBE_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as file:
            json.dump(subscriptions, file, indent=2, ensure_ascii=False)
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())
        os.chmod(temp_name, 0o600)
        os.replace(temp_name, path)
        os.chmod(path, 0o600)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)

@contextlib.contextmanager
def subscription_lock(path=SUBSCRIBE_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = Path(str(path) + ".lock")
    with open(lock_path, "a+", encoding="utf-8") as lock:
        os.chmod(lock_path, 0o600)
        if fcntl is not None:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            if fcntl is not None:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)

def load_subscriptions(path=SUBSCRIBE_FILE):
    with subscription_lock(path):
        return _read_unlocked(path)

def mutate_subscriptions(mutator, path=SUBSCRIBE_FILE):
    with subscription_lock(path):
        subscriptions = _read_unlocked(path)
        result = mutator(subscriptions)
        _write_unlocked(subscriptions, path)
        return result

def merge_subscription_updates(updates, path=SUBSCRIBE_FILE):
    """Merge query-produced fields without resurrecting removed subscriptions."""
    by_number = {item["tracking_number"]: item for item in updates}
    def apply(items):
        for item in items:
            update = by_number.get(item.get("tracking_number"))
            if update:
                item.update(update)
    mutate_subscriptions(apply, path)
