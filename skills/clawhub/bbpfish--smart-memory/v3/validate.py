"""
Smart Memory v3 — 一致性校验

校验 manifest 表 + cues 表 + signals 表的多方一致性。
"""

import json
import os
from pathlib import Path
from typing import Any


class ValidationReport:
    """校验报告，收集所有不一致项。"""

    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.stats: dict[str, int] = {
            "manifest_docs": 0,
            "cues_total": 0,
            "signals_total": 0,
            "orphan_signals": 0,
        }

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    @property
    def valid(self) -> bool:
        return len(self.errors) == 0

    def summary(self) -> str:
        lines = [
            f"清单文档数: {self.stats['manifest_docs']}",
            f"线索卡数: {self.stats['cues_total']}",
            f"信号记录数: {self.stats['signals_total']}",
            f"孤立信号数: {self.stats['orphan_signals']}",
            f"错误: {len(self.errors)}, 警告: {len(self.warnings)}",
        ]
        return "\n".join(lines)


def validate(base_dir: str | None = None) -> ValidationReport:
    """执行完整一致性校验。

    Args:
        base_dir: v3 根目录（包含 docs/ 和 data/smart_memory.db）。None 则自动推导。
    """
    from .db import get_connection, init_db

    conn = get_connection()
    init_db(conn)

    report = ValidationReport()

    # 确定 v3 根目录
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    base = Path(base_dir)

    # ==================================================================
    # 1. cues 表校验
    # ==================================================================
    cues_rows = conn.execute("SELECT * FROM cues").fetchall()
    report.stats["cues_total"] = len(cues_rows)

    valid_statuses = {"active", "stale_observed", "stale_confirmed", "deleted"}

    for row in cues_rows:
        card = dict(row)

        # 1a. status 合法性
        status = card.get("status", "")
        if status not in valid_statuses:
            report.add_error(
                f"[CUES] {card['id']} 的 status='{status}' 不合法，"
                f"应为 {valid_statuses}"
            )

        # 1b. retention 范围
        retention = card.get("retention", 1.0)
        if not (0 <= retention <= 1):
            report.add_error(
                f"[CUES] {card['id']} 的 retention={retention} 超出 [0,1] 范围"
            )

        # 1c. importance 范围
        importance = card.get("importance", 0.5)
        if not (0 <= importance <= 1):
            report.add_error(
                f"[CUES] {card['id']} 的 importance={importance} 超出 [0,1] 范围"
            )

        # 1d. stale_count 与 status 一致性
        stale_count = card.get("stale_count", 0)
        if status == "stale_confirmed" and stale_count < 3:
            report.add_warning(
                f"[CUES] {card['id']} 状态为 stale_confirmed 但 stale_count={stale_count} < 3 (STALE_CONFIRM_COUNT)"
            )
        if status == "stale_observed" and stale_count < 1:
            report.add_warning(
                f"[CUES] {card['id']} 状态为 stale_observed 但 stale_count={stale_count} < 1"
            )
        if status == "active" and stale_count > 0:
            report.add_warning(
                f"[CUES] {card['id']} 状态为 active 但 stale_count={stale_count} > 0"
            )

    # ==================================================================
    # 2. signals 表校验
    # ==================================================================
    signals_rows = conn.execute("SELECT * FROM signals").fetchall()
    report.stats["signals_total"] = len(signals_rows)

    valid_signal_types = {"recall", "used", "failed", "confirmed", "ignored", "contradicted"}

    for row in signals_rows:
        sig = dict(row)

        # 2a. signal_type 合法性
        if sig.get("signal_type") not in valid_signal_types:
            report.add_error(
                f"[SIGNALS] id={sig['id']} signal_type='{sig['signal_type']}' 不合法"
            )

        # 2b. cue_id 引用的卡片是否存在
        cue_id = sig.get("cue_id", "")
        exists = conn.execute(
            "SELECT 1 FROM cues WHERE id = ?", (cue_id,)
        ).fetchone()
        if exists is None:
            report.add_error(
                f"[SIGNALS→CUES] signals id={sig['id']} 引用了不存在的 cue_id='{cue_id}'"
            )
            report.stats["orphan_signals"] += 1

    # ==================================================================
    # 3. manifest 表校验
    # ==================================================================
    manifest_rows = conn.execute("SELECT * FROM manifest").fetchall()
    report.stats["manifest_docs"] = len(manifest_rows)

    docs_dir = base / "docs"

    for row in manifest_rows:
        entry = dict(row)
        doc_id = entry.get("doc_id")
        rel_path = entry.get("rel_path", "")
        checksum = entry.get("checksum", "")

        # 3a. 关联的 docs/ 文件是否存在
        abs_path = base / rel_path
        if not abs_path.exists():
            report.add_error(
                f"[MANIFEST→DISK] manifest 注册了 {doc_id} → {rel_path}，但文件不存在"
            )

        # 3b. checksum 非空（警告级别，因为可能是迁移时文件不存在）
        if not checksum and abs_path.exists():
            report.add_warning(
                f"[MANIFEST] {doc_id} ({rel_path}) 的 checksum 为空"
            )

    # ==================================================================
    # 4. env_snapshots 校验
    # ==================================================================
    env_rows = conn.execute(
        """SELECT e.id, e.cue_id FROM env_snapshots e
           WHERE e.cue_id IS NOT NULL
             AND e.cue_id NOT IN (SELECT id FROM cues)"""
    ).fetchall()
    for row in env_rows:
        report.add_warning(
            f"[ENV_SNAP] env_snapshot id={row['id']} 引用了不存在的 cue_id='{row['cue_id']}'"
        )

    # ==================================================================
    # 5. precondition_cache 校验
    # ==================================================================
    cache_rows = conn.execute(
        """SELECT p.cue_id FROM precondition_cache p
           WHERE p.cue_id NOT IN (SELECT id FROM cues)"""
    ).fetchall()
    for row in cache_rows:
        report.add_warning(
            f"[CACHE] precondition_cache 引用了不存在的 cue_id='{row['cue_id']}'"
        )

    return report


def print_report(report: ValidationReport) -> str:
    """格式化输出校验报告。"""
    lines = [
        "=" * 60,
        "Smart Memory v3 — 一致性校验报告",
        "=" * 60,
        "",
        report.summary(),
        "",
    ]

    if report.errors:
        lines.append(f"--- 错误 ({len(report.errors)}) ---")
        for e in report.errors:
            lines.append(f"  X {e}")
        lines.append("")

    if report.warnings:
        lines.append(f"--- 警告 ({len(report.warnings)}) ---")
        for w in report.warnings:
            lines.append(f"  ! {w}")
        lines.append("")

    if report.valid:
        lines.append("V 校验通过，数据一致！")
    else:
        lines.append("X 校验未通过，请修复以上错误。")

    return "\n".join(lines)
