"""
check_numbering — 层次序数（章节标题）序号正确性检查

依据：GB/T 9704-2012 §7.3.3.2 公文层次序数规范
    一级「一、」  二级「（一）」  三级「1.」  四级「①」

机器可检查项（仅针对被识别为层次序数的段落）：
1. 层级合法性（层级跳跃）：子级必须紧邻父级出现，不能跨级
   —— 例如「一、」之后直接出现「1.」（缺「（一）」）属结构错误（ERROR）
2. 序号连续性：同一父级下，同级序号应从 1 顺序递增，缺号即告警（WARN）
3. 序号重复性：同一父级下出现两个「一、」属错误（ERROR）
4. 前缀层级一致性：标题文本前缀（如「（一）」）与其所在嵌套层级不符（WARN）
5. 起点合法性：首个层次序数应为一级「一、」（WARN）

本模块导出两个入口：
- `validate_layer_list(layers)`：纯函数，输入层次段落列表，输出问题 dict 列表。
  被 Word 路径（check.py）与 Markdown 路径（md_parser.py）共用，避免逻辑分叉。
- `run(doc, lib)`：check.py 检查器标准入口，基于 python-docx 文档对象识别层次序数段落。
"""
from __future__ import annotations

import re
from typing import Dict, List, Optional

from docx.oxml.ns import qn

from report import Issue, Severity, CheckResult

CHECK_ID = "layer-numbering"
CHECK_NAME = "层次序数序号正确性"

# 各层级文本前缀正则
PAT_L1 = re.compile(r"^[一二三四五六七八九十]+、")
PAT_L2 = re.compile(r"^[（(][一二三四五六七八九十]+[)）]")
PAT_L3 = re.compile(r"^\d+[\.．]")
PAT_L4 = re.compile(r"^[（(]\d+[)）]")
# 综合：命中任一即视为层次序数段（供 Word 路径初筛）
PAT_LAYER_ANY = re.compile(
    r"^\s*("
    r"[一二三四五六七八九十]+、|"
    r"[（(][一二三四五六七八九十]+[)）]|"
    r"\d+[\.．]|"
    r"[（(]\d+[)）]"
    r")"
)

_CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩"
_CN_DIGITS = {
    "零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
    "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
}

_CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩"  # 兼容旧式带圈数字，识别时仍作为层次序数处理


def _chinese_to_int(s: str) -> Optional[int]:
    """把中文数字（1-99）转整数。失败返回 None。"""
    if not s:
        return None
    if s == "十":
        return 10
    if "十" in s:
        left, _, right = s.partition("十")
        tens = _CN_DIGITS.get(left, 1) if left else 1
        ones = _CN_DIGITS.get(right, 0) if right else 0
        return tens * 10 + ones
    total = 0
    for ch in s:
        if ch in _CN_DIGITS:
            total = total * 10 + _CN_DIGITS[ch]
        else:
            return None
    return total if total > 0 else None


def _infer_level(text: str) -> Optional[int]:
    """由文本前缀推断层级（1-4），无前缀返回 None。"""
    if PAT_L1.match(text):
        return 1
    if PAT_L2.match(text):
        return 2
    if PAT_L3.match(text):
        return 3
    if PAT_L4.match(text):
        return 4
    return None


def _parse_index(text: str, level: int) -> Optional[int]:
    """从文本中提取该层级的序号数值（1-99），无则返回 None。"""
    if level == 1:
        m = PAT_L1.match(text)
        if m:
            return _chinese_to_int(m.group(0)[:-1])
    elif level == 2:
        m = PAT_L2.match(text)
        if m:
            inner = m.group(0)[1:-1]
            return _chinese_to_int(inner)
    elif level == 3:
        m = PAT_L3.match(text)
        if m:
            return int(m.group(0)[:-1])
    elif level == 4:
        m = PAT_L4.match(text)
        if m:
            inner = m.group(0)[1:-1]
            try:
                return int(inner)
            except ValueError:
                return None
    return None


def validate_layer_list(layers: List[Dict]) -> List[Dict]:
    """对层次序数段落列表做序号正确性检查。

    参数 layers：每个元素为 dict，含字段
        idx         段落序号（用于定位，整数）
        level       显式层级（int|None，Markdown 路径由标题级数给出；Word 路径为 None）
        text        段落文本
        numPr_ilvl  Word 自动编号的 ilvl（int|None，0..3）

    返回：问题 dict 列表，每项含 severity / title / message / location / fix。
    """
    issues: List[Dict] = []
    prev_level = 0
    last_index = [0, 0, 0, 0]            # 各层级最近一次用到的序号（1-based，0=未用）
    seen = [set(), set(), set(), set()]  # 各层级在当前父链下出现过的序号

    for entry in layers:
        idx = entry.get("idx")
        explicit = entry.get("level")
        text = (entry.get("text") or "").strip()
        numpr = entry.get("numPr_ilvl")

        # 确定有效层级：显式 > numPr ilvl > 文本前缀推断
        eff = explicit
        if eff is None and numpr is not None:
            eff = numpr + 1
        if eff is None:
            eff = _infer_level(text)
        if eff is None or eff < 1 or eff > 4:
            # 无法判定层级，跳过严格校验，但保留 prev 不推进
            continue

        # 起点合法性：首个层次序数应为一级
        if prev_level == 0 and eff != 1:
            issues.append({
                "severity": "WARN",
                "title": "章节未从一级序号开始",
                "message": (
                    f"第 {idx} 段「{text[:24]}」以第 {eff} 级序号开头，"
                    f"公文层次序数通常应从一级「一、」起始，可能缺失上级标题。"
                ),
                "location": f"第 {idx} 段",
                "fix": "在前面补充对应的一级（或更高级）标题，或将该段改为一级「一、」。",
            })

        # 层级跳跃：子级必须紧邻父级，不能跨级
        if prev_level > 0 and eff > prev_level + 1:
            issues.append({
                "severity": "ERROR",
                "title": "层次序号层级跳跃",
                "message": (
                    f"第 {idx} 段「{text[:24]}」位于第 {prev_level} 级之后却直接跳到第 {eff} 级，"
                    f"缺少中间层级（如一级「一、」之后应先有二级「（一）」）。"
                ),
                "location": f"第 {idx} 段",
                "fix": "补齐缺失的中间层级，或调整该段的层级归属。",
            })

        # 回退/上跳时，重置更深层级计数器（保留当前级自身的连续性）
        if eff < prev_level:
            for k in range(eff, 4):   # 重置层级值 > eff 的计数器（0-based 索引 >= eff）
                last_index[k] = 0
                seen[k].clear()

        # 序号数值校验
        num = _parse_index(text, eff)
        if num is not None:
            if num <= 0:
                issues.append({
                    "severity": "WARN",
                    "title": "序号取值异常",
                    "message": f"第 {idx} 段「{text[:24]}」解析到的序号非正，请检查编号。",
                    "location": f"第 {idx} 段",
                    "fix": "修正该层次的序号，使其为合法正整数。",
                })
            else:
                if num in seen[eff - 1]:
                    issues.append({
                        "severity": "ERROR",
                        "title": "同层序号重复",
                        "message": (
                            f"第 {idx} 段「{text[:24]}」的序号 {num} "
                            f"与同层级前述段落重复，同一父级下序号应唯一。"
                        ),
                        "location": f"第 {idx} 段",
                        "fix": "修改重复的序号，或确认是否遗漏了更高级别的父标题。",
                    })
                else:
                    expected = last_index[eff - 1] + 1
                    if last_index[eff - 1] > 0 and num != expected:
                        if num > expected:
                            issues.append({
                                "severity": "WARN",
                                "title": "序号不连续（可能缺号）",
                                "message": (
                                    f"第 {idx} 段「{text[:24]}」序号为 {num}，"
                                    f"而上一层级下该级序号应从 {expected} 开始，疑似缺失中间编号。"
                                ),
                                "location": f"第 {idx} 段",
                                "fix": "补回缺失的序号，或检查是否有章节被删除/遗漏。",
                            })
                        else:
                            issues.append({
                                "severity": "WARN",
                                "title": "序号回退/乱序",
                                "message": (
                                    f"第 {idx} 段「{text[:24]}」序号为 {num}，"
                                    f"小于同层级已出现的 {last_index[eff - 1]}，顺序不合理。"
                                ),
                                "location": f"第 {idx} 段",
                                "fix": "按递增顺序重新排列该层级序号。",
                            })
                    seen[eff - 1].add(num)
                    last_index[eff - 1] = num

        # 前缀层级与嵌套层级一致性（显式层级已知时才有意义，如 Markdown 路径）
        nat = _infer_level(text)
        if explicit is not None and nat is not None and nat != explicit:
            issues.append({
                "severity": "WARN",
                "title": "前缀层级与所在层级不符",
                "message": (
                    f"第 {idx} 段文本前缀属第 {nat} 级（如「{'一、' if nat==1 else '（一）' if nat==2 else '1.' if nat==3 else '（1）'}」），"
                    f"但按文档结构它位于第 {explicit} 级，前缀与位置不一致。"
                ),
                "location": f"第 {idx} 段",
                "fix": "统一文本前缀与标题层级（建议删除前缀，交由自动编号生成）。",
            })

        prev_level = eff

    return issues


def _para_numpr_ilvl(para) -> Optional[int]:
    """读取段落 Word 自动编号的 ilvl（0..3），无则返回 None。"""
    pPr = para._p.pPr
    if pPr is None:
        return None
    numPr = pPr.find(qn("w:numPr"))
    if numPr is None:
        return None
    num_id_el = numPr.find(qn("w:numId"))
    if num_id_el is None or num_id_el.get(qn("w:val")) in (None, "0"):
        return None
    ilvl_el = numPr.find(qn("w:ilvl"))
    if ilvl_el is None:
        return 0
    try:
        return int(ilvl_el.get(qn("w:val")))
    except (TypeError, ValueError):
        return 0


def run(doc, lib) -> CheckResult:
    """check.py 入口：扫描文档全部层次序数段落并校验序号正确性。"""
    result = CheckResult(check_id=CHECK_ID, check_name=CHECK_NAME)

    layers: List[Dict] = []
    for i, para in enumerate(doc.paragraphs):
        text = (para.text or "").strip()
        if not text:
            continue
        has_numpr = _para_numpr_ilvl(para) is not None
        if not (PAT_LAYER_ANY.match(text) or has_numpr):
            continue
        layers.append({
            "idx": i + 1,
            "level": None,
            "text": text,
            "numPr_ilvl": _para_numpr_ilvl(para),
        })

    if not layers:
        result.add(Issue(
            check_id=CHECK_ID,
            rule_id="NO-LAYER",
            severity=Severity.INFO,
            title="未识别到层次序数",
            message="文档中无「一、/（一）/1./①」等层次序数段落，跳过序号正确性检查。",
            reference="GB/T 9704-2012 §7.3.3.2",
        ))
        return result

    issues = validate_layer_list(layers)
    if not issues:
        result.add(Issue(
            check_id=CHECK_ID,
            rule_id="ALL-PASS",
            severity=Severity.PASS,
            title="层次序数序号正确",
            message=f"共 {len(layers)} 个层次序数段落，序号连续、层级合法、无重复。",
            reference="GB/T 9704-2012 §7.3.3.2",
        ))
        return result

    for it in issues:
        sev = Severity.ERROR if it["severity"] == "ERROR" else Severity.WARN
        result.add(Issue(
            check_id=CHECK_ID,
            rule_id=("NUM-JUMP" if sev == Severity.ERROR and "跳跃" in it["title"]
                     else "NUM-DUP" if sev == Severity.ERROR
                     else "NUM-WARN"),
            severity=sev,
            title=it["title"],
            message=it["message"],
            location=it["location"],
            fix=it.get("fix", ""),
            reference="GB/T 9704-2012 §7.3.3.2",
        ))
    return result
