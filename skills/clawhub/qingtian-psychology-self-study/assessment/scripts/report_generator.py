#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 scoring_engine 的计分结果渲染成中文测评报告（HTML，自包含、含内联样式）。

用法：
    from report_generator import render, save
    html = render(scale, result)       # 返回 HTML 字符串
    path = save(scale, result)         # 保存到 reports/ 目录并返回路径

设计：单文件自包含 HTML（CSS 内联），可直接双击用浏览器打开，无需任何外部依赖。
"""

import json
import os
from datetime import datetime

DISCLAIMER = (
    "⚠️ 免责声明：本测评为基于标准量表的自评筛查工具，结果仅供参考，"
    "不构成任何医学或心理诊断，不能替代精神科医师或持证心理咨询师的当面评估。"
    "如你正经历明显心理困扰，或测评结果提示高风险，请尽快联系专业机构或当地心理援助热线。"
)

# 危机求助资源：单一数据源。首选从 resources/crisis-resources.md 解析（跨目录相对定位），
# 解析失败才回退以下内置常量（与单源文件保持同步）。修改热线请改 resources/crisis-resources.md。
CRISIS_INTRO = "如果你有伤害自己的念头，请立即寻求帮助："
CRISIS_HOTLINES = [
    ("全国统一心理援助热线", "12356"),
    ("北京心理危机研究与干预中心（24小时）", "010-82951332"),
    ("希望24热线（24小时）", "400-161-9995"),
]
CRISIS_EMERGENCY = "或直接前往最近医院急诊 / 拨打 120"

_CRISIS_FALLBACK = CRISIS_HOTLINES


def _load_crisis_hotlines():
    """从 resources/crisis-resources.md 解析热线（`- 名称：号码` 行），失败回退内置常量。"""
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        src = os.path.normpath(os.path.join(here, "..", "..", "resources", "crisis-resources.md"))
        with open(src, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        hotlines = []
        for ln in lines:
            ln = ln.strip()
            if not ln.startswith("- ") or "：" not in ln:
                continue
            name, _, num = ln[2:].partition("：")
            num = num.strip()
            if name and num and any(ch.isdigit() for ch in num):
                hotlines.append((name.strip(), num))
        if hotlines:
            return hotlines
    except Exception:
        pass
    return _CRISIS_FALLBACK

CRISIS_RESOURCES = (
    "🆘 **" + CRISIS_INTRO + "**\n"
    + "\n".join(f"- {label}：{num}" for label, num in CRISIS_HOTLINES)
    + f"\n- {CRISIS_EMERGENCY}\n"
)

# 分级 -> CSS 徽章类名 / 进度条配色
BAR_COLORS = {
    "low": "linear-gradient(90deg,#34d399,#16a34a)",
    "mid": "linear-gradient(90deg,#fbbf24,#f59e0b)",
    "high": "linear-gradient(90deg,#f87171,#ef4444)",
    "gray": "#9ca3af",
}

STYLE = """
:root{
  --bg:#eef1f8; --card:#ffffff; --ink:#1f2937; --muted:#6b7280;
  --brand:#6366f1; --brand2:#8b5cf6;
  --line:#eceef3;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{
  background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  line-height:1.75;-webkit-font-smoothing:antialiased;
}
.report{max-width:820px;margin:0 auto;padding:28px 18px 56px;}
.report-header{
  background:linear-gradient(135deg,#6366f1 0%,#8b5cf6 55%,#a855f7 100%);
  color:#fff;border-radius:20px;padding:30px 30px 26px;
  box-shadow:0 14px 36px rgba(99,102,241,.28);
}
.report-header h1{margin:0 0 8px;font-size:23px;font-weight:700;letter-spacing:.5px;}
.report-header .meta{font-size:13px;opacity:.85;}
.report-header .desc{margin-top:12px;font-size:14px;opacity:.96;}
.report-header .desc + .desc{margin-top:6px;}
.card{
  background:var(--card);border:1px solid var(--line);border-radius:18px;
  padding:22px 24px;margin-top:18px;box-shadow:0 6px 22px rgba(17,24,39,.05);
}
.card h2{margin:0 0 16px;font-size:18px;display:flex;align-items:center;gap:9px;font-weight:700;}
.card h2::before{content:"";width:5px;height:20px;border-radius:4px;
  background:linear-gradient(180deg,#6366f1,#8b5cf6);}
table{width:100%;border-collapse:collapse;border-radius:12px;overflow:hidden;}
thead th{background:#f5f6fb;color:var(--muted);font-weight:600;font-size:13px;
  text-align:left;padding:11px 14px;border-bottom:1px solid var(--line);}
tbody td{padding:11px 14px;font-size:14px;border-bottom:1px solid var(--line);}
tbody tr:last-child td{border-bottom:none;}
.badge{display:inline-block;padding:3px 13px;border-radius:999px;font-size:12.5px;
  font-weight:600;color:#fff;white-space:nowrap;}
.badge.low{background:linear-gradient(135deg,#34d399,#16a34a);}
.badge.mid{background:linear-gradient(135deg,#fbbf24,#f59e0b);}
.badge.high{background:linear-gradient(135deg,#f87171,#ef4444);}
.badge.gray{background:#9ca3af;}
.bar-row{margin:16px 0;}
.bar-label{display:flex;justify-content:space-between;align-items:baseline;
  font-size:14px;margin-bottom:7px;gap:12px;}
.bar-label .v{color:var(--muted);}
.bar-label strong{font-size:15px;color:var(--ink);}
.bar-track{height:13px;background:#eef1f6;border-radius:999px;overflow:hidden;}
.bar-fill{height:100%;border-radius:999px;transition:width 1.1s cubic-bezier(.22,1,.36,1);}
.note{font-size:12.5px;color:var(--muted);margin:12px 0 0;}
.interp{margin:14px 0;}
.interp p{margin:8px 0 0;font-size:14px;color:#374151;}
.interp .badge{margin-bottom:2px;}
.advice-block{margin:14px 0;padding:14px 16px;background:#f8f9fd;
  border:1px solid var(--line);border-radius:14px;}
.advice-title{font-weight:700;color:#4338ca;font-size:15px;margin-bottom:6px;}
.advice-block p{margin:0;font-size:14px;color:#374151;}
.advice-block .sub{font-size:13px;color:var(--muted);}
.tips{margin:8px 0 0;padding-left:20px;}
.tips li{margin:5px 0;font-size:14px;color:#374151;}
.warn{background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;
  border-radius:14px;padding:14px 16px;font-size:14px;margin-top:18px;}
.crisis{background:linear-gradient(135deg,#ef4444,#f97316);color:#fff;
  border-radius:18px;padding:22px 24px;margin-top:18px;
  box-shadow:0 12px 30px rgba(239,68,68,.3);}
.crisis h2{color:#fff;margin:0 0 10px;font-size:18px;display:flex;align-items:center;gap:8px;}
.crisis h2::before{background:#fff;}
.crisis ul{margin:8px 0 0;padding-left:20px;}
.crisis li{margin:5px 0;font-size:14px;}
.crisis-notes{margin-top:12px;font-size:13px;opacity:.95;}
.disclaimer{background:#fffaf0;border:1px solid #fde68a;color:#92400e;
  border-radius:14px;padding:16px 18px;font-size:13.5px;margin-top:18px;line-height:1.7;}
.disclaimer .source{margin-top:10px;font-size:12.5px;color:#b45309;opacity:.9;}
.foot{text-align:center;color:var(--muted);font-size:12px;margin-top:26px;}
@media (max-width:560px){
  .report{padding:16px 10px 40px;}
  .report-header{padding:22px 18px;}
  .card{padding:18px 16px;}
}
"""


def _esc(s):
    """HTML 转义，避免量表文本中的特殊字符破坏结构。"""
    if s is None:
        return ""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;"))


def _fmt(x):
    """整数值以整数形式显示，避免 4.0 之类的尾零。"""
    try:
        if float(x).is_integer():
            return str(int(float(x)))
    except (TypeError, ValueError):
        pass
    return str(x)


def _dim_max(scale, dim_name):
    """估算某维度的最大可能得分（用于可视化进度条）。"""
    dims = {d["name"]: d for d in scale.get("dimensions", [])}
    d = dims.get(dim_name)
    if not d:
        return None
    items_by_id = {it["id"]: it for it in scale["items"]}
    mx = []
    for iid in d["items"]:
        it = items_by_id.get(iid)
        if not it:
            continue
        scores = [o["score"] for o in it["options"]]
        if scores:
            mx.append(max(scores))
    if not mx:
        return None
    if d.get("method") == "average":
        return max(mx)
    return sum(mx)


def _band_class(level):
    """把分级文字映射为徽章/进度条配色类名。"""
    s = level or ""
    if s == "未分级":
        return "gray"
    if any(k in s for k in ("无", "正常", "低", "极轻", "良好", "健康")):
        return "low"
    if any(k in s for k in ("重", "高", "严重", "中重")):
        return "high"
    return "mid"


def _tier(level):
    """把分级文字映射为严重程度档位：0 低 / 1 中 / 2 高。"""
    s = level or ""
    if any(k in s for k in ("无", "正常", "低", "极轻", "良好", "健康")):
        return 0
    if any(k in s for k in ("重", "高", "严重", "中重")):
        return 2
    return 1


def _seek_threshold(scale, dim_name):
    """返回该维度「需要寻求专业帮助」的最低分数阈值及对应级别。

    取首个非低档 band 的 min，返回 (阈值, 级别)；无则 None。
    标注用「定义该阈值的 band 级别」，而非用户当前级别，避免误导。
    """
    bands = scale.get("interpretation", {}).get("bands", [])
    best = None
    for b in bands:
        if b.get("dimension") in (None, dim_name) and _tier(b.get("level", "")) > 0:
            if best is None or b["min"] < best[0]:
                best = (b["min"], b.get("level", ""))
    return best


def render(scale, result, include_disclaimer=True):
    """生成 HTML 报告字符串（自包含，含内联样式）。"""
    sname = scale.get("name", "")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    hotlines = _load_crisis_hotlines()  # 单源：resources/crisis-resources.md

    # 头部
    header = f"""
    <header class="report-header">
      <h1>{_esc(sname)} — 测评报告</h1>
      <div class="meta">生成时间：{now}</div>
      <div class="desc"><strong>量表简介：</strong>{_esc(scale.get('description', ''))}</div>
      <div class="desc"><strong>适用人群：</strong>{_esc(scale.get('target_population', '—'))}　|　<strong>预计用时：</strong>{_esc(scale.get('estimated_time', '—'))}</div>
    </header>"""

    # 危机资源（严格前置）
    crisis_html = ""
    if result.get("crisis_flag"):
        notes = result.get("crisis_notes", [])
        note_html = ""
        if notes:
            note_html = "<ul class='crisis-notes'>" + "".join(
                f"<li>⚑ {_esc(n)}</li>" for n in notes) + "</ul>"
        hotline_html = "".join(
            f"<li>{_esc(label)}：<strong>{_esc(num)}</strong></li>"
            for label, num in hotlines
        )
        crisis_html = f"""
    <section class="crisis">
      <h2>🆘 紧急求助资源</h2>
      <p>{_esc(CRISIS_INTRO)}请<strong>立即</strong>寻求帮助：</p>
      <ul>
        {hotline_html}
        <li>{_esc(CRISIS_EMERGENCY)}</li>
      </ul>
      {note_html}
    </section>"""

    # 缺失提示
    missing_html = ""
    if result.get("missing_items"):
        mids = result["missing_items"]
        missing_html = f"""
    <section class="warn">
      <strong>⚠️ 注意：</strong>有 {len(mids)} 道题未作答（{_esc('、'.join(mids))}），结果可能不准确，建议补全后重测。
    </section>"""

    # 一、得分概览
    std = result.get("standard_scores", {})
    sstd = scale.get("standard_score") or {}
    slope = float(sstd.get("slope", 1.0))
    intercept = float(sstd.get("intercept", 0.0))
    rows = []
    for dim, val in result["dimension_scores"].items():
        std_val = std.get(dim, "—")
        level = result["bands"].get(dim, "—")
        cls = _band_class(level)
        rows.append(f"""      <tr>
        <td>{_esc(dim)}</td>
        <td>{_fmt(val)}</td>
        <td>{_esc(std_val)}</td>
        <td><span class="badge {cls}">{_esc(level)}</span></td>
      </tr>""")
    std_note = ""
    if sstd:
        std_note = ('<p class="note">注：本量表按中国常模换算标准分'
                    f'（原始分 ×{_fmt(slope)}），最终分级以标准分为准。</p>')
    overview = f"""
    <section class="card">
      <h2>一、得分概览</h2>
      <table>
        <thead><tr><th>维度</th><th>原始分</th><th>标准分</th><th>分级</th></tr></thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>
      {std_note}
    </section>"""

    # 分数可视化（CSS 进度条）
    bars = []
    for dim, val in result["dimension_scores"].items():
        if dim in std:
            v = std[dim]
            raw_max = _dim_max(scale, dim)
            vmax = raw_max * slope + intercept if raw_max is not None else None
            unit = "（标准分）"
        else:
            v = val
            vmax = _dim_max(scale, dim)
            unit = ""
        level = result["bands"].get(dim, "—")
        cls = _band_class(level)
        pct = 0
        if vmax and vmax > 0:
            pct = max(0, min(100, int(round(float(v) / float(vmax) * 100))))
        color = BAR_COLORS.get(cls, "#9ca3af")
        bars.append(f"""      <div class="bar-row">
        <div class="bar-label"><span>{_esc(dim)}</span><span class="v"><strong>{_fmt(v)}</strong>{unit} / {_fmt(vmax)}　·　{_esc(level)}</span></div>
        <div class="bar-track"><div class="bar-fill" style="width:{pct}%;background:{color}"></div></div>
      </div>""")
    viz = f"""
    <section class="card">
      <h2>分数可视化</h2>
{chr(10).join(bars)}
    </section>"""

    # 二、结果解读
    bands = scale.get("interpretation", {}).get("bands", [])
    shown = set()
    blocks = []
    for dim, level in result["bands"].items():
        key = (dim, level)
        if key in shown:
            continue
        shown.add(key)
        for b in bands:
            if b.get("dimension") in (None, dim) and b.get("level") == level:
                cls = _band_class(level)
                summary = b.get("summary", "")
                blocks.append(f"""      <div class="interp">
        <span class="badge {cls}">{_esc(dim)}：{_esc(level)}</span>
        <p>{_esc(summary)}</p>
      </div>""")
                break
    interp = f"""
    <section class="card">
      <h2>二、结果解读</h2>
{chr(10).join(blocks)}
    </section>"""

    # 三、行动建议（分层）
    overall = max((_tier(lv) for lv in result["bands"].values()), default=0)
    if overall == 0:
        immediate = "当前状态平稳，维持现有的生活节奏与社交连接即可，无需特别干预；继续保持规律作息。"
    elif overall == 1:
        immediate = "处于轻到中度区间，建议先自我调节并观察约 2 周；若没有改善或持续加重，考虑预约一次专业心理评估。"
    else:
        immediate = "结果提示较高风险，建议尽快到精神科或心理科就诊，不要独自硬扛；如有自伤念头请立即拨打危机热线（见上方资源）。"
    tips = (
        "保持规律作息与充足睡眠，尽量固定入睡与起床时间",
        "每天进行适度身体活动（如快走 20–30 分钟）",
        "维持与亲友的社交连接，避免长期独处孤立",
        "减少酒精、咖啡因摄入，尤其晚间",
        "尝试正念呼吸、冥想或放松训练，帮助情绪回落",
    )
    tips_html = "".join(f"<li>{_esc(t)}</li>" for t in tips)
    seek_parts = []
    for dim, level in result["bands"].items():
        if _tier(level) == 0:
            continue
        tl = _seek_threshold(scale, dim)
        if not tl:
            continue
        thr, thr_level = tl
        unit = "（标准分）" if dim in std else ""
        seek_parts.append(f"「{_esc(dim)}」达到 {thr}{unit} 即进入「{_esc(thr_level)}」级")
    if seek_parts:
        seek = "当以下情况出现时，建议尽快寻求精神科/心理科专业帮助：" + "；".join(seek_parts) + "。"
    else:
        seek = "若情绪或状态持续困扰你、明显影响工作与生活，建议预约一次专业评估。"
    seek += "若出现持续两周以上的显著情绪低落/焦虑、食欲或睡眠明显紊乱、或出现自伤念头，请立即就医或拨打危机热线。"
    advice = f"""
    <section class="card">
      <h2>三、行动建议</h2>
      <div class="advice-block">
        <div class="advice-title">① 立即行动</div>
        <p>{_esc(immediate)}</p>
      </div>
      <div class="advice-block">
        <div class="advice-title">② 日常调节</div>
        <p class="sub">以下方式仅供参考，非治疗，不能替代专业帮助：</p>
        <ul class="tips">{tips_html}</ul>
      </div>
      <div class="advice-block">
        <div class="advice-title">③ 何时就医</div>
        <p>{_esc(seek)}</p>
      </div>
    </section>"""

    # 四、重要声明
    disclaimer_html = ""
    if include_disclaimer:
        disclaimer_html = f"""
    <section class="disclaimer">
      {_esc(DISCLAIMER)}
      <div class="source">量表来源：{_esc(scale.get('source', '—'))}　|　授权：{_esc(scale.get('license', '—'))}</div>
    </section>"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{_esc(sname)} 测评报告</title>
<style>{STYLE}</style>
</head>
<body>
<main class="report">
{header}
{crisis_html}
{missing_html}
{overview}
{viz}
{interp}
{advice}
{disclaimer_html}
  <footer class="foot">本报告由心理量表测评助手生成 · 自评筛查结果仅供参考，不替代专业评估<br>如需保存为 PDF：浏览器打开本报告后按 Ctrl+P（Mac 为 ⌘+P），选择「另存为 PDF」即可</footer>
</main>
</body>
</html>"""
    return html


def save(scale, result, out_dir="reports"):
    os.makedirs(out_dir, exist_ok=True)
    html = render(scale, result)
    fname = f"{scale['id']}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    path = os.path.join(out_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


if __name__ == "__main__":
    # 简易自测：python report_generator.py <scale_id> <answers_json>
    import sys
    if len(sys.argv) < 3:
        print("Usage: python report_generator.py <scale_id> <answers_json_file>")
        sys.exit(1)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from scoring_engine import load_scale, score
    sc = load_scale(sys.argv[1])
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        ans = json.load(f)
    res = score(sc, ans)
    out = save(sc, res)
    print(f"HTML 报告已保存：{out}")
