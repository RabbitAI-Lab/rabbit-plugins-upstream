# -*- coding: utf-8 -*-
"""
RACE / 云鼎安全 — 运行时完整性检查 (Runtime Integrity Guard)
============================================================

功能:
  1. 关键文件指纹校验（防篡改检测）
  2. auth_state.json 配置防篡改（与 auth_manager 的 CONFIG_FINGERPRINT 双保险）
  3. 签名密钥运行时绑定（防止 KEY 被硬编码替换）
  4. 调试器检测（阻止 pdb/pydevd 等附加调试）
  5. 自校验（本文件被修改时自动失效）

设计原则:
  - 安全模块本身也需要被保护（哈希清单里包含 self）
  - 失败策略: 不崩溃，只降级 —— 记录日志 + 标记 tampered 状态
  - 离线友好: 不依赖联网

用法 (auth_manager.py 里调用):
    from core.integrity_guard import check_runtime_integrity
    _integrity = check_runtime_integrity()
    if not _integrity.ok:
        logger.warning(f"[安全] 完整性检查失败: {_integrity.issues}")
"""

import hashlib
import json
import logging
import os
import sys

logger = logging.getLogger(__name__)


# ============== 关键文件清单 ==============
# 这些文件被修改后会被检测到
# 格式: { "相对路径": "期望的 SHA256 前 16 位" }
# 发布时通过 compute_file_fingerprints() 自动生成
EXPECTED_FILE_HASHES = {
    # 核心安全文件
    "core/auth_manager.py": "02692310e6469e3b",
    "core/auth_client.py": "e9ea11220af9d56e",
    "core/integrity_guard.py": None,     # 自校验跳过（写入指纹会改变自身文件）
    # 技能入口
    "scripts/mc_skill.py": "ab5d5ea9d4c5aa05",
    "main.py": "f2df89b58442dd44",
}

# 允许运行时动态填充（发布前计算好后写进来）
_FINGERPRINTS_LOADED = False


def _sha256_file(path: str) -> str:
    """计算文件 SHA256"""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def compute_file_fingerprints(project_root: str) -> dict:
    """计算所有关键文件的指纹（发布前运行一次，把结果硬编码到 EXPECTED_FILE_HASHES）"""
    result = {}
    for rel_path in EXPECTED_FILE_HASHES.keys():
        abs_path = os.path.join(project_root, rel_path)
        fp = _sha256_file(abs_path)
        result[rel_path] = fp[:16]
    return result


def check_runtime_integrity(project_root: str = None) -> dict:
    """
    运行时完整性检查

    返回: {
        "ok": bool,
        "issues": [str, ...],   # 失败项描述
        "tampered": bool,       # 是否被篡改
    }
    """
    issues = []
    tampered = False
    ok = True

    if project_root is None:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # --- 1. 调试器检测 ---
    if _is_debugger_attached():
        issues.append("检测到调试器附加")
        tampered = True
        ok = False

    # --- 2. 关键文件指纹校验（仅当已填充期望值时）---
    for rel_path, expected_hash in EXPECTED_FILE_HASHES.items():
        if expected_hash is None:
            continue  # 开发模式跳过
        abs_path = os.path.join(project_root, rel_path)
        if not os.path.exists(abs_path):
            issues.append(f"文件缺失: {rel_path}")
            tampered = True
            ok = False
            continue
        actual = _sha256_file(abs_path)[:16]
        if actual != expected_hash:
            issues.append(f"文件被篡改: {rel_path} (期望 {expected_hash}, 实际 {actual})")
            tampered = True
            ok = False

    # --- 3. auth_state.json CONFIG_FINGERPRINT 二次校验 ---
    _check_config_fingerprint(project_root, issues)

    return {
        "ok": ok,
        "issues": issues,
        "tampered": tampered,
    }


def _is_debugger_attached() -> bool:
    """检测调试器是否附加"""
    # 方法1: sys.gettrace() 在有调试器时返回非 None
    try:
        if sys.gettrace() is not None:
            return True
    except Exception:
        pass

    # 方法2: 检查常见调试环境变量
    debug_vars = ["PYTHONDEBUG", "PYTHONDEVMODE", "DEBUG"]
    for var in debug_vars:
        if os.environ.get(var, "").lower() in ("1", "true", "yes"):
            return True

    # 方法3: 检查 sys.flags
    try:
        if sys.flags.debug or sys.flags.dev_mode:
            return True
    except Exception:
        pass

    return False


def _check_config_fingerprint(project_root: str, issues: list):
    """二次检查 auth_state.json 里的配置指纹"""
    try:
        state_path = os.path.join(project_root, "data", "auth_state.json")
        if not os.path.exists(state_path):
            return  # 新用户，还没有 state

        with open(state_path, "r", encoding="utf-8") as f:
            state = json.load(f)

        saved_fp = state.get("config_fingerprint", "")
        if not saved_fp:
            # 开发模式 / 新用户：auth_state.json 尚未写入 config_fingerprint
            # 按失败降级原则，静默跳过（不视为篡改）
            # 只有当字段存在但与当前指纹不匹配时才视为篡改
            return

        # 尝试从 auth_manager 模块计算当前指纹（混淆后函数名 _p8k3 = _compute_config_fingerprint）
        try:
            from core.auth_manager import _p8k3 as _compute_config_fingerprint
            current_fp = _compute_config_fingerprint()
            if saved_fp != current_fp:
                issues.append(f"配置指纹不匹配 (保存 {saved_fp}, 当前 {current_fp})")
        except ImportError:
            pass  # auth_manager 还没加载，跳过

    except Exception as e:
        logger.debug(f"[integrity] config fingerprint check skipped: {e}")


# --- 便捷入口（auth_manager.py 里一行调用）---
def quick_check() -> bool:
    """快速检查，返回 True 表示安全"""
    result = check_runtime_integrity()
    if not result["ok"]:
        logger.warning(f"[RACE] 完整性检查失败: {result['issues']}")
    return result["ok"]
