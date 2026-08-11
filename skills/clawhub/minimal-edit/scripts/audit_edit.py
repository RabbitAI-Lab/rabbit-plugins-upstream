#!/usr/bin/env python3
"""Audit a minimal edit by comparing before/after text.

Usage:
    python audit_edit.py --before before.txt --after after.txt
    python audit_edit.py --before-text "old" --after-text "new" --must-remove "综上所述"

Marker lists are heuristic and incomplete. They cannot replace manual judgment.
"""

import argparse
import difflib
import re
import sys

CN_MARKERS = [
    "综上所述",
    "综上可见",
    "总体来看",
    "总体而言",
    "值得注意的是",
    "需要注意的是",
    "需要指出的是",
    "换言之",
    "换句话说",
    "更准确地说",
    "更具体地说",
    "需要说明的是",
    "不难发现",
    "毋庸置疑",
    "显而易见",
    "毫无疑问",
    "从某种意义上说",
    "改动如下",
    "修改如下",
    "赋能",
    "抓手",
    "闭环",
    "颗粒度",
    "场景化",
    "生态化",
    "平台化",
    "底层逻辑",
    "战略协同",
    "深度绑定",
    "价值最大化",
    "一站式",
    "全方位",
    "多维度",
    "系统性",
    "组合拳",
    "矩阵",
    "拉通",
    "对齐",
    "沉淀",
    "方法论",
    "打法",
    "降本增效",
    "提质增效",
    "共建",
    "打通",
    "深耕",
    "聚焦",
    "打造",
    "构建",
    "助力",
    "驱动",
    "撬动",
    "释放",
]

EN_MARKERS = [
    "in conclusion",
    "to summarize",
    "to sum up",
    "all in all",
    "it is worth noting",
    "it should be noted",
    "it is important to note",
    "needless to say",
    "moreover",
    "furthermore",
    "in other words",
    "to put it another way",
    "more precisely",
    "that is to say",
    "leverage",
    "synergy",
    "holistic",
    "ecosystem",
    "end-to-end",
    "seamless",
    "cutting-edge",
    "game-changer",
    "paradigm shift",
    "actionable insights",
    "key takeaways",
    "next steps",
    "empower",
    "unlock",
    "streamline",
    "robust",
    "granular",
    "landscape",
    "pivotal",
    "underscore",
    "delve",
]


def normalize(text):
    return re.sub(r"\s+", "", text)


def find_new_markers(before, after):
    lowered_before = before.lower()
    lowered_after = after.lower()
    found = []
    for marker in CN_MARKERS:
        if marker in after and marker not in before:
            found.append(marker)
    for marker in EN_MARKERS:
        if marker in lowered_after and marker not in lowered_before:
            found.append(marker)
    return found


def main():
    parser = argparse.ArgumentParser(description="Audit a minimal text edit.")
    before_group = parser.add_mutually_exclusive_group(required=True)
    before_group.add_argument("--before", help="Original text file")
    before_group.add_argument("--before-text", help="Original text passed inline")
    after_group = parser.add_mutually_exclusive_group(required=True)
    after_group.add_argument("--after", help="Edited text file")
    after_group.add_argument("--after-text", help="Edited text passed inline")
    parser.add_argument(
        "--must-remove",
        action="append",
        default=[],
        help="Phrase the user asked to delete; repeat for multiple phrases",
    )
    parser.add_argument("--threshold", type=float, default=1.5, help="Max new/old ratio")
    parser.add_argument("--fail", action="store_true", help="Exit 1 on warnings")
    args = parser.parse_args()

    if args.before is not None:
        with open(args.before, encoding="utf-8") as fh:
            before = fh.read()
    else:
        before = args.before_text

    if args.after is not None:
        with open(args.after, encoding="utf-8") as fh:
            after = fh.read()
    else:
        after = args.after_text

    nb = normalize(before)
    na = normalize(after)
    matcher = difflib.SequenceMatcher(None, nb, na)

    changed_old = 0
    changed_new = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag in ("replace", "insert"):
            changed_old += i2 - i1
            changed_new += j2 - j1
        elif tag == "delete":
            changed_old += i2 - i1

    warnings = []
    if changed_old > 0:
        ratio = changed_new / changed_old
        if ratio > args.threshold:
            warnings.append(
                f"new changed text is {changed_new} chars vs {changed_old} old chars "
                f"(ratio {ratio:.2f} > {args.threshold})"
            )

    new_markers = find_new_markers(before, after)
    if new_markers:
        warnings.append(
            "new AI-flavor candidates (manual review): " + ", ".join(new_markers)
        )

    if after.count("**") > before.count("**"):
        warnings.append("added bold markers")

    if changed_new > changed_old + 80:
        warnings.append(f"added {changed_new - changed_old} chars beyond the replaced text")

    for phrase in args.must_remove:
        if phrase in before and phrase in after:
            warnings.append(f"must-remove phrase still present: {phrase}")
        elif phrase not in before:
            warnings.append(f"must-remove phrase not found in original: {phrase}")

    print(f"chars before={len(nb)} after={len(na)} changed_old={changed_old} changed_new={changed_new}")
    for warning in warnings:
        print("WARN:", warning)
    if not warnings:
        print("OK: no expansion, deletion, or AI-flavor warnings.")
    print("NOTE: marker lists are heuristic and incomplete; manual judgment still required.")

    if args.fail and warnings:
        sys.exit(1)


if __name__ == "__main__":
    main()
