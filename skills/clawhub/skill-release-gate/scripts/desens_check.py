#!/usr/bin/env python3
"""去敏复核 —— 验证发布物不含必须剥离的内部信息（离线，仅标准库）。

检查项：
  - 内部绝对路径（D:/ C:/ /Users/ /home/）
  - 内部项目代号 / 工作区路径片段
  - 明显的内部服务器名 (.internal / .local / .corp)
  - 客户/真实姓名占位（可由 --names 传入额外名单）

用法：
  python desens_check.py --path ./to_publish [--names 张三,李四]
退出码：0=通过，1=发现需去敏项，2=错误
"""
import argparse
import os
import re
import sys

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".vault", "venv"}
# 扫描器自身的源文件不参与自审（避免模式字符串自指命中）
SELF_SKIP = {"secret_scan.py", "desens_check.py"}
SCAN_EXT = {".md", ".py", ".js", ".ts", ".json", ".txt", ".yaml", ".yml", ".toml", ".sh", ".bat"}

# 仅匹配"真实内部路径形态"，避免裸 /c/ /d/ 误命中 URL 或无关文本
PATTERNS = {
    "绝对路径": re.compile(r"[A-Za-z]:\\[^\n\r]+|/(?:Users|home|root)/[\w.-]+"),
    "内网域名": re.compile(r"\b[\w-]+\.(?:internal|local|corp|lan)\b", re.I),
    "工作区片段": re.compile(r"2026-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}"),
}


def check(text, extra_names):
    hits = []
    for label, pat in PATTERNS.items():
        for m in pat.finditer(text):
            hits.append((label, m.group(0)))
    for name in extra_names:
        if name and name in text:
            hits.append(("真实姓名", name))
    return hits


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--path", required=True)
    p.add_argument("--names", default="", help="额外需剥离的真实姓名，逗号分隔")
    a = p.parse_args()
    extra = [n.strip() for n in a.names.split(",") if n.strip()]
    results = []
    if os.path.isfile(a.path):
        targets = [a.path]
    else:
        targets = []
        for root, dirs, files in os.walk(a.path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            fp_full = os.path.join(root, f)
            if os.path.basename(fp_full) in SELF_SKIP:
                continue
            if os.path.splitext(f)[1].lower() in SCAN_EXT:
                targets.append(fp_full)
    for fp in targets:
        try:
            with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            continue
        for label, snip in check(content, extra):
            results.append((fp, label, snip))
    if not results:
        print("[PASS] 去敏复核通过：未检出内部路径/内网域名/工作区片段/指定姓名。")
        sys.exit(0)
    print(f"[BLOCK] 去敏复核发现 {len(results)} 处需处理：")
    for fp, label, snip in results:
        print(f"  - {fp}  [{label}]  {snip}")
    sys.exit(1)


if __name__ == "__main__":
    main()
