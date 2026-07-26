"""
archive.py - 历史研究案例库

每次完成一份研究后，可以归档到 workspace/memory/research_archive/，
下次做同样商品的研究时先检索历史。

存储格式：Markdown + YAML front matter
- 商品
- 日期
- 类型（commodity / sector / event / ...）
- 主要结论
- 关键数字
"""

from __future__ import annotations
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Optional


# 默认归档目录
ARCHIVE_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "research_archive"


def ensure_dir():
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)


def archive_research(
    commodity: str,
    summary: str,
    findings: dict,
    files: Optional[list[str]] = None,
    tags: Optional[list[str]] = None,
) -> Path:
    """
    归档一份研究到本地。

    Args:
        commodity: 商品名（如"铜" / "白酒" / "半导体"）
        summary: 一句话总结
        findings: dict, 结构化数据（如 {"price_change": "-1.75%", "top_stocks": [...]}）
        files: 关联文件路径列表（图片/报告/CSV）
        tags: 标签

    Returns:
        归档文件的路径
    """
    ensure_dir()

    today = datetime.now().strftime("%Y-%m-%d")
    safe_name = commodity.replace("/", "_").replace("\\", "_")
    path = ARCHIVE_DIR / f"{today}_{safe_name}.md"

    front_matter = {
        "commodity": commodity,
        "date": today,
        "tags": tags or [],
        "files": files or [],
    }

    content = f"""---
commodity: {commodity}
date: {today}
tags: {json.dumps(tags or [], ensure_ascii=False)}
---

# {commodity} 研究归档

> 归档时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}
> {summary}

## 关键发现

```json
{json.dumps(findings, ensure_ascii=False, indent=2)}
```

## 关联文件

{chr(10).join('- ' + f for f in (files or [])) if files else '（无）'}

## 标签

{', '.join(tags or ['未分类'])}
"""
    path.write_text(content, encoding="utf-8")
    print(f"📁 已归档: {path}")
    return path


def search_archive(commodity: str, limit: int = 5) -> list[dict]:
    """
    检索历史研究。

    Returns:
        [{path, commodity, date, summary, tags, findings}, ...]
    """
    ensure_dir()
    if not ARCHIVE_DIR.exists():
        return []

    results = []
    for md in sorted(ARCHIVE_DIR.glob("*.md"), reverse=True):
        try:
            content = md.read_text(encoding="utf-8")
            # 简单匹配：检查商品名是否出现
            if commodity in content:
                # 抓 front matter (到第一个 ---)
                fm_str, body = content.split("---\n", 2)[1:3]
                fm = {}
                for line in fm_str.strip().split("\n"):
                    if ":" in line:
                        k, v = line.split(":", 1)
                        fm[k.strip()] = v.strip()

                summary_line = ""
                for line in body.split("\n"):
                    if line.startswith(">") and "归档" not in line:
                        summary_line = line.lstrip("> ").strip()
                        break

                results.append({
                    "path": str(md),
                    "commodity": fm.get("commodity", "?"),
                    "date": fm.get("date", "?"),
                    "tags": fm.get("tags", "[]"),
                    "summary": summary_line,
                })
                if len(results) >= limit:
                    break
        except Exception:
            continue
    return results


def print_search_result(results: list[dict], commodity: str):
    print(f"\n{'=' * 55}")
    print(f"  '{commodity}' 历史研究检索 (共 {len(results)} 条)")
    print(f"{'=' * 55}")
    if not results:
        print(f"  未找到历史研究。首次研究请用 archive_research() 记录。")
        return
    for r in results:
        print(f"\n  📄 {r['date']} — {r['commodity']}")
        print(f"     {r['summary']}")
        print(f"     path: {r['path']}")
    print(f"\n{'=' * 55}\n")


def list_archive() -> list[dict]:
    """列出所有归档"""
    ensure_dir()
    if not ARCHIVE_DIR.exists():
        return []
    out = []
    for md in sorted(ARCHIVE_DIR.glob("*.md"), reverse=True):
        out.append({"path": str(md), "name": md.name})
    return out
