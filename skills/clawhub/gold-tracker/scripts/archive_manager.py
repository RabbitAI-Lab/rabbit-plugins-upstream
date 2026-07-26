#!/usr/bin/env python3
"""
黄金追踪 - 归档管理器
基于现实市场行为重构：自动归档、统一命名、索引机制、保留策略
零第三方依赖。
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict, Optional

ROOT = Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT / "logs"
ARCHIVE_DIR = ROOT / "archive"
INDEX_FILE = ARCHIVE_DIR / "index.json"

LOGS_DIR.mkdir(exist_ok=True)
ARCHIVE_DIR.mkdir(exist_ok=True)

TZ_BEIJING = timezone(timedelta(hours=8))


def load_index() -> Dict:
    if INDEX_FILE.exists():
        try:
            return json.loads(INDEX_FILE.read_text())
        except Exception:
            pass
    return {"runs": [], "months": {}}


def save_index(index: Dict):
    for month_info in index.get("months", {}).values():
        if isinstance(month_info.get("dates"), set):
            month_info["dates"] = sorted(list(month_info["dates"]))
    INDEX_FILE.write_text(json.dumps(index, indent=2))


def parse_run_id(text: str) -> Optional[str]:
    m = re.search(r'run_id:\s*"?([^"\n]+)"?', text)
    if m:
        return m.group(1).strip()
    return None


def parse_timestamp(text: str) -> Optional[str]:
    m = re.search(r'timestamp:\s*"?([^"\n]+)"?', text)
    if m:
        return m.group(1).strip()
    return None


def parse_price_usd(text: str) -> Optional[float]:
    m = re.search(r'price_usd:\s*([\d.]+)', text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    return None


def get_month_dir(date_str: str) -> Path:
    year_month = date_str[:7]
    month_dir = ARCHIVE_DIR / year_month
    month_dir.mkdir(exist_ok=True)
    return month_dir


def generate_archive_filename(run_id: str, timestamp: str) -> str:
    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        dt = dt.astimezone(TZ_BEIJING)
        date_part = dt.strftime("%Y-%m-%d")
        time_part = dt.strftime("%H%M")
        return f"{date_part}-{time_part}.yaml"
    except Exception:
        return f"{run_id}.yaml"


def extract_runs_from_log(text: str) -> List[Dict]:
    runs = []
    documents = [d.strip() for d in text.split("---") if d.strip()]
    for doc in documents:
        run_id = parse_run_id(doc)
        timestamp = parse_timestamp(doc)
        price = parse_price_usd(doc)
        if run_id or timestamp:
            runs.append({
                "run_id": run_id or "",
                "timestamp": timestamp or "",
                "price_usd": price,
                "content": doc,
            })
    return runs


def archive_log_file(log_path: Path) -> int:
    if not log_path.exists():
        return 0

    text = log_path.read_text(encoding="utf-8")
    runs = extract_runs_from_log(text)
    if not runs:
        return 0

    index = load_index()
    archived = 0

    for run in runs:
        timestamp = run["timestamp"]
        if not timestamp:
            continue

        month_dir = get_month_dir(timestamp)
        filename = generate_archive_filename(run["run_id"], timestamp)
        archive_path = month_dir / filename

        if archive_path.exists():
            existing_text = archive_path.read_text(encoding="utf-8")
            if run["content"] in existing_text:
                continue

        archive_path.write_text(run["content"] + "\n", encoding="utf-8")

        if run["run_id"] and run["run_id"] not in index["runs"]:
            index["runs"].append(run["run_id"])

        year_month = timestamp[:7]
        if year_month not in index["months"]:
            index["months"][year_month] = {"count": 0, "dates": set()}
        index["months"][year_month]["count"] += 1
        index["months"][year_month]["dates"].add(timestamp[:10])

        archived += 1

    if archived > 0:
        save_index(index)

    return archived


def archive_all_logs() -> int:
    total = 0
    if not LOGS_DIR.exists():
        return 0

    today = datetime.now(TZ_BEIJING).strftime("%Y-%m-%d")
    for log_file in sorted(LOGS_DIR.iterdir()):
        if log_file.suffix not in (".yaml", ".yml"):
            continue

        if today in log_file.name:
            continue

        archived = archive_log_file(log_file)
        if archived > 0:
            log_file.unlink()
            print(f"[已归档] {log_file.name} → {archived} 条记录")
            total += archived

    return total


def find_log_by_date(date_str: str) -> List[Dict]:
    results = []
    month_dir = get_month_dir(date_str)
    if not month_dir.exists():
        return results

    for f in sorted(month_dir.iterdir()):
        if f.suffix not in (".yaml", ".yml"):
            continue

        stem = f.stem
        if stem.startswith(date_str):
            try:
                text = f.read_text(encoding="utf-8")
                runs = extract_runs_from_log(text)
                results.extend([{
                    "file": f.name,
                    "path": str(f),
                    **run
                } for run in runs])
            except Exception:
                pass

    return sorted(results, key=lambda x: x.get("timestamp", ""))


def get_price_history(days: int = 30) -> List[Dict]:
    history = []
    now = datetime.now(TZ_BEIJING)

    for i in range(days):
        date = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        logs = find_log_by_date(date)
        if logs:
            prices = [l["price_usd"] for l in logs if l["price_usd"]]
            if prices:
                history.append({
                    "date": date,
                    "price_usd": sum(prices) / len(prices),
                    "count": len(prices),
                    "high": max(prices),
                    "low": min(prices),
                })

    return sorted(history, key=lambda x: x["date"])


def cleanup_old_archives(retention_days: int = 365):
    now = datetime.now(TZ_BEIJING)
    removed_files = 0
    removed_dirs = 0

    for month_dir in sorted(ARCHIVE_DIR.iterdir()):
        if not month_dir.is_dir() or month_dir.name == ".DS_Store":
            continue

        month_date = month_dir.name + "-01"
        try:
            month_dt = datetime.strptime(month_date, "%Y-%m-%d")
            if (now - month_dt).days > retention_days:
                for f in month_dir.iterdir():
                    if f.is_file():
                        f.unlink()
                        removed_files += 1
                month_dir.rmdir()
                removed_dirs += 1
                print(f"[已清理] {month_dir.name}/")
        except Exception:
            pass

    index = load_index()
    months_to_remove = []
    for year_month in index.get("months", {}):
        month_date = year_month + "-01"
        try:
            month_dt = datetime.strptime(month_date, "%Y-%m-%d")
            if (now - month_dt).days > retention_days:
                months_to_remove.append(year_month)
        except Exception:
            pass

    for year_month in months_to_remove:
        index["months"].pop(year_month, None)
    save_index(index)

    return removed_files, removed_dirs


def rebuild_index():
    index = {"runs": [], "months": {}}

    for month_dir in sorted(ARCHIVE_DIR.iterdir()):
        if not month_dir.is_dir() or month_dir.name == ".DS_Store":
            continue

        year_month = month_dir.name
        if year_month not in index["months"]:
            index["months"][year_month] = {"count": 0, "dates": set()}

        for f in month_dir.iterdir():
            if f.suffix not in (".yaml", ".yml"):
                continue

            try:
                text = f.read_text(encoding="utf-8")
                runs = extract_runs_from_log(text)
                for run in runs:
                    if run["run_id"] and run["run_id"] not in index["runs"]:
                        index["runs"].append(run["run_id"])

                    if run["timestamp"]:
                        date = run["timestamp"][:10]
                        index["months"][year_month]["dates"].add(date)

                    index["months"][year_month]["count"] += 1
            except Exception:
                pass

    save_index(index)
    return len(index["runs"]), len(index["months"])


def show_index_summary():
    index = load_index()
    total_runs = len(index.get("runs", []))
    total_months = len(index.get("months", {}))

    lines = [
        "## 📚 归档索引摘要",
        "",
        f"- 总记录数: {total_runs}",
        f"- 覆盖月份: {total_months}",
        "",
        "### 月份分布:",
    ]

    for month in sorted(index.get("months", {}).keys()):
        info = index["months"][month]
        lines.append(f"- {month}: {info['count']} 条记录 ({len(info['dates'])} 天)")

    print("\n".join(lines))


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  archive_manager.py archive      # 归档所有过期日志")
        print("  archive_manager.py find <date>  # 按日期查询归档记录")
        print("  archive_manager.py history <days> # 获取价格历史")
        print("  archive_manager.py cleanup      # 清理过期归档")
        print("  archive_manager.py rebuild      # 重建索引")
        print("  archive_manager.py summary      # 显示索引摘要")
        sys.exit(0)

    action = sys.argv[1]

    if action == "archive":
        archived = archive_all_logs()
        print(f"\n[完成] 共归档 {archived} 条记录")

    elif action == "find":
        if len(sys.argv) < 3:
            print("用法: archive_manager.py find <YYYY-MM-DD>")
            sys.exit(1)
        date_str = sys.argv[2]
        logs = find_log_by_date(date_str)
        if logs:
            print(f"找到 {len(logs)} 条记录:")
            for log in logs:
                print(f"\n--- {log['file']} ---")
                print(f"Run ID: {log.get('run_id', 'N/A')}")
                print(f"时间: {log.get('timestamp', 'N/A')}")
                print(f"价格: ${log.get('price_usd', 'N/A')}")
        else:
            print(f"未找到 {date_str} 的记录")

    elif action == "history":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        history = get_price_history(days)
        if history:
            print(f"过去 {days} 天价格历史:")
            print(f"{'日期':<12} {'价格':>10} {'数量':>6} {'最高':>10} {'最低':>10}")
            print("-" * 60)
            for h in history:
                print(f"{h['date']:<12} ${h['price_usd']:>9.2f} {h['count']:>6} ${h['high']:>9.2f} ${h['low']:>9.2f}")
        else:
            print("无历史数据")

    elif action == "cleanup":
        retention_days = int(sys.argv[2]) if len(sys.argv) > 2 else 365
        files, dirs = cleanup_old_archives(retention_days)
        print(f"[完成] 清理 {files} 个文件, {dirs} 个目录")

    elif action == "rebuild":
        runs, months = rebuild_index()
        print(f"[完成] 重建索引: {runs} 条记录, {months} 个月份")

    elif action == "summary":
        show_index_summary()

    else:
        print(f"未知操作: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()