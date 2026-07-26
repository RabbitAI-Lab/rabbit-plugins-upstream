#!/usr/bin/env python3
"""
Auto Reviser — 评审意见驱动的自动修订引擎
解析评审意见，定位原文段，生成修订Patch
"""

import json
import sys
import difflib
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class RevisionPatch:
    """修订补丁"""
    comment_id: str
    target_req: str
    location: str
    type: str  # enhance / add / fix / remove
    original: str
    revised: str
    rationale: str
    status: str = "pending"  # pending / applied / rejected


def parse_review_comment(comment: str) -> dict:
    """
    解析评审意见，提取: 需求定位 + 问题类型 + 修改方向

    支持格式:
    - "REQ-005: 技术方案缺少测试计划" → {target: REQ-005, type: add, direction: test_plan}
    - "报价明细表格式不规范" → {target: auto, type: fix, direction: format}
    """
    import re

    result = {
        "target_req": None,
        "type": "enhance",
        "direction": "",
        "original_comment": comment,
    }

    # 提取REQ-ID
    req_match = re.search(r'(REQ-\d{3})', comment)
    if req_match:
        result["target_req"] = req_match.group(1)

    # 判断修改类型
    type_keywords = {
        "add": ["缺少", "缺失", "没有", "未包含", "未提供", "需要补充", "增加", "新增", "添加"],
        "fix": ["错误", "不正确", "不规范", "不符合", "修正", "调整", "修改", "改正"],
        "remove": ["删除", "移除", "去掉", "冗余", "多余", "违规"],
        "enhance": ["不足", "不够", "不够深入", "需加强", "需完善", "深化", "增强", "补充"],
    }

    for t, keywords in type_keywords.items():
        for kw in keywords:
            if kw in comment:
                result["type"] = t
                break
        if result["type"] != "enhance":
            break

    # 提取修改方向
    result["direction"] = comment[:100]

    return result


def generate_revision_patch(comment: dict, original_text: str = "",
                            section_name: str = "未定位") -> RevisionPatch:
    """
    根据评审意见生成修订Patch

    Args:
        comment: 解析后的评审意见
        original_text: 原文内容(可选，用于生成前后对比)
        section_name: 所在章节名称
    """
    parsed = comment if isinstance(comment, dict) else parse_review_comment(comment)

    patch = RevisionPatch(
        comment_id=f"C-{hash(parsed['original_comment']) % 10000:04d}",
        target_req=parsed.get("target_req", "REQ-???"),
        location=section_name,
        type=parsed["type"],
        original=original_text or "[未能定位原文]",
        revised=_generate_revised_text(parsed, original_text),
        rationale=parsed["direction"],
    )

    return patch


def _generate_revised_text(parsed: dict, original: str) -> str:
    """根据修改方向生成修订后文本"""
    rev_type = parsed["type"]
    direction = parsed["direction"]

    if rev_type == "add":
        return f"{original}\n\n【新增内容】根据评审要求，补充以下内容：{direction}"

    elif rev_type == "fix":
        return f"【已修正】原内容已根据评审意见调整：{direction}\n{_mark_correction(original)}"

    elif rev_type == "remove":
        return "【已删除】根据评审意见，已移除原段落中不适当的内容。"

    elif rev_type == "enhance":
        return _enhance_text(original, direction)

    return original


def _mark_correction(text: str) -> str:
    """标记修正位置"""
    if not text:
        return "[原文为空]"
    return f"~~{text}~~ → [修正后文本]"


def _enhance_text(original: str, direction: str) -> str:
    """增强/深化内容"""
    if not original:
        return f"【深化内容】{direction}"
    return f"{original}\n\n【深化补充】根据评审专家意见，对以上内容进行了深化：\n- {direction}"


def generate_diff(original: str, revised: str) -> str:
    """生成文本Diff"""
    diff_lines = list(difflib.unified_diff(
        original.splitlines(keepends=True),
        revised.splitlines(keepends=True),
        fromfile="原始版本",
        tofile="修订版本",
        lineterm="",
    ))
    return "".join(diff_lines)


def batch_revise(comments: list[str], sections: dict[str, str] = None) -> list[dict]:
    """
    批量处理评审意见

    Args:
        comments: 评审意见字符串列表
        sections: {章节名: 原文内容} 映射

    Returns:
        修订Patch列表
    """
    if sections is None:
        sections = {}

    patches = []
    for i, comment in enumerate(comments):
        parsed = parse_review_comment(comment)
        parsed["original_comment"] = comment

        # 尝试定位原文段
        section_name = "未定位"
        original_text = ""
        for sec_name, sec_text in sections.items():
            if parsed.get("target_req") and parsed["target_req"] in sec_text:
                section_name = sec_name
                original_text = sec_text[:500]
                break

        patch = generate_revision_patch(parsed, original_text, section_name)
        patches.append(asdict(patch))

    return patches


def main():
    """CLI和演示模式"""
    if len(sys.argv) < 2 or "--demo" in sys.argv:
        # 演示模式
        comments = [
            "REQ-005: 技术方案缺少详细的测试计划和测试用例",
            "报价明细表格式不规范，需按照招标文件模板重新整理",
            "未包含7×24小时运维保障的具体SLA指标",
            "知识产权条款的响应不够深入，需补充开源软件使用声明",
        ]

        print("=== Auto Reviser Demo ===\n")
        print("评审意见:")
        for i, c in enumerate(comments, 1):
            print(f"  {i}. {c}")

        print("\n解析结果:")
        for c in comments:
            parsed = parse_review_comment(c)
            print(f"  目标: {parsed['target_req']} | 类型: {parsed['type']} | 方向: {parsed['direction'][:60]}...")

        print("\n修订Patch示例:")
        sections = {
            "第3.2节 技术方案": "技术方案包含架构设计和模块划分...\nREQ-005 相关技术参数已满足要求。",
            "第4.1节 报价明细": "报价明细表: 总计500万元，分3年付款...",
        }
        patches = batch_revise(comments, sections)
        for p in patches:
            print(f"  [{p['type']}] {p['target_req']} @ {p['location']}")
            print(f"    {p['rationale'][:80]}")
        return

    # JSON模式
    input_data = json.loads(sys.stdin.read() if len(sys.argv) == 1 else open(sys.argv[1]).read())

    if isinstance(input_data, list):
        patches = batch_revise(input_data)
    else:
        patches = batch_revise(
            input_data.get("comments", []),
            input_data.get("sections", {}),
        )

    print(json.dumps(patches, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
