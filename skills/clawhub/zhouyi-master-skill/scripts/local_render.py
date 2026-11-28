#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""local_render — 本地兜底渲染器（读 data JSON 生成自包含 HTML）。

定位（重要）：
  默认展示口径始终是云端返回的 ``render.html``（服务端统一治理中文标签/分组/截断/转义，
  全调用方一致）。本脚本是 **离线 / 自定义样式** 的备用通道：直接读取响应里的 ``data``
  原始字段本地渲染成一页 HTML。它 **不复用** 服务端 Java 侧的 FieldLabels/分组内核，而是
  用随包分发的极简 HTML 模板 + 模板内嵌的「声明式渲染规格(spec)」来近似复刻云端各功能的
  分节与中文标签。字段口径以云端为准，本通道可能出现英文字段名或未分组——这是预期取舍。

按功能选模板（覆盖钩子）：
  传入 ``--func``（支持 funcCode 如 ``F3``，或功能名/族名如 ``bazi``/``nametest``）时，
  解析链为： ``template.<族>.html`` → ``template.html``（通用） → 内置同款模板。
  每个 ``template.<族>.html`` 可内嵌 ``<script type="application/json" id="zhouyi-render-spec">``
  声明该功能的分节/行标签/局部中文标签/已处置顶层键；渲染器解释 spec（单套逻辑，不重复实现），
  未被 spec 覆盖的顶层键自动并入「补充信息」卡，保证不丢项。不带 ``--func`` 则走通用递归。

依赖：仅 Python 3 标准库（无需 requests / 无需联网 / 无需 API-KEY）。

用法：
    python3 local_render.py resp.json -o out.html            # 通用渲染
    python3 local_render.py resp.json --func F3 -o out.html  # 八字精做分节
    python3 local_render.py resp.json --func bazi  -o out.html
    curl -s ... | python3 local_render.py - --func lingqian -o out.html
    python3 local_render.py --list-families                  # 列出可用功能族/编号映射
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

TEMPLATE_FILE = "template.html"          # 通用默认模板（generic 族使用）
SPEC_SCRIPT_ID = "zhouyi-render-spec"   # 模板内嵌渲染规格的 script id
MAX_DEPTH = 8

_PH_TITLE = "{{TITLE}}"
_PH_BODY = "{{BODY}}"
_PH_GEN = "{{GENERATED}}"

# 内置同款极简模板（所有模板文件缺失时的最终兜底）
_DEFAULT_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>""" + _PH_TITLE + """</title>
<style>body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",Arial,sans-serif;
background:#faf6f5;color:#333;margin:0;padding:16px;font-size:15px}
.wrap{max-width:720px;margin:0 auto}.hd{background:#b8232f;color:#fff;padding:16px 18px;
border-radius:12px 12px 0 0}.hd h1{margin:0;font-size:19px}.hd .sub{margin-top:6px;font-size:12px;opacity:.9}
.card{background:#fff;border:1px solid #e7d5d5;border-radius:12px;margin:12px 0;padding:4px 14px 12px}
.card-title{color:#8f1720;font-weight:700;font-size:16px;margin:10px 0 6px;border-left:4px solid #b8232f;padding-left:8px}
table{width:100%;border-collapse:collapse;margin:4px 0}table.kv th{text-align:left;width:34%;color:#8f1720;
padding:7px;border-bottom:1px solid #eee;vertical-align:top;font-weight:600}table.kv td{padding:7px;
border-bottom:1px solid #eee;vertical-align:top;word-break:break-word}
table.grid th,table.grid td{border:1px solid #e7d5d5;padding:6px;vertical-align:top}
table.grid thead th{background:#f6eaea;color:#8f1720}.empty{color:#bbb}
.prose{line-height:1.8;white-space:pre-wrap;color:#444}.note{margin:14px 4px;font-size:12px;color:#999;line-height:1.6}</style>
</head><body><div class="wrap"><div class="hd"><h1>""" + _PH_TITLE + """</h1>
<div class="sub">本地兜底渲染 · """ + _PH_GEN + """</div></div>
<div class="card">""" + _PH_BODY + """
<div class="note">本页由 local_render.py 读取 data 原始字段本地生成，仅用于离线/自定义样式；
权威可读版本以云端 render.html 为准。</div></div></div></body></html>"""


# ==================== 功能 → 模板族 映射（镜像云端 TEMPLATE_BY_FUNC 共用关系） ====================

# 精做功能：funcCode → 族（每个族对应一份 template.<族>.html）
FAMILY_BY_FUNCCODE = {
    "F3": "bazi", "F5": "nametest", "F6": "nametest", "F15": "paipan-bazi",
    "F16": "liuyao", "F18": "qimen", "F19": "feixing", "F20": "ziwei",
    "F21": "jinkoujue", "F23": "lingqian", "F24": "lingqian", "F25": "lingqian",
    "F26": "lingqian", "F27": "lingqian", "F35": "huangli", "F17": "liuren",
}
# 功能名/别名 → 族（大小写不敏感；族名本身也直接可用）
FAMILY_BY_ALIAS = {
    "bazi": "bazi", "八字": "bazi", "fortune-bazi": "bazi",
    "nametest": "nametest", "name-test": "nametest", "姓名测试": "nametest",
    "paipan-bazi": "paipan-bazi", "siZhu": "paipan-bazi", "四柱八字排盘": "paipan-bazi",
    "liuyao": "liuyao", "六爻": "liuyao",
    "qimen": "qimen", "奇门": "qimen", "奇门遁甲": "qimen",
    "feixing": "feixing", "飞星": "feixing", "玄空飞星": "feixing",
    "ziwei": "ziwei", "紫微": "ziwei", "紫微斗数": "ziwei",
    "jinkoujue": "jinkoujue", "金口诀": "jinkoujue",
    "lingqian": "lingqian", "灵签": "lingqian", "抽签": "lingqian",
    "huangli": "huangli", "黄历": "huangli", "黄道日历": "huangli",
    "liuren": "liuren", "六壬": "liuren", "大六壬": "liuren", "大六壬起课": "liuren",
    "generic": "generic", "通用": "generic",
}
# 全部精做族（用于 --list-families 展示）
CURATED_FAMILIES = ["bazi", "paipan-bazi", "nametest", "liuyao", "qimen",
                    "feixing", "ziwei", "jinkoujue", "lingqian", "huangli", "liuren"]

# 别名大小写不敏感查找表（修正 camelCase 别名如 "siZhu" 因 lower() 失配而不可达的问题）
_ALIAS_LOOKUP = {str(k).lower(): v for k, v in FAMILY_BY_ALIAS.items()}

# 局部中文标签：spec 命中优先，其次内置公共表，最后回落原始键名（避免整页英文）
_COMMON_LABELS = {
    "startAge": "起运年龄", "ganZhi": "干支", "note": "备注", "year": "年", "month": "月",
    "day": "日", "hour": "时辰", "name": "姓名", "gender": "性别", "sex": "性别",
    "jin": "金", "mu": "木", "shui": "水", "huo": "火", "tu": "土",
    "score": "评分", "level": "等级", "luck": "吉凶", "desc": "说明", "remark": "备注",
    "date": "日期", "time": "时间", "type": "类型", "index": "序号", "no": "编号",
    # 第9轮清单中文化：星座/生肖配对、名字类型、节气、笔画格局相关
    "constellation1": "星座1", "constellation2": "星座2", "zodiac1": "生肖1", "zodiac2": "生肖2",
    "nameType": "名字类型", "jieQi": "节气", "strokePatterns": "笔画格局",
    "surname": "姓氏", "zuhe": "笔画组合", "sancaiWuxing": "三才五行", "sancaiJixiong": "三才吉凶",
    # 第9轮清单：F15 神煞子字段 / F17 大六壬字母缩写字段中文化（对齐云端 FieldLabels）
    "shenSha": "神煞", "position": "宫位", "description": "释义",
    "jkInitZhi": "初爻地支", "jk1": "第一课", "jk2": "第二课", "jk3": "第三课", "jk4": "第四课",
    "gs1": "第一课贵神", "gs2": "第二课贵神", "gs3": "第三课贵神", "gs4": "第四课贵神",
    "lq1": "初传六亲", "lq2": "中传六亲", "lq3": "末传六亲",
    "chuan1": "初传", "chuan2": "中传", "chuan3": "末传",
    "chuan1Gs": "初传贵神", "chuan2Gs": "中传贵神", "chuan3Gs": "末传贵神",
    "chuan1Tg": "初传天干", "chuan2Tg": "中传天干", "chuan3Tg": "末传天干",
    "yueJiang": "月将", "nextJieQi": "下一节气", "xunKong": "旬空",
    "guiShens": "天将", "tianPan": "天盘", "diPan": "地盘",
    "nianMing": "年命", "hangNian": "行年", "zhanshi": "占事",
    # F8 称骨各项分量（年/月/日/时重）嵌套对象段标题（对齐云端 FieldLabels）
    "components": "骨重",
}

# 路径级中文标签（全路径→标签）：同名末段键按父路径精确区分，镜像云端 FieldLabels 结构级标签。
# 例：节气子对象 JieQiInfo 的 name 应为「节气名称」而非全局的「姓名」。
_PATH_LABELS = {
    "previousJie.name": "节气名称", "previousQi.name": "节气名称",
    "nextJie.name": "节气名称", "nextQi.name": "节气名称",
    "previousJieQi.name": "节气名称", "nextJieQi.name": "节气名称",
    # F15 神煞子对象：name 为神煞名而非姓名，position 为宫位
    "shenSha.name": "神煞", "shenSha.position": "宫位", "shenSha.description": "释义",
}

# F15 神煞宫位码→中文（对齐云端 RenderService.buildShenShaGroups 与移动端 _buildShenShaCard posMap）
_SHENSHA_POS_MAP = {
    "YZ": "年柱", "MZ": "月柱", "DZ": "日柱", "HZ": "时柱",
    "SZ": "四柱", "TY": "胎元", "MG": "命宫",
}


def resolve_family(func: Optional[str]) -> Optional[str]:
    """把 --func 入参解析为族名；无法识别返回 None（走通用渲染）。"""
    if not func:
        return None
    s = str(func).strip()
    if not s:
        return None
    up = s.upper()
    if re.fullmatch(r"F\d{1,2}", up) and up in FAMILY_BY_FUNCCODE:
        return FAMILY_BY_FUNCCODE[up]
    low = s.lower()
    if low in CURATED_FAMILIES or low == "generic":
        return low
    if low in _ALIAS_LOOKUP:
        return _ALIAS_LOOKUP[low]
    if low in FAMILY_BY_ALIAS:
        return FAMILY_BY_ALIAS[low]
    if re.fullmatch(r"F\d{1,2}", up):
        return "generic"  # 已知编号但无专属模板 → 通用
    return None


# ==================== 数据抽取 ====================

def coerce_data(payload: Any) -> Any:
    """从「完整响应」或「直接就是 data」中取出用于渲染的结果体。"""
    if isinstance(payload, dict):
        looks_like_response = ("data" in payload) and (
            "render" in payload or "code" in payload or "message" in payload or "meta" in payload
        )
        if looks_like_response or ("data" in payload and len(payload) <= 3):
            return payload.get("data")
    return payload


def extract_title(payload: Any, fallback: str = "排盘结果") -> str:
    if isinstance(payload, dict):
        meta = payload.get("meta")
        if isinstance(meta, dict):
            for k in ("funcName", "func_name", "functionName", "func", "funcCode"):
                v = meta.get(k)
                if isinstance(v, str) and v.strip():
                    return v.strip()
    return fallback


def has_cloud_render(payload: Any) -> bool:
    if isinstance(payload, dict):
        render = payload.get("render")
        return bool(isinstance(render, dict) and str(render.get("html") or "").strip())
    return False


# ==================== 通用递归渲染 ====================

_LABELS: Dict[str, str] = {}

# 按功能隐藏不渲染的字段（末段名，对齐云端 RenderService.RENDER_HIDDEN_FIELDS 与 Web 页面展示口径）。
# F14 流日 Web 页仅展示当日干支/十神/长生/神煞/干支关系/生克影响与 12 流时，不展示
# 大运/流年/流月上下文字段及原始天干(gan)/地支(zhi)/时辰序号(index)；仅作用于本地兜底页展示。
_HIDDEN_LIURI = {
    "daYunGanZhi", "daYunStartDate", "daYunEndDate",
    "liuNianGanZhi", "liuNianStartDate", "liuNianEndDate",
    "liuYueGanZhi", "liuYueStartDate", "liuYueEndDate",
    "gan", "zhi", "index",
}
_FUNC_HIDDEN = {"F14": _HIDDEN_LIURI}
_FUNC_HIDDEN_ALIAS = {"liuri": "F14", "流日": "F14"}

# 当前渲染需隐藏的末段字段名集合（随 _LABELS 同样的全局作用域模式，渲染前设置、渲染后清空）
_HIDDEN: set = set()


def hidden_for_func(func: Optional[str]) -> set:
    """由 --func 入参（F14/liuri/流日）解析需隐藏的字段集合。"""
    if not func:
        return set()
    up = str(func).strip().upper()
    if up in _FUNC_HIDDEN:
        return set(_FUNC_HIDDEN[up])
    code = _FUNC_HIDDEN_ALIAS.get(str(func).strip().lower())
    return set(_FUNC_HIDDEN[code]) if code else set()


def _combine(parent: Optional[str], k: Any) -> str:
    return (str(parent) + "." + str(k)) if parent else str(k)


def _label(k: Any, path: Optional[str] = None) -> str:
    ks = str(k)
    if path and path in _PATH_LABELS:
        return _PATH_LABELS[path]
    return _LABELS.get(ks) or _COMMON_LABELS.get(ks) or ks


# 值回译（对齐云端 render.html：性别 male/female→男/女；时辰序号 1–12→地支；名字类型 double→双字）
_GENDER_VALUE_MAP = {"male": "男", "female": "女", "m": "男", "f": "女"}
_SHI_CHEN_NAMES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def _display_value(k: Any, v: Any) -> Any:
    ks = str(k)
    if ks in ("gender", "sex"):
        if isinstance(v, str):
            return _GENDER_VALUE_MAP.get(v.strip().lower(), v)
        if isinstance(v, bool):
            return "男" if v else "女"
        if isinstance(v, int) and v in (0, 1):
            return "男" if v == 1 else "女"
    if ks == "nameType" and isinstance(v, str) and v.strip():
        return "双字" if v.strip().lower() == "double" else "单字"
    if ks == "hour" and isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 12:
        return _SHI_CHEN_NAMES[v - 1] + "时"
    # F15 神煞宫位字母码（YZ/MZ/…）回译为中文宫位，避免本地兑底页裸露字母
    if ks == "position" and isinstance(v, str):
        return _SHENSHA_POS_MAP.get(v.strip().upper(), v)
    return v


def _esc(v: Any) -> str:
    # 先解码数据中残留的 HTML 实体（如六爻爻位方块符 &#9608;→█、&nbsp;），
    # 再统一转义，避免对已有实体二次转义成 &amp;#9608; 裸显（与云端 render.html 口径一致）。
    s = "" if v is None else str(v)
    return html.escape(html.unescape(s))


_HTML_TAG_RE = re.compile(r"<[^>]+>")
_HTML_BREAK_RE = re.compile(r"(?i)<br\s*/?>|</(?:p|div|li|tr|h[1-6])>")


def _strip_html_tags(s: Any) -> Any:
    """剥离字符串中的 HTML 标签（对齐云端 RenderService.stripHtml 与移动端 _stripHtml 口径）。

    开放接口的 data 原值仍带标签（如 F6 六亲关系运势的 <h4>/<p>），云端渲染前由
    normalize() 递归剥标；本地兜底页若不剥，转义后会裸显 &lt;h4&gt; 标记。
    换行类标签转 \\n，其余标签整体移除。
    """
    if not isinstance(s, str) or "<" not in s:
        return s
    text = _HTML_BREAK_RE.sub("\n", s)
    text = _HTML_TAG_RE.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _is_scalar(v: Any) -> bool:
    return v is None or isinstance(v, (str, int, float, bool))


def _scalar_text(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "是" if v else "否"
    return str(v)


def _is_empty(v: Any) -> bool:
    if v is None:
        return True
    if isinstance(v, str):
        return not v.strip()
    if isinstance(v, (list, dict)):
        return len(v) == 0
    return False


def _scalar_html(v: Any) -> str:
    if v is None:
        return "<span class=\"empty\">—</span>"
    if isinstance(v, bool):
        return "是" if v else "否"
    return _esc(_strip_html_tags(v)).replace("\n", "<br>")


def _value_html(v: Any, depth: int, parent: Optional[str] = None) -> str:
    if depth > MAX_DEPTH:
        return "<em>（层级过深，已省略）</em>"
    if _is_scalar(v):
        return _scalar_html(v)
    if isinstance(v, dict):
        return _dict_html(v, depth, parent)
    if isinstance(v, list):
        return _list_html(v, depth, parent)
    return _esc(v)


def _dict_html(d: dict, depth: int, parent: Optional[str] = None) -> str:
    if not d:
        return "<span class=\"empty\">—</span>"
    rows = []
    for k, v in d.items():
        if str(k) in _HIDDEN:
            continue
        path = _combine(parent, k)
        vv = _display_value(k, v) if _is_scalar(v) else v
        rows.append("<tr><th>" + _esc(_label(k, path)) + "</th><td>" + _value_html(vv, depth + 1, path) + "</td></tr>")
    return "<table class=\"kv\">" + "".join(rows) + "</table>"


def _list_html(lst: list, depth: int, parent: Optional[str] = None) -> str:
    if not lst:
        return "<span class=\"empty\">—</span>"
    if all(_is_scalar(x) for x in lst):
        return _esc("、".join(_scalar_text(x) for x in lst))
    if all(isinstance(x, dict) for x in lst):
        cols: List[str] = []
        for it in lst:
            for k in it.keys():
                if k not in cols and str(k) not in _HIDDEN:
                    cols.append(k)
        thead = "".join("<th>" + _esc(_label(c, _combine(parent, c))) + "</th>" for c in cols)
        body = []
        for it in lst:
            tds = "".join("<td>" + _value_html(_display_value(c, it.get(c)) if _is_scalar(it.get(c)) else it.get(c), depth + 1, _combine(parent, c)) + "</td>" for c in cols)
            body.append("<tr>" + tds + "</tr>")
        return "<table class=\"grid\"><thead><tr>" + thead + "</tr></thead><tbody>" + "".join(body) + "</tbody></table>"
    items = "".join("<div class=\"prose\">" + _value_html(x, depth + 1) + "</div>" for x in lst)
    return "<div>" + items + "</div>"


def render_generic(data: Any) -> str:
    """无 spec 时的通用渲染（第9轮 B2）：
    - 顶层 dict → 每个键一张分卡（h3 标题 + 结构化内容），避免整块扁平铺表；
    - 顶层 list → 表格或顿号（沿用 _list_html）；
    - 标量 → 直接文本。
    深层结构（列表→表格、对象→ kv 表）由 _value_html/_dict_html/_list_html 递归完成，
    不丢项；本函数仅重塑顶层版式。
    """
    if isinstance(data, dict) and data:
        parts = []
        for k, v in data.items():
            if str(k) in _HIDDEN:
                continue
            vv = _display_value(k, v) if _is_scalar(v) else v
            body = _value_html(vv, 1, str(k))
            parts.append(
                '<section class="sec"><h3 class="sec-title">' + _esc(_label(k)) + "</h3>"
                '<div class="sec-body">' + body + "</div></section>"
            )
        return "".join(parts)
    return _value_html(data, 0)


# ==================== 声明式 spec 引擎 ====================

def _get_path(obj: Any, path: str) -> Any:
    cur = obj
    if not path:
        return None
    for seg in path.split("."):
        if isinstance(cur, dict) and seg in cur:
            cur = cur[seg]
        else:
            return None
    return cur


def _render_section(sec: dict, data: dict, covered: set) -> Optional[str]:
    title = sec.get("title", "")
    inner: List[str] = []
    table_rows: List[str] = []

    def flush_table():
        if table_rows:
            inner.append("<table class=\"kv\">" + "".join(table_rows) + "</table>")
            table_rows.clear()

    def consume(ref: str) -> None:
        """标记某键路径已被本行消费：标量顶层键整体计入 covered；点路径父键另记「父键+子路径」供剪枝。"""
        ref = str(ref)
        if not ref:
            return
        seg0 = ref.split(".")[0]
        if "." in ref:
            covered.add(seg0)
            covered.add(ref)
        else:
            covered.add(ref)

    for row in sec.get("rows", []):
        key = row.get("k", "")
        # 条件行（用于同一模板服务多个分节口径的功能，如 F5/F6 姓名测试）：
        #   unless_covered：该键已被前序节消费则跳过（防同一内容重复展示）；
        #   skip_if：引用的任一字段非空则跳过本行（把内容让给后面的节承接）。
        if row.get("unless_covered") and key and key in covered:
            continue
        if any(not _is_empty(_get_path(data, ref)) for ref in (row.get("skip_if") or [])):
            continue
        # 仅标记「本行实际消费」的键：主键、被启用的 fallback、被拼接的 append。
        # 未使用的 fallback 候选不能计入 covered，否则既不展示又被补充信息跳过 → 丢项。
        val = _get_path(data, key)
        used_fallback = False
        if _is_empty(val) and row.get("fallback"):
            fb = _get_path(data, row["fallback"])
            if not _is_empty(fb):
                val = fb
                used_fallback = True
        used_append = False
        if row.get("append"):
            a = _get_path(data, row["append"])
            if not _is_empty(val) and not _is_empty(a):
                val = str(val).strip() + " " + str(a).strip()
                used_append = True
        if _is_empty(val):
            continue
        if row.get("pick") and isinstance(val, dict):
            val = {k: val[k] for k in row["pick"] if k in val}
            if _is_empty(val):
                continue
        consume(key)
        if used_append:
            consume(row["append"])
        if used_fallback:
            consume(row["fallback"])
        # 标量值回译（与 render_generic/_dict_html 口径一致）：gender/sex→中文、nameType→双/单字、hour→地支、神煞 position→宫位
        if _is_scalar(val):
            val = _display_value(key, val)
        label = row.get("l")
        # block：列表/对象整幅输出（不套进本节 kv 表），对齐移动端
        # 「基础测算信息」的全宽逐字表格（F5/F6 nametest spec 使用）
        if row.get("block") and not _is_scalar(val):
            flush_table()
            inner.append(_value_html(val, 1, key))
            continue
        if label == "" and row.get("prose"):
            flush_table()
            inner.append("<div class=\"prose\">" + _esc(_strip_html_tags(val)) + "</div>")
            continue
        cell = _value_html(val, 1, key)
        if row.get("prose"):
            cell = "<div class=\"prose\">" + _esc(_strip_html_tags(val)) + "</div>"
        table_rows.append("<tr><th>" + _esc(label) + "</th><td>" + cell + "</td></tr>")

    flush_table()
    if not inner:
        return None
    head = ("<div class=\"card-title\">" + _esc(title) + "</div>") if title else ""
    return "<div class=\"card\">" + head + "".join(inner) + "</div>"


def _prune_consumed(value: Any, parent: str, covered: set, depth: int = 0) -> Any:
    """从父对象中剪掉已被 spec 行消费（以「父键.子路径」记入 covered）的子字段，余量留给补充信息。"""
    if depth > MAX_DEPTH or not isinstance(value, dict):
        return value
    out: Dict[str, Any] = {}
    for k, v in value.items():
        path = parent + "." + str(k)
        if path in covered:
            continue
        if isinstance(v, dict) and any(cp.startswith(path + ".") for cp in covered):
            v = _prune_consumed(v, path, covered, depth + 1)
        if _is_empty(v):
            continue
        out[k] = v
    return out


def _render_extra(data: dict, covered: set, suppress: List[str], extra_title: str) -> Optional[str]:
    leftover: Dict[str, Any] = {}
    for k, v in data.items():
        if k in suppress or _is_empty(v):
            continue
        if k not in covered:
            leftover[k] = v
            continue
        # 顶层键被某行整体消费（k.段==k 无子路径）→ 已展示，无需重复；仅当存在 k.* 子路径时剪出余量。
        if any(cp.startswith(k + ".") for cp in covered):
            pruned = _prune_consumed(v, k, covered)
            if not _is_empty(pruned):
                leftover[k] = pruned
    if not leftover:
        return None
    body = _dict_html(leftover, 1)
    return ("<div class=\"card\"><div class=\"card-title\">" + _esc(extra_title) + "</div>" + body + "</div>")


def render_with_spec(spec: dict, data: Any) -> str:
    """按 spec 分节渲染；未覆盖的顶层键自动并入「补充信息」，保证不丢项。"""
    global _LABELS
    _LABELS = dict(spec.get("labels") or {})
    covered: set = set(spec.get("covered") or [])
    suppress = list(spec.get("suppress") or [])
    parts: List[str] = []
    if isinstance(data, dict):
        for sec in spec.get("sections", []):
            card = _render_section(sec, data, covered)
            if card:
                parts.append(card)
        extra = _render_extra(data, covered, suppress, spec.get("extraTitle", "补充信息"))
        if extra:
            parts.append(extra)
    else:
        parts.append("<div class=\"card\">" + _value_html(data, 0) + "</div>")
    _LABELS = {}
    return "".join(parts) if parts else "<div class=\"card\"><div class=\"empty\">暂无结果</div></div>"


# ==================== 模板加载 ====================

def _extract_spec(text: str) -> Optional[dict]:
    m = re.search(r"<script[^>]*id=\"" + re.escape(SPEC_SCRIPT_ID) + r"\"[^>]*>(.*?)</script>",
                  text, re.DOTALL | re.IGNORECASE)
    if not m:
        return None
    try:
        return json.loads(m.group(1).strip())
    except (ValueError, TypeError):
        return None


def load_template(family: Optional[str], here: str) -> Tuple[str, Optional[dict]]:
    """按族解析模板文件链：template.<族>.html → template.html → 内置模板；返回(模板文本, spec)。"""
    candidates: List[str] = []
    if family and family != "generic":
        candidates.append("template." + family + ".html")
    candidates.append(TEMPLATE_FILE)
    for name in candidates:
        path = os.path.join(here, name)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
            if _PH_BODY in text and _PH_TITLE in text:
                return text, _extract_spec(text)
        except OSError:
            continue
    return _DEFAULT_TEMPLATE, None


# ==================== 顶层渲染入口 ====================

def render_to_html(data: Any, title: str = "排盘结果", family: Optional[str] = None,
                   hidden: Optional[set] = None) -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    global _HIDDEN
    _HIDDEN = set(hidden or set())
    tpl, spec = load_template(family, here)
    if spec and isinstance(data, dict):
        body = render_with_spec(spec, data)
    else:
        global _LABELS
        _LABELS = {}
        body = render_generic(data)
    _HIDDEN = set()
    return (tpl.replace(_PH_TITLE, _esc(title))
               .replace(_PH_BODY, body)
               .replace(_PH_GEN, time.strftime("%Y-%m-%d %H:%M:%S")))


def _safe_name(title: str) -> str:
    name = re.sub(r'[\\/:*?"<>|\s]+', "_", str(title)).strip("_")
    return (name or "result")[:40]


# ==================== CLI ====================

def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description="本地兜底渲染器：读取接口响应 JSON（或其中的 data），按功能选模板生成 HTML。")
    parser.add_argument("input", nargs="?", help="响应 JSON 文件路径；'-' 表示标准输入")
    parser.add_argument("-o", "--output", default=None,
                        help="输出 HTML 路径；'-' 打印到 stdout；缺省写 <title>_<日期>.html")
    parser.add_argument("--title", default=None, help="页面标题（缺省尝试从 meta.funcName 提取）")
    parser.add_argument("--func", default=None, help="功能标识（F3 或 bazi/nametest…），据此选择 template.<族>.html")
    parser.add_argument("--family", default=None, help="直接指定模板族（等价 --func 的族名形式）")
    parser.add_argument("--list-families", action="store_true", help="列出可用功能族与 funcCode 映射")
    args = parser.parse_args(argv)

    if args.list_families:
        print("精做功能族（有专属 template.<族>.html）：")
        for fc in sorted(FAMILY_BY_FUNCCODE, key=lambda x: int(x[1:])):
            print("  %-4s -> %s" % (fc, FAMILY_BY_FUNCCODE[fc]))
        print("其余功能（F1/F2/F4/F7-F14/F17/F22/F28-F34/F36-F48 等）→ generic 通用模板")
        return 0

    if not args.input:
        parser.error("缺少 input（或改用 --list-families）")

    if args.input == "-":
        payload = json.load(sys.stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as fh:
            payload = json.load(fh)

    data = coerce_data(payload)
    title = args.title or extract_title(payload)
    family = resolve_family(args.family or args.func)

    if has_cloud_render(payload):
        sys.stderr.write("提示：该响应已含云端 render.html（权威可读版本）；本次为本地兜底渲染。\n")
    if family and family != "generic":
        sys.stderr.write("已选用功能模板族: %s\n" % family)

    html_text = render_to_html(data, title, family, hidden_for_func(args.func))

    if args.output == "-":
        sys.stdout.write(html_text)
        return 0

    out_path = args.output or os.path.join(".", _safe_name(title) + "_" + time.strftime("%Y%m%d") + ".html")
    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html_text)
    sys.stderr.write("已生成本地 HTML: " + out_path + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
