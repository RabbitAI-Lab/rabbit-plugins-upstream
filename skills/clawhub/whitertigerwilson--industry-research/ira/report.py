"""
report.py - 自动生成 HTML 研报

功能：
- 读取最近的归档（含 findings JSON）
- 调用 CLI 函数取最新数据（financial/technical/futures/chain/billboard）
- 渲染为单文件 HTML
"""

from __future__ import annotations
from pathlib import Path
from datetime import datetime
import json
import re


REPORT_DIR = Path.home() / ".openclaw" / "workspace" / "ira-new" / "industry-research" / "reports"


def _esc(text: str) -> str:
    """HTML 转义"""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def _format_findings(findings: dict) -> str:
    """把 findings dict 转 HTML"""
    if not isinstance(findings, dict):
        return "<p>无结构化数据</p>"

    rows = []
    def walk(prefix, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                walk(f"{prefix}.{k}" if prefix else k, v)
        elif isinstance(obj, list):
            rows.append(f"<li><b>{_esc(prefix)}</b> (list): {len(obj)} 项")
            for it in obj[:3]:
                walk(f"{prefix}[0]", it)
        else:
            rows.append(f"<li><b>{_esc(prefix)}</b>: {_esc(obj)}</li>")

    walk("", findings)
    return "<ul>" + "\n".join(rows) + "</ul>"


def generate_report(commodity: str, archive_file: Path = None) -> Path:
    """
    生成单个商品的 HTML 研报。
    """
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    # 找归档
    if archive_file is None:
        archive_dir = Path.home() / ".openclaw" / "workspace" / "memory" / "research_archive"
        today = datetime.now().strftime("%Y-%m-%d")
        archive_file = archive_dir / f"{today}_{commodity}.md"

    if not archive_file.exists():
        return None

    content = archive_file.read_text(encoding="utf-8")
    # 解析 front matter
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return None
    fm_str, body = parts[1], parts[2]

    summary = ""
    for line in body.split("\n"):
        if line.startswith(">") and "归档时间" not in line:
            summary = line.lstrip("> ").strip()
            break

    # 解析 findings JSON
    findings = {}
    in_json = False
    for line in body.split("\n"):
        if line.strip() == "```json":
            in_json = True
            json_buf = []
            continue
        if line.strip() == "```" and in_json:
            in_json = False
            try:
                findings = json.loads("\n".join(json_buf))
            except Exception:
                pass
            break
        if in_json:
            json_buf.append(line)

    # 调 CLI 取最新数据
    sections = []

    # 1. 期货价格
    try:
        from .futures import get_main_contract
        fut = get_main_contract(commodity, 30)
        if fut.get("latest_close"):
            change_color = "#ef4444" if (fut.get("change_pct_5d") or 0) < 0 else "#10b981"
            sections.append(f"""
            <section>
              <h2>一、价格走势</h2>
              <div class="kpi-grid">
                <div class="kpi"><div class="kpi-label">最新价</div><div class="kpi-value">{_esc(fut['latest_close'])}</div></div>
                <div class="kpi"><div class="kpi-label">日期</div><div class="kpi-value">{_esc(fut['latest_date'])}</div></div>
                <div class="kpi"><div class="kpi-label">5日累计</div><div class="kpi-value" style="color:{change_color}">{_esc(fut.get('change_pct_5d', '—'))}%</div></div>
              </div>
            </section>
            """)
    except Exception as e:
        sections.append(f"<section><h2>一、价格走势</h2><p>数据获取失败: {_esc(e)}</p></section>")

    # 2. 三级联动
    try:
        from .etf_chain import get_chain
        chain = get_chain(commodity)
        stock_html = "".join(
            f"<tr><td>{_esc(s['code'])}</td><td>{_esc(s['name'])}</td><td>{_esc(s['weight'])}</td></tr>"
            for s in chain.get("stocks", [])
        )
        etf_html = "".join(
            f"<tr><td>{_esc(e['code'])}</td><td>{_esc(e['name'])}</td>"
            f"<td>{_esc(e.get('最新价', '—'))}</td>"
            f"<td>{_esc(e.get('涨跌幅', '—'))}%</td>"
            f"<td>{_esc(e.get('logic', '—'))}</td></tr>"
            for e in chain.get("etfs", [])
        )
        sections.append(f"""
        <section>
          <h2>二、三级联动（商品 → 个股 → ETF）</h2>
          <h3>个股</h3>
          <table><thead><tr><th>代码</th><th>名称</th><th>主营</th></tr></thead><tbody>{stock_html}</tbody></table>
          <h3>ETF</h3>
          <table><thead><tr><th>代码</th><th>名称</th><th>最新</th><th>涨跌</th><th>匹配逻辑</th></tr></thead><tbody>{etf_html}</tbody></table>
        </section>
        """)
    except Exception as e:
        sections.append(f"<section><h2>二、三级联动</h2><p>失败: {_esc(e)}</p></section>")

    # 3. 主要公司财务 + 技术
    head_stock = None
    head_pe = findings.get("head_stock_financial", {}).get("pe")
    head_code = None
    if isinstance(findings, dict):
        # 从 stocks 列表找
        stocks = findings.get("stocks", [])
        if stocks and isinstance(stocks[0], dict):
            head_code = stocks[0]["code"]

    if head_code:
        try:
            from .financial import get_financial
            from .technical import analyze as tech
            from .anomaly import detect_volume_anomaly

            fin = get_financial(head_code)
            tech_data = tech(head_code, 60)
            anomaly_data = detect_volume_anomaly(head_code, 60)

            tech_html = ""
            if tech_data.get("macd") and not tech_data["macd"].get("error"):
                tech_html = f"""
                <table><thead><tr><th>指标</th><th>数值</th><th>状态</th></tr></thead><tbody>
                  <tr><td>MACD</td><td>{_esc(tech_data['macd']['latest'][0])}</td><td>—</td></tr>
                  <tr><td>RSI</td><td>{_esc(tech_data['rsi']['latest'])}</td><td>—</td></tr>
                </tbody></table>
                """

            anomaly_count = anomaly_data.get("anomaly_count", 0)
            sections.append(f"""
            <section>
              <h2>三、重点公司 {head_code}</h2>
              <div class="kpi-grid">
                <div class="kpi"><div class="kpi-label">价格</div><div class="kpi-value">{_esc(fin.get('price', '—'))}</div></div>
                <div class="kpi"><div class="kpi-label">PE</div><div class="kpi-value">{_esc(fin.get('pe_ttm', '—'))}</div></div>
                <div class="kpi"><div class="kpi-label">PB</div><div class="kpi-value">{_esc(fin.get('pb', '—'))}</div></div>
                <div class="kpi"><div class="kpi-label">市值(亿)</div><div class="kpi-value">{_esc(fin.get('market_cap_total_yi', '—'))}</div></div>
                <div class="kpi"><div class="kpi-label">换手率%</div><div class="kpi-value">{_esc(fin.get('turnover_pct', '—'))}</div></div>
                <div class="kpi"><div class="kpi-label">量价异动</div><div class="kpi-value">{anomaly_count}</div></div>
              </div>
              {tech_html}
            </section>
            """)
        except Exception as e:
            sections.append(f"<section><h2>三、重点公司</h2><p>失败: {_esc(e)}</p></section>")

    # 4. 关键 findings
    findings_html = _format_findings(findings)

    # 生成完整 HTML
    today_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{commodity} 研报 - {today_str}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; margin: 0; padding: 24px; background: #0f172a; color: #e2e8f0; }}
  h1 {{ color: #f8fafc; border-bottom: 2px solid #475569; padding-bottom: 12px; }}
  h2 {{ color: #38bdf8; margin-top: 32px; }}
  h3 {{ color: #94a3b8; }}
  section {{ background: #1e293b; padding: 24px; border-radius: 8px; margin: 16px 0; }}
  .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; margin: 16px 0; }}
  .kpi {{ background: #334155; padding: 16px; border-radius: 6px; text-align: center; }}
  .kpi-label {{ font-size: 12px; color: #94a3b8; margin-bottom: 8px; }}
  .kpi-value {{ font-size: 20px; font-weight: 600; color: #f8fafc; }}
  table {{ width: 100%; border-collapse: collapse; margin: 12px 0; }}
  th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #475569; }}
  th {{ background: #334155; color: #cbd5e1; }}
  td {{ color: #e2e8f0; }}
  ul {{ padding-left: 24px; }}
  li {{ margin: 4px 0; }}
  .meta {{ color: #94a3b8; font-size: 14px; }}
  .summary {{ background: #064e3b; padding: 16px; border-radius: 6px; border-left: 4px solid #10b981; margin: 16px 0; }}
  .disclaimer {{ margin-top: 32px; padding: 16px; background: #7c2d12; border-radius: 6px; border-left: 4px solid #f97316; font-size: 14px; }}
</style>
</head>
<body>
  <h1>{commodity} 行业研究报告</h1>
  <p class="meta">报告日期：{today_str} | 数据来源：CLI 自动化采集 + 公开资料</p>

  <div class="summary">
    <strong>一句话总结：</strong> {_esc(summary)}
  </div>

  {chr(10).join(sections)}

  <section>
    <h2>关键 findings</h2>
    {findings_html}
  </section>

  <div class="disclaimer">
    ⚠️ 以上内容仅供参考，不构成投资建议。数据来源于公开资料，部分为公司历史披露数据，请以公司公告为准。投资有风险，入市需谨慎。
  </div>
</body>
</html>
"""

    out_path = REPORT_DIR / f"{commodity}_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


def generate_all_reports():
    """为所有今日归档生成研报"""
    archive_dir = Path.home() / ".openclaw" / "workspace" / "memory" / "research_archive"
    today = datetime.now().strftime("%Y-%m-%d")

    if not archive_dir.exists():
        return []

    paths = []
    for md in sorted(archive_dir.glob(f"{today}_*.md"), reverse=True):
        # 抽取商品名
        # 文件名格式：2026-06-29_铜.md
        commodity = md.stem.replace(f"{today}_", "")
        out = generate_report(commodity, md)
        if out:
            paths.append(out)
    return paths