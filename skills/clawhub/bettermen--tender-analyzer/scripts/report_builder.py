#!/usr/bin/env python3
"""
Report Builder — 交互式HTML分析报告组装器
将各阶段分析结果组装为完整HTML报告
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional

CST = timezone(timedelta(hours=8))


def build_html_report(
    project_info: dict,
    requirements: list[dict],
    mece_analysis: Optional[dict] = None,
    expert_review: Optional[dict] = None,
    version_history: Optional[list[dict]] = None,
    revisions: Optional[list[dict]] = None,
    risks: Optional[list[dict]] = None,
) -> str:
    """
    组装完整的HTML交互式报告

    Args:
        project_info: 项目基本信息
        requirements: 需求清单
        mece_analysis: MECE分析结果
        expert_review: 评审模拟结果
        version_history: 版本历史
        revisions: 修订记录
        risks: 风险清单

    Returns:
        完整HTML字符串
    """
    template_path = Path(__file__).parent.parent / "assets" / "report_template.html"
    if template_path.exists():
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()
    else:
        template = _get_minimal_template()

    # 生成各模块HTML
    overview_html = _build_overview(project_info)
    requirements_html = _build_requirements_table(requirements)

    mece_html = ""
    if mece_analysis:
        mece_html = _build_mece_section(mece_analysis)

    review_html = ""
    if expert_review:
        review_html = _build_review_section(expert_review)

    revision_html = ""
    if revisions:
        revision_html = _build_revision_section(revisions)

    version_html = ""
    if version_history:
        version_html = _build_version_section(version_history)

    risk_html = _build_risk_section(risks or [])

    # 填充模板
    html = template.replace("{{PROJECT_NAME}}", project_info.get("project_name", "投标分析报告"))
    html = html.replace("{{REPORT_DATE}}", datetime.now(CST).strftime("%Y-%m-%d %H:%M"))
    html = html.replace("{{OVERVIEW_SECTION}}", overview_html)
    html = html.replace("{{REQUIREMENTS_SECTION}}", requirements_html)
    html = html.replace("{{MECE_SECTION}}", mece_html)
    html = html.replace("{{REVIEW_SECTION}}", review_html)
    html = html.replace("{{REVISION_SECTION}}", revision_html)
    html = html.replace("{{VERSION_SECTION}}", version_html)
    html = html.replace("{{RISK_SECTION}}", risk_html)

    return html


def _build_overview(info: dict) -> str:
    """构建项目概览卡片"""
    items = [
        ("项目名称", info.get("project_name", "未提取")),
        ("项目编号", info.get("project_number", "未提取")),
        ("预算金额", info.get("budget", "未提取")),
        ("招标人", info.get("bidder", "未提取")),
        ("投标截止", info.get("bid_deadline", "未提取")),
    ]
    cards = "".join(
        f'<div class="info-card"><span class="info-label">{label}</span><span class="info-value">{value}</span></div>'
        for label, value in items
    )
    return f'<div class="section"><h2>项目概览</h2><div class="info-grid">{cards}</div></div>'


def _build_requirements_table(requirements: list[dict]) -> str:
    """构建需求清单表格"""
    if not requirements:
        return '<div class="section"><h2>需求清单</h2><p>暂未提取需求</p></div>'

    rows = ""
    for req in requirements:
        mandatory_icon = "★" if req.get("mandatory") else ""
        risk_class = f"risk-{req.get('risk_level', 'low')}"
        rows += f"""
        <tr class="{risk_class}">
            <td>{req.get('id', '')}</td>
            <td>{req.get('category', '')}</td>
            <td>{mandatory_icon}{req.get('content', '')}</td>
            <td>{req.get('weight', '-')}</td>
            <td>{req.get('source_page', '-')}</td>
        </tr>"""

    return f"""
    <div class="section">
        <h2>结构化需求清单</h2>
        <div class="table-container">
            <table class="data-table">
                <thead><tr><th>ID</th><th>类别</th><th>需求内容</th><th>分值</th><th>来源页</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    </div>"""


def _build_mece_section(mece: dict) -> str:
    """构建MECE分析模块"""
    stats = mece.get("dimension_stats", {})
    dim_cards = ""
    for dim_name, dim_info in stats.items():
        dim_cards += f"""
        <div class="mece-dim-card">
            <h3>{dim_name} ({dim_info['count']}项, {dim_info['percentage']}%)</h3>
            <div class="progress-bar"><div class="progress-fill" style="width:{dim_info['weight_percentage']}%"></div></div>
            <span class="dim-weight">权重占比: {dim_info['weight_percentage']}%</span>
            <span class="dim-mandatory">实质性条款: {dim_info['mandatory_count']}条</span>
        </div>"""

    # 隐含需求
    implicit_items = ""
    for imp in mece.get("implicit_requirements", []):
        implicit_items += f'<li><strong>{imp["id"]}</strong>: {imp["description"]} [{imp["dimension"]}]</li>'

    return f"""
    <div class="section">
        <h2>MECE多维分析</h2>
        <div class="mece-grid">{dim_cards}</div>
        <h3>隐含需求识别</h3>
        <ul>{implicit_items or '<li>未发现隐含需求</li>'}</ul>
    </div>"""


def _build_review_section(review: dict) -> str:
    """构建评审模拟模块"""
    score = review.get("overall_score", 0)
    rating = review.get("rating", "")
    score_color = "#10B981" if score >= 85 else "#F59E0B" if score >= 65 else "#EF4444"

    # 角色评分
    expert_scores = ""
    for rev in review.get("expert_reviews", []):
        score_pct = round(rev["total_score"] / rev["total_max"] * 100, 1)
        expert_scores += f"""
        <div class="expert-card">
            <h4>{rev['expert_name']} (权重{int(rev['role_weight']*100)}%)</h4>
            <div class="expert-score" style="color:{score_color}">{score_pct}分</div>
        </div>"""

    # 扣分明细
    ded_rows = ""
    for i, ded in enumerate(review.get("deductions", [])[:10]):
        ded_rows += f"""
        <tr>
            <td>{i+1}</td>
            <td>{ded['expert']}</td>
            <td>{ded['req_id']}</td>
            <td>{ded['content'][:60]}</td>
            <td class="deduction">-{ded['deduction']}分</td>
            <td>{ded['reason']}</td>
        </tr>"""

    return f"""
    <div class="section">
        <h2>评审模拟结果</h2>
        <div class="score-card">
            <div class="total-score" style="color:{score_color}">{score}<span>分</span></div>
            <div class="rating">{rating}</div>
        </div>
        <div class="expert-grid">{expert_scores}</div>
        <h3>扣分明细</h3>
        <div class="table-container">
            <table class="data-table">
                <thead><tr><th>#</th><th>专家</th><th>需求ID</th><th>内容</th><th>扣分</th><th>原因</th></tr></thead>
                <tbody>{ded_rows or '<tr><td colspan="6">无扣分项</td></tr>'}</tbody>
            </table>
        </div>
    </div>"""


def _build_revision_section(revisions: list[dict]) -> str:
    """构建修订记录模块"""
    rev_items = ""
    for rev in revisions:
        rev_type_emoji = {"add": "➕", "fix": "🔧", "remove": "🗑️", "enhance": "📝"}
        emoji = rev_type_emoji.get(rev.get("type", ""), "📌")
        rev_items += f"""
        <div class="revision-item">
            <div class="rev-header">{emoji} [{rev.get('type', '')}] {rev.get('target_req', '')} @ {rev.get('location', '')}</div>
            <div class="rev-rationale">{rev.get('rationale', '')}</div>
        </div>"""

    return f"""
    <div class="section">
        <h2>修订记录</h2>
        <div class="revision-list">{rev_items or '<p>暂无修订记录</p>'}</div>
    </div>"""


def _build_version_section(versions: list[dict]) -> str:
    """构建版本历史模块"""
    ver_items = ""
    for v in versions:
        score_str = f" | 评分: {v['score']}" if v.get("score") else ""
        ver_items += f"""
        <div class="version-item">
            <div class="ver-badge">{v['version']}</div>
            <div class="ver-info">
                <span>{v['timestamp'][:16]}{score_str}</span>
                <span>← {v.get('parent', 'root')}</span>
            </div>
        </div>"""

    return f"""
    <div class="section">
        <h2>版本演化</h2>
        <div class="version-timeline">{ver_items or '<p>暂无版本记录</p>'}</div>
    </div>"""


def _build_risk_section(risks: list[dict]) -> str:
    """构建风险清单"""
    if not risks:
        return '<div class="section"><h2>风险清单</h2><p>未识别重大风险</p></div>'

    risk_items = ""
    level_emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}

    for r in risks:
        emoji = level_emoji.get(r.get("level", "low"), "⚪")
        risk_items += f"""
        <div class="risk-item">
            <span class="risk-level">{emoji}</span>
            <span class="risk-desc">{r.get('description', '')}</span>
            <span class="risk-impact">影响: {r.get('impact', '未知')}</span>
        </div>"""

    return f"""
    <div class="section">
        <h2>风险清单</h2>
        <div class="risk-list">{risk_items}</div>
    </div>"""


def _get_minimal_template() -> str:
    """获取最小化HTML模板"""
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{PROJECT_NAME}} — 投标分析报告</title>
<style>
:root { --primary: #2563EB; --secondary: #7C3AED; --success: #10B981; --warning: #F59E0B; --danger: #EF4444;
  --bg: #F8FAFC; --card-bg: #FFFFFF; --text: #1E293B; --text-secondary: #64748B; --border: #E2E8F0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px; }
.header { text-align: center; padding: 40px 20px; background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; border-radius: 12px; margin-bottom: 24px; }
.header h1 { font-size: 2em; margin-bottom: 8px; }
.section { background: var(--card-bg); border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.section h2 { color: var(--primary); margin-bottom: 16px; font-size: 1.4em; border-bottom: 2px solid var(--border); padding-bottom: 8px; }
.info-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.info-card { background: var(--bg); padding: 12px 16px; border-radius: 8px; border-left: 4px solid var(--primary); }
.info-label { display: block; font-size: 0.85em; color: var(--text-secondary); }
.info-value { display: block; font-weight: 600; margin-top: 4px; }
.table-container { overflow-x: auto; }
.data-table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
.data-table th { background: var(--primary); color: white; padding: 10px 12px; text-align: left; }
.data-table td { padding: 8px 12px; border-bottom: 1px solid var(--border); }
.data-table tr:hover { background: #F1F5F9; }
.risk-critical { background: #FEE2E2; }
.risk-high { background: #FEF3C7; }
.score-card { text-align: center; padding: 30px; }
.total-score { font-size: 4em; font-weight: 800; }
.total-score span { font-size: 0.4em; }
.rating { font-size: 1.4em; margin-top: 8px; }
.expert-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; margin: 16px 0; }
.expert-card { background: var(--bg); padding: 16px; border-radius: 8px; text-align: center; }
.expert-score { font-size: 1.8em; font-weight: 700; }
.deduction { color: var(--danger); font-weight: 700; }
.mece-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; margin: 16px 0; }
.mece-dim-card { background: var(--bg); padding: 16px; border-radius: 8px; }
.progress-bar { height: 6px; background: var(--border); border-radius: 3px; margin: 8px 0; }
.progress-fill { height: 100%; background: var(--primary); border-radius: 3px; }
.dim-weight, .dim-mandatory { display: block; font-size: 0.85em; color: var(--text-secondary); }
.version-timeline { border-left: 3px solid var(--primary); padding-left: 20px; margin: 16px 0; }
.version-item { margin: 12px 0; position: relative; }
.ver-badge { display: inline-block; background: var(--primary); color: white; padding: 2px 10px; border-radius: 12px; font-size: 0.85em; font-weight: 600; }
.ver-info { display: block; font-size: 0.85em; color: var(--text-secondary); margin-top: 4px; }
.revision-item { background: var(--bg); padding: 12px; border-radius: 8px; margin: 8px 0; border-left: 4px solid var(--secondary); }
.risk-item { display: flex; gap: 12px; align-items: center; padding: 8px 0; border-bottom: 1px solid var(--border); }
@media (max-width: 768px) { .container { padding: 10px; } .info-grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
<div class="container">
<div class="header"><h1>{{PROJECT_NAME}}</h1><p>生成时间: {{REPORT_DATE}}</p></div>
{{OVERVIEW_SECTION}}
{{REQUIREMENTS_SECTION}}
{{MECE_SECTION}}
{{REVIEW_SECTION}}
{{REVISION_SECTION}}
{{VERSION_SECTION}}
{{RISK_SECTION}}
</div>
</body>
</html>"""
