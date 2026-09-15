#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成一日「涨停板龙虎榜深度研判」三件套（HTML + PDF + PPTX）。

工作流：
    1. 载入候选数据 JSON
    2. 跑四层漏斗（L1→L2→L2.5→L3）+ 评分管道 → 产信号行
    3. 渲染数据驱动的 HTML（基于 templates/report_template.html 头）
    4. 用 Playwright 把 HTML 渲成 PDF
    5. 复用 templates/make_pptx.py 产出 PPTX（v1.1 仍含硬编码示例数据，
       全数据驱动重写列入 v2.0 roadmap —— 见 docs/wealth-password-strategy.md）

用法：
    python3 scripts/generate_daily.py
    python3 scripts/generate_daily.py --data strategy/sample_data.json --date 2026-09-11
    python3 scripts/generate_daily.py --data strategy/sample_data.json --out out/20260911
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import sys
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from strategy import calibers as C          # noqa: E402
from strategy import formulas as F          # noqa: E402
from strategy import funnel as FN           # noqa: E402
from strategy import pipeline as PL         # noqa: E402
from strategy import playbook as PB         # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATES = REPO / "templates"
ASSETS = REPO / "assets"
ECHARTS_PATH = ASSETS / "echarts.min.js"


def load_data(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        sys.exit(f"[!] 数据文件不存在：{path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"[!] JSON 解析失败 {path}: {e}")


def render_html(data: dict, date: str, out_path: pathlib.Path) -> None:
    """生成数据驱动的 HTML（含 funnel + signal 表）。"""
    inds, stocks = _build_inputs(data)

    fr = FN.run_funnel(inds, stocks)
    funnel_pass = [s.merged for s in fr.l3_pass] or data.get("candidates", [])
    ctx = data.get("context", {}) or {}
    equity = float(ctx.get("equity", 1_000_000))
    stage = (ctx.get("stage", "II")).upper()
    ice = F.is_ice_point(int(ctx.get("limit_up_count", 60)), float(ctx.get("broken_rate", 0.2)),
                         float(ctx.get("index_pct", 0))) if ctx else False
    result = PL.run_pipeline(funnel_pass, equity=equity, stage=stage, ice_point=ice)

    rows_html = _render_signal_rows(result["rows"])
    funnel_html = _render_funnel_section(fr, inds)
    caliber_html = (
        "<pre>" + C.describe().replace("<", "&lt;").replace(">", "&gt;") + "</pre>"
    )

    body = f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="UTF-8">
<title>涨停板龙虎榜深度研判报告-{date}</title>
<style>
body{{font-family:"PingFang SC","Microsoft YaHei",sans-serif;max-width:980px;margin:24px auto;color:#12181F;line-height:1.65}}
h1{{color:#002B5C;border-bottom:3px solid #C5A572;padding-bottom:8px}}
h2{{color:#002B5C;margin-top:32px;border-left:4px solid #C5A572;padding-left:10px}}
pre{{background:#F6F8FA;padding:12px;border-left:3px solid #C5A572;overflow:auto}}
table{{border-collapse:collapse;width:100%;margin:12px 0;font-size:13px}}
th,td{{border:1px solid #DDE3EA;padding:6px 10px;text-align:left}}
th{{background:#0A3D6E;color:#fff;font-weight:600}}
tr:nth-child(even){{background:#F6F8FA}}
.ok{{color:#1E8449;font-weight:600}}
.no{{color:#C1272D;font-weight:600}}
.callout{{background:#FDF3F3;border-left:4px solid #C1272D;padding:10px 14px;margin:12px 0}}
.muted{{color:#6B7785;font-size:12px}}
</style>
</head><body>
<h1>涨停板龙虎榜深度研判报告 · {date}</h1>
<p class="muted">口径版本 <b>{C.CALIBER_VERSION}</b> · 框架：L1→L2→L2.5→L3 四层漏斗 + 财富密码选股策略</p>

<h2>0. 本报告口径（v2 永久生效）</h2>
{caliber_html}

<h2>1. 四层漏斗执行结果</h2>
{funnel_html}

<h2>2. 评分管道 · 风控信号表</h2>
{rows_html}

<h2>3. α 账本</h2>
<p class="muted">阶段 <b>{result['ledger']['stage']}</b> · α_max <b>{result['ledger']['alpha_budget']:.1%}</b> ·
已用 <b>{result['ledger']['used_pct']:.2%}</b> · 剩余 <b>{result['ledger']['remaining']:,.0f}</b> 元 ·
持仓 <b>{result['ledger']['positions']}</b> 笔</p>

<h2>4. 盘前 6 项检查</h2>
{PB.render_checklist_md().replace("<table>", '<table><thead>').replace("</table>", "</thead></table>").replace("<tr>", "<tr><th>#</th><th>检查项</th><th>做法</th><th>产出</th></tr>", 1).replace("<th>", "<th>")}

<h2>5. 免责声明</h2>
<p class="callout">{PB.playbook()['disclaimer']}</p>

<p class="muted">由 <code>scripts/generate_daily.py</code> 自动生成 · {dt.datetime.now().isoformat(timespec='seconds')}</p>
</body></html>"""

    # 注入 echarts（即使本报告未用图，也保留占位以兼容模板样式）
    body = body.replace("/*__ECHARTS__*/", "")  # 本数据驱动版未含图表
    out_path.write_text(body, encoding="utf-8")
    print(f"[1] HTML 已写出: {out_path} ({out_path.stat().st_size/1024:.1f} KB)")


def _build_inputs(data: dict) -> tuple[list, list]:
    inds = [FN.Industry(i["code"], i["name"], float(i["rank"]), float(i["vr"]),
                        float(i.get("dispersion", 0.0)), i.get("note", ""))
            for i in data.get("industries", [])]
    stocks = []
    for c in data.get("candidates", []):
        raw = {k: v for k, v in c.items()
               if k not in ("code", "name", "sector", "rank", "vr", "note")}
        stocks.append(FN.Stock(c["code"], c["name"], c.get("sector", ""),
                               float(c["rank"]) if c.get("rank") is not None else None,
                               float(c["vr"]) if c.get("vr") is not None else None,
                               raw))
    return inds, stocks


def _render_funnel_section(fr: Any, inds: list) -> str:
    parts = ["<table><tr><th>层</th><th>标的/行业</th><th>分位</th><th>额比</th><th>结果</th></tr>"]
    for ind in inds:
        passed = (ind.rank <= C.RANK_LOW_THRESHOLD and ind.vr >= C.VR_THRESHOLD)
        parts.append(
            f"<tr><td>L1 行业</td><td>{ind.name}</td><td>{ind.rank:.1f}%</td><td>{ind.vr:.2f}×</td>"
            f"<td class='{'ok' if passed else 'no'}'>{'入池' if passed else '未入池'}</td></tr>"
        )
    for s in fr.l2_pass:
        parts.append(
            f"<tr><td>L2 个股</td><td>{s.name}</td><td>{s.rank:.1f}%</td><td>{s.vr:.2f}×</td>"
            f"<td class='ok'>入池</td></tr>"
        )
    for g in fr.l2_5_removed:
        parts.append(
            f"<tr><td>L2.5 可交易</td><td>{g.name}</td><td>—</td><td>—</td>"
            f"<td class='no'>{g.reasons[0]}</td></tr>"
        )
    for g in fr.l3_vetoed:
        parts.append(
            f"<tr><td>L3 基本面</td><td>{g.name}</td><td>—</td><td>—</td>"
            f"<td class='no'>{g.reasons[0]}</td></tr>"
        )
    for s in fr.l3_pass:
        parts.append(
            f"<tr><td><b>最终</b></td><td><b>{s.name}</b></td><td>—</td><td>—</td>"
            f"<td class='ok'><b>通过</b></td></tr>"
        )
    parts.append("</table>")
    sens = fr.sensitivity
    parts.append(
        f"<p class='callout'>敏感度：50% 相对线（默认）→ <b>{sens['rule_50pct_relative']}</b> 只过会；"
        f"任何减速即排除 → <b>{sens['rule_any_deceleration']}</b> 只过会；"
        f"±{abs(sens['rule_50pct_relative']-sens['rule_any_deceleration'])} 只</p>"
    )
    return "\n".join(parts)


def _render_signal_rows(rows) -> str:
    parts = [
        "<table><tr><th>代码</th><th>名称</th><th>综合分</th><th>动作</th><th>股数</th><th>名义</th><th>说明</th></tr>"
    ]
    for r in rows:
        note = r.blocked_by or ("；".join(r.notes)[:140] if r.notes else "—")
        parts.append(
            f"<tr><td>{r.code}</td><td>{r.name}</td><td>{r.score:.1f}</td>"
            f"<td>{r.action}</td><td>{r.shares or '—'}</td><td>{r.notional or '—'}</td>"
            f"<td>{note}</td></tr>"
        )
    parts.append("</table>")
    return "\n".join(parts)


def render_pdf(html_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--allow-file-access-from-files"])
        page = browser.new_page(viewport={"width": 980, "height": 1400})
        page.emulate_media(media="print")
        page.goto(html_path.as_uri(), wait_until="load", timeout=120_000)
        page.wait_for_timeout(1200)
        page.pdf(
            path=str(pdf_path), format="A4",
            print_background=True, prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
    print(f"[2] PDF  已写出: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)")


def render_pptx(html_dir: pathlib.Path, date: str) -> pathlib.Path:
    """复用 templates/make_pptx.py（通过环境变量切换输出路径）。

    v1.1 限制：PPTX 内容仍使用 make_pptx.py 内硬编码的 2026-09-11 数据。
    v2.0 roadmap：将 make_pptx.py 重构为接受 data dict 的函数式 API。
    """
    import subprocess
    base = f"涨停板龙虎榜深度研判报告-{date}"
    out_html = html_dir / f"{base}.html"
    pptx_path = html_dir / f"{base}.pptx"
    env = os.environ.copy()
    env["POUT"] = str(html_dir)
    env["PFILE"] = f"{base}.pptx"
    # make_pptx 期望从 templates/ 目录运行
    cmd = [sys.executable, str(TEMPLATES / "make_pptx.py")]
    # 把 HTML 临时放到 templates/ 下（make_pptx 不读 HTML，但需要目录存在以导入样式）
    print(f"[3] 调用 make_pptx.py 生成 PPTX（v1.1 仍含 2026-09-11 硬编码示例）...")
    res = subprocess.run(cmd, cwd=str(TEMPLATES), env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[!] make_pptx 失败:\n{res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)
    # 默认输出到 templates/，移到目标目录
    default_pptx = TEMPLATES / "涨停板龙虎榜深度研判报告-20260911.pptx"
    if default_pptx.exists():
        default_pptx.rename(pptx_path)
    print(f"[3] PPTX 已写出: {pptx_path} ({pptx_path.stat().st_size/1024:.1f} KB)")
    return pptx_path


def main() -> int:
    ap = argparse.ArgumentParser(description="生成一日龙虎榜报告三件套")
    ap.add_argument("--data", default=str(REPO / "strategy" / "sample_data.json"))
    ap.add_argument("--date", default=dt.date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--out", default=None, help="输出目录（默认 out/dragon-tiger-YYYYMMDD）")
    args = ap.parse_args()

    date_compact = args.date.replace("-", "")
    out_dir = pathlib.Path(args.out) if args.out else REPO / "out" / f"dragon-tiger-{date_compact}"
    out_dir = out_dir.expanduser().resolve()   # 必须转绝对路径：subprocess 用 cwd=TEMPLATES
    out_dir.mkdir(parents=True, exist_ok=True)
    base = f"涨停板龙虎榜深度研判报告-{date_compact}"

    print("=" * 60)
    print(f" A股龙虎榜深度研判 · {args.date} · 口径 {C.CALIBER_VERSION}")
    print("=" * 60)

    data = load_data(pathlib.Path(args.data))
    html_path = out_dir / f"{base}.html"
    pdf_path = out_dir / f"{base}.pdf"
    pptx_path = render_pptx(out_dir, date_compact)  # 先做 PPTX（避免 HTML 触发 Playwright 期间 UI 阻塞）

    render_html(data, args.date, html_path)
    render_pdf(html_path, pdf_path)

    print("\n" + "=" * 60)
    print(f" 三件套已生成于: {out_dir}")
    for f in (html_path, pdf_path, pptx_path):
        if f.exists():
            print(f"  · {f.name} ({f.stat().st_size/1024:.1f} KB)")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())