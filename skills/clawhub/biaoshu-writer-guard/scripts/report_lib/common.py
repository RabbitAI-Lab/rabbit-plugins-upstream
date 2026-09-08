"""Common data helpers and constants for report rendering."""

import json
import os

# ============================== 配色/常量 ==============================
# 风险分桶：兼容真实后端(high/review/tip) 与文档(高/中/低)
def _risk_bucket(level):
    s = str(level)
    if s in ("高", "high"):
        return "high"
    if s in ("中", "review"):
        return "review"
    if s in ("低", "tip"):
        return "tip"
    return "other"


_RISK_LABEL = {"high": "高风险", "review": "待复核", "tip": "提示", "other": "其他"}
# 行动建议优先级 high/medium/low → 中文
_PRIORITY_ZH = {"high": "高", "medium": "中", "low": "低"}
_SEMANTIC_STATE_ZH = {
    "full": "完整完成",
    "complete": "完整完成",
    "completed": "完整完成",
    "done": "完整完成",
    "rules_only": "仅规则检查",
    "semantic_partial": "部分完成",
    "partial": "部分完成",
    "running": "处理中",
    "processing": "处理中",
    "pending": "等待处理",
    "failed": "异常",
    "error": "异常",
    "skipped": "未执行",
}
_DOCX_RISK_COLOR = {"high": "C0392B", "review": "B9770E", "tip": "0E7490", "other": "475569"}
_LABEL = {"interpretation": "智能解读", "compliance": "合规审查", "bid_duplicate": "标书查重"}
_DUP_RISK_LABEL = {"high": "高风险", "medium": "中风险", "low": "低风险", "other": "其他"}
_DUP_RISK_BUCKET = {"high": "high", "medium": "review", "low": "tip"}
_DUP_FRAGMENT_LIMIT_PER_PAIR = 20
_DUP_RISK_LIMIT_PER_PAIR = 20
# Locale scope: report artifacts currently ship with zh-CN labels because bidding terminology
# and exported templates follow mainland-China procurement conventions.


def _safe_name(name):
    name = os.path.splitext(os.path.basename(str(name)))[0]
    for ch in '/\\:*?"<>|':
        name = name.replace(ch, "_")
    return name.strip() or "report"

def _unwrap(data):
    if isinstance(data, dict) and "result" in data and "service" in data:
        return data.get("service"), (data.get("result") or {})
    if isinstance(data, dict) and ("duplicate" in data or "pairs" in data):
        return "bid_duplicate", data
    if isinstance(data, dict) and ("issues" in data or "run_id" in data or "compliance" in data):
        return "compliance", data
    return "interpretation", (data or {})


def _g(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict) and k in d and d[k] is not None:
            return d[k]
    return default


def _ev(obj):
    """证据多形态归一：兼容 {excerpt}/{text}/{field,expected_text}/{source} 等。"""
    if not isinstance(obj, dict):
        return str(obj or "")
    for k in ("excerpt", "text", "requirement_excerpt", "bid_excerpt"):
        if obj.get(k):
            v = str(obj[k])
            p = obj.get("page") or obj.get("section_title")
            return f"{v}（{p}）" if p else v
    if obj.get("field") or obj.get("expected_text"):
        return f"{obj.get('field','')}：{obj.get('expected_text','')}".strip("：")
    if obj.get("source"):
        return f"来源：{obj['source']}"
    return ""


def _pct(value):
    try:
        return f"{float(value) * 100:.1f}%"
    except (TypeError, ValueError):
        return "-"


def _filesize(value):
    try:
        n = int(value)
    except (TypeError, ValueError):
        return "-"
    if n >= 1024 * 1024 * 1024:
        return f"{n / 1024 / 1024 / 1024:.2f} GB"
    if n >= 1024 * 1024:
        return f"{n / 1024 / 1024:.1f} MB"
    if n >= 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n} B"


def _short_json(value, limit=220):
    if value in (None, "", [], {}):
        return ""
    if isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False)
    else:
        text = str(value)
    return text if len(text) <= limit else text[:limit] + "..."


def _semantic_review_lines(summary):
    """把合规语义审查状态转成总览区可读文案。"""
    if not isinstance(summary, dict):
        return []
    lines = []
    phase = _g(summary, "conclusion_phase", default="")
    overview_ready = _g(summary, "overview_ready", default=None)
    semantic = _g(summary, "semantic_review", default={}) or {}
    state = _g(semantic, "state", default="")
    state_label = _SEMANTIC_STATE_ZH.get(str(state).strip(), str(state).strip()) if state else ""
    phase_label = _SEMANTIC_STATE_ZH.get(str(phase).strip(), str(phase).strip()) if phase else ""
    if state_label:
        lines.append(f"语义审查状态：{state_label}")
    if phase_label and phase_label != state_label:
        lines.append(f"结论阶段：{phase_label}")
    if overview_ready is not None:
        lines.append(f"总览状态：{'可用' if bool(overview_ready) else '未完整生成'}")
    msg = _g(semantic, "message_zh", default="") or _g(semantic, "message", default="")
    if msg:
        lines.append(str(msg))
    return lines


def _partial_summary_items(partial):
    """兼容字段可能漂移的 partial_summary，只展示短值，跳过复杂嵌套。"""
    if not isinstance(partial, dict) or not partial:
        return []
    labels = {
        "high_count": "高风险",
        "review_count": "待复核",
        "tip_count": "提示项",
        "similarity_count": "多文件雷同",
        "manual_unchecked_count": "手动待确认",
        "conclusion": "阶段结论",
        "message": "阶段说明",
        "message_zh": "阶段说明",
        "state": "阶段状态",
        "status": "阶段状态",
        "checked_count": "已检查项",
        "total_count": "总项数",
    }
    items = []
    for key, label in labels.items():
        val = partial.get(key)
        if val in (None, "", [], {}):
            continue
        if key in ("state", "status"):
            val = _SEMANTIC_STATE_ZH.get(str(val).strip(), val)
        items.append(f"{label}：{val}")
    for key, val in partial.items():
        if key in labels or val in (None, "", [], {}):
            continue
        if isinstance(val, (dict, list)):
            continue
        items.append(f"{key}：{val}")
    return items


def _auto_tender_name(service, result):
    if not isinstance(result, dict):
        return None
    for k in ("tender_filename", "original_filename", "filename"):
        if result.get(k):
            return result[k]
    if service == "interpretation":
        for it in (result.get("project_info") or []):
            if isinstance(it, dict) and it.get("field_name") in (
                    "项目名称", "招标项目名称", "采购项目名称") and it.get("field_value"):
                return it["field_value"]
    return None
