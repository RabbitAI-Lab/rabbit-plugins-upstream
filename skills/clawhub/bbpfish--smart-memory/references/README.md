# Smart Memory v3

线索驱动的渐进式记忆系统。基于 Ebbinghaus 遗忘曲线建模知识衰减，通过线索卡（Cue）+ 信号（Signal）双层机制实现智能记忆管理。

## 核心概念

| 概念 | 说明 |
|------|------|
| **线索卡 (Cue)** | 最小记忆单元，含标题、关键词、场景、关联文档、前置条件 |
| **信号 (Signal)** | 对线索卡的交互反馈（recall/used/failed/confirmed 等），驱动 retention 升降 |
| **三步决策 (Decide)** | 召回 → 相关性评分 → 冗余检测 → 决定是否注入上下文 |
| **渐进式召回** | L1（线索级摘要）→ L2（文档全文展开），按需加载 |
| **衰减模型** | 基于 Ebbinghaus 公式：retention × e^(-t/S)，S = importance × 720h |
| **垃圾回收 (GC)** | active → stale_observed → stale_confirmed → deleted 状态机 |

## 环境要求

- Python ≥ 3.10
- 操作系统：Windows / Linux / macOS

## 安装

```bash
cd smart-memory/v3
pip install -r requirements.txt
```

## 快速开始

```bash
# 1. 初始化数据库
python memory.py init-db

# 2. 记录一条线索
python memory.py record \
  --title "FastAPI 异步最佳实践" \
  --keywords "Python,FastAPI,异步,事件循环" \
  --scene "使用 FastAPI 构建异步 Web 服务时需要注意事件循环管理"

# 3. 召回记忆
python memory.py recall -q "Python 异步编程"
```

## CLI 命令速览

| 命令 | 用途 |
|------|------|
| `init-db` | 初始化数据库（幂等） |
| `record` | 记录知识卡片 |
| `recall` | 召回记忆（L1/L2 渐进披露） |
| `decide` | 执行三步决策 |
| `signal` | 记录交互信号 |
| `validate` | 运行一致性校验 |
| `stale-detect` | 巡检过期卡片 |
| `gc` | 垃圾回收 |
| `restore` | 恢复卡片到 active |
| `delete` | 标记删除卡片 |
| `decay-report` | 衰减报告 |
| `scan-round` | 扫描 docs/ 更新 manifest + 前置条件 |
| `rebuild-manifest` | 重建文档注册表 |
| `orphans` | 检测孤文档和断引用 |
| `slim` | 文档瘦身规则检测 |
| `migrate` | 从 v2 迁移 |
| `env-snapshot` | 采集系统环境指纹 |

### recall 详细参数

```
python memory.py recall -q <查询> [--top N] [--days N] [--mode l1|l2|full]
    [--load] [--max-docs N] [--verbose] [--include-stale]
    [--skip-precond-cache] [--json]
```

### record 详细参数

```
python memory.py record --title <标题> [--id <ID>] [--keywords <逗号分隔>]
    [--scene <场景/内容>] [--docs <文档ID,逗号分隔>]
    [--importance 0.5] [--retention 1.0] [--preconditions <;;分隔>]
    [--capture-env]
```

## 目录结构

```
v3/
├── memory.py              # CLI 入口
├── db.py                  # 数据库连接管理
├── schema.sql             # 表结构定义
├── cues.py                # 线索卡数据层
├── signals.py             # 信号数据层
├── manifest.py            # 文档注册表
├── recall.py              # 召回引擎（L1/L2）
├── decide.py              # 三步决策引擎
├── gc.py                  # 垃圾回收
├── precondition.py        # 前置条件预检
├── validate.py            # 一致性校验
├── migrate.py             # v2 → v3 迁移
├── tokenizer.py           # 中文分词器
├── __init__.py            # 公共 API 导出
├── requirements.txt       # 依赖声明
├── .flake8                # Linting 配置
├── docs/                  # 关联文档目录
├── test_all.py            # 综合测试入口
├── test_db.py             # 数据库初始化测试
├── test_data_layer.py     # 数据层集成测试
├── test_recall_decide.py  # 召回/决策测试
├── test_gc.py             # GC 测试
├── test_migrate.py        # 迁移测试
├── test_signals.py        # 信号测试
└── test_manifest.py       # 注册表测试
```

## 运行测试

```bash
# 运行全部测试
python test_all.py

# 运行单个模块测试
python test_db.py
python -m pytest test_gc.py -v
```

## 架构简述

```
CLI (memory.py)
    │
    ▼
核心引擎层
├── RecallEngine   (recall.py)    — 线索召回 + 全文展开
├── DecideEngine   (decide.py)    — 三步决策
├── GarbageCollector (gc.py)     — 状态机推进 + 物理删除
└── PreconditionEvaluator        — 前置条件批量检查
    │
    ▼
数据访问层
├── CueStore       (cues.py)     — 线索 CRUD + 全文搜索
├── SignalStore    (signals.py)  — 信号记录 + retention 更新
├── ManifestStore  (manifest.py) — 文档注册表
└── db.py / schema.sql           — 连接管理 + 表结构
```
