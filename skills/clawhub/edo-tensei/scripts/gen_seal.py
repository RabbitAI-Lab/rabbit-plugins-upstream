#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_seal.py —— 为「秽土转生」技能包生成权属溯源戳记 SEAL.json

用法:
    python gen_seal.py <技能包目录> [--version 1.0.0]

功能:
    1. 遍历技能包内所有文件，计算 SHA-256（排除 SEAL.json 自身与 .git）；
    2. 组装 files 清单 + package_sha256（全文件哈希拼接后的总哈希）；
    3. 对「排除 seal_hash 字段」的规范化 JSON 计算 seal_hash（自签哈希）；
    4. 写出 provenance/SEAL.json。

说明:
    - 本脚本只产出「内容指纹」，不加密技能内容；
    - 可信时间戳（RFC3161 TSA）需在本机发布时另行申请，再把 .tsr 一并备份。
"""

import argparse
import hashlib
import json
import os
import sys

# 与 SEAL.schema.json 保持一致的固定元数据
SKILL_ID = "edo-tensei-1fef9b18bc9c451395d4bf85c0814afd"
SKILL_NAME = "秽土转生 (Multi-Session Control Tower)"
AUTHOR_DECLARED = "晋锡斌"
AUTHOR_CONTACT = "jinxibin1993@foxmail.com"
CREATED_UTC = "2026-09-15T08:35:05Z"
WATERMARK = "edo-seal-1fef9b18bc9c451395d4bf85c0814afd"

# 计算哈希时跳过的项
SKIP_DIRS = {".git", "__pycache__", "node_modules"}
SKIP_FILES = {"SEAL.json"}


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_files(skill_dir: str):
    result = {}
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name in SKIP_FILES:
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, skill_dir).replace(os.sep, "/")
            result[rel] = {
                "sha256": sha256_of_file(full),
                "bytes": os.path.getsize(full),
            }
    return result


def build_seal(skill_dir: str, version: str) -> dict:
    files = collect_files(skill_dir)
    # 按相对路径排序，保证可复现
    ordered = {k: files[k] for k in sorted(files)}
    # package_sha256: 把所有文件哈希按序拼接再哈希
    concat = "".join(v["sha256"] for k, v in ordered.items())
    package_sha256 = hashlib.sha256(concat.encode("utf-8")).hexdigest()

    seal = {
        "skill_id": SKILL_ID,
        "skill_name": SKILL_NAME,
        "version": version,
        "author_declared": AUTHOR_DECLARED,
        "author_contact": AUTHOR_CONTACT,
        "created_utc": CREATED_UTC,
        "files": ordered,
        "package_sha256": package_sha256,
        "seal_hash": "",  # 先留空
        "watermark_token": WATERMARK,
        "tsa_timestamp": None,
        "notes": "本 SEAL 为权属溯源指纹，非加密。发布时建议另取可信时间戳（RFC3161 TSA）锚定存在时间。",
    }
    # 自签哈希：对排除 seal_hash 后的规范化 JSON 再哈希
    canonical = json.dumps(seal, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    seal["seal_hash"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return seal


def main():
    ap = argparse.ArgumentParser(description="生成秽土转生技能权属戳记 SEAL.json")
    ap.add_argument("skill_dir", help="技能包根目录")
    ap.add_argument("--version", default="1.0.0", help="本次版本号")
    args = ap.parse_args()

    skill_dir = os.path.abspath(args.skill_dir)
    if not os.path.isdir(skill_dir):
        print(f"[错误] 目录不存在: {skill_dir}", file=sys.stderr)
        sys.exit(1)

    seal = build_seal(skill_dir, args.version)
    out_dir = os.path.join(skill_dir, "provenance")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "SEAL.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(seal, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"[OK] 已生成: {out_path}")
    print(f"     文件数: {len(seal['files'])}")
    print(f"     package_sha256: {seal['package_sha256'][:16]}...")
    print(f"     seal_hash:      {seal['seal_hash'][:16]}...")


if __name__ == "__main__":
    main()
