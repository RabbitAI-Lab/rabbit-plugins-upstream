"""
Smart Memory v3 — 信号系统（基于 SQLite signals 表）

六种信号类型（对齐 SPEC §3.1）：
  recall / used / failed / confirmed / ignored / contradicted

每次 record() 自动应用 Ebbinghaus 遗忘曲线衰减 + 信号 boost，
并更新 cues.retention。
"""

import math
import sqlite3
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from .db import get_connection, utcnow_str


# 信号 boost 值（SPEC §3.1）
SIGNAL_BOOST = {
    "recall": 0.15,
    "used": 0.40,
    "failed": -0.10,
    "confirmed": 0.50,
    "ignored": -0.05,
    "contradicted": -0.30,
}

VALID_SIGNAL_TYPES = frozenset(SIGNAL_BOOST.keys())


def _now_iso() -> str:
    """返回 UTC 时间的 ISO 格式字符串，兼容 Python 3.13+。"""
    return utcnow_str()


class SignalStore:
    """信号记录与 retention 衰减管理。"""

    def __init__(self, db_path: Optional[str] = None):
        self._conn = get_connection()
        self._db_path = db_path

    def __repr__(self) -> str:
        return f"SignalStore(db_path={self._db_path!r})"

    def record(self, card_id: str, signal_type: str, metadata: Optional[str] = None) -> int:
        """记录一条信号并更新 cues.retention。

        Args:
            card_id: 线索卡 ID
            signal_type: recall/used/failed/confirmed/ignored/contradicted
            metadata: 可选 JSON 字符串（当前版本忽略，signals 表无此列）

        Returns:
            新信号的 id（INTEGER）

        Raises:
            ValueError: signal_type 不合法
        """
        if signal_type not in VALID_SIGNAL_TYPES:
            raise ValueError(
                f"Invalid signal_type '{signal_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_SIGNAL_TYPES))}"
            )

        now = _now_iso()

        # BEGIN IMMEDIATE：将整个 record 流程包裹在一笔事务中，
        # 确保读取-计算-写入的原子性与 snapshot 隔离。
        self._conn.execute("BEGIN IMMEDIATE")
        try:
            # 1. 读取当前线索卡数据
            cue = self._conn.execute(
                "SELECT id, importance, retention, updated FROM cues WHERE id = ?",
                (card_id,),
            ).fetchone()
            if cue is None:
                raise ValueError(f"Cue '{card_id}' not found")

            importance = cue["importance"]
            old_retention = cue["retention"]
            last_updated_str = cue["updated"]

            # 2. 计算时间差 Δt（小时），统一使用 UTC 时间比较
            try:
                last_updated = datetime.strptime(last_updated_str, "%Y-%m-%d %H:%M:%S")
            except (ValueError, TypeError):
                last_updated = datetime.now(timezone.utc).replace(tzinfo=None)

            now_naive = datetime.now(timezone.utc).replace(tzinfo=None)
            delta = now_naive - last_updated
            delta_hours = delta.total_seconds() / 3600.0

            # 3. Ebbinghaus 衰减: retention *= e^(-Δt / S)
            S = importance * 720.0
            if S > 0 and delta_hours > 0:
                decay_factor = math.exp(-delta_hours / S)
            else:
                decay_factor = 1.0

            new_retention = old_retention * decay_factor

            # 4. 叠加信号 boost
            boost = SIGNAL_BOOST.get(signal_type, 0)
            new_retention += boost

            # 5. 裁剪到 [0, 1]
            new_retention = max(0.0, min(1.0, new_retention))

            # 6. 写入 signals 表
            cursor = self._conn.execute(
                "INSERT INTO signals (cue_id, signal_type, recorded_at) VALUES (?, ?, ?)",
                (card_id, signal_type, now),
            )
            signal_id = cursor.lastrowid

            # 7. 更新 cues.retention + updated
            self._conn.execute(
                "UPDATE cues SET retention = ?, updated = ? WHERE id = ?",
                (new_retention, now, card_id),
            )

            # 8. 自动恢复检查（SPEC §2.3）
            self._check_auto_recovery(card_id, new_retention)

            # 9. 信号驱动标记检查（SPEC §2.4）
            self._check_signal_driven_mark(card_id)

            self._conn.commit()
            return signal_id
        except Exception:
            self._conn.rollback()
            raise

    def _check_auto_recovery(self, card_id: str, new_retention: float):
        """检查是否需要自动恢复 stale 卡片。

        SPEC §2.3：stale 后恢复活跃（被 used/reinforce 拉回 retention > 0.3）
        → 自动恢复为 active。

        注意：直接使用 self._conn 执行 SQL，不创建外部 CueStore()，
        避免在父事务中产生嵌套 COMMIT（Bug #1 修复）。
        """
        if new_retention <= 0.3:
            return

        cue = self._conn.execute(
            "SELECT status FROM cues WHERE id = ?", (card_id,)
        ).fetchone()
        if cue is None:
            return

        status = cue["status"]
        if status in ("stale_observed", "stale_confirmed"):
            now = _now_iso()
            self._conn.execute(
                """UPDATE cues SET status = 'active',
                   stale_count = 0, stale_reason = '',
                   stale_detected_at = NULL, retention = ?,
                   updated = ?
                   WHERE id = ?""",
                (new_retention, now, card_id),
            )

    def _check_signal_driven_mark(self, card_id: str):
        """信号驱动标记检查（SPEC §2.4）。

        条件：过去30天内 failed_count >= 3 且 failed_rate > 40%
        failed_rate = failed_count / (used_count + failed_count)

        仅对 status='active' 的卡片生效，避免：
        - 对 stale_observed 卡片跳过 24h 间隔直接增加 stale_count
        - 对 stale_confirmed/deleted 卡片降级修改状态

        注意：使用 UTC 时间（与 _now_iso() 对齐），直接使用 self._conn
        执行 SQL，不创建外部 CueStore()，避免嵌套 COMMIT（Bug #1+#3 修复）。
        """
        # 仅对 active 卡片执行信号驱动标记
        cue = self._conn.execute(
            "SELECT status FROM cues WHERE id = ?", (card_id,)
        ).fetchone()
        if cue is None or cue["status"] != "active":
            return

        # 统计过去30天内的 used 和 failed 信号（UTC）
        # 使用 utcnow_dt() 构造 cutoff 而非 SQLite 本地时间函数，
        # 避免 SQLite 本地时间与 UTC recorded_at 的时区偏移。
        from .db import utcnow_dt
        cutoff = (utcnow_dt() - __import__('datetime').timedelta(days=30)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        row = self._conn.execute(
            """SELECT
                SUM(CASE WHEN signal_type = 'used' THEN 1 ELSE 0 END) AS used_count,
                SUM(CASE WHEN signal_type = 'failed' THEN 1 ELSE 0 END) AS failed_count
            FROM signals
            WHERE cue_id = ?
              AND recorded_at >= ?""",
            (card_id, cutoff),
        ).fetchone()

        if row is None:
            return

        used_count = row["used_count"] or 0
        failed_count = row["failed_count"] or 0
        total = used_count + failed_count

        if failed_count < 3:
            return
        if total == 0:
            return

        failed_rate = failed_count / total
        if failed_rate > 0.4:
            now = _now_iso()
            self._conn.execute(
                """UPDATE cues SET status = 'stale_observed',
                   stale_count = stale_count + 1,
                   stale_detected_at = COALESCE(stale_detected_at, ?),
                   stale_reason = ?,
                   updated = ?
                   WHERE id = ?""",
                (now, f"signal_driven: failed_rate={failed_rate:.2f}", now, card_id),
            )

    def get_for_card(self, card_id: str, limit: int = 50) -> list[dict]:
        """获取某卡片的所有信号记录（最近优先）。"""
        rows = self._conn.execute(
            "SELECT * FROM signals WHERE cue_id = ? ORDER BY recorded_at DESC LIMIT ?",
            (card_id, limit),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_recent(self, days: int = 30) -> list[dict]:
        """获取最近 N 天的信号记录（UTC 时区，与 _now_iso() 对齐）。"""
        from .db import utcnow_dt
        cutoff = (utcnow_dt() - timedelta(days=days)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        rows = self._conn.execute(
            "SELECT * FROM signals WHERE recorded_at >= ? "
            "ORDER BY recorded_at DESC",
            (cutoff,),
        ).fetchall()
        return [dict(r) for r in rows]

    def count_by_type(self, card_id: Optional[str] = None) -> dict:
        """按信号类型统计。card_id 为 None 则全局统计。"""
        if card_id:
            rows = self._conn.execute(
                "SELECT signal_type, COUNT(*) AS cnt FROM signals "
                "WHERE cue_id = ? GROUP BY signal_type",
                (card_id,),
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT signal_type, COUNT(*) AS cnt FROM signals GROUP BY signal_type"
            ).fetchall()
        return {r["signal_type"]: r["cnt"] for r in rows}

    def signal_analysis(self, days: int = 30) -> list[dict]:
        """分析信号数据，返回每张卡片的成熟度评估。

        对每张有信号的卡片，计算：
          - total_signals: 总信号数
          - used_rate: used / (used + failed + ignored + contradicted)
          - confirmed_rate: confirmed / total_signals
          - maturity: 综合评分
        """
        from .db import utcnow_dt
        cutoff = (utcnow_dt() - timedelta(days=days)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        rows = self._conn.execute(
            """SELECT
                s.cue_id,
                c.title,
                c.importance,
                c.retention,
                c.status,
                COUNT(*) AS total_signals,
                SUM(CASE WHEN s.signal_type = 'recall' THEN 1 ELSE 0 END) AS recall_cnt,
                SUM(CASE WHEN s.signal_type = 'used' THEN 1 ELSE 0 END) AS used_cnt,
                SUM(CASE WHEN s.signal_type = 'failed' THEN 1 ELSE 0 END) AS failed_cnt,
                SUM(CASE WHEN s.signal_type = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_cnt,
                SUM(CASE WHEN s.signal_type = 'ignored' THEN 1 ELSE 0 END) AS ignored_cnt,
                SUM(CASE WHEN s.signal_type = 'contradicted' THEN 1 ELSE 0 END) AS contradicted_cnt
            FROM signals s
            JOIN cues c ON c.id = s.cue_id
            WHERE s.recorded_at >= ?
            GROUP BY s.cue_id
            ORDER BY total_signals DESC""",
            (cutoff,),
        ).fetchall()

        results = []
        for r in rows:
            d = dict(r)
            neg_total = d.get("used_cnt", 0) + d.get("failed_cnt", 0) + \
                        d.get("ignored_cnt", 0) + d.get("contradicted_cnt", 0)
            d["used_rate"] = d["used_cnt"] / neg_total if neg_total > 0 else 0.0
            d["confirmed_rate"] = d["confirmed_cnt"] / d["total_signals"] \
                if d["total_signals"] > 0 else 0.0
            # 成熟度 = retention * (used_rate + confirmed_rate) / 2
            d["maturity"] = d["retention"] * (d["used_rate"] + d["confirmed_rate"]) / 2
            results.append(d)
        return results
