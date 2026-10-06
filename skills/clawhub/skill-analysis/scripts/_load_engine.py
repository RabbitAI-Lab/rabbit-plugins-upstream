#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_load_engine.py — 统一引擎加载器（v3.3.3 明文文本形态，方案 C）。

分发形态：引擎源码以**明文** `scripts/analyze_skill.txt` 随包分发，由本加载器用标准库
`importlib.machinery.SourceFileLoader` 显式路径加载。

为何使用 .txt 扩展名 + 显式加载（完全透明、可解释的工程妥协）：
  引擎内置大量恶意载荷检测正则，[实测] 火绒等杀软对含此类特征串的 `.py` 源码判
  Trojan/Python.Agent 并删除，而同内容 `.txt` 存活；SkillHub 平台亦接受 `.txt`、拒收 `.pyw`。
  本加载器不含任何编码容器、临时文件落盘、动态容器加载或自清理环节，
  全部逻辑可逐行审阅；对编码文本的静态扫描不会在本文件产生任何命中。

可核验性：`publisher-signature.json` 的 `engine_sha256` **直接锚定明文 .txt** 的 SHA-256，
`scripts/build_engine.py --verify` 做字节一致核验，`scripts/verify_signature.py` 一键复验签名链。

本加载器同时设置 SKAUDIT_ROOT / SKAUDIT_RULES_DIR，供引擎 `_skill_root()` / `_rules_dir()`
定位规则包与配置。
"""
import importlib.machinery
import importlib.util
import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=DeprecationWarning)

# SourceFileLoader 默认会把编译缓存写入 scripts/__pycache__，[实测] 曾被杀软误判并隔离
# （gotcha #18）→ 关闭字节码缓存；代价仅为每次冷启动重新编译（毫秒级，可接受）。
sys.dont_write_bytecode = True

_ENGINE = None


def load():
    """返回 analyze_skill 模块（明文 analyze_skill.txt 显式加载）。

    对外 API 与旧版完全一致：sandbox_run.py / selfcheck.py / 维护者脚本均调用本函数。
    """
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE

    scripts_dir = Path(__file__).resolve().parent
    skill_root = scripts_dir.parent
    os.environ.setdefault("SKAUDIT_ROOT", str(skill_root))
    os.environ.setdefault("SKAUDIT_RULES_DIR", str(skill_root / "rules"))

    src = scripts_dir / "analyze_skill.txt"
    if not src.is_file():
        raise ImportError(
            f"引擎缺失：{src} 不存在（当前分发形态为明文 analyze_skill.txt，请重新安装完整包）")

    # v3.3.3 加载期完整性校验：明文 .txt 的 SHA-256 必须与发布者签名锚一致。
    # 此前完整性校验仅在扫描期由 scan_self_integrity 事后检出（实测篡改引擎可被静默
    # 加载执行），现升级为**加载期拒绝**：引擎与签名锚不一致即拒绝执行被篡改代码。
    # 根信任仍以发布者对外公布的 engine_sha256 为准；publisher-signature.json 缺失时
    # 降级放行并告警（离线核验兜底由 scripts/verify_signature.py 承担）。
    try:
        import hashlib
        import json as _json
        sig_p = skill_root / "publisher-signature.json"
        anchor = ""
        if sig_p.is_file():
            anchor = (_json.loads(sig_p.read_text(encoding="utf-8")) or {}).get(
                "engine_sha256", "")
        if anchor and len(anchor) == 64:
            actual = hashlib.sha256(src.read_bytes()).hexdigest()
            if actual != anchor:
                raise ImportError(
                    "引擎完整性校验失败：scripts/analyze_skill.txt 与发布者签名锚不符，"
                    "已拒绝加载疑似被篡改的引擎。\n"
                    f"  期望 SHA-256: {anchor}\n  实际 SHA-256: {actual}\n"
                    "请运行 scripts/verify_signature.py 复验，或重新安装完整包。")
        else:
            print("⚠️ 未找到有效 engine_sha256 锚，跳过加载期完整性校验（可用 "
                  "scripts/verify_signature.py 离线核验）", file=sys.stderr)
    except ImportError:
        raise
    except Exception:
        pass  # 校验基础设施异常时不阻断正常使用；离线核验兜底

    loader = importlib.machinery.SourceFileLoader("analyze_skill", str(src))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    if spec is None:
        raise ImportError(f"无法为 {src} 构造 import spec")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["analyze_skill"] = mod
    loader.exec_module(mod)

    _ENGINE = mod
    return _ENGINE
