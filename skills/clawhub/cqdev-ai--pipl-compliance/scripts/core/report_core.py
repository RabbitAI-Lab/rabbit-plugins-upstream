#!/usr/bin/env python3
"""
ReportGenerator — 统一报告生成引擎

支持多种输出格式，包括 JSON / Markdown / HTML / PDF（后端扩展）。
"""

import json
import csv
import io
from datetime import datetime
from typing import Dict, List, Any, Optional
from enum import Enum


class ReportFormat(Enum):
    JSON = "json"
    MARKDOWN = "markdown"
    HTML = "html"
    CSV = "csv"
    PLAIN_TEXT = "text"


class ReportGenerator:
    """报告生成器 - 将合规检查结果转换为多种格式"""

    @staticmethod
    def to_json(data: dict, pretty: bool = True) -> str:
        indent = 2 if pretty else None
        return json.dumps(data, indent=indent, ensure_ascii=False, default=str)

    @staticmethod
    def to_markdown(data: dict) -> str:
        lines = []
        lines.append(f"# {data.get('tool', '合规检查报告')}")
        lines.append(f"\n- **法规**: {data.get('regulation', '')}")
        lines.append(f"- **时间**: {data.get('check_time', '')[:19]}")
        lines.append(f"- **场景**: {data.get('scenario', '未知')}")
        
        summary = data.get('summary', {})
        lines.append(f"\n## 总览")
        lines.append(f"| 总计 | 通过 | 提醒 | 问题 |")
        lines.append(f"|:---:|:---:|:---:|:---:|")
        lines.append(f"| {summary.get('total',0)} | {summary.get('passed',0)} | "
                     f"{summary.get('warned',0)} | {summary.get('failed',0)} |")
        
        lines.append(f"\n## 检查明细")
        for r in data.get('results', []):
            lines.append(f"\n### {r.get('description','')}")
            lines.append(f"- **状态**: {r.get('severity','')}")
            if r.get('details'):
                lines.append(f"- **详情**: {r['details']}")
            if r.get('recommendation'):
                lines.append(f"- **建议**: {r['recommendation']}")
        return "\n".join(lines)

    @staticmethod
    def to_html(data: dict) -> str:
        results = data.get('results', [])
        summary = data.get('summary', {})
        rows = ""
        for r in results:
            icon = "✅" if r["severity"] == "通过" else "⚠️" if r["severity"] in ("提示", "警告") else "❌"
            rows += f"""<tr>
                <td>{icon}</td>
                <td>{r['check_id']}</td>
                <td>{r['description']}</td>
                <td>{r['severity']}</td>
                <td>{r.get('recommendation','')}</td>
            </tr>\n"""
        
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8">
<title>{data.get('tool','合规检查报告')}</title>
<style>
body {{ font-family: -apple-system, sans-serif; max-width: 960px; margin: 2rem auto; padding: 0 1rem; }}
h1 {{ color: #1a1a2e; }}
.summary {{ display: flex; gap: 1rem; margin: 1rem 0; }}
.card {{ padding: 1rem 1.5rem; border-radius: 8px; background: #f5f5f5; text-align: center; }}
.card.pass {{ background: #d4edda; }} .card.warn {{ background: #fff3cd; }} .card.fail {{ background: #f8d7da; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; }}
th, td {{ padding: 0.5rem; text-align: left; border-bottom: 1px solid #ddd; }}
th {{ background: #e9ecef; }}
</style>
</head><body>
<h1>{data.get('tool','')}</h1>
<p><strong>法规：</strong>{data.get('regulation','')} | <strong>时间：</strong>{data.get('check_time','')[:19]}</p>
<div class="summary">
<div class="card"><strong>总计</strong><br>{summary.get('total',0)}</div>
<div class="card pass"><strong>✅ 通过</strong><br>{summary.get('passed',0)}</div>
<div class="card warn"><strong>⚠️ 提醒</strong><br>{summary.get('warned',0)}</div>
<div class="card fail"><strong>❌ 问题</strong><br>{summary.get('failed',0)}</div>
</div>
<table><thead><tr><th></th><th>编号</th><th>检查项</th><th>状态</th><th>建议</th></tr></thead>
<tbody>{rows}</tbody></table>
<p style="margin-top:2rem;color:#999;font-size:0.8em;">生成时间: {datetime.now().isoformat()[:19]}</p>
</body></html>"""

    @staticmethod
    def to_csv(data: dict) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["check_id", "description", "severity", "passed", "details", "recommendation", "regulation_ref"])
        for r in data.get('results', []):
            writer.writerow([
                r.get('check_id',''), r.get('description',''),
                r.get('severity',''), r.get('passed', False),
                r.get('details',''), r.get('recommendation',''),
                r.get('regulation_ref','')
            ])
        return output.getvalue()
