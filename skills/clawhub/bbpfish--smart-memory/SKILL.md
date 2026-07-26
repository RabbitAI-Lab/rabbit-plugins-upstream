---
name: smart-memory
description: >
  分层长期记忆管理系统。线索驱动（Cue-driven），任务前 TF-IDF 语义召回，任务后 LLM 结构化收割知识卡片，支持语义去重、时间衰减权重、四级 GC 状态机、信号分析与成熟度报告、跨卡关联与聚类合成。三语文档。
  触发关键词：记忆、memory、记录、记住、回忆、recall、经验、沉淀、知识库、长期记忆、smart-memory。
---

# smart-memory v3

分层长期记忆管理系统 — 线索驱动（Cue-driven），跨会话持久化知识，任务前自动召回，任务后自动沉淀。

## 快速使用

```bash
python memory.py init-db
python memory.py recall -q "查询" --top 8 --days 30
python memory.py record --title "标题" --content "内容"
python memory.py signal <card_id> recall
python memory.py env-snapshot
python memory.py migrate --from <v2_dir>
```

## 维护命令

```bash
python memory.py validate
python memory.py decay-report
python memory.py slim
python memory.py stale-detect
python memory.py restore <card_id>
python memory.py gc --dry-run
python memory.py gc
```

## 核心架构

```
memory.py (CLI 入口)
├── recall.py       → L1 TF-IDF → L2 语义渐进召回
├── precondition.py → 前置条件检查
├── decide.py       → 三步决策引擎
├── gc.py           → 四级 GC 状态机
├── cues.py         → 线索 CRUD
├── signals.py      → 信号驱动 retention
├── manifest.py     → 文档清单
├── db.py           → SQLite 数据层
├── tokenizer.py    → 中英文分词
├── validate.py     → 一致性校验
├── migrate.py      → v2→v3 迁移
└── schema.sql      → 表结构
```

## 数据存储

SQLite 数据库：`v3/data/smart_memory.db`（WAL 模式）

## 关键概念

**四级 GC**：ACTIVE → WEAK → DORMANT → DELETED

**六种信号**：recall +0.05 / update +0.1 / create=初始 / decay(遗忘曲线) / merge +0.08 / reference +0.03

**三步决策**：是否写入 → 覆盖/合并 → 执行

---

## English

Cue-driven long-term memory system. TF-IDF recall before tasks, structured harvesting after tasks, semantic deduplication, time-decay weighting, four-tier GC.

**Commands**: `init-db`, `recall`, `record`, `decide`, `signal`, `stale-detect`, `gc`, `validate`, `slim`, `decay-report`, `migrate`, `env-snapshot`

---

## 繁體中文

線索驅動長期記憶系統。任務前 TF-IDF 召回，任務後結構化收割，語義去重，時間衰減權重，四級 GC。

**命令**: `init-db`, `recall`, `record`, `decide`, `signal`, `stale-detect`, `gc`, `validate`, `slim`, `decay-report`, `migrate`, `env-snapshot`
