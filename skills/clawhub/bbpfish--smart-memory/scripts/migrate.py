"""
Smart Memory v3 — v2 → v3 迁移工具

核心流程:
  1. migrate_cues():  cues.jsonl → cues + signals 表
  2. migrate_manifest(): manifest.yaml → manifest 表
  3. migrate_docs(): 复制 docs/ 目录
  4. verify(): 迁移后数据校验
  5. rollback(): 清空 cues/signals/manifest/environment_snapshots 表
"""

import hashlib
import json
import logging
import os
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# v2 status → v3 status 映射
# ---------------------------------------------------------------------------
STATUS_MAP = {
    "active": "active",
    "stale": "stale_observed",
    "deprecated": "stale_confirmed",
    "": "active",
}

# v3 允许的 status 枚举值
VALID_STATUSES = frozenset({"active", "stale_observed", "stale_confirmed", "deleted"})


# ---------------------------------------------------------------------------
# Migrator
# ---------------------------------------------------------------------------
class Migrator:
    """v2 → v3 数据迁移器。"""

    def __init__(self, v2_dir: str, db_path: str | None = None):
        """
        参数:
            v2_dir: v2 数据目录路径（包含 cues.jsonl / manifest.yaml / docs/）
            db_path: v3 数据库路径，None 则使用 db.py 默认路径。
        """
        self.v2_dir = Path(v2_dir).resolve()
        if not self.v2_dir.is_dir():
            raise FileNotFoundError(f"v2 目录不存在: {self.v2_dir}")

        if db_path is None:
            from v3.db import DB_PATH

            db_path = DB_PATH

        self.db_path = str(db_path)
        self._conn: sqlite3.Connection | None = None

        # 缓存：迁移前的源统计数据（run() 时填充）
        self._src_cue_count = 0
        self._src_signal_total = 0
        self._src_manifest_count = 0

    # ------------------------------------------------------------------
    # 内部连接管理
    # ------------------------------------------------------------------
    def _get_conn(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_path)
            self._conn.row_factory = sqlite3.Row
            self._conn.execute("PRAGMA foreign_keys = ON;")
            # 确保表存在
            from v3.db import init_db

            init_db(self._conn)
        return self._conn

    def _close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    # ------------------------------------------------------------------
    # migrate_cues
    # ------------------------------------------------------------------
    def migrate_cues(self, dry_run: bool = False) -> int:
        """从 v2/cues.jsonl 迁移到 cues + signals 表。

        返回: 迁入的卡片数量。
        """
        cues_path = self.v2_dir / "cues.jsonl"
        if not cues_path.exists():
            logger.warning(f"cues.jsonl 不存在: {cues_path}")
            return 0

        conn = self._get_conn()
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        migrated = 0
        total_signals = 0

        with open(cues_path, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    cue = json.loads(line)
                except json.JSONDecodeError as exc:
                    logger.warning(f"跳过无效 JSON 行: {exc}")
                    continue

                cue_id = cue.get("id")
                if not cue_id:
                    logger.warning("跳过缺少 id 的条目")
                    continue

                # 映射 status
                v2_status = cue.get("status", "active")
                v3_status = STATUS_MAP.get(v2_status, v2_status)
                if v3_status not in VALID_STATUSES:
                    v3_status = "active"

                stale_count = 0
                if v2_status == "stale":
                    stale_count = 1
                elif v2_status == "deprecated":
                    stale_count = 3

                # 映射 importance：兼容 v2 的 weight 字段
                importance = cue.get("importance")
                if importance is None and "weight" in cue:
                    weight = float(cue["weight"])
                    importance = max(0.0, min(1.0, weight))

                if dry_run:
                    migrated += 1
                    # 统计 signals 数量
                    sigs = cue.get("signals", {})
                    if isinstance(sigs, dict):
                        total_signals += sum(
                            v for k, v in sigs.items() if k in ("recalled", "used", "failed")
                        )
                    continue

                # 插入 cues 表 (INSERT OR IGNORE 实现幂等)
                conn.execute(
                    """INSERT OR IGNORE INTO cues
                       (id, title, keywords, scene, docs,
                        importance, retention, status, stale_count,
                        stale_reason, stale_detected_at, preconditions,
                        created, updated)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        cue_id,
                        cue.get("title", ""),
                        json.dumps(cue.get("keywords", []), ensure_ascii=False),
                        cue.get("scene", ""),
                        json.dumps(cue.get("docs", []), ensure_ascii=False),
                        importance if importance is not None else 0.5,
                        cue.get("retention", 1.0),
                        v3_status,
                        stale_count,
                        cue.get("stale_reason", ""),
                        cue.get("stale_detected_at"),
                        json.dumps(cue.get("preconditions", []), ensure_ascii=False),
                        cue.get("created", ""),
                        cue.get("updated", ""),
                    ),
                )

                # 迁移 signals → signals 表
                sigs = cue.get("signals", {})
                if isinstance(sigs, dict):
                    signal_types = {
                        "recalled": "recall",
                        "used": "used",
                        "failed": "failed",
                        "confirmed": "confirmed",
                        "ignored": "ignored",
                        "contradicted": "contradicted",
                    }
                    for json_key, signal_type in signal_types.items():
                        count = int(sigs.get(json_key, 0))
                        for _ in range(count):
                            conn.execute(
                                "INSERT INTO signals (cue_id, signal_type, recorded_at) VALUES (?, ?, ?)",
                                (cue_id, signal_type, now),
                            )
                            total_signals += 1

                # 迁移 env_fingerprint → env_snapshots 表
                fp = cue.get("env_fingerprint")
                if isinstance(fp, dict):
                    conn.execute(
                        """INSERT INTO env_snapshots (cue_id, os, python, shell, git, captured_at)
                           VALUES (?, ?, ?, ?, ?, ?)""",
                        (
                            cue_id,
                            fp.get("os", ""),
                            fp.get("python", ""),
                            fp.get("shell", ""),
                            fp.get("git"),
                            fp.get("captured_at", now),
                        ),
                    )

                migrated += 1

        if not dry_run:
            conn.commit()

        self._src_cue_count = migrated
        self._src_signal_total = total_signals
        return migrated

    # ------------------------------------------------------------------
    # migrate_manifest
    # ------------------------------------------------------------------
    def migrate_manifest(self, dry_run: bool = False) -> int:
        """从 v2/manifest.yaml 迁移到 manifest 表。

        返回: 迁入的文档数量。
        """
        manifest_path = self.v2_dir / "manifest.yaml"
        if not manifest_path.exists():
            logger.warning(f"manifest.yaml 不存在: {manifest_path}")
            return 0

        with open(manifest_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not data or "docs" not in data:
            logger.warning("manifest.yaml 格式异常，缺少 docs 字段")
            return 0

        docs = data["docs"]
        if not isinstance(docs, dict):
            logger.warning("manifest.yaml docs 不是 dict 类型")
            return 0

        if dry_run:
            self._src_manifest_count = len(docs)
            return len(docs)

        conn = self._get_conn()
        migrated = 0

        for doc_id, rel_path in docs.items():
            abs_path = self.v2_dir / rel_path
            checksum = ""
            if abs_path.exists():
                checksum = self._sha256_file(str(abs_path))

            conn.execute(
                """INSERT OR IGNORE INTO manifest (doc_id, rel_path, checksum) VALUES (?, ?, ?)""",
                (doc_id, str(rel_path), checksum),
            )
            migrated += 1

        conn.commit()
        self._src_manifest_count = migrated
        return migrated

    # ------------------------------------------------------------------
    # migrate_docs
    # ------------------------------------------------------------------
    def migrate_docs(self, dry_run: bool = False, target_dir: str | None = None) -> int:
        """复制 v2/docs/ 到 v3/docs/。

        参数:
            dry_run: 仅列出文件不复制
            target_dir: 目标目录，None 则使用 v3/docs/。
        返回: 复制的文件数量。
        """
        src_docs = self.v2_dir / "docs"
        if not src_docs.exists():
            logger.warning(f"docs/ 目录不存在: {src_docs}")
            return 0

        if target_dir is None:
            # v3 模块目录下的 docs/
            target_dir = str(Path(__file__).resolve().parent / "docs")

        if dry_run:
            count = 0
            for root, _dirs, files in os.walk(src_docs):
                for fname in files:
                    rel = Path(root) / fname
                    if not fname.startswith(".deprecated"):
                        count += 1
            return count

        # 确保目标父目录存在
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)

        # 如果目标已存在，先删除
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

        file_count = 0

        def _ignore_deprecated(directory, contents):
            return [c for c in contents if c.startswith(".deprecated")]

        shutil.copytree(
            str(src_docs),
            target_dir,
            ignore=_ignore_deprecated,
            dirs_exist_ok=False,
        )

        for root, _dirs, files in os.walk(target_dir):
            file_count += len(files)

        return file_count

    # ------------------------------------------------------------------
    # run
    # ------------------------------------------------------------------
    def run(self, dry_run: bool = False) -> dict[str, Any]:
        """执行完整迁移。

        返回:
            {
                'cues': int, 'signals': int, 'manifest': int, 'docs': int,
                'errors': list[str], 'dry_run': bool
            }
        """
        errors: list[str] = []

        # 1. 迁移 cues + signals
        try:
            cues_count = self.migrate_cues(dry_run=dry_run)
        except Exception as exc:
            errors.append(f"migrate_cues 失败: {exc}")
            cues_count = 0

        # 2. 迁移 manifest
        try:
            manifest_count = self.migrate_manifest(dry_run=dry_run)
        except Exception as exc:
            errors.append(f"migrate_manifest 失败: {exc}")
            manifest_count = 0

        # 3. 复制 docs
        try:
            docs_count = self.migrate_docs(dry_run=dry_run)
        except Exception as exc:
            errors.append(f"migrate_docs 失败: {exc}")
            docs_count = 0

        self._close()

        return {
            "cues": cues_count,
            "signals": self._src_signal_total,
            "manifest": manifest_count,
            "docs": docs_count,
            "errors": errors,
            "dry_run": dry_run,
        }

    # ------------------------------------------------------------------
    # verify
    # ------------------------------------------------------------------
    def verify(self) -> dict[str, Any]:
        """迁移后数据校验。

        返回:
            {
                'cues_match': bool,
                'manifest_match': bool,
                'sample_check': dict,
                'errors': list[str],
                'details': dict,
            }
        """
        errors: list[str] = []
        conn = self._get_conn()

        # ---- 校验 cues ----
        v3_cues = conn.execute("SELECT COUNT(*) as cnt FROM cues").fetchone()["cnt"]
        v2_cues = self._count_cues_jsonl()
        cues_match = v3_cues == v2_cues

        if not cues_match:
            errors.append(f"cues 数量不一致: v2={v2_cues}, v3={v3_cues}")

        # ---- 校验 manifest ----
        v3_manifest = conn.execute("SELECT COUNT(*) as cnt FROM manifest").fetchone()["cnt"]
        v2_manifest = self._count_manifest_entries()
        manifest_match = v3_manifest == v2_manifest

        if not manifest_match:
            errors.append(f"manifest 数量不一致: v2={v2_manifest}, v3={v3_manifest}")

        # ---- 抽样校验 3 条内容 ----
        sample_check = {}
        cues_rows = conn.execute("SELECT id, title, keywords, importance FROM cues LIMIT 3").fetchall()
        v2_map = self._load_v2_cues_map()

        for row in cues_rows:
            cue_id = row["id"]
            v2_cue = v2_map.get(cue_id)
            if v2_cue is None:
                sample_check[cue_id] = {"match": False, "reason": "v2 中找不到此卡片"}
                continue

            # 兼容 weight 字段映射
            v2_importance = v2_cue.get("importance")
            if v2_importance is None and "weight" in v2_cue:
                v2_importance = max(0.0, min(1.0, float(v2_cue["weight"])))
            if v2_importance is None:
                v2_importance = 0.5

            checks = {
                "title_match": row["title"] == v2_cue.get("title"),
                "keywords_match": json.loads(row["keywords"]) == v2_cue.get("keywords", []),
                "importance_match": abs(row["importance"] - v2_importance) < 0.001,
            }
            all_match = all(checks.values())
            sample_check[cue_id] = {"match": all_match, "checks": checks}
            if not all_match:
                errors.append(f"抽样 {cue_id} 内容不一致: {checks}")

        self._close()

        return {
            "cues_match": cues_match,
            "manifest_match": manifest_match,
            "sample_check": sample_check,
            "errors": errors,
            "details": {
                "v2_cues": v2_cues,
                "v3_cues": v3_cues,
                "v2_manifest": v2_manifest,
                "v3_manifest": v3_manifest,
            },
        }

    # ------------------------------------------------------------------
    # rollback
    # ------------------------------------------------------------------
    def rollback(self) -> dict[str, int]:
        """回滚迁移：清空 v3 数据库的 cues/signals/manifest/env_snapshots 表。

        注意：precondition_cache 有 ON DELETE CASCADE 级联 cues，
              删除 cues 时会自动清空。

        返回: 各表删除行数。
        """
        conn = self._get_conn()

        # 先删子表（有外键约束），再删主表
        signals_rowcount = conn.execute("DELETE FROM signals").rowcount
        env_snapshots_rowcount = conn.execute("DELETE FROM env_snapshots").rowcount
        manifest_rowcount = conn.execute("DELETE FROM manifest").rowcount
        cues_rowcount = conn.execute("DELETE FROM cues").rowcount

        conn.commit()
        self._close()

        return {
            "cues": cues_rowcount,
            "signals": signals_rowcount,
            "manifest": manifest_rowcount,
            "env_snapshots": env_snapshots_rowcount,
        }

    # ------------------------------------------------------------------
    # 内部辅助方法
    # ------------------------------------------------------------------
    def _count_cues_jsonl(self) -> int:
        """统计 v2/cues.jsonl 非空行数。"""
        path = self.v2_dir / "cues.jsonl"
        if not path.exists():
            return 0
        count = 0
        with open(path, "r", encoding="utf-8-sig") as f:
            for line in f:
                if line.strip():
                    count += 1
        return count

    def _count_manifest_entries(self) -> int:
        """统计 v2/manifest.yaml 中 docs 条目数。"""
        path = self.v2_dir / "manifest.yaml"
        if not path.exists():
            return 0
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and isinstance(data.get("docs"), dict):
            return len(data["docs"])
        return 0

    def _load_v2_cues_map(self) -> dict[str, dict]:
        """加载 v2/cues.jsonl 为 {cue_id: cue} 映射。"""
        path = self.v2_dir / "cues.jsonl"
        result = {}
        if not path.exists():
            return result
        with open(path, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    cue = json.loads(line)
                    if "id" in cue:
                        result[cue["id"]] = cue
                except json.JSONDecodeError:
                    pass
        return result

    @staticmethod
    def _sha256_file(filepath: str) -> str:
        """计算文件的 SHA256 哈希。"""
        sha = hashlib.sha256()
        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                sha.update(chunk)
        return sha.hexdigest()
