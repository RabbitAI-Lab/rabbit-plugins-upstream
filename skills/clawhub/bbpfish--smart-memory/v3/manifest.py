"""
Smart Memory v3 — 文档注册表（基于 SQLite manifest 表）

ManifestStore 管理 doc_id ↔ rel_path + checksum 映射。
"""

import hashlib
import json
import os
import sqlite3
from typing import Any, Optional

from .db import get_connection, utcnow_str


class ManifestStore:
    """文档注册表数据访问层。"""

    def __init__(self, conn: sqlite3.Connection | None = None, db_path: Optional[str] = None):
        self._conn = conn if conn is not None else get_connection()
        self._db_path = db_path

    def __repr__(self) -> str:
        return f"ManifestStore(db_path={self._db_path!r})"

    # ---- 注册 ----

    def add_entry(
        self,
        doc_id: str,
        file_path: str,
        checksum: str = "",
    ) -> bool:
        """注册一个文档。

        Args:
            doc_id: 文档唯一 ID
            file_path: 文件相对路径
            checksum: SHA256 校验和，留空则不计算

        Returns:
            True 表示插入成功
        """
        if not checksum:
            checksum = ""

        now = utcnow_str()

        self._conn.execute(
            """INSERT OR REPLACE INTO manifest
               (doc_id, rel_path, checksum, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?)""",
            (doc_id, file_path, checksum, now, now),
        )
        self._conn.commit()
        return True

    # ---- 查询 ----

    def get_entry(self, doc_id: str) -> Optional[dict]:
        """按 doc_id 查询注册信息。"""
        row = self._conn.execute(
            "SELECT * FROM manifest WHERE doc_id = ?", (doc_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_by_path(self, file_path: str) -> Optional[dict]:
        """按文件路径查询注册信息。"""
        row = self._conn.execute(
            "SELECT * FROM manifest WHERE rel_path = ?", (file_path,)
        ).fetchone()
        return dict(row) if row else None

    def list_all(self) -> list[dict]:
        """列出所有注册文档。"""
        rows = self._conn.execute(
            "SELECT * FROM manifest ORDER BY updated_at DESC"
        ).fetchall()
        return [dict(r) for r in rows]

    # ---- 更新 ----

    def update_entry(self, doc_id: str, updates: dict) -> bool:
        """更新文档注册信息。返回是否成功。"""
        allowed = {"rel_path", "checksum"}
        filtered = {k: v for k, v in updates.items() if k in allowed}
        if not filtered:
            return False

        filtered["updated_at"] = utcnow_str()
        set_clause = ", ".join(f"{k} = ?" for k in filtered)
        values = list(filtered.values()) + [doc_id]

        cursor = self._conn.execute(
            f"UPDATE manifest SET {set_clause} WHERE doc_id = ?", values
        )
        self._conn.commit()
        return cursor.rowcount > 0

    def remove_entry(self, doc_id: str) -> bool:
        """删除注册记录。返回是否成功。"""
        cursor = self._conn.execute(
            "DELETE FROM manifest WHERE doc_id = ?", (doc_id,)
        )
        self._conn.commit()
        return cursor.rowcount > 0

    # ---- Checksum ----

    @staticmethod
    def compute_checksum(file_path: str) -> Optional[str]:
        """计算文件 SHA256。文件不存在返回 None。"""
        if not os.path.isfile(file_path):
            return None
        sha = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha.update(chunk)
        return sha.hexdigest()

    def verify_all(self, base_dir: Optional[str] = None) -> list[dict]:
        """校验所有注册文档的 checksum。

        Args:
            base_dir: v3 根目录，用于将 rel_path 解析为绝对路径。
                      默认取当前文件所在目录。

        Returns:
            不匹配的条目列表，每项含 doc_id / rel_path / expected / actual
        """
        if base_dir is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))

        rows = self._conn.execute("SELECT * FROM manifest").fetchall()
        mismatches = []
        for row in rows:
            doc_id = row["doc_id"]
            rel_path = row["rel_path"]
            expected = row["checksum"]
            abs_path = os.path.join(base_dir, rel_path)
            actual = self.compute_checksum(abs_path)
            if actual is None:
                mismatches.append({
                    "doc_id": doc_id,
                    "rel_path": rel_path,
                    "expected": expected,
                    "actual": None,
                    "error": "file_not_found",
                })
            elif actual != expected:
                mismatches.append({
                    "doc_id": doc_id,
                    "rel_path": rel_path,
                    "expected": expected,
                    "actual": actual,
                    "error": "checksum_mismatch",
                })
        return mismatches

    def rebuild(self, docs_dir: str) -> int:
        """扫描 docs/ 目录重建 manifest。

        遍历 docs_dir 下所有文件，自动生成 doc_id（相对路径转 ID），
        计算 SHA256 并写入 manifest 表。

        Args:
            docs_dir: docs/ 目录的绝对路径

        Returns:
            注册的文件数量
        """
        if not os.path.isdir(docs_dir):
            return 0

        # 重建语义：先清空旧条目再重新扫描，包裹在事务中确保原子性
        self._conn.execute("BEGIN")
        try:
            self._conn.execute("DELETE FROM manifest")

            count = 0
            for root, dirs, files in os.walk(docs_dir):
                for fname in files:
                    abs_path = os.path.join(root, fname)
                    rel_path = os.path.relpath(abs_path, os.path.dirname(docs_dir))
                    doc_id = rel_path.replace("\\", "/").replace("/", "_").replace(".", "_")
                    ext = os.path.splitext(fname)[1].lstrip(".")
                    checksum = self.compute_checksum(abs_path) or ""
                    now = utcnow_str()

                    self._conn.execute(
                        """INSERT OR REPLACE INTO manifest
                           (doc_id, rel_path, checksum, created_at, updated_at)
                           VALUES (?, ?, ?, ?, ?)""",
                        (doc_id, rel_path, checksum, now, now),
                    )
                    count += 1

            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise

        return count
