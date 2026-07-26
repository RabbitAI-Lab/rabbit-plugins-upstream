"""
Smart Memory v3 — 垃圾回收模块

GarbageCollector 实现：
- scan_stale(): 巡检所有 active/stale_observed 卡片，推进删除状态机
- gc(): 物理删除 stale_confirmed 卡片（级联删除 signals）
- restore(): 恢复 stale 卡片到 active
- get_stale_report(): 返回当前状态分布

状态机（按阶段 4 任务定义）：
    active → stale_observed  (第1次巡检：retention<0.1 或 30天无信号)
    stale_observed → stale_confirmed (连续3次巡检 stale_count>=3)
    stale_confirmed → deleted (gc 命令执行物理删除)
    stale_* → active (restore 恢复)
"""

from datetime import datetime, timedelta
import sqlite3
from typing import Any, Optional

from .db import get_connection, utcnow_str, utcnow_dt
from .cues import CueStore

# ---------------------------------------------------------------------------
# 阈值常量
# ---------------------------------------------------------------------------
STALE_RETENTION_THRESHOLD = 0.1       # retention 低于此值视为 stale
STALE_NO_SIGNAL_DAYS = 30            # 最近 N 天无信号视为 stale
STALE_CONFIRM_COUNT = 3              # stale_count 达到此值推进到 stale_confirmed
INSPECTION_INTERVAL_HOURS = 24       # 两次巡检之间至少间隔 24 小时（防抖）
RESTORE_RETENTION = 1.0              # restore 后重置 retention 为 1.0


class GarbageCollector:
    """垃圾回收器，管理卡片状态机和物理删除。"""

    def __init__(self, conn: sqlite3.Connection | None = None, db_path: Optional[str] = None):
        """初始化 GarbageCollector。

        Args:
            conn: 外部 SQLite 连接，None 则使用模块级单例。
            db_path: SQLite 数据库路径。
        """
        self._conn = conn if conn is not None else get_connection()
        self._cue_store = CueStore(conn=self._conn, db_path=db_path)
        self._db_path = db_path

    def __repr__(self) -> str:
        return f"GarbageCollector(db_path={self._db_path!r})"

    # ------------------------------------------------------------------
    # scan_stale — 巡检
    # ------------------------------------------------------------------

    def scan_stale(self, dry_run: bool = False) -> dict[str, list[dict]]:
        """巡检所有 active 和 stale_observed 卡片，推进状态机。

        对每个卡片检查两个 stale 条件（任一满足即标记）：
        1. retention < 0.1
        2. 最近 30 天无任何 signals 记录

        - active 卡片满足条件 → mark_stale（status='stale_observed', stale_count+=1）
        - stale_observed 卡片再次满足条件 → stale_count+=1；
          若 stale_count >= STALE_CONFIRM_COUNT(3) → mark_stale_confirmed

        Args:
            dry_run: True 时仅检测，不实际标记（用于 stale-detect 不带 --mark 的场景）

        Returns:
            {'new_stale': [...], 'confirmed': [...]}
            或 dry_run 时: {'detected': [...], 'would_confirm': [...]}
        """
        rows = self._conn.execute(
            """SELECT * FROM cues
               WHERE status IN ('active', 'stale_observed')
               ORDER BY updated DESC"""
        ).fetchall()

        new_stale: list[dict] = []
        confirmed: list[dict] = []

        for row in rows:
            card = CueStore._row_to_dict(row)
            card_id = card["id"]
            status = card["status"]
            retention = card["retention"]

            is_stale, stale_reason = self._is_stale(card)

            if not is_stale:
                # 自动恢复：stale_observed 卡片 retention > 0.3 → 恢复为 active
                # 直接执行 UPDATE，保持当前 retention 值不变（不调用 restore）
                if status == 'stale_observed' and retention > 0.3:
                    now = utcnow_str()
                    self._conn.execute(
                        """UPDATE cues SET status = 'active',
                           stale_count = 0,
                           stale_reason = '',
                           stale_detected_at = NULL,
                           updated = ?
                           WHERE id = ?""",
                        (now, card_id),
                    )
                    self._conn.commit()
                continue

            # 24h 防抖：已 stale 的卡片，两次巡检之间至少间隔 24 小时
            # 首次标记（status='active', stale_detected_at 为 NULL）不受此限制
            if status == 'stale_observed':
                stale_detected = card.get("stale_detected_at")
                if stale_detected:
                    try:
                        detected_time = datetime.strptime(stale_detected, "%Y-%m-%d %H:%M:%S")
                        if (utcnow_dt() - detected_time) < timedelta(hours=INSPECTION_INTERVAL_HOURS):
                            continue
                    except (ValueError, TypeError):
                        pass

            if dry_run:
                # 仅检测，不标记：模拟推进结果
                current_count = card.get("stale_count", 0)
                would_confirm = (current_count + 1) >= STALE_CONFIRM_COUNT
                detected = {
                    "id": card_id,
                    "title": card.get("title", ""),
                    "status": status,
                    "retention": retention,
                    "stale_count": current_count,
                    "would_confirm": would_confirm,
                }
                if would_confirm:
                    confirmed.append(detected)
                else:
                    new_stale.append(detected)
                continue

            # 标记 stale（stale_count += 1）
            self._cue_store.mark_stale(card_id, reason=stale_reason)

            # 重新读取更新后的 stale_count
            updated = self._cue_store.get(card_id)
            if updated is None:
                continue
            stale_count = updated.get("stale_count", 0)

            if stale_count >= STALE_CONFIRM_COUNT:
                # 推进到 stale_confirmed
                self._cue_store.mark_stale_confirmed(card_id)
                confirmed_card = self._cue_store.get(card_id)
                if confirmed_card:
                    confirmed.append(confirmed_card)
            elif status == "active":
                # 首次被标记
                fresh = self._cue_store.get(card_id)
                if fresh:
                    new_stale.append(fresh)

        if dry_run:
            return {"detected": new_stale, "would_confirm": confirmed}

        return {"new_stale": new_stale, "confirmed": confirmed}

    def _is_stale(self, card: dict) -> tuple[bool, str]:
        """判断卡片是否满足 stale 条件。

        条件1: retention < 0.1
        条件2: 最近 30 天无任何 signals 记录

        任一满足即返回 (True, reason)。
        """
        # 条件1: retention < 阈值
        if card["retention"] < STALE_RETENTION_THRESHOLD:
            return True, f"retention={card['retention']:.4f}<{STALE_RETENTION_THRESHOLD}"

        # 条件2: 30 天无信号
        if self._has_no_recent_signals(card["id"]):
            return True, f"no signals in {STALE_NO_SIGNAL_DAYS} days"

        return False, ""

    def _has_no_recent_signals(self, card_id: str) -> bool:
        """检查最近 30 天内是否无任何信号记录。"""
        cutoff = (utcnow_dt() - timedelta(days=STALE_NO_SIGNAL_DAYS)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        row = self._conn.execute(
            """SELECT COUNT(*) AS cnt FROM signals
               WHERE cue_id = ? AND recorded_at >= ?""",
            (card_id, cutoff),
        ).fetchone()
        return row["cnt"] == 0

    # ------------------------------------------------------------------
    # cleanup_signals — 信号老化清理
    # ------------------------------------------------------------------

    def cleanup_signals(self, max_age_days: int = 180, dry_run: bool = True,
                        min_keep: int = 5) -> dict:
        """清理过期信号记录。

        仅清理 status IN ('active', 'stale_observed') 卡片的信号，
        stale_confirmed 和 deleted 的信号由 gc 物理删除时级联处理。

        Args:
            max_age_days: 信号最大保留天数，默认 180 天。
            dry_run: True 仅返回待删除计数，不实际删除。
            min_keep: 每张 active 卡片最少保留信号数，默认 5。

        Returns:
            {
                "dry_run": bool,
                "deleted_count": int,
                "affected_cards": int,
                "total_signals_before": int,
                "total_signals_after": int,
            }
        """
        # 统计清理前信号总数
        total_before = self._conn.execute(
            "SELECT COUNT(*) AS cnt FROM signals"
        ).fetchone()["cnt"]

        # 找出有旧信号的 active / stale_observed 卡片
        active_cards = self._conn.execute(
            """SELECT s.cue_id, COUNT(*) AS total,
                      COUNT(CASE WHEN s.recorded_at < datetime('now', ?)
                            THEN 1 END) AS old_count
               FROM signals s
               INNER JOIN cues c ON s.cue_id = c.id
               WHERE c.status IN ('active', 'stale_observed')
               GROUP BY s.cue_id
               HAVING old_count > 0""",
            (f"-{max_age_days} days",),
        ).fetchall()

        deleted_count = 0
        affected_cards = 0

        for row in active_cards:
            cue_id = row["cue_id"]
            old_count = row["old_count"]
            total = row["total"]

            if dry_run:
                # 预览模式：计算 min_keep 约束下实际可删除数
                keep_at_least = max(0, total - min_keep)
                to_delete = min(old_count, keep_at_least)
                if to_delete > 0:
                    deleted_count += to_delete
                    affected_cards += 1
                continue

            # 实际删除：子查询保留最近 min_keep 条
            cursor = self._conn.execute(
                """DELETE FROM signals
                   WHERE cue_id = ?
                     AND recorded_at < datetime('now', ?)
                     AND rowid NOT IN (
                         SELECT rowid FROM signals s2
                         WHERE s2.cue_id = ?
                         ORDER BY s2.recorded_at DESC
                         LIMIT ?
                     )""",
                (cue_id, f"-{max_age_days} days", cue_id, min_keep),
            )
            if cursor.rowcount > 0:
                deleted_count += cursor.rowcount
                affected_cards += 1

        if not dry_run:
            self._conn.commit()

        total_after = total_before - deleted_count

        return {
            "dry_run": dry_run,
            "deleted_count": deleted_count,
            "affected_cards": affected_cards,
            "total_signals_before": total_before,
            "total_signals_after": total_after,
        }

    # ------------------------------------------------------------------
    # gc — 垃圾回收
    # ------------------------------------------------------------------

    def gc(self, dry_run: bool = False, force: bool = False) -> dict[str, Any]:
        """执行垃圾回收：物理删除 stale_confirmed 和 deleted 卡片。

        stale_confirmed：经过 3 次巡检确认 + 距 stale_detected_at ≥ 24h 的失效卡片
        deleted：用户通过 CLI `delete` 命令主动标记删除的卡片

        删除后额外清理 env_snapshots 中 cue_id=NULL 的孤儿记录
        （这些是之前的 DELETE CASCADE 产生的孤儿，env_snapshots 使用 SET NULL 而非 CASCADE）。

        Args:
            dry_run: True 时仅列出待删除卡片，不执行删除。
            force: True 时直接删除，False 时不执行删除（仅 dry_run 角色）。

        Returns:
            {'deleted': [...], 'deleted_count': int, 'orphan_snapshots_cleaned': int}
            或 dry_run 时：{'pending': [...], 'pending_count': int}
        """
        # stale_confirmed 必须满足 24h 巡检间隔（DELETE_POLICY §5.2）
        interval_cutoff = (utcnow_dt() - timedelta(hours=INSPECTION_INTERVAL_HOURS)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        rows = self._conn.execute(
            """SELECT * FROM cues WHERE status = 'deleted'
               UNION ALL
               SELECT * FROM cues WHERE status = 'stale_confirmed'
               AND (stale_detected_at IS NULL OR stale_detected_at <= ?)""",
            (interval_cutoff,),
        ).fetchall()

        pending = [CueStore._row_to_dict(r) for r in rows]

        # 识别被 24h 间隔排除的 stale_confirmed 卡片（仅供 dry_run 报告）
        excluded_rows = self._conn.execute(
            """SELECT * FROM cues WHERE status = 'stale_confirmed'
               AND stale_detected_at IS NOT NULL
               AND stale_detected_at > ?""",
            (interval_cutoff,),
        ).fetchall()
        excluded = [CueStore._row_to_dict(r) for r in excluded_rows]

        if dry_run or not force:
            return {"pending": pending, "pending_count": len(pending),
                    "excluded_by_interval": excluded,
                    "excluded_count": len(excluded)}

        # 物理删除
        deleted: list[dict] = []
        for card in pending:
            card_id = card["id"]
            deleted.append(card)
            # CASCADE: signals, precondition_cache 自动级联删除
            self._conn.execute("DELETE FROM cues WHERE id = ?", (card_id,))

        # 清理孤儿 env_snapshots（cue_id=NULL，由 DELETE SET NULL 产生）
        cursor = self._conn.execute("DELETE FROM env_snapshots WHERE cue_id IS NULL")
        orphan_count = cursor.rowcount

        self._conn.commit()
        return {"deleted": deleted, "deleted_count": len(deleted),
                "orphan_snapshots_cleaned": orphan_count}

    # ------------------------------------------------------------------
    # restore — 恢复
    # ------------------------------------------------------------------

    def restore(self, card_id: str) -> bool:
        """恢复卡片到 active 状态。

        重置：stale_count=0, status='active', retention=1.0,
              stale_reason='', stale_detected_at=NULL

        Returns:
            True 如果恢复成功。
        """
        now = utcnow_str()
        cursor = self._conn.execute(
            """UPDATE cues
               SET status = 'active',
                   stale_count = 0,
                   stale_reason = '',
                   stale_detected_at = NULL,
                   retention = ?,
                   updated = ?
               WHERE id = ?""",
            (RESTORE_RETENTION, now, card_id),
        )
        self._conn.commit()
        return cursor.rowcount > 0

    # ------------------------------------------------------------------
    # get_stale_report — 状态报告
    # ------------------------------------------------------------------

    def get_stale_report(self) -> dict[str, Any]:
        """返回当前 stale 相关状态分布。

        Returns:
            {
                'total': int,
                'by_status': {
                    'active': int,
                    'stale_observed': int,
                    'stale_confirmed': int,
                    'deleted': int
                },
                'stale_observed_details': [...],   # 卡片列表
                'stale_confirmed_details': [...]   # 卡片列表
            }
        """
        status_counts = self._cue_store.count_by_status()

        stale_observed = self._cue_store.list_all(status="stale_observed")
        stale_confirmed = self._cue_store.list_all(status="stale_confirmed")

        return {
            "total": self._cue_store.count(),
            "by_status": {
                "active": status_counts.get("active", 0),
                "stale_observed": status_counts.get("stale_observed", 0),
                "stale_confirmed": status_counts.get("stale_confirmed", 0),
                "deleted": status_counts.get("deleted", 0),
            },
            "stale_observed_details": stale_observed,
            "stale_confirmed_details": stale_confirmed,
        }
