"""Service-specific report renderers."""

from datetime import datetime

from .common import (
    _DUP_FRAGMENT_LIMIT_PER_PAIR,
    _DUP_RISK_BUCKET,
    _DUP_RISK_LABEL,
    _DUP_RISK_LIMIT_PER_PAIR,
    _PRIORITY_ZH,
    _RISK_LABEL,
    _ev,
    _filesize,
    _g,
    _partial_summary_items,
    _pct,
    _risk_bucket,
    _semantic_review_lines,
    _short_json,
)
from .writers import Report

# ============================== 解读报告 ==============================
def render_interpretation(result):
    r = Report("招标文件智能解读报告")
    pid = _g(result, "project_id", default="-")
    r.cover("Intelligent Interpretation · 智能解读", "招标文件智能解读报告",
            [("项目句柄", f"project_id {pid}"), ("生成时间", f"{datetime.now():%Y-%m-%d %H:%M}")])

    n0 = len(r.blocks)
    pinfo = _g(result, "project_info", default=[]) or []
    if pinfo:
        r.h2("一、项目基本信息")
        for it in pinfo:
            r.bullet(f"{_g(it,'field_name',default='')}：{_g(it,'field_value',default='')}")

    da = _g(result, "decision_analysis", default={}) or {}
    if da:
        r.h2("二、控标洞察（竞争分析）")
        r.callout(f"投标建议：{_g(da,'participation_recommendation',default='-')}　|　"
                  f"控标风险：{_g(da,'control_risk_level',default='-')}　|　"
                  f"分析置信度：{_g(da,'confidence_level',default='-')}")
        for s in (_g(da, "summary", default=[]) or []):
            r.bullet(s)
        for sig in (_g(da, "signals", default=[]) or []):
            rc = _risk_bucket(_g(sig, "risk_level"))
            badge = _RISK_LABEL.get(rc, str(_g(sig, "risk_level", default="-")))
            note = ("判定依据：" + _g(sig, "reasoning", default="")) if _g(sig, "reasoning") else ""
            r.signal_card(rc, badge, _g(sig, "title", default=""), _g(sig, "description", default=""), note)
        acts = _g(da, "actions", default=[]) or []
        if acts:
            r.h3("行动建议")
            for a in acts:
                prio = _PRIORITY_ZH.get(str(_g(a, "priority")), _g(a, "priority", default="-"))
                r.bullet(f"[{prio}] {_g(a,'recommendation',default='')}")
        gap = _g(da, "our_gap_assessment", default=[]) or []
        if gap:
            r.h3("我方差距 / 优势")
            for g in gap:
                r.bullet(g)

    def list_section(title, key, head_keys, body_key):
        rows = _g(result, key, default=[]) or []
        if not rows:
            return
        r.h2(title)
        for it in rows:
            head = "　".join(str(_g(it, f, default="")) for f in head_keys if _g(it, f))
            if head:
                r.h3(head)
            if _g(it, body_key):
                r.p(_g(it, body_key, default=""))
            if _g(it, "source_text"):
                r.bullet(f"原文（第{_g(it,'source_page',default='?')}页）：{_g(it,'source_text',default='')}")

    list_section("三、合标项要求（参与资格）", "compliance", ["category"], "requirement_text")
    list_section("四、废标项要求（红线）", "disqualification", ["type", "category"], "requirement_text")
    ev = _g(result, "evaluation", default=[]) or []
    if ev:
        r.h2("五、评审项（评分标准）")
        for it in ev:
            t = "　".join(str(_g(it, f, default="")) for f in ("component", "item", "factor") if _g(it, f))
            sc = _g(it, "score")
            r.bullet(f"{t}　{'（'+str(sc)+'分）' if sc is not None else ''}")
    list_section("六、关键要求", "key_requirements", ["category"], "requirement_text")
    list_section("七、商务条款", "business_terms", ["term_type"], "term_content")
    list_section("八、报价要求", "pricing", ["component"], "requirement_text")

    pa = _g(result, "procurement_analysis", default={}) or {}
    if pa:
        r.h2("九、采购背景与需求分析")
        if _g(pa, "analysis_summary"):
            r.p(_g(pa, "analysis_summary", default=""))
        for label, k in (("采购背景", "procurement_background"), ("采购目标", "procurement_objectives")):
            if _g(pa, k):
                r.h3(label)
                r.p(_g(pa, k, default=""))
        for label, k in (("采购范围", "procurement_scope_items"), ("关键约束", "key_constraints")):
            items = _g(pa, k, default=[]) or []
            if items:
                r.h3(label)
                for x in items:
                    r.bullet(x)
        ksm = _g(pa, "key_success_metrics", default=[]) or []
        if ksm:
            r.h3("关键成功指标")
            for m in ksm:
                if isinstance(m, dict):
                    nm, dt = m.get("name", ""), m.get("detail", "")
                    r.bullet(f"{nm}：{dt}" if dt else nm)
                else:
                    r.bullet(m)

    if len(r.blocks) <= n0:
        r.p("⚠️ 本次解读结果未包含结构化内容字段（后端可能未按文档返回完整数据），无可渲染明细。")
    return r.render_html(), r.blocks

# ============================== 合规报告 ==============================
def render_compliance(result):
    comp = result.get("compliance") if isinstance(result, dict) and isinstance(
        result.get("compliance"), dict) else result
    r = Report("合规审查报告")

    summary = _g(comp, "summary", default={}) or {}
    bid_files = _g(comp, "bid_files", default=[]) or []
    issues = _g(comp, "issues", default=[]) or []
    sims = _g(comp, "similarity_issues", default=[]) or []
    manual = _g(comp, "manual_items", default=[]) or []
    scope = _g(comp, "scope_summary_lines", default=[]) or []
    partial = _g(comp, "partial_summary", default={}) or {}

    files = "、".join(_g(f, "filename", default="") for f in bid_files) or "-"
    r.cover("Compliance Review · 合规审查", "合规审查报告",
            [("投标文件", files), ("生成时间", f"{datetime.now():%Y-%m-%d %H:%M}")])

    def _i(k):
        try:
            return int(_g(summary, k, default=0) or 0)
        except (TypeError, ValueError):
            return 0

    r.h2("一、风险概览")
    r.risk_bar(_i("high_count"), _i("review_count"), _i("tip_count"))
    r.metrics([
        ("高风险", _i("high_count"), "high"),
        ("待复核", _i("review_count"), "review"),
        ("提示项", _i("tip_count"), "tip"),
        ("多文件雷同", _i("similarity_count"), "ok"),
        ("手动待确认", _i("manual_unchecked_count"), "ok"),
    ])
    if _g(summary, "conclusion"):
        r.callout(_g(summary, "conclusion", default=""))
    semantic_lines = _semantic_review_lines(summary)
    if semantic_lines:
        r.h3("审查完整性")
        for line in semantic_lines:
            r.bullet(line)
    partial_items = _partial_summary_items(partial)
    if partial_items:
        r.h3("阶段性/部分结果摘要")
        for line in partial_items:
            r.bullet(line)
    for line in scope:
        r.bullet(line)

    def block(it):
        rc = _risk_bucket(_g(it, "risk_level"))
        r.issue_card(rc, _RISK_LABEL.get(rc, str(_g(it, "risk_level", default="-"))),
                     _g(it, "title", default=""), _g(it, "bid_filename", default=""),
                     _g(it, "description", default=""),
                     _ev(_g(it, "tender_evidence", default={})),
                     _ev(_g(it, "bid_evidence", default={})),
                     _g(it, "suggestion", default=""))

    highs = [i for i in issues if _risk_bucket(_g(i, "risk_level")) == "high"]
    reviews = [i for i in issues if _risk_bucket(_g(i, "risk_level")) == "review"]
    tips = [i for i in issues if _risk_bucket(_g(i, "risk_level")) == "tip"]

    r.h2("二、高风险问题（优先修改）")
    if highs:
        for it in highs:
            block(it)
    else:
        r.p("✅ 未发现高风险问题。")

    if reviews:
        r.h2(f"三、待人工复核（{len(reviews)} 项）")
        for it in reviews:
            block(it)
    if tips:
        r.h2(f"四、提示项（格式 / 规范，{len(tips)} 项）")
        for it in tips:
            r.bullet(f"{_g(it,'title',default='')}：{_g(it,'description',default='')}")

    if sims:
        r.h2("五、多文件相似度（串标风险）")
        for s in sims:
            rc = _risk_bucket(_g(s, "risk_level"))
            r.signal_card(rc, _RISK_LABEL.get(rc, str(_g(s, "risk_level", default="-"))),
                          f"{_g(s,'title',default='')}（{_g(s,'file_a_name',default='')} ↔ "
                          f"{_g(s,'file_b_name',default='')}，相似度 {_g(s,'similarity_score',default='-')}）",
                          _g(s, "suggestion", default=""))

    if manual:
        r.h2("六、手动核查清单")
        by_cat = {}
        for m in manual:
            by_cat.setdefault(_g(m, "category", default="其他"), []).append(m)
        for cat, items in by_cat.items():
            r.h3(cat)
            for m in items:
                mark = "☑" if _g(m, "is_checked") else "☐"
                line = f"{mark} {_g(m,'title',default='')}"
                if _g(m, "note"):
                    line += f"（备注：{_g(m,'note')}）"
                r.bullet(line)
                if _g(m, "description"):
                    r.p(_g(m, "description", default=""))

    if not issues and not sims and not manual and not summary:
        r.p("⚠️ 本次合规结果为空（后端可能未按文档返回完整数据）。")
    return r.render_html(), r.blocks

# ============================== 查重报告 ==============================
def render_bid_duplicate(result):
    dup = result.get("duplicate") if isinstance(result, dict) and isinstance(
        result.get("duplicate"), dict) else result
    dup = dup if isinstance(dup, dict) else {}
    r = Report("标书查重报告")

    summary = _g(dup, "summary", default={}) or {}
    files = _g(dup, "files", default=[]) or []
    pairs = _g(dup, "pairs", default=[]) or []
    risk_counts = summary.get("risk_counts") if isinstance(summary.get("risk_counts"), dict) else {}
    run_id = _g(dup, "run_id", default=_g(result, "run_id", default="-"))
    file_names = [str(_g(item, "filename", default="")).strip() for item in files if isinstance(item, dict)]
    title_files = "、".join(x for x in file_names[:3] if x) or "-"

    r.cover("Bid Duplicate Review · 标书查重", "标书查重报告",
            [("任务编号", f"run_id {run_id}"), ("投标文件", title_files),
             ("生成时间", f"{datetime.now():%Y-%m-%d %H:%M}")])

    def _count(key):
        try:
            return int(risk_counts.get(key, 0) or 0)
        except (TypeError, ValueError):
            return 0

    high, medium, low = _count("high"), _count("medium"), _count("low")
    r.h2("一、风险概览")
    r.risk_bar(high, medium, low)
    r.metrics([
        ("投标文件数", _g(summary, "file_count", default=len([f for f in files if _g(f, "role") == "bid"])), "ok"),
        ("文件组合数", _g(summary, "pair_count", default=len(pairs)), "ok"),
        ("高风险组合", high, "high"),
        ("中风险组合", medium, "review"),
        ("低风险组合", low, "tip"),
    ])
    r.callout("本报告用于投标文件提交前内部自查，仅呈现雷同/相似风险线索，不构成围标、串标、违法违规或投标有效性的法律认定。")

    options = _g(dup, "options", default={}) or {}
    if options:
        r.h3("检查选项")
        for label, key in (
            ("图片相似检查", "enable_image"),
            ("文档元数据检查", "enable_metadata"),
            ("语义相似检查", "enable_semantic"),
            ("排除招标原文共同表述", "exclude_tender_baseline"),
        ):
            if key in options:
                r.bullet(f"{label}：{'开启' if bool(options.get(key)) else '关闭'}")

    if files:
        r.h2("二、参与文件")
        for item in files:
            role = "招标文件" if _g(item, "role") == "tender" else "投标文件"
            r.bullet(f"{role}：{_g(item,'filename',default='')}（{_g(item,'format',default='-')}，{_filesize(_g(item,'size_bytes'))}）")

    warnings = summary.get("parse_warnings") if isinstance(summary, dict) else []
    warnings = [item for item in (warnings or []) if isinstance(item, dict)]
    if warnings:
        r.h2("三、解析告警")
        for item in warnings:
            r.bullet(f"{_g(item,'role',default='')} · {_g(item,'filename',default='')} · {_g(item,'code',default='')} · {_g(item,'message',default='')}")

    pair_section_title = "四、文件组合判定" if warnings else "三、文件组合判定"
    r.h2(pair_section_title)
    if not pairs:
        r.p("未生成文件组合。")
    for idx, pair in enumerate([p for p in pairs if isinstance(p, dict)], 1):
        raw_level = str(_g(pair, "risk_level", default="other") or "other")
        rc = _DUP_RISK_BUCKET.get(raw_level, "other")
        badge = _DUP_RISK_LABEL.get(raw_level, _DUP_RISK_LABEL["other"])
        title = f"{idx}. {_g(pair,'file_a_name',default='文件A')} ↔ {_g(pair,'file_b_name',default='文件B')}"
        metric_text = (
            f"双向综合重复率：{_pct(_g(pair,'combined_text_rate'))}；"
            f"章节加权重复率：{_pct(_g(pair,'weighted_combined_text_rate'))}；"
            f"文件A覆盖率：{_pct(_g(pair,'file_a_coverage_rate'))}；"
            f"文件B覆盖率：{_pct(_g(pair,'file_b_coverage_rate'))}"
        )
        reasons = _g(_g(pair, "summary", default={}) or {}, "reasons", default=[]) or []
        note = "判级依据：" + "；".join(str(x) for x in reasons[:8]) if reasons else ""
        r.signal_card(rc, badge, title, metric_text, note)

        risks = [item for item in (_g(pair, "risks", default=[]) or []) if isinstance(item, dict)]
        if risks:
            r.h3(f"非文本风险线索（展示前 {min(len(risks), _DUP_RISK_LIMIT_PER_PAIR)} 条，共 {len(risks)} 条）")
            for risk in risks[:_DUP_RISK_LIMIT_PER_PAIR]:
                r.bullet(" · ".join(part for part in [
                    str(_g(risk, "category", default="")),
                    str(_g(risk, "evidence_kind", default="")),
                    str(_g(risk, "strength", default="")),
                    str(_g(risk, "explanation", default="")),
                    _short_json(_g(risk, "evidence", default={})),
                ] if part))

        fragments = [item for item in (_g(pair, "fragments", default=[]) or []) if isinstance(item, dict)]
        if fragments:
            r.h3(f"文本重复证据（展示前 {min(len(fragments), _DUP_FRAGMENT_LIMIT_PER_PAIR)} 条，共 {len(fragments)} 条）")
            for fragment in fragments[:_DUP_FRAGMENT_LIMIT_PER_PAIR]:
                role = _g(fragment, "section_role", default="") or "未分类"
                chars = _g(fragment, "normalized_chars", default="-")
                r.issue_card(rc, "重复片段", f"{role} · {chars} 字",
                             f"{_g(pair,'file_a_name',default='文件A')} ↔ {_g(pair,'file_b_name',default='文件B')}",
                             "", "", _g(fragment, "text_a", default=""),
                             f"对照片段：{_g(fragment, 'text_b', default='')}")

    if not summary and not files and not pairs:
        r.p("⚠️ 本次查重结果为空（后端可能未按文档返回完整数据）。")
    return r.render_html(), r.blocks


RENDERERS = {
    "interpretation": render_interpretation,
    "compliance": render_compliance,
    "bid_duplicate": render_bid_duplicate,
}
