"""Shared helpers for admin-assistant scripts (stdlib only)."""
from __future__ import annotations

import json
import os
import re
import uuid
from datetime import date, datetime, time, timedelta

try:
    from zoneinfo import ZoneInfo
except Exception:  # pragma: no cover
    ZoneInfo = None  # type: ignore

TZ_NAME = os.environ.get("ADMIN_ASSIST_TZ", "Asia/Shanghai")
_TZ = None
if ZoneInfo is not None:
    try:
        _TZ = ZoneInfo(TZ_NAME)
    except Exception:
        _TZ = None

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIME_RE = re.compile(r"^\d{2}:\d{2}$")


# ---------------------------------------------------------------- time utils
def now() -> datetime:
    return datetime.now(_TZ) if _TZ else datetime.now()


def today() -> date:
    return now().date()


def tzinfo():
    return _TZ


def parse_date(value: str) -> date:
    """Accept YYYY-MM-DD | today | tomorrow | tomorrow+<n> | +<n> | <n> days."""
    raw = (value or "").strip().lower()
    if not raw:
        raise ValueError("empty date")
    if raw == "today":
        return today()
    if raw == "tomorrow":
        return today() + timedelta(days=1)
    m = re.match(r"^(?:tomorrow|today)?\s*\+\s*(\d+)\s*d?a?y?s?$", raw)
    if m:
        base = today() + (timedelta(days=1) if raw.startswith("tomorrow") else timedelta())
        return base + timedelta(days=int(m.group(1)))
    m = re.match(r"^-(\d+)d?a?y?s?$", raw)
    if m:
        return today() - timedelta(days=int(m.group(1)))
    if DATE_RE.match(raw):
        return date.fromisoformat(raw)
    for fmt in ("%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", "%b %d %Y", "%B %d %Y"):
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"unrecognised date: {value!r} (use YYYY-MM-DD / today / tomorrow / +3)")


def parse_time(value: str) -> time:
    raw = (value or "").strip()
    if not TIME_RE.match(raw):
        raise ValueError(f"unrecognised time: {value!r} (use HH:MM 24h)")
    hh, mm = raw.split(":")
    return time(int(hh), int(mm))


def iso(dt: datetime) -> str:
    return dt.isoformat(timespec="minutes")


def fmt_dt(dt: datetime | None) -> str:
    if dt is None:
        return "-"
    return dt.strftime("%Y-%m-%d %H:%M %Z").replace(" ", " ", 1).strip()


# ---------------------------------------------------------------- storage
def data_home() -> str:
    p = os.environ.get("ADMIN_ASSIST_HOME") or os.path.join(
        os.path.expanduser("~"), ".openclaw", "workspace", "assistant-data"
    )
    os.makedirs(p, exist_ok=True)
    os.makedirs(os.path.join(p, "calendar"), exist_ok=True)
    return p


def fpath(*parts: str) -> str:
    return os.path.join(data_home(), *parts)


def load(name: str, default):
    p = fpath(name)
    if not os.path.exists(p):
        return default
    with open(p, encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError:
            return default


def save(name: str, obj) -> None:
    p = fpath(name)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, p)


def append_log(name: str, record: dict) -> None:
    p = fpath(name)
    record = dict(record)
    record.setdefault("at", iso(now()))
    with open(p, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_log(name: str) -> list[dict]:
    p = fpath(name)
    if not os.path.exists(p):
        return []
    out = []
    with open(p, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def new_id(prefix: str, items: list[dict]) -> str:
    used = {i.get("id") for i in items}
    while True:
        cand = f"{prefix}-{uuid.uuid4().hex[:6]}"
        if cand not in used:
            return cand


# ---------------------------------------------------------------- output
def out(text: str = "") -> None:
    print(text)


def fail(msg: str, code: int = 2) -> None:
    print(f"ERROR: {msg}")
    raise SystemExit(code)


def bool_env(name: str, default: bool = False) -> bool:
    v = os.environ.get(name)
    if v is None:
        return default
    return v.strip().lower() in {"1", "true", "yes", "on"}
