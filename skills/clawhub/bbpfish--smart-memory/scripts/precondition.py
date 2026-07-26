"""
Smart Memory v3 — 前置条件预检模块

PreconditionEvaluator 负责：
- 批量评估所有 active cue 的 preconditions
- 写入 precondition_cache 表（带 TTL）
- 前置条件失败的 cue 标记为 stale_observed
"""

import json
import os
import sqlite3
import sys
from typing import Optional

from .db import get_connection, utcnow_str
from .cues import CueStore


class PreconditionEvaluator:
    """批量评估器，检查所有 active cue 的前置条件并写入缓存。"""

    def __init__(self, conn: sqlite3.Connection | None = None, base_dir: Optional[str] = None, db_path: Optional[str] = None):
        """
        Args:
            conn: 外部 SQLite 连接，None 则使用模块级单例。
            base_dir: v3 模块根目录（用于解析 docs/ 相对路径）
            db_path: SQLite 数据库路径
        """
        self._conn = conn if conn is not None else get_connection()
        self._base_dir = base_dir or os.path.dirname(os.path.abspath(__file__))
        self._docs_dir = os.path.join(self._base_dir, "docs")

    def __repr__(self) -> str:
        return f"PreconditionEvaluator(base_dir={self._base_dir!r})"

    # ------------------------------------------------------------------
    # 公共入口
    # ------------------------------------------------------------------

    def evaluate_all(self, ttl_minutes: int = 60) -> dict:
        """批量评估所有 active cue 的前置条件，写入 precondition_cache。

        Args:
            ttl_minutes: 缓存 TTL，默认 60 分钟。建议与 scan-round 间隔对齐。

        Returns:
            {
                "total": int,       # 评估总数
                "passed": int,      # 全部通过
                "failed": int,      # 至少一项失败
                "details": [...]    # 每条评估结果
            }
        """
        store = CueStore()
        active_cues = store.list_active()

        total = 0
        passed = 0
        failed = 0
        details = []

        now = utcnow_str()

        for cue in active_cues:
            cue_id = cue["id"]
            preconditions = cue.get("preconditions", [])

            # 确保 preconditions 是 list
            if isinstance(preconditions, str):
                try:
                    preconditions = json.loads(preconditions)
                except (json.JSONDecodeError, TypeError):
                    preconditions = []

            if not preconditions:
                # 无前置条件 → 默认通过
                self._write_cache(cue_id, True, [], now, ttl_minutes)
                total += 1
                passed += 1
                continue

            # 逐条检查
            checks = []
            all_ok = True

            for pc in preconditions:
                check_result = self._check_one(pc)
                checks.append(check_result)
                if not check_result.get("passed", False):
                    all_ok = False

            self._write_cache(cue_id, all_ok, checks, now, ttl_minutes)
            total += 1
            if all_ok:
                passed += 1
            else:
                failed += 1
                # 前置条件失败 → 标记 stale_observed（带失败原因）
                failed_reasons = [c.get("detail", "") for c in checks if not c.get("passed", False)]
                reason_str = "; ".join(failed_reasons) if failed_reasons else "precondition_failed"
                store.mark_stale(cue_id, reason=reason_str)

            details.append({
                "cue_id": cue_id,
                "title": cue.get("title", ""),
                "all_passed": all_ok,
                "checks": checks,
            })

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "details": details,
        }

    def check_single(self, cue_id: str) -> dict:
        """检查单个 cue 的前置条件（不写入缓存）。

        Returns:
            {"all_passed": bool, "checks": [...]}
        """
        store = CueStore()
        cue = store.get(cue_id)
        if cue is None:
            return {"all_passed": False, "checks": [], "error": "cue not found"}

        preconditions = cue.get("preconditions", [])
        if isinstance(preconditions, str):
            try:
                preconditions = json.loads(preconditions)
            except (json.JSONDecodeError, TypeError):
                preconditions = []

        checks = []
        all_ok = True
        for pc in preconditions:
            result = self._check_one(pc)
            checks.append(result)
            if not result.get("passed", False):
                all_ok = False

        return {"all_passed": all_ok, "checks": checks}

    # ------------------------------------------------------------------
    # 单条前置条件检查
    # ------------------------------------------------------------------

    def _check_one(self, precondition: dict) -> dict:
        """检查单条前置条件。

        支持的类型：
        - file_exists: {"type": "file_exists", "path": "...", "reason": "..."}
        - env_var: {"type": "env_var", "name": "PYTHONPATH", "reason": "..."}
        - python_version: {"type": "python_version", "min": "3.10", "reason": "..."}

        Returns:
            {"type": str, "passed": bool, "detail": str}
        """
        pc_type = precondition.get("type", "")

        if pc_type == "file_exists":
            return self._check_file_exists(precondition)
        elif pc_type == "env_var":
            return self._check_env_var(precondition)
        elif pc_type == "python_version":
            return self._check_python_version(precondition)
        else:
            return {
                "type": pc_type,
                "passed": False,
                "detail": f"unknown precondition type: {pc_type}",
            }

    def _check_file_exists(self, pc: dict) -> dict:
        path = pc.get("path", "")
        reason = pc.get("reason", "")

        # 先尝试绝对路径
        abs_path = path if os.path.isabs(path) else os.path.join(self._docs_dir, path)

        exists = os.path.exists(abs_path)
        return {
            "type": "file_exists",
            "passed": exists,
            "detail": f"文件 '{path}' {'存在' if exists else '不存在'} — {reason}" if reason
                      else f"文件 '{path}' {'存在' if exists else '不存在'}",
        }

    def _check_env_var(self, pc: dict) -> dict:
        name = pc.get("name", "")
        reason = pc.get("reason", "")

        exists = name in os.environ
        return {
            "type": "env_var",
            "passed": exists,
            "detail": f"环境变量 '{name}' {'已设置' if exists else '未设置'} — {reason}" if reason
                      else f"环境变量 '{name}' {'已设置' if exists else '未设置'}",
        }

    def _check_python_version(self, pc: dict) -> dict:
        min_ver = pc.get("min", "")
        reason = pc.get("reason", "")

        current = f"{sys.version_info.major}.{sys.version_info.minor}"

        try:
            parts = min_ver.split(".")
            min_major = int(parts[0])
            min_minor = int(parts[1]) if len(parts) > 1 else 0

            ok = (sys.version_info.major > min_major or
                  (sys.version_info.major == min_major and sys.version_info.minor >= min_minor))
        except (ValueError, IndexError):
            ok = False

        return {
            "type": "python_version",
            "passed": ok,
            "detail": f"Python >= {min_ver} 要求，当前 {current} — {reason}" if reason
                      else f"Python >= {min_ver} 要求，当前 {current}",
        }

    # ------------------------------------------------------------------
    # 缓存写入
    # ------------------------------------------------------------------

    def _write_cache(
        self,
        cue_id: str,
        all_passed: bool,
        checks: list[dict],
        evaluated_at: str,
        ttl_minutes: int,
    ):
        """写入或更新 precondition_cache 记录。"""
        all_passed_int = 1 if all_passed else 0
        checks_json = json.dumps(checks, ensure_ascii=False)

        self._conn.execute(
            """INSERT OR REPLACE INTO precondition_cache
               (cue_id, all_passed, checks_json, evaluated_at, ttl_minutes)
               VALUES (?, ?, ?, ?, ?)""",
            (cue_id, all_passed_int, checks_json, evaluated_at, ttl_minutes),
        )
        self._conn.commit()
