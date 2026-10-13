#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_signature.py — 发布者签名链一键核验（v3.3.1）。

对随包 `publisher-signature.json` 逐项核验，检出**任何**关键文件被篡改或未同步改动：

  1. **引擎源码锚**：明文引擎源码 scripts/analyze_skill.txt 的 SHA-256 == engine_sha256；
  2. **文件锚**：anchors 中每个关键文件（引擎明文源码 / 规则完整性库 / 规则包清单 / 指令文件 /
     加载器与入口脚本）的 SHA-256 逐项相符；
  3. **签名摘要**：signature_digest == 对 (engine_sha256 + 排序后的 anchors) 的规范化 SHA-256
     （检出签名文件本身的损坏/被改写）。

退出码 0=全部通过，1=存在不符。

诚实标注：本核验为**完整性**防护，可检出篡改与未同步改动；它不构成对「发布后重新签名」的
密码学防护——根信任请以发布者对外公布的 `engine_sha256`（或独立源码核验包）为最终基准。
纯标准库实现，无第三方依赖。

用法：
  python scripts/verify_signature.py [--skill <skill根>]
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_signature_digest(engine_sha256: str, anchors: dict) -> str:
    """与 gen_signature.py 保持一致的规范化摘要算法。"""
    parts = ["engine_sha256=" + engine_sha256]
    for k in sorted(anchors):
        parts.append(f"{k}={anchors[k]}")
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


def verify(skill_root: Path) -> int:
    sig_p = skill_root / "publisher-signature.json"
    engine_p = skill_root / "scripts" / "analyze_skill.txt"
    if not sig_p.is_file():
        print(f"❌ 缺少 publisher-signature.json：{sig_p}")
        return 1
    if not engine_p.is_file():
        print(f"❌ 缺少明文引擎源码：{engine_p}")
        return 1
    try:
        sig = json.loads(sig_p.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"❌ publisher-signature.json 解析失败：{exc}")
        return 1

    problems = []
    anchor = sig.get("engine_sha256", "")
    if len(anchor) != 64:
        problems.append("engine_sha256 锚缺失或非法（应为 64 位十六进制）")

    # 1) 引擎源码锚
    engine_actual = ""
    try:
        engine_actual = _sha256_file(engine_p)
        if anchor and engine_actual != anchor:
            problems.append(f"引擎源码锚不符：期望 {anchor[:12]}… 实际 {engine_actual[:12]}…")
    except Exception as exc:
        problems.append(f"明文引擎源码读取失败：{exc}")

    # 2) 文件锚
    anchors = sig.get("anchors", {}) or {}
    if not anchors:
        problems.append("anchors 为空")
    for rel, expected in sorted(anchors.items()):
        fp = skill_root / rel
        if not fp.is_file():
            problems.append(f"锚定文件缺失：{rel}")
            continue
        actual = _sha256_file(fp)
        if actual != expected:
            problems.append(f"文件锚不符：{rel}（期望 {expected[:12]}… 实际 {actual[:12]}…）")

    # 3) 签名摘要（检出签名文件本身被改写/损坏）
    declared_digest = sig.get("signature_digest", "")
    if declared_digest:
        recomputed = compute_signature_digest(anchor, anchors)
        if recomputed != declared_digest:
            problems.append("signature_digest 不符（签名文件可能被改写或与锚不同步）")

    total_files = len(anchors)
    if problems:
        print("✗ 签名链核验失败（疑似被篡改或未同步）：")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("✓ 签名链核验通过：引擎源码锚 + "
          f"{total_files} 个文件锚 + 签名摘要全部相符")
    print(f"  engine_sha256: {anchor}")
    print(f"  signature_digest: {declared_digest[:16]}…" if declared_digest else "  signature_digest: (未设置)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="skill-analysis 发布者签名链核验")
    ap.add_argument("--skill", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    return verify(Path(args.skill))


if __name__ == "__main__":
    sys.exit(main())
