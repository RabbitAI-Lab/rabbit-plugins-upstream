-- Smart Memory v3 — SQLite 数据库完整建表脚本
-- 版本: v3.0 | 日期: 2026-07-04
-- 可直接通过 sqlite3 执行: sqlite3 memory.db < schema.sql

PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- ============================================================
-- 1. cues — 线索卡主表
-- 存储已学习的操作线索，含权重（importance/retention）和状态流转。
-- ============================================================
CREATE TABLE IF NOT EXISTS cues (
    id          TEXT PRIMARY KEY,
    title       TEXT NOT NULL,              -- 线索标题
    keywords    TEXT NOT NULL,              -- JSON 数组字符串：'["kw1","kw2"]'
    scene       TEXT NOT NULL DEFAULT '',   -- 执行场景/上下文描述
    docs        TEXT NOT NULL DEFAULT '[]', -- JSON 数组字符串：关联的文档 rel_path 列表
    importance  REAL NOT NULL DEFAULT 0.5   -- 重要度权重 [0,1]，由用户反馈 signals 驱动
                    CHECK(importance >= 0 AND importance <= 1),
    retention   REAL NOT NULL DEFAULT 1.0   -- 记忆保持度 [0,1]，Ebbinghaus 衰减模型
                    CHECK(retention >= 0 AND retention <= 1),
    status      TEXT NOT NULL DEFAULT 'active'
                    CHECK(status IN ('active','stale_observed','stale_confirmed','deleted')),
    stale_count INTEGER NOT NULL DEFAULT 0, -- 连续失效信号计数
    stale_reason TEXT DEFAULT '',           -- 失效原因（信号驱动标记 / 前置条件失败 / retention 过低）
    stale_detected_at TEXT DEFAULT NULL,    -- 首次检测失效时间
    preconditions TEXT DEFAULT '[]',        -- JSON：前置条件列表
    created     TEXT NOT NULL DEFAULT (datetime('now')),
    updated     TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ============================================================
-- 2. manifest — 文档注册表
-- 记录关联文档的路径和 SHA256 校验和，支持完整性校验。
-- ============================================================
CREATE TABLE IF NOT EXISTS manifest (
    doc_id      TEXT PRIMARY KEY,            -- 文档唯一标识
    rel_path    TEXT NOT NULL,               -- 相对于 v3 根目录的文件路径
    checksum    TEXT NOT NULL DEFAULT '',    -- SHA256 校验和
    created_at  TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ============================================================
-- 3. signals — 信号记录表（事件日志模式）
-- 每次 record() 插入一条，驱动 Ebbinghaus 衰减重算 + 自动恢复 / 信号驱动标记。
-- ============================================================
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

-- ============================================================
-- 4. env_snapshots — 环境指纹表
-- ============================================================
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

-- ============================================================
-- 5. precondition_cache — 前置条件缓存表
-- L1 recall 阶段查询此表，决定对匹配卡片的降权策略（passed / failed / unknown）。
-- ============================================================
CREATE TABLE IF NOT EXISTS precondition_cache (
    cue_id      TEXT PRIMARY KEY,
    all_passed  INTEGER NOT NULL DEFAULT 1,
    checks_json TEXT NOT NULL DEFAULT '[]',
    evaluated_at TEXT NOT NULL DEFAULT (datetime('now')),
    ttl_minutes INTEGER NOT NULL DEFAULT 60,
    FOREIGN KEY (cue_id) REFERENCES cues(id) ON DELETE CASCADE
);

-- ============================================================
-- 索引汇总
-- ============================================================

-- cues 表索引
CREATE INDEX IF NOT EXISTS idx_cues_status ON cues(status);
CREATE INDEX IF NOT EXISTS idx_cues_retention ON cues(retention);
CREATE INDEX IF NOT EXISTS idx_cues_importance ON cues(importance);

-- manifest 表索引
CREATE INDEX IF NOT EXISTS idx_manifest_checksum ON manifest(checksum);

-- signals 表索引
CREATE INDEX IF NOT EXISTS idx_signals_cue_id ON signals(cue_id);
CREATE INDEX IF NOT EXISTS idx_signals_type ON signals(signal_type);
CREATE INDEX IF NOT EXISTS idx_signals_recorded ON signals(recorded_at);

-- env_snapshots 表索引
CREATE INDEX IF NOT EXISTS idx_env_snapshots_cue_id ON env_snapshots(cue_id);
CREATE INDEX IF NOT EXISTS idx_env_snapshots_captured ON env_snapshots(captured_at);

-- precondition_cache 表索引
CREATE INDEX IF NOT EXISTS idx_precond_cache_ttl ON precondition_cache(evaluated_at);

-- ============================================================
-- 组合索引（热点查询优化）
-- ============================================================

-- signals: cue_id + signal_type 组合查询（信号驱动标记 & 统计分析）
CREATE INDEX IF NOT EXISTS idx_signals_cue_type ON signals(cue_id, signal_type);

-- cues: status + retention 组合查询（GC scan_stale 效率）
CREATE INDEX IF NOT EXISTS idx_cues_status_retention ON cues(status, retention);

-- ============================================================
-- 触发器
-- ============================================================

-- manifest 表 updated_at 自动更新（仅当应用层未主动设置 updated_at 时触发）
CREATE TRIGGER IF NOT EXISTS trg_manifest_updated_at
AFTER UPDATE ON manifest
FOR EACH ROW
WHEN NEW.updated_at = OLD.updated_at
BEGIN
    UPDATE manifest SET updated_at = datetime('now') WHERE doc_id = NEW.doc_id;
END;
