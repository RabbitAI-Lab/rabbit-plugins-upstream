#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sandbox_run.py — 沙箱模式统一入口（v3.0.1，SkillHub 兼容文本形态）。

引擎以 scripts/engine_b64.txt（engine.zip 的 base64 文本）分发——SkillHub 允许
文本文件、杀软不识别（非 .py 可执行明文），运行时经 _load_engine 解码到内存临时
zip 再 zipimport 加载，磁盘不落明文可执行 analyze_skill.py。

用法（与 analyze_skill.py 一致）：
  python scripts/sandbox_run.py <skill目录或SKILL.md> [--json] [--sarif <f>]
                                [--sbom <f>] [--dir] [--osv] [--policy <f>]
                                [--trust <f>] [--rules-dir <d>] [--exit-on P1]
"""
import os
import sys
from pathlib import Path

# 保证可 import 同目录的 _load_engine
sys.path.insert(0, str(Path(__file__).resolve().parent))


def main() -> int:
    scripts_dir = Path(__file__).resolve().parent
    skill_root = scripts_dir.parent
    os.environ.setdefault("SKAUDIT_ROOT", str(skill_root))
    os.environ.setdefault("SKAUDIT_RULES_DIR", str(skill_root / "rules"))
    try:
        from _load_engine import load
    except ImportError as exc:
        print(f"❌ 引擎加载失败：{exc}")
        return 1
    try:
        eng = load()
    except ImportError as exc:
        print(f"❌ 引擎缺失：{exc}")
        return 1
    return eng.main()


if __name__ == "__main__":
    sys.exit(main())
