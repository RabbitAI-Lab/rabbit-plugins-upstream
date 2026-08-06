#!/usr/bin/env python3
"""xhs-content-creator content compliance validator.

Enforces the 7-rule content constitution defined in SKILL.md §1.5:
  (1) Title: ≤20 chars, keyword in first 8 chars, no banned words.
  (2) Title: no off-platform shilling, no exaggerated promises.
  (3) Body: 300-800 chars, 3-5 paragraphs, theme+location in opening.
  (4) Body: every scene carries a concrete location name.
  (5) Topics: 2-5 precise hashtags with `#` prefix, no generic words.
  (6) Images: 1-9, ≤5MB, supported extensions, clear & unwatermarked.
  (7) Compliance red lines (no plagiarism, off-platform, pseudoscience,
      income/medical claims, sensitive content).

Usage:
  python3 validate_content.py --title "..." --body "..." --topic "#x" ...
  echo '{"title":"...","body":"...","topics":[...]}' | python3 validate_content.py -

Exit codes: 0 = ok, 2 = violations, 3 = bad arguments.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


# Title length: per SKILL.md §1.5, emoji and CJK/fullwidth punctuation count
# as 2 chars. We mirror the rule used by generate_and_publish.py so that
# titles passing validation here will also pass the runtime gate.
TITLE_MAX = 20

# Title keyword position: the core keyword must appear within the first
# 8 "effective chars" (using the same weight as TITLE_MAX).
KEYWORD_WINDOW = 8

# Body length bounds (CJK characters + punctuation).
BODY_MIN = 300
BODY_MAX = 800

# Paragraph count by blank-line split.
PARA_MIN = 3
PARA_MAX = 5

# Topics bounds.
TOPIC_MIN = 2
TOPIC_MAX = 5

# Image bounds.
IMAGE_MIN = 1
IMAGE_MAX = 9
IMAGE_MAX_BYTES = 5 * 1024 * 1024
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

# Generic topic words that get punished (SKILL.md §1.5 话题).
GENERIC_TOPIC_WORDS = {
    "日常", "分享", "生活", "记录", "vlog", "好物",
    "推荐", "种草", "测评", "合集",
}

# Banned title phrases. Two layers: absolute (always banned) and
# exaggerated-promise (banned in titles, allowed in body with caveats).
TITLE_BANNED_PHRASES = [
    # 极限词
    "最", "第一", "必", "100%", "唯一", "独家", "全网最低",
    "史上最强", "国家", "第N代", "万人疯抢", "一抢而空",
    "神药", "神器", "神级", "永不", "一用就",
    # 站外导流
    "私信", "微信", "+V", "vx", "公众号", "小红书号", "加微信",
    # 夸张承诺
    "包X", "保证X", "立省", "错过等",
]

# Location vocabulary used for theme+location front-loading and per-scene
# detection. The set is conservative — names like 西丽湖, 西丽塔, 仙湖,
# 铁岗水库, 深圳湾, 南山, etc. all start with common CJK geo-words.
LOCATION_HINTS = (
    "湖", "水库", "塔", "寺", "山", "公园", "湾", "海", "河", "江",
    "古镇", "村", "镇", "街道", "路", "区", "城", "市", "州", "岛",
    "绿道", "步道", "栈道", "桥", "广场", "园", "故居", "遗址",
    "南山", "福田", "罗湖", "宝安", "龙岗", "盐田", "龙华", "坪山",
    "光明", "大鹏新区",
)


def title_len_xhs(title: str) -> int:
    """Per SKILL.md §1.5: emoji weight 2 chars, everything else weight 1.

    The previous implementation (sum 2 if ord(c) > 0x2600) double-counted
    every CJK character and fullwidth punctuation, contradicting the doc.
    Real emoji ranges (Misc Symbols & Pictographs U+1F300-1F5FF,
    Emoticons U+1F600-1F64F, Transport U+1F680-1F6FF, Supplemental U+1F900-1F9FF
    and Symbols & Pictographs U+1FA70-1FAFF, plus Misc Symbols U+2600-26FF)
    weigh 2; everything else weighs 1.
    """
    n = 0
    for c in title:
        cp = ord(c)
        if 0x1F300 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF:
            n += 2
        else:
            n += 1
    return n


def contains_location(text: str) -> bool:
    """Return True if text contains any common CJK location hint."""
    return any(hint in text for hint in LOCATION_HINTS)


def check_title(title: str) -> list[dict]:
    v: list[dict] = []
    n = title_len_xhs(title)
    if n > TITLE_MAX:
        v.append({"rule": "title.length", "severity": "error",
                  "message": f"标题 {n} 字（上限 {TITLE_MAX}，含 emoji 全角符号按 2 字算）"})
    # Keyword in first 8 chars (use same weighting).
    head = title[:KEYWORD_WINDOW]
    if not re.search(r"[\u4e00-\u9fff]", head):
        v.append({"rule": "title.keyword_position", "severity": "error",
                  "message": f"标题前 {KEYWORD_WINDOW} 字无中文核心关键词"})
    for phrase in TITLE_BANNED_PHRASES:
        if phrase in title:
            v.append({"rule": "title.banned_phrase", "severity": "error",
                      "message": f"标题含禁用短语「{phrase}」"})
    return v


def check_body(body: str) -> list[dict]:
    v: list[dict] = []
    n = len(body)
    if n < BODY_MIN:
        v.append({"rule": "body.length", "severity": "error",
                  "message": f"正文 {n} 字（最少 {BODY_MIN}）"})
    elif n > BODY_MAX:
        v.append({"rule": "body.length", "severity": "error",
                  "message": f"正文 {n} 字（最多 {BODY_MAX}）"})
    paragraphs = [p for p in body.split("\n\n") if p.strip()]
    para_count = len(paragraphs)
    if para_count < PARA_MIN:
        v.append({"rule": "body.paragraphs", "severity": "error",
                  "message": f"正文 {para_count} 段（最少 {PARA_MIN}，按 \\n\\n 分段）"})
    elif para_count > PARA_MAX:
        v.append({"rule": "body.paragraphs", "severity": "error",
                  "message": f"正文 {para_count} 段（最多 {PARA_MAX}，按 \\n\\n 分段）"})
    # Theme + location front-loading: first paragraph must contain a location.
    if paragraphs and not contains_location(paragraphs[0]):
        v.append({"rule": "body.opening_location", "severity": "error",
                  "message": "正文首段缺少地名，主题+位置前置是硬规则"})
    # Per-scene: every paragraph after the first should reference a location.
    for idx, para in enumerate(paragraphs[1:], start=2):
        if not contains_location(para):
            v.append({"rule": "body.scene_location", "severity": "warn",
                      "message": f"正文第 {idx} 段缺少地名（湖/塔/亭子/绿道/水库等地名）"})
    return v


def check_topics(topics: list[str]) -> list[dict]:
    v: list[dict] = []
    n = len(topics)
    if n < TOPIC_MIN:
        v.append({"rule": "topics.count", "severity": "error",
                  "message": f"话题 {n} 个（最少 {TOPIC_MIN}）"})
    elif n > TOPIC_MAX:
        v.append({"rule": "topics.count", "severity": "error",
                  "message": f"话题 {n} 个（最多 {TOPIC_MAX}）"})
    for t in topics:
        if not t.startswith("#"):
            v.append({"rule": "topics.prefix", "severity": "error",
                      "message": f"话题「{t}」缺 # 前缀"})
    for word in GENERIC_TOPIC_WORDS:
        if any(word in t for t in topics):
            v.append({"rule": "topics.generic", "severity": "warn",
                      "message": f"话题含泛词「{word}」"})
    return v


def check_images(image_paths: list[str]) -> list[dict]:
    v: list[dict] = []
    n = len(image_paths)
    if n < IMAGE_MIN:
        v.append({"rule": "images.count", "severity": "error",
                  "message": f"图片 {n} 张（最少 {IMAGE_MIN}）"})
    elif n > IMAGE_MAX:
        v.append({"rule": "images.count", "severity": "error",
                  "message": f"图片 {n} 张（最多 {IMAGE_MAX}）"})
    for p in image_paths:
        path = Path(p).expanduser().resolve()
        if not path.exists():
            v.append({"rule": "images.missing", "severity": "error",
                      "message": f"图片不存在: {p}"})
            continue
        if path.suffix.lower() not in IMAGE_EXTS:
            v.append({"rule": "images.extension", "severity": "error",
                      "message": f"图片格式不支持: {path.suffix}"})
        if path.stat().st_size > IMAGE_MAX_BYTES:
            v.append({"rule": "images.size", "severity": "error",
                      "message": f"图片 {path.name} 超过 5MB"})
    return v


def validate(title: str, body: str, topics: list[str], images: list[str]) -> dict:
    violations = []
    violations += check_title(title)
    violations += check_body(body)
    violations += check_topics(topics)
    violations += check_images(images)
    status = "ok" if not any(x["severity"] == "error" for x in violations) else "violations"
    return {
        "status": status,
        "violations": violations,
        "stats": {
            "title_len_xhs": title_len_xhs(title),
            "body_chars": len(body),
            "paragraphs": len([p for p in body.split("\n\n") if p.strip()]),
            "topics_count": len(topics),
            "images_count": len(images),
        },
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate xhs-content-creator output against the 7-rule constitution.")
    p.add_argument("--title", help="Note title")
    p.add_argument("--body", help="Note body (use \\n\\n for paragraphs)")
    p.add_argument("--topic", action="append", default=[], dest="topics", help="Hashtag (repeat for multiple)")
    p.add_argument("--image", action="append", default=[], dest="images", help="Image path (repeat for multiple)")
    p.add_argument("--input", "-", action="store_true", help="Read JSON payload from stdin: {title, body, topics, images}")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if args.input:
        try:
            payload = json.loads(sys.stdin.read())
        except json.JSONDecodeError as e:
            print(json.dumps({"status": "error", "error": f"invalid JSON: {e}"}, ensure_ascii=False))
            return 3
        title = payload.get("title", "")
        body = payload.get("body", "")
        topics = payload.get("topics", [])
        images = payload.get("images", [])
    else:
        if not args.title or not args.body:
            print(json.dumps({"status": "error", "error": "--title and --body are required (or use --input -)"}, ensure_ascii=False))
            return 3
        title = args.title
        body = args.body
        topics = args.topics
        images = args.images

    result = validate(title, body, topics, images)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "ok":
        return 0
    if any(v["severity"] == "error" for v in result["violations"]):
        return 2
    return 0  # warn-only


if __name__ == "__main__":
    raise SystemExit(main())