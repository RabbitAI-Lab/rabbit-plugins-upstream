"""
Smart Memory v3 — 线索卡 CRUD（基于 SQLite）

CueStore 提供 cues 表的完整增删改查，字段对齐 SCHEMA.md。
"""

import json
import sqlite3
from typing import Any, Optional
import uuid

from .db import get_connection, utcnow_str


class CueStore:
    """线索卡数据访问层，封装 cues 表的所有 CRUD 操作。"""

    def __init__(self, conn: sqlite3.Connection | None = None, db_path: Optional[str] = None):
        """初始化 CueStore。

        Args:
            conn: 外部 SQLite 连接，None 则使用 db.py 的单例连接。
            db_path: SQLite 数据库路径（兼容旧接口）。
        """
        self._conn = conn if conn is not None else get_connection()
        self._db_path = db_path

    def __repr__(self) -> str:
        return f"CueStore(db_path={self._db_path!r})"

    # ---- 写入 ----

    def add(self, card: dict) -> str:
        """插入新线索卡。

        card 可包含以下字段（兼容 content/tags 和 scene/keywords 两种命名）：
          title (必填)
          scene 或 content: 适用场景/卡片内容（存入 scene 列）
          keywords 或 tags: 关键词（存入 keywords 列）
        其余字段取默认值。自动生成 UUID4 id、created、updated。

        Returns:
            card_id (str)
        """
        title = card.get("title", "")
        if not title:
            raise ValueError("card must contain 'title'")

        normalized = CueStore._normalize_card(card)
        scene_text = normalized["scene"]
        keywords_list = normalized["keywords"]
        keywords_json = json.dumps(keywords_list, ensure_ascii=False)

        card_id = card.get("id") or str(uuid.uuid4())
        scene = scene_text  # scene 列
        docs = json.dumps(card.get("docs", []), ensure_ascii=False)
        importance = float(card.get("importance", 0.5))
        retention = float(card.get("retention", 1.0))
        preconditions = json.dumps(card.get("preconditions", []), ensure_ascii=False)
        now = utcnow_str()

        self._conn.execute(
            """INSERT INTO cues (id, title, keywords, scene, docs,
               importance, retention, preconditions, created, updated)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (card_id, title, keywords_json, scene, docs,
             importance, retention, preconditions, now, now),
        )
        self._conn.commit()
        return card_id

    # ---- 读取 ----

    def get(self, card_id: str) -> Optional[dict]:
        """按 ID 查询单张线索卡，返回 dict 或 None。"""
        row = self._conn.execute(
            "SELECT * FROM cues WHERE id = ?", (card_id,)
        ).fetchone()
        if row is None:
            return None
        return self._row_to_dict(row)

    def list_all(self, status: Optional[str] = None) -> list[dict]:
        """列出所有卡片，可按 status 过滤。"""
        if status:
            rows = self._conn.execute(
                "SELECT * FROM cues WHERE status = ? ORDER BY updated DESC",
                (status,),
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM cues ORDER BY updated DESC"
            ).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def list_active(self) -> list[dict]:
        """列出 status='active' 的卡片。"""
        return self.list_all(status="active")

    def list_stale(self) -> list[dict]:
        """列出 status LIKE 'stale%' 的卡片。"""
        rows = self._conn.execute(
            "SELECT * FROM cues WHERE status LIKE 'stale%' ORDER BY updated DESC"
        ).fetchall()
        return [self._row_to_dict(r) for r in rows]

    # ---- 更新 ----

    def update(self, card_id: str, updates: dict) -> bool:
        """更新卡片字段，自动更新 updated_at。返回是否成功。"""
        allowed = {
            "title", "keywords", "scene", "docs", "importance",
            "retention", "status", "stale_count", "stale_reason",
            "stale_detected_at", "preconditions",
        }
        filtered = {k: v for k, v in updates.items() if k in allowed}
        if not filtered:
            return False

        filtered["updated"] = utcnow_str()

        set_clause = ", ".join(f"{k} = ?" for k in filtered)
        values = list(filtered.values()) + [card_id]

        cursor = self._conn.execute(
            f"UPDATE cues SET {set_clause} WHERE id = ?", values
        )
        self._conn.commit()
        return cursor.rowcount > 0

    # ---- 状态流转 ----

    def mark_stale(self, card_id: str, reason: Optional[str] = None) -> bool:
        """标记为 stale_observed，stale_count += 1。

        Args:
            card_id: 线索卡 ID
            reason: 可选，标记原因（写入 stale_reason）
        """
        now = utcnow_str()
        if reason is not None:
            cursor = self._conn.execute(
                """UPDATE cues SET status = 'stale_observed',
                   stale_count = stale_count + 1,
                   stale_detected_at = COALESCE(stale_detected_at, ?),
                   stale_reason = ?,
                   updated = ?
                   WHERE id = ?""",
                (now, reason, now, card_id),
            )
        else:
            cursor = self._conn.execute(
                """UPDATE cues SET status = 'stale_observed',
                   stale_count = stale_count + 1,
                   stale_detected_at = COALESCE(stale_detected_at, ?),
                   updated = ?
                   WHERE id = ?""",
                (now, now, card_id),
            )
        self._conn.commit()
        return cursor.rowcount > 0

    def mark_stale_confirmed(self, card_id: str) -> bool:
        """推进到 stale_confirmed。"""
        now = utcnow_str()
        cursor = self._conn.execute(
            "UPDATE cues SET status = 'stale_confirmed', updated = ? WHERE id = ?",
            (now, card_id),
        )
        self._conn.commit()
        return cursor.rowcount > 0

    def mark_deleted(self, card_id: str) -> bool:
        """软删除：标记为 deleted。"""
        now = utcnow_str()
        cursor = self._conn.execute(
            "UPDATE cues SET status = 'deleted', updated = ? WHERE id = ?",
            (now, card_id),
        )
        self._conn.commit()
        return cursor.rowcount > 0

    def restore(self, card_id: str) -> bool:
        """恢复卡片到 active，重置 stale_count=0。"""
        now = utcnow_str()
        cursor = self._conn.execute(
            """UPDATE cues SET status = 'active',
               stale_count = 0, stale_reason = '',
               stale_detected_at = NULL, updated = ?
               WHERE id = ?""",
            (now, card_id),
        )
        self._conn.commit()
        return cursor.rowcount > 0

    # ---- 搜索与统计 ----

    def search_by_tags(self, tags: list[str]) -> list[dict]:
        """按标签搜索（keywords JSON 数组包含任一 tag）。

        使用 json_each 精确匹配，避免 LIKE 子串误匹配。
        """
        if not tags:
            return []
        placeholders = ", ".join("?" for _ in tags)
        rows = self._conn.execute(
            f"""SELECT * FROM cues WHERE EXISTS (
                SELECT 1 FROM json_each(cues.keywords) WHERE value IN ({placeholders})
            ) ORDER BY updated DESC""",
            tags,
        ).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def count(self) -> int:
        row = self._conn.execute("SELECT COUNT(*) FROM cues").fetchone()
        return row[0]

    def count_by_status(self) -> dict[str, int]:
        rows = self._conn.execute(
            "SELECT status, COUNT(*) AS cnt FROM cues GROUP BY status"
        ).fetchall()
        return {r["status"]: r["cnt"] for r in rows}

    # ---- 内部 ----

    @staticmethod
    def _normalize_card(card: dict) -> dict:
        """规范化 card 的 scene 和 keywords 字段。

        兼容 content/tags 和 scene/keywords 两种命名风格，
        统一转换为 scene/keywords 格式。
        """
        scene_text = card.get("scene", "") or card.get("content", "")

        tags_value = card.get("keywords") or card.get("tags", [])
        if isinstance(tags_value, str):
            keywords_list = [t.strip() for t in tags_value.split(",") if t.strip()]
        elif isinstance(tags_value, list):
            keywords_list = [str(t).strip() for t in tags_value if str(t).strip()]
        else:
            keywords_list = []

        return {
            "scene": scene_text,
            "keywords": keywords_list,
        }

    @staticmethod
    def _row_to_dict(row) -> dict:
        """将 sqlite3.Row 转为 dict，并反序列化 JSON 列便于阅读。"""
        d = dict(row)
        for col in ("keywords", "docs", "preconditions"):
            try:
                d[col] = json.loads(d[col])
            except (json.JSONDecodeError, TypeError, KeyError):
                pass
        return d
