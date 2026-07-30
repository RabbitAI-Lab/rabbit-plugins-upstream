#!/usr/bin/env python3
"""
黄金追踪 - web_fetch 行为记录器
智能体每次调用 web_fetch 抓取网页后，必须立即调用本脚本记录该 URL。
未记录的 URL 不会通过 check_analysis.py 的 sources 校验。
零第三方依赖。

用法:
    python3 scripts/log_fetch.py <url> [标题]
    python3 scripts/log_fetch.py list            # 列出本次会话已记录的 URL
    python3 scripts/log_fetch.py clear           # 清空记录（开始新一次分析时调用）
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = ROOT / ".cache" / "fetch_log.json"
TZ_BEIJING = timezone(timedelta(hours=8))


def load_log() -> list:
    if not LOG_FILE.exists():
        return []
    try:
        data = json.loads(LOG_FILE.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []


def save_log(entries: list):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")


def add(url: str, title: str = "") -> dict:
    url = url.strip()
    if not url:
        print("[错误] URL 不能为空", file=sys.stderr)
        sys.exit(1)

    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        print(f"[错误] 非合法 http(s) URL: {url}", file=sys.stderr)
        sys.exit(1)

    entries = load_log()
    # 同一 URL 不重复记录，但更新访问时间
    for e in entries:
        if e.get("url") == url:
            e["last_fetch_at"] = datetime.now(TZ_BEIJING).isoformat()
            if title:
                e["title"] = title
            save_log(entries)
            print(f"[已记录] {url} (已存在，更新时间)")
            return e

    entry = {
        "url": url,
        "domain": parsed.netloc,
        "title": title or "",
        "fetched_at": datetime.now(TZ_BEIJING).isoformat(),
        "last_fetch_at": datetime.now(TZ_BEIJING).isoformat(),
    }
    entries.append(entry)
    save_log(entries)
    print(f"[已记录] {url}")
    if title:
        print(f"           标题: {title}")
    return entry


def list_entries():
    entries = load_log()
    if not entries:
        print("(空) 尚未记录任何 web_fetch")
        return
    print(f"共 {len(entries)} 条记录:")
    domains = set()
    for e in entries:
        domains.add(e.get("domain", "?"))
        print(f"  - [{e.get('fetched_at', '?')[:19]}] {e['url']}")
        if e.get("title"):
            print(f"      标题: {e['title']}")
    print(f"\n覆盖 {len(domains)} 个独立域名: {', '.join(sorted(domains))}")


def clear():
    save_log([])
    print("[已清空] fetch_log.json")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "list":
        list_entries()
    elif arg == "clear":
        clear()
    elif arg.startswith("http://") or arg.startswith("https://"):
        title = sys.argv[2] if len(sys.argv) > 2 else ""
        add(arg, title)
    else:
        print(f"[错误] 第一个参数应为 URL 或 list/clear，得到: {arg}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
