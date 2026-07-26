"""
Smart Memory v3 — SQLite 数据库初始化模块

特性：
- 模块级单例连接（线程安全）
- WAL 模式 + 外键约束
- 幂等 init_db()（所有建表语句均为 CREATE TABLE IF NOT EXISTS）
"""

import os
import sqlite3
import threading
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# 路径常量
# ---------------------------------------------------------------------------
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(MODULE_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "smart_memory.db")

# 确保 data 目录存在
os.makedirs(DB_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 单例连接管理（线程安全）
# ---------------------------------------------------------------------------
_connection: sqlite3.Connection | None = None
_lock = threading.Lock()


def get_connection() -> sqlite3.Connection:
    """返回模块级单例 sqlite3.Connection。

    线程安全：通过 threading.Lock 保护初始化过程。
    首次调用时自动启用 WAL 模式和 foreign_keys。
    """
    global _connection

    if _connection is not None:
        return _connection

    with _lock:
        if _connection is not None:
            return _connection

        _connection = sqlite3.connect(DB_PATH, check_same_thread=False)
        _connection.row_factory = sqlite3.Row
        _connection.execute("PRAGMA journal_mode=WAL;")
        _connection.execute("PRAGMA foreign_keys=ON;")
        return _connection


def close_db() -> None:
    """关闭数据库连接（若存在），关闭前执行 WAL checkpoint。"""
    global _connection

    with _lock:
        if _connection is not None:
            _connection.execute("PRAGMA wal_checkpoint(TRUNCATE);")
            _connection.close()
            _connection = None


def checkpoint_db() -> None:
    """执行 WAL checkpoint(TRUNCATE)，供批量操作后外部调用。"""
    conn = get_connection()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")


# ---------------------------------------------------------------------------
# DDL 语句（与 schema.sql 保持同步）
# ---------------------------------------------------------------------------

DDL_CUES = """\
CREATE TABLE IF NOT EXISTS cues (
    id          TEXT PRIMARY KEY,
    title       TEXT NOT NULL,
    keywords    TEXT NOT NULL,
    scene       TEXT NOT NULL DEFAULT '',
    docs        TEXT NOT NULL DEFAULT '[]',
    importance  REAL NOT NULL DEFAULT 0.5
                    CHECK(importance >= 0 AND importance <= 1),
    retention   REAL NOT NULL DEFAULT 1.0
                    CHECK(retention >= 0 AND retention <= 1),
    status      TEXT NOT NULL DEFAULT 'active'
                    CHECK(status IN ('active','stale_observed','stale_confirmed','deleted')),
    stale_count INTEGER NOT NULL DEFAULT 0,
    stale_reason TEXT DEFAULT '',
    stale_detected_at TEXT DEFAULT NULL,
    preconditions TEXT DEFAULT '[]',
    created     TEXT NOT NULL DEFAULT (datetime('now')),
    updated     TEXT NOT NULL DEFAULT (datetime('now'))
);
"""

DDL_MANIFEST = """\
CREATE TABLE IF NOT EXISTS manifest (
    doc_id      TEXT PRIMARY KEY,
    rel_path    TEXT NOT NULL,
    checksum    TEXT NOT NULL DEFAULT '',
    created_at  TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at  TEXT NOT NULL DEFAULT (datetime('now'))
);
"""

DDL_SIGNALS = """\
CREATE TABLE IF NOT EXISTS signals (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    cue_id      TEXT NOT NULL,
    signal_type TEXT NOT NULL
                    CHECK(signal_type IN (
                        'recall','used','failed',
                        'confirmed','ignored','contradicted'
                    )),
    recorded_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (cue_id) REFERENCES cues(id) ON DELETE CASCADE
);
"""

DDL_ENV_SNAPSHOTS = """\
CREATE TABLE IF NOT EXISTS env_snapshots (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    cue_id      TEXT,
    os          TEXT NOT NULL,
    python      TEXT NOT NULL,
    shell       TEXT NOT NULL DEFAULT '',
    git         TEXT DEFAULT NULL,
    captured_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (cue_id) REFERENCES cues(id) ON DELETE SET NULL
);
"""

DDL_PRECONDITION_CACHE = """\
CREATE TABLE IF NOT EXISTS precondition_cache (
    cue_id      TEXT PRIMARY KEY,
    all_passed  INTEGER NOT NULL DEFAULT 1,
    checks_json TEXT NOT NULL DEFAULT '[]',
    evaluated_at TEXT NOT NULL DEFAULT (datetime('now')),
    ttl_minutes INTEGER NOT NULL DEFAULT 60,
    FOREIGN KEY (cue_id) REFERENCES cues(id) ON DELETE CASCADE
);
"""

# 索引 DDL（按 SCHEMA.md §3 顺序）
INDEX_DDL = [
    "CREATE INDEX IF NOT EXISTS idx_cues_status ON cues(status);",
    "CREATE INDEX IF NOT EXISTS idx_cues_retention ON cues(retention);",
    "CREATE INDEX IF NOT EXISTS idx_cues_importance ON cues(importance);",
    "CREATE INDEX IF NOT EXISTS idx_manifest_checksum ON manifest(checksum);",
    "CREATE INDEX IF NOT EXISTS idx_signals_cue_id ON signals(cue_id);",
    "CREATE INDEX IF NOT EXISTS idx_signals_type ON signals(signal_type);",
    "CREATE INDEX IF NOT EXISTS idx_signals_recorded ON signals(recorded_at);",
    "CREATE INDEX IF NOT EXISTS idx_env_snapshots_cue_id ON env_snapshots(cue_id);",
    "CREATE INDEX IF NOT EXISTS idx_env_snapshots_captured ON env_snapshots(captured_at);",
    "CREATE INDEX IF NOT EXISTS idx_precond_cache_ttl ON precondition_cache(evaluated_at);",
    # 组合索引（热点查询优化）
    "CREATE INDEX IF NOT EXISTS idx_signals_cue_type ON signals(cue_id, signal_type);",
    "CREATE INDEX IF NOT EXISTS idx_cues_status_retention ON cues(status, retention);",
]


def init_db(conn: sqlite3.Connection | None = None) -> sqlite3.Connection:
    """执行所有 CREATE TABLE IF NOT EXISTS + 索引 DDL，幂等。

    参数:
        conn: 可选外部连接；不传则使用模块级单例。

    返回:
        使用的 sqlite3.Connection 对象。
    """
    if conn is None:
        conn = get_connection()

    # 建表
    conn.execute(DDL_CUES)
    conn.execute(DDL_MANIFEST)
    conn.execute(DDL_SIGNALS)
    conn.execute(DDL_ENV_SNAPSHOTS)
    conn.execute(DDL_PRECONDITION_CACHE)

    # 建索引
    for ddl in INDEX_DDL:
        conn.execute(ddl)

    # 为 manifest 表添加 updated_at 自动更新触发器（避免递归触发）
    conn.execute("""
        CREATE TRIGGER IF NOT EXISTS trg_manifest_updated_at
        AFTER UPDATE ON manifest
        FOR EACH ROW
        WHEN NEW.updated_at = OLD.updated_at
        BEGIN
            UPDATE manifest SET updated_at = datetime('now') WHERE doc_id = NEW.doc_id;
        END;
    """)

    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# UTC 时间工具函数
# ---------------------------------------------------------------------------

def utcnow_str() -> str:
    """返回 UTC 时间字符串（naive），格式 YYYY-MM-DD HH:MM:SS。"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def utcnow_dt() -> datetime:
    """返回当前 UTC 时间的 naive datetime 对象。"""
    return datetime.now(timezone.utc).replace(tzinfo=None)
