#!/usr/bin/env python3
# yuanzi-wechat-suite / scripts/master/v7_check.py
# 元子公众号图文 v7 master 散文体自动校验
# 用法：
#   python3 v7_check.py <article.md>
#   python3 v7_check.py --stdin  # 从 stdin 读
#
# 8 大铁律（v7 master + v8 prose 实战沉淀）：
#   1. 事实可考据    — 仅标记，不自动校验（无外部知识库）
#   2. 谁在说话      — 0 命中「龙虾5号 / 吾 / 汝 / 智能体 / AI / 讲得很清楚 / 直接点破」
#   3. 入戏不套话    — 0 命中「上节讲 / 这节讲 / 上两节 / 讲到这，我们一起想」
#   4. 行文节奏      — 仅标记每节是否有「数据/事实/案例」开头
#   5. 散文体 4 不妥协（v8）：
#      5a. 句长 35-50 字/句（汉语按字符计）
#      5b. 短句（<20 字）占比 < 20%
#      5c. 字数 800-3,500（老板号调性，非 v7 铁律 8,500-9,500）
#      5d. 关键词密度 > 50/万字（文学类）
#   6. 4 禁句开头：
#      - "X，反差很大——"
#      - "很多人 X，但 Y" / "很多人以为 X，其实 Y"
#      - "先看几个数字 / 先说几个数据"
#      - "谈到 X，不得不提 Y"
#
# 输出：JSON 含 PASS/FAIL + 违规清单 + 文本统计

import sys
import re
import json
from pathlib import Path


def clean_markdown(text: str) -> str:
    """剥 markdown 标记：标题、链接、强调、代码块、图片。"""
    # 去掉代码块
    text = re.sub(r"```[\s\S]*?```", "", text)
    # 去掉行内代码
    text = re.sub(r"`[^`]+`", "", text)
    # 去掉图片
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    # 去掉链接
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    # 去掉标题标记
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    # 去掉强调
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    # 合并空行
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_sentences_zh(text: str) -> list:
    """中文按句末标点切句（。！？ + 换行）"""
    # 按 。！？ 切句
    parts = re.split(r"[。！？]", text)
    # 合并空段
    return [p.strip() for p in parts if p.strip()]


def split_paragraphs(text: str) -> list:
    """按空行分段"""
    paras = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paras if p.strip()]


def check_v7(article: str) -> dict:
    """v7 + v8 散文体校验，返回 result dict"""
    raw_text = article
    clean = clean_markdown(article)
    chars = len(re.sub(r"\s", "", clean))
    sentences = split_sentences_zh(clean)
    paragraphs = split_paragraphs(clean)

    result = {
        "chars_total": chars,
        "sentences_count": len(sentences),
        "paragraphs_count": len(paragraphs),
        "violations": [],
        "warnings": [],
        "stats": {},
    }

    # 5a / 5b — 句长统计
    sentence_lengths = [len(s) for s in sentences]
    if sentence_lengths:
        avg_len = sum(sentence_lengths) / len(sentence_lengths)
        short_count = sum(1 for n in sentence_lengths if n < 20)
        short_ratio = short_count / len(sentence_lengths)
        result["stats"]["avg_sentence_len"] = round(avg_len, 1)
        result["stats"]["short_sentence_ratio"] = round(short_ratio * 100, 1)
        result["stats"]["sentence_lengths"] = sentence_lengths

        # 5a
        if avg_len < 35 or avg_len > 50:
            result["violations"].append(
                f"句长均值 {avg_len:.1f} 字，应在 35-50 范围"
            )

        # 5b
        if short_ratio > 0.20:
            result["violations"].append(
                f"短句占比 {short_ratio * 100:.1f}%，应 < 20%"
            )

    # 5c — 字数
    if chars < 800 or chars > 3500:
        result["violations"].append(
            f"字数 {chars}，老板号调性范围 800-3,500"
        )

    # 2 — 谁在说话
    who_violations = {
        "龙虾5号": r"龙虾\s*5\s*号",
        "吾": r"(?<![\u4e00-\u9fff])吾(?![\u4e00-\u9fff])",
        "汝": r"(?<![\u4e00-\u9fff])汝(?![\u4e00-\u9fff])",
        "智能体": r"智能体",
        "AI（评估者视角）": r"AI(?! 转型)",
        "X 讲得很清楚": r"讲得很清楚",
        "直接点破": r"直接点破",
    }
    for label, pat in who_violations.items():
        hits = re.findall(pat, clean)
        if hits:
            result["violations"].append(
                f"[谁在说话] 命中 {len(hits)} 次「{label}」"
            )

    # 3 — 入戏不套话
    taohua_violations = {
        "上节讲": r"上节讲",
        "这节讲": r"这节讲",
        "上两节": r"上两节",
        "讲到这，我们一起想": r"讲到这.{0,5}一起想",
        "老板 2026-06-27 给我讲的一段话": r"老板\s*202\d.*给我讲",
    }
    for label, pat in taohua_violations.items():
        hits = re.findall(pat, clean)
        if hits:
            result["violations"].append(
                f"[入戏不套话] 命中 {len(hits)} 次「{label}」"
            )

    # 6 — 4 禁句开头
    first_para = paragraphs[0] if paragraphs else ""
    forbidden_openers = {
        "反差很大——": r"反差\s*很大",
        "很多人 X，但 Y / 很多人以为 X，其实 Y": r"很多人.{1,15}(但|其实)",
        "先看几个数字 / 先说几个数据": r"先(看|说).{0,5}(几个|几组)?(数字|数据)",
        "谈到 X，不得不提 Y": r"谈到.{2,15}不得不提",
    }
    for label, pat in forbidden_openers.items():
        if re.search(pat, first_para[:200]):
            result["violations"].append(
                f"[4 禁句] 开头命中「{label}」"
            )

    # 1 / 4 — 仅做提示，不阻断
    if re.search(r"\d{4}\s*年", clean):
        result["warnings"].append(
            "[事实可考据] 文中含年份，请确保来源可公开验证"
        )

    # overall
    result["pass"] = len(result["violations"]) == 0
    return result


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(
            "用法：\n"
            "  python3 v7_check.py <article.md|article.txt>\n"
            "  python3 v7_check.py --stdin  # 从 stdin 读"
        )
        return 0

    if argv[1] == "--check":
        print("[OK] v7_check.py 可用")
        return 0

    if argv[1] == "--stdin":
        text = sys.stdin.read()
    else:
        path = Path(argv[1])
        if not path.exists():
            print(f"[X] 文件不存在: {path}")
            return 1
        text = path.read_text(encoding="utf-8")

    result = check_v7(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
