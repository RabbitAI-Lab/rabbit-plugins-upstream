#!/usr/bin/env python3
"""校验生成的报告:占位符替换干净、注入的 JSON 能被浏览器解析。"""
import json
import re
import sys

import console  # noqa: F401

HTML = "data/score-report.html"


def main():
    html = open(HTML, encoding="utf-8").read()

    m = re.search(r'<script\b[^>]*\bid=["\']score-data["\'][^>]*>(.*?)</script>',
                  html, re.S)
    if not m:
        print("✗ 找不到 score-data script 标签")
        return 1

    if "__SCORE_DATA__" in m.group(1):
        print("✗ script 标签里的占位符没被替换")
        return 1

    # 注释里提到占位符名字是正常的(模板在说明用途),只要没被灌进 JSON 就行
    leftover = html.count("__SCORE_DATA__")
    if leftover:
        print(f"  注:模板注释里还有 {leftover} 处占位符字样,未被注入(正确)")

    # 还原 build_report.py 对 </ 的转义
    raw = m.group(1).replace("<\\/", "</")
    d = json.loads(raw)

    print("✓ 注入的 JSON 可解析")
    print(f"  题数: {len(d['per_question'])}")
    bn = d["bottleneck"]
    print(f"  瓶颈: {bn['dimension']} / {bn['label']} = {bn['score']}")
    print(f"  partial: {d['partial']} | answered: {d['answered_count']}")
    q1 = d["per_question"][0]
    print(f"  q1 题干已回填: {bool(q1.get('question'))}")
    print(f"  q1 摘录: {q1['answer_excerpt'][:28]}…")
    print(f"  q1 语音时长: {q1['duration_sec']}")
    print(f"  报告体积: {len(html):,} 字节(自包含)")

    # 报告不能引本地相对资源,否则单独发给别人就裂了
    ext = re.findall(r'(?:src|href)="(?!https?://|#|data:)([^"]+)"', html)
    if ext:
        print(f"  ⚠ 引用了本地相对资源,单独分享会裂: {ext}")
    else:
        print("  ✓ 无本地相对引用")
    return 0


if __name__ == "__main__":
    sys.exit(main())
