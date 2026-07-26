#!/usr/bin/env python3
"""
科研助理报告生成器
将分析结果JSON转换为交互式HTML可视化报告
用法: python generate_report.py --data '<json_string>' --output <output_path>
"""

import argparse
import json
import os
import sys
from datetime import datetime
from html import escape


# ============ 模块中文名映射 ============
MODULE_NAMES = {
    "literature_search": {"icon": "🔍", "name": "文献检索与发现"},
    "literature_reading": {"icon": "📖", "name": "文献阅读与理解"},
    "literature_review": {"icon": "📝", "name": "文献综述"},
    "research_topic": {"icon": "💡", "name": "研究选题与创新"},
    "research_design": {"icon": "🧪", "name": "研究设计与方法"},
    "data_analysis": {"icon": "📊", "name": "数据采集与分析"},
    "paper_writing": {"icon": "✍️", "name": "论文写作辅助"},
    "paper_polish": {"icon": "🔧", "name": "润色与校对"},
    "citation_mgmt": {"icon": "📎", "name": "引用管理"},
    "journal_select": {"icon": "🎯", "name": "投稿选刊"},
    "grant_writing": {"icon": "💰", "name": "基金申请"},
    "presentation": {"icon": "🎤", "name": "学术汇报"},
}


def score_color(score):
    if score >= 4:
        return "#52c41a"
    elif score >= 3:
        return "#faad14"
    elif score >= 2:
        return "#fa8c16"
    else:
        return "#f5222d"


def score_label(score):
    if score >= 4.5:
        return "优秀"
    elif score >= 3.5:
        return "良好"
    elif score >= 2.5:
        return "一般"
    elif score >= 1.5:
        return "较差"
    else:
        return "很差"


def build_chart_js():
    """返回 Chart.js CDN"""
    return '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>'


def make_tabs(modules):
    """生成模块Tab导航"""
    tabs_html = ""
    for i, m in enumerate(modules):
        info = MODULE_NAMES.get(m, {"icon": "📋", "name": m})
        active = "active" if i == 0 else ""
        tabs_html += f'<button class="tab-btn {active}" onclick="switchTab(\'{m}\')">{info["icon"]} {info["name"]}</button>'
    return tabs_html


def make_module_content(data, modules):
    """生成所有模块内容"""
    all_html = ""
    for i, m in enumerate(modules):
        module_data = data.get(m, {})
        active = "active" if i == 0 else ""
        content = render_module(m, module_data)
        all_html += f'<div id="tab-{m}" class="tab-content {active}">{content}</div>'
    return all_html


def render_module(mod, data):
    """渲染单个模块的HTML内容"""
    if not data:
        return '<div class="empty-state">📭 此模块暂无数据</div>'

    html = ""
    title = data.get("title", MODULE_NAMES.get(mod, {}).get("name", mod))

    if mod == "literature_search":
        html = render_literature_search(data)
    elif mod == "literature_reading":
        html = render_literature_reading(data)
    elif mod == "literature_review":
        html = render_literature_review(data)
    elif mod == "research_topic":
        html = render_research_topic(data)
    elif mod == "research_design":
        html = render_research_design(data)
    elif mod == "data_analysis":
        html = render_data_analysis(data)
    elif mod == "paper_writing":
        html = render_paper_writing(data)
    elif mod == "paper_polish":
        html = render_paper_polish(data)
    elif mod == "citation_mgmt":
        html = render_citation_mgmt(data)
    elif mod == "journal_select":
        html = render_journal_select(data)
    elif mod == "grant_writing":
        html = render_grant_writing(data)
    elif mod == "presentation":
        html = render_presentation(data)
    else:
        html = render_generic(data)

    return html


def render_literature_search(data):
    papers = data.get("papers", [])
    trends = data.get("trends", {})
    network = data.get("network", "")
    highlights = data.get("highlights", [])
    summary = data.get("summary", "")

    html = '<div class="section">'

    # Summary
    if summary:
        html += f'<div class="summary-box">{escape(summary)}</div>'

    # Trend chart
    if trends and trends.get("years"):
        chart_id = "trendChart"
        years = json.dumps(trends.get("years", []))
        counts = json.dumps(trends.get("counts", []))
        html += f'''
        <div class="chart-container">
            <h3>📈 研究趋势</h3>
            <canvas id="{chart_id}" height="200"></canvas>
        </div>
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var ctx = document.getElementById('{chart_id}');
            if (ctx) {{
                new Chart(ctx, {{
                    type: 'line',
                    data: {{
                        labels: {years},
                        datasets: [{{
                            label: '发表数量',
                            data: {counts},
                            borderColor: '#4A90D9',
                            backgroundColor: 'rgba(74,144,217,0.1)',
                            fill: true,
                            tension: 0.3,
                            pointRadius: 4,
                            pointBackgroundColor: '#4A90D9'
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        plugins: {{ legend: {{ display: false }} }}
                    }}
                }});
            }}
        }});
        </script>
        '''

    # Paper list
    if papers:
        html += '<h3>📚 检索到的文献</h3>'
        html += '<div class="paper-list">'
        for p in papers:
            title = escape(p.get("title", ""))
            authors = escape(p.get("authors", ""))
            year = escape(str(p.get("year", "")))
            journal = escape(p.get("journal", ""))
            citations = p.get("citations", 0)
            relevance = p.get("relevance", 3)
            doi = escape(p.get("doi", ""))
            abstract = escape(p.get("abstract", ""))
            color = score_color(relevance)

            html += f'''
            <div class="paper-card">
                <div class="paper-header">
                    <span class="relevance-badge" style="background:{color}">相关性 {relevance}/5</span>
                    <span class="citation-count">被引 {citations}</span>
                </div>
                <h4>📄 {title}</h4>
                <div class="paper-meta">
                    <span>👤 {authors}</span>
                    <span>📅 {year}</span>
                </div>
                <div class="paper-journal">📰 {journal}</div>
                <div class="paper-abstract">{abstract[:300]}{"..." if len(abstract) > 300 else ""}</div>
                {f'<a class="doi-link" href="https://doi.org/{doi}" target="_blank">🔗 DOI: {doi}</a>' if doi else ''}
            </div>
            '''
        html += '</div>'

    # Network visualization placeholder
    if network:
        html += f'<div class="network-section"><h3>🕸️ 引用网络</h3><div class="network-note">{escape(network)}</div></div>'

    # Highlights
    if highlights:
        html += '<h3>⭐ 重点论文深度解析</h3>'
        for h in highlights:
            html += f'<div class="highlight-card"><h4>{escape(h.get("title", ""))}</h4><p>{escape(h.get("insight", ""))}</p></div>'

    html += '</div>'
    return html


def render_literature_reading(data):
    papers = data.get("papers", [])
    html = '<div class="section">'
    for p in papers:
        title = escape(p.get("title", ""))
        tldr = escape(p.get("tldr", ""))
        method = escape(p.get("method", ""))
        findings = escape(p.get("findings", ""))
        innovation = escape(p.get("innovation", ""))
        limitations = escape(p.get("limitations", ""))
        scores = p.get("scores", {})

        html += f'<div class="reading-card">'
        html += f'<h2>📄 {title}</h2>'

        if tldr:
            html += f'<div class="tldr-box">💡 <strong>TL;DR:</strong> {tldr}</div>'

        # Radar chart for quality assessment
        if scores:
            rid = f"radar_{hash(title) % 100000}"
            labels = json.dumps(list(scores.keys()))
            values = json.dumps(list(scores.values()))
            html += f'''
            <div class="mini-chart">
                <canvas id="{rid}" height="200"></canvas>
            </div>
            <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var ctx = document.getElementById('{rid}');
                if (ctx) {{
                    new Chart(ctx, {{
                        type: 'radar',
                        data: {{
                            labels: {labels},
                            datasets: [{{
                                label: '评分',
                                data: {values},
                                borderColor: '#4A90D9',
                                backgroundColor: 'rgba(74,144,217,0.2)',
                                pointBackgroundColor: '#4A90D9'
                            }}]
                        }},
                        options: {{
                            responsive: true,
                            scales: {{ r: {{ min: 0, max: 5, ticks: {{ stepSize: 1 }} }} }}
                        }}
                    }});
                }}
            }});
            </script>
            '''

        html += f'<div class="method-section"><strong>🔬 方法论:</strong> {method}</div>' if method else ''
        html += f'<div class="findings-section"><strong>📊 关键发现:</strong> {findings}</div>' if findings else ''
        html += f'<div class="innovation-section"><strong>⭐ 创新点:</strong> {innovation}</div>' if innovation else ''
        html += f'<div class="limitation-section"><strong>⚠️ 局限性:</strong> {limitations}</div>' if limitations else ''
        html += '</div>'
    html += '</div>'
    return html


def render_literature_review(data):
    framework = data.get("framework", [])
    themes = data.get("themes", [])
    gaps = data.get("gaps", [])
    body = data.get("body_text", "")
    references = data.get("references", [])
    html = '<div class="section">'

    if framework:
        html += '<h3>📋 综述框架</h3><div class="framework-list">'
        for f in framework:
            html += f'<div class="framework-item">• {escape(f)}</div>'
        html += '</div>'

    if themes:
        html += '<h3>🗂️ 主题分类</h3>'
        for t in themes:
            name = escape(t.get("name", ""))
            desc = escape(t.get("description", ""))
            count = t.get("paper_count", 0)
            html += f'<div class="theme-card"><h4>{name} <span class="badge">{count}篇</span></h4><p>{desc}</p></div>'

    if gaps:
        html += '<h3>🕳️ 研究空白与机会</h3><div class="gap-list">'
        for g in gaps:
            html += f'<div class="gap-item">🎯 <strong>{escape(g.get("direction", ""))}</strong><br>{escape(g.get("description", ""))}</div>'
        html += '</div>'

    if body:
        html += f'<h3>📝 综述正文</h3><div class="review-body">{escape(body)}</div>'

    if references:
        html += '<h3>📚 参考文献 ({})</h3><div class="ref-list">'.format(len(references))
        for i, r in enumerate(references, 1):
            html += f'<div class="ref-item">[{i}] {escape(r)}</div>'
        html += '</div>'

    html += '</div>'
    return html


def render_research_topic(data):
    ideas = data.get("ideas", [])
    assessment = data.get("assessment", {})
    html = '<div class="section">'

    if assessment:
        dims = assessment.get("dimensions", {})
        if dims:
            rid = "radar_idea"
            labels = json.dumps(list(dims.keys()))
            values = json.dumps(list(dims.values()))
            html += f'''
            <div class="chart-container">
                <h3>🎯 选题六维评估</h3>
                <canvas id="{rid}" height="250"></canvas>
            </div>
            <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var ctx = document.getElementById('{rid}');
                if (ctx) new Chart(ctx, {{ type: 'radar', data: {{ labels: {labels}, datasets: [{{ label: '评分', data: {values}, borderColor: '#4A90D9', backgroundColor: 'rgba(74,144,217,0.2)' }}] }}, options: {{ responsive: true, scales: {{ r: {{ min: 0, max: 5 }} }} }} }});
            }});
            </script>
            '''

    if ideas:
        html += '<h3>💡 可选研究方向</h3>'
        for idea in ideas:
            html += f'''
            <div class="idea-card">
                <h4>🔹 {escape(idea.get("title", ""))}</h4>
                <p>{escape(idea.get("description", ""))}</p>
                <div class="idea-meta">
                    <span>创新性: {"⭐" * min(5, int(idea.get("novelty", 3)))}</span>
                    <span>可行性: {"⭐" * min(5, int(idea.get("feasibility", 3)))}</span>
                    <span>影响力: {"⭐" * min(5, int(idea.get("impact", 3)))}</span>
                </div>
            </div>'''

    html += '</div>'
    return html


def render_research_design(data):
    html = '<div class="section">'

    flowchart = data.get("flowchart", "")
    variables = data.get("variables", {})
    methods = data.get("methods", [])
    sample_size = data.get("sample_size", "")
    timeline = data.get("timeline", [])
    stats_plan = data.get("statistics_plan", "")

    if flowchart:
        html += f'<div class="flowchart-section"><h3>🧭 研究设计流程</h3><div class="flowchart-box">{escape(flowchart)}</div></div>'

    if variables:
        html += '<h3>📐 变量定义</h3>'
        iv = escape(variables.get("independent", ""))
        dv = escape(variables.get("dependent", ""))
        cv = escape(", ".join(variables.get("control", [])))
        confound = escape(", ".join(variables.get("confound", [])))
        html += f'<table class="var-table"><tr><th>自变量</th><td>{iv}</td></tr><tr><th>因变量</th><td>{dv}</td></tr><tr><th>控制变量</th><td>{cv}</td></tr><tr><th>混淆变量</th><td>{confound}</td></tr></table>'

    if methods:
        html += '<h3>🔬 推荐方法</h3>'
        for m in methods:
            html += f'<div class="method-card"><strong>{escape(m.get("name", ""))}</strong><br>{escape(m.get("reason", ""))}</div>'

    if sample_size:
        html += f'<div class="sample-size"><h3>👥 样本量</h3><p>{escape(sample_size)}</p></div>'

    if stats_plan:
        html += f'<div class="stats-plan"><h3>📊 统计分析计划</h3><p>{escape(stats_plan)}</p></div>'

    if timeline:
        html += '<h3>📅 时间线</h3><div class="timeline">'
        for t in timeline:
            html += f'<div class="timeline-item"><span class="time">{escape(t.get("period", ""))}</span> {escape(t.get("task", ""))}</div>'
        html += '</div>'

    html += '</div>'
    return html


def render_data_analysis(data):
    html = '<div class="section">'

    data_quality = data.get("data_quality", "")
    methods = data.get("recommended_methods", [])
    code = data.get("code", "")
    code_lang = data.get("code_lang", "python")
    visuals = data.get("visuals", "")
    interpretation = data.get("interpretation", "")

    if data_quality:
        html += f'<div class="quality-box"><h3>📋 数据质量评估</h3><p>{escape(data_quality)}</p></div>'

    if methods:
        html += '<h3>📊 推荐统计方法</h3><div class="method-list">'
        for m in methods:
            html += f'<div class="method-item">📌 <strong>{escape(m.get("name", ""))}</strong>: {escape(m.get("condition", ""))}</div>'
        html += '</div>'

    if code:
        html += f'<h3>💻 分析代码 ({code_lang})</h3><pre class="code-block"><code>{escape(code)}</code></pre>'

    if visuals:
        html += f'<div class="visuals-section"><h3>📈 可视化结果</h3><div>{escape(visuals)}</div></div>'

    if interpretation:
        html += f'<div class="interpretation"><h3>📝 结果解读</h3><p>{escape(interpretation)}</p></div>'

    html += '</div>'
    return html


def render_paper_writing(data):
    html = '<div class="section">'

    outline = data.get("outline", [])
    sections = data.get("sections", {})
    checklist = data.get("checklist", [])

    if outline:
        html += '<h3>📑 论文大纲</h3><div class="outline-list">'
        for o in outline:
            html += f'<div class="outline-item">{escape(o)}</div>'
        html += '</div>'

    section_order = ["introduction", "methods", "results", "discussion", "abstract"]
    for s in section_order:
        if s in sections:
            title_map = {"introduction": "引言", "methods": "方法", "results": "结果", "discussion": "讨论", "abstract": "摘要"}
            html += f'<h3>📝 {title_map.get(s, s)}</h3><div class="written-section">{escape(sections[s])}</div>'

    for k, v in sections.items():
        if k not in section_order:
            html += f'<h3>📝 {k}</h3><div class="written-section">{escape(v)}</div>'

    if checklist:
        html += '<h3>✅ 写作质量检查清单</h3><div class="checklist">'
        for c in checklist:
            html += f'<div class="checklist-item">☐ {escape(c)}</div>'
        html += '</div>'

    html += '</div>'
    return html


def render_paper_polish(data):
    html = '<div class="section">'

    original = data.get("original", "")
    polished = data.get("polished", "")
    changes = data.get("changes", [])
    scores = data.get("scores", {})

    if original and polished:
        html += f'''
        <h3>📝 润色对比</h3>
        <div class="comparison">
            <div class="compare-col">
                <h4>原文</h4>
                <div class="original-text">{escape(original)}</div>
            </div>
            <div class="compare-col">
                <h4>润色版</h4>
                <div class="polished-text">{escape(polished)}</div>
            </div>
        </div>
        '''

    if changes:
        html += '<h3>🔧 修改点</h3><div class="changes-list">'
        for c in changes:
            cat = escape(c.get("category", ""))
            desc = escape(c.get("description", ""))
            html += f'<div class="change-item"><span class="change-cat">{cat}</span> {desc}</div>'
        html += '</div>'

    if scores:
        rid = "polish_radar"
        labels = json.dumps(list(scores.keys()))
        values = json.dumps(list(scores.values()))
        html += f'''
        <h3>📊 综合评分</h3>
        <div class="chart-container"><canvas id="{rid}" height="200"></canvas></div>
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var ctx = document.getElementById('{rid}');
            if (ctx) new Chart(ctx, {{ type: 'radar', data: {{ labels: {labels}, datasets: [{{ label: '评分', data: {values}, borderColor: '#4A90D9', backgroundColor: 'rgba(74,144,217,0.2)' }}] }}, options: {{ responsive: true, scales: {{ r: {{ min: 0, max: 5 }} }} }} }});
        }});
        </script>
        '''

    html += '</div>'
    return html


def render_citation_mgmt(data):
    html = '<div class="section">'
    citations = data.get("citations", [])
    format_type = data.get("format", "APA 7th")
    issues = data.get("issues", [])

    html += f'<h3>📎 引用列表 ({format_type})</h3>'
    html += '<div class="citation-list">'
    for i, ref in enumerate(citations, 1):
        html += f'<div class="citation-item"><span class="ref-num">[{i}]</span> {escape(ref)}</div>'
    html += '</div>'

    if issues:
        html += '<h3>⚠️ 引用检查</h3><div class="issues-list">'
        for iss in issues:
            html += f'<div class="issue-item">🔸 {escape(iss)}</div>'
        html += '</div>'

    html += '</div>'
    return html


def render_journal_select(data):
    html = '<div class="section">'
    journals = data.get("journals", [])
    strategy = data.get("strategy", "")
    cover_letter = data.get("cover_letter", "")

    if journals:
        html += '<h3>🎯 推荐期刊</h3><table class="journal-table"><tr><th>期刊名</th><th>影响因子</th><th>审稿周期</th><th>接受率</th><th>梯度</th></tr>'
        for j in journals:
            name = escape(j.get("name", ""))
            if_score = escape(str(j.get("impact_factor", "N/A")))
            review_time = escape(str(j.get("review_time", "N/A")))
            acceptance = escape(str(j.get("acceptance_rate", "N/A")))
            tier = escape(j.get("tier", ""))

            tier_color = {"冲刺": "#f5222d", "匹配": "#faad14", "保底": "#52c41a"}.get(tier, "#999")
            html += f'<tr><td><strong>{name}</strong></td><td>{if_score}</td><td>{review_time}</td><td>{acceptance}</td><td><span style="color:{tier_color};font-weight:bold">{tier}</span></td></tr>'
        html += '</table>'

    if strategy:
        html += f'<div class="strategy-box"><h3>📋 投稿策略</h3><p>{escape(strategy)}</p></div>'

    if cover_letter:
        html += f'<div class="cover-letter"><h3>✉️ Cover Letter 模板</h3><pre>{escape(cover_letter)}</pre></div>'

    html += '</div>'
    return html


def render_grant_writing(data):
    html = '<div class="section">'

    grant_type = data.get("grant_type", "")
    sections = data.get("sections", {})
    budget = data.get("budget", [])
    checklist = data.get("checklist", [])
    route = data.get("tech_route", "")

    if grant_type:
        html += f'<div class="grant-type"><strong>基金类型:</strong> {escape(grant_type)}</div>'

    if route:
        html += f'<div class="tech-route"><h3>🧭 技术路线</h3><p>{escape(route)}</p></div>'

    section_order = ["background", "objectives", "content", "innovation", "outcomes", "basis"]
    titles = {"background": "立项依据", "objectives": "研究目标", "content": "研究内容与方案", "innovation": "创新点", "outcomes": "预期成果", "basis": "研究基础"}
    for s in section_order:
        if s in sections:
            html += f'<h3>📄 {titles.get(s, s)}</h3><div class="grant-section">{escape(sections[s])}</div>'

    for k, v in sections.items():
        if k not in section_order:
            html += f'<h3>📄 {k}</h3><div class="grant-section">{escape(v)}</div>'

    if budget:
        html += '<h3>💰 经费预算</h3><table class="budget-table"><tr><th>项目</th><th>金额(万元)</th><th>说明</th></tr>'
        total = 0
        for b in budget:
            item = escape(b.get("item", ""))
            amount = b.get("amount", 0)
            desc = escape(b.get("description", ""))
            total += amount
            html += f'<tr><td>{item}</td><td class="amount">{amount}</td><td>{desc}</td></tr>'
        html += f'<tr class="total-row"><td><strong>合计</strong></td><td class="amount"><strong>{total}</strong></td><td></td></tr>'
        html += '</table>'

    if checklist:
        html += '<h3>✅ 评审自查清单</h3><div class="checklist">'
        for c in checklist:
            html += f'<div class="checklist-item">☐ {escape(c)}</div>'
        html += '</div>'

    html += '</div>'
    return html


def render_presentation(data):
    html = '<div class="section">'

    pres_type = data.get("type", "")
    slides = data.get("slides", [])
    script = data.get("script", "")
    qa = data.get("qa", [])
    tips = data.get("tips", [])

    if pres_type:
        html += f'<div class="pres-type">类型: <strong>{escape(pres_type)}</strong></div>'

    if slides:
        html += '<h3>📊 幻灯片大纲</h3>'
        for s in slides:
            num = escape(str(s.get("slide_num", "")))
            title = escape(s.get("title", ""))
            content = escape(s.get("content", ""))
            html += f'<div class="slide-card"><h4>Slide {num}: {title}</h4><p>{content}</p></div>'

    if script:
        html += f'<h3>🎙️ 讲稿</h3><div class="script-box">{escape(script)}</div>'

    if qa:
        html += '<h3>❓ 预判Q&A</h3>'
        for q in qa:
            question = escape(q.get("question", ""))
            answer = escape(q.get("answer", ""))
            html += f'<div class="qa-item"><strong>Q: {question}</strong><br>A: {answer}</div>'

    if tips:
        html += '<h3>💡 排练建议</h3><div class="tips-list">'
        for t in tips:
            html += f'<div class="tip-item">✅ {escape(t)}</div>'
        html += '</div>'

    html += '</div>'
    return html


def render_generic(data):
    """通用渲染"""
    html = '<div class="section">'
    for k, v in data.items():
        html += f'<h3>{escape(k)}</h3><p>{escape(str(v))}</p>'
    html += '</div>'
    return html


def build_full_html(title, subject, modules, tab_nav, tab_contents, timestamp):
    """构建完整HTML页面"""
    mod_list = ", ".join([MODULE_NAMES.get(m, {}).get("name", m) for m in modules])

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>科研助理报告 - {escape(title)}</title>
    {build_chart_js()}
    <style>
        :root {{
            --primary: #1a3a5c;
            --primary-light: #4A90D9;
            --bg: #f7f9fc;
            --card-bg: #ffffff;
            --text: #2c3e50;
            --text-secondary: #7f8c8d;
            --border: #e1e8ed;
            --accent: #3498db;
            --success: #27ae60;
            --warning: #f39c12;
            --danger: #e74c3c;
            --radius: 12px;
            --shadow: 0 2px 12px rgba(0,0,0,0.06);
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.7;
            padding: 20px;
        }}
        .container {{ max-width: 1100px; margin: 0 auto; }}

        /* Header */
        .report-header {{
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            color: white;
            padding: 40px;
            border-radius: var(--radius);
            margin-bottom: 24px;
            text-align: center;
        }}
        .report-header h1 {{ font-size: 28px; margin-bottom: 8px; }}
        .report-header .subject {{ font-size: 16px; opacity: 0.9; }}
        .report-header .meta {{ font-size: 13px; opacity: 0.7; margin-top: 8px; }}

        /* Tab Navigation */
        .tab-nav {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 20px;
            padding: 12px;
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
        }}
        .tab-btn {{
            padding: 8px 16px;
            border: 1.5px solid var(--border);
            border-radius: 8px;
            background: white;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
            white-space: nowrap;
        }}
        .tab-btn:hover {{ border-color: var(--accent); color: var(--accent); }}
        .tab-btn.active {{
            background: var(--primary-light);
            color: white;
            border-color: var(--primary-light);
        }}

        /* Tab Content */
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}

        /* Cards */
        .section {{ animation: fadeIn 0.3s ease; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}

        .summary-box {{
            background: linear-gradient(135deg, #e8f4fd, #d0e8f9);
            border-left: 4px solid var(--accent);
            padding: 16px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}

        h2, h3, h4 {{ color: var(--primary); margin: 20px 0 12px 0; }}
        h2 {{ font-size: 22px; border-bottom: 2px solid var(--border); padding-bottom: 8px; }}

        .chart-container {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            margin-bottom: 20px;
        }}

        /* Paper Cards */
        .paper-list {{ display: flex; flex-direction: column; gap: 16px; }}
        .paper-card {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            border-left: 4px solid var(--primary-light);
            transition: transform 0.2s;
        }}
        .paper-card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
        .paper-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
        .relevance-badge {{
            padding: 2px 10px;
            border-radius: 12px;
            color: white;
            font-size: 12px;
            font-weight: bold;
        }}
        .citation-count {{ font-size: 13px; color: var(--text-secondary); }}
        .paper-meta {{ display: flex; gap: 16px; font-size: 13px; color: var(--text-secondary); margin: 8px 0; }}
        .paper-journal {{ font-size: 13px; color: var(--accent); margin-bottom: 8px; }}
        .paper-abstract {{ font-size: 14px; color: #555; line-height: 1.6; }}
        .doi-link {{ display: inline-block; margin-top: 8px; font-size: 12px; color: var(--accent); text-decoration: none; }}
        .doi-link:hover {{ text-decoration: underline; }}

        /* Reading Card */
        .reading-card {{
            background: var(--card-bg);
            padding: 24px;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            margin-bottom: 20px;
        }}
        .tldr-box {{
            background: #fff8e1;
            border-left: 4px solid var(--warning);
            padding: 12px 16px;
            border-radius: 6px;
            margin: 12px 0;
        }}
        .mini-chart {{ max-width: 350px; margin: 16px auto; }}

        /* Theme Cards */
        .theme-card {{
            background: var(--card-bg);
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 12px;
            box-shadow: var(--shadow);
        }}
        .badge {{
            background: var(--primary-light);
            color: white;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
        }}

        /* Gap */
        .gap-list {{ display: flex; flex-direction: column; gap: 12px; }}
        .gap-item {{
            background: #fff3e0;
            padding: 14px 18px;
            border-radius: 8px;
            border-left: 4px solid var(--warning);
        }}

        /* Idea Card */
        .idea-card {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            margin-bottom: 16px;
            border-left: 4px solid var(--success);
        }}
        .idea-meta {{ display: flex; gap: 20px; margin-top: 10px; font-size: 13px; color: var(--text-secondary); }}

        /* Variables Table */
        .var-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0;
        }}
        .var-table th {{
            background: var(--primary);
            color: white;
            padding: 8px 16px;
            text-align: left;
            width: 120px;
        }}
        .var-table td {{
            padding: 8px 16px;
            border: 1px solid var(--border);
        }}

        /* Timeline */
        .timeline {{ border-left: 3px solid var(--primary-light); margin-left: 20px; padding-left: 20px; }}
        .timeline-item {{
            position: relative;
            margin-bottom: 16px;
            padding: 8px 0;
        }}
        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -28px;
            top: 12px;
            width: 10px;
            height: 10px;
            background: var(--primary-light);
            border-radius: 50%;
        }}
        .time {{ color: var(--accent); font-weight: bold; margin-right: 8px; }}

        /* Code Block */
        .code-block {{
            background: #1e293b;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Fira Code', 'Cascadia Code', 'Consolas', monospace;
            font-size: 13px;
            line-height: 1.6;
        }}

        /* Comparison */
        .comparison {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 16px 0; }}
        .compare-col {{
            background: var(--card-bg);
            padding: 16px;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }}
        .compare-col h4 {{ margin-top: 0; }}
        .original-text {{ color: #888; white-space: pre-wrap; }}
        .polished-text {{ color: var(--text); white-space: pre-wrap; }}

        /* Changes */
        .changes-list {{ display: flex; flex-direction: column; gap: 8px; }}
        .change-item {{ padding: 8px 12px; background: #f0f4f8; border-radius: 6px; }}
        .change-cat {{
            background: var(--accent);
            color: white;
            padding: 1px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-right: 8px;
        }}

        /* Citation */
        .citation-list {{ font-size: 13px; line-height: 1.8; }}
        .citation-item {{ margin-bottom: 6px; }}
        .ref-num {{ color: var(--accent); font-weight: bold; margin-right: 6px; }}

        /* Journal Table */
        .journal-table, .budget-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            background: var(--card-bg);
            border-radius: var(--radius);
            overflow: hidden;
            box-shadow: var(--shadow);
        }}
        .journal-table th, .budget-table th {{
            background: var(--primary);
            color: white;
            padding: 10px 16px;
            text-align: left;
            font-size: 13px;
        }}
        .journal-table td, .budget-table td {{
            padding: 10px 16px;
            border-bottom: 1px solid var(--border);
            font-size: 14px;
        }}
        .total-row {{ background: #e8f5e9; }}
        .amount {{ text-align: right; font-variant-numeric: tabular-nums; }}

        /* Grant */
        .grant-section, .review-body, .written-section {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            box-shadow: var(--shadow);
            margin-bottom: 16px;
            white-space: pre-wrap;
            line-height: 1.8;
        }}
        .grant-type {{
            background: #e8f5e9;
            padding: 10px 16px;
            border-radius: 6px;
            margin-bottom: 16px;
        }}

        /* Presentation */
        .slide-card {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 12px;
            box-shadow: var(--shadow);
            border-left: 4px solid var(--accent);
        }}
        .qa-item {{
            background: #fef9e7;
            padding: 14px 18px;
            border-radius: 8px;
            margin-bottom: 10px;
        }}
        .script-box, .cover-letter {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            box-shadow: var(--shadow);
            white-space: pre-wrap;
        }}

        /* Checklist */
        .checklist {{ display: flex; flex-direction: column; gap: 6px; margin: 12px 0; }}
        .checklist-item {{ padding: 6px 0; font-size: 14px; }}

        /* Empty */
        .empty-state {{
            text-align: center;
            padding: 60px 20px;
            color: var(--text-secondary);
            font-size: 18px;
        }}

        /* Footer */
        .report-footer {{
            text-align: center;
            padding: 30px;
            color: var(--text-secondary);
            font-size: 13px;
            margin-top: 30px;
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            body {{ padding: 10px; }}
            .report-header {{ padding: 24px 16px; }}
            .comparison {{ grid-template-columns: 1fr; }}
            .tab-nav {{ gap: 4px; }}
            .tab-btn {{ padding: 6px 10px; font-size: 12px; }}
        }}

        /* Print */
        @media print {{
            .tab-nav {{ display: none; }}
            .tab-content {{ display: block !important; margin-bottom: 30px; }}
            body {{ background: white; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="report-header">
            <h1>🔬 科研助理分析报告</h1>
            <div class="subject">主题: {escape(title)}</div>
            <div class="meta">分析模块: {mod_list} | 生成时间: {timestamp}</div>
        </div>

        <div class="tab-nav">{tab_nav}</div>

        {tab_contents}

        <div class="report-footer">
            <p>🤖 本报告由 AI 科研助理自动生成 | 内容仅供参考，请人工核实关键信息</p>
            <p>遵循学术诚信原则 | AI辅助≠代写</p>
            <p>Generated by WorkBuddy Research Assistant v1.0.0</p>
        </div>
    </div>

    <script>
    function switchTab(tabId) {{
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
        event.target.closest('.tab-btn').classList.add('active');
        document.getElementById('tab-' + tabId).classList.add('active');
    }}
    </script>
</body>
</html>'''


def main():
    parser = argparse.ArgumentParser(description="科研助理报告生成器")
    parser.add_argument("--data", required=True, help="JSON 格式的分析数据")
    parser.add_argument("--output", required=True, help="输出 HTML 文件路径")
    args = parser.parse_args()

    try:
        data = json.loads(args.data)
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}", file=sys.stderr)
        sys.exit(1)

    title = data.get("title", "科研分析报告")
    subject = data.get("subject", "")
    modules = data.get("modules", [])
    module_data = data.get("data", {})

    tab_nav = make_tabs(modules)
    tab_contents = make_module_content(module_data, modules)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    full_html = build_full_html(title, subject, modules, tab_nav, tab_contents, timestamp)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"报告已生成: {args.output}")
    print(f"文件大小: {os.path.getsize(args.output):,} bytes")


if __name__ == "__main__":
    main()
