---
name: knowledge-graph
version: 1.0.0
description: "知识图谱全栈——通用 Agent 记忆图谱（CRUD/规划/跨skill通信）+ OWL 语义推理（RDFS/OWL Lite/OWL RL/SPARQL/NL混合查询）"
tags: [domain-specific, data, memory-based, file-based, cli]
triggers:
  - 知识图谱
  - 实体关系
  - 本体
  - ontology
  - OWL 推理
  - SPARQL
---

# Knowledge Graph v1.0.0

知识图谱全栈：**通用记忆（轻量CRUD）→ 语义推理（重量OWL）→ 协同路由**。

> 来源：ontology v1.0.0（通用图谱）+ domain-kit-owl v1.0.0（OWL推理）

---

## Part 1: 通用图谱 — Agent 记忆

> 一切皆实体（Entity），带类型、属性、关系。每次变更经类型约束验证后提交。

### 1.1 核心模型

```
Entity: { id, type, properties, relations, created, updated }
Relation: { from_id, relation_type, to_id, properties }
```

### 1.2 核心类型

```yaml
# 人与组织
Person: { name, email?, phone?, notes? }
Organization: { name, type?, members[] }

# 工作
Project: { name, status, goals[], owner? }
Task: { title, status, due?, priority?, assignee?, blockers[] }
Goal: { description, target_date?, metrics[] }

# 时间与地点
Event: { title, start, end?, location?, attendees[], recurrence? }
Location: { name, address?, coordinates? }

# 信息
Document: { title, path?, url?, summary? }
Message: { content, sender, recipients[], thread? }
Thread: { subject, participants[], messages[] }
Note: { content, tags[], refs[] }

# 资源
Account: { service, username, credential_ref? }
Device: { name, type, identifiers[] }
Credential: { service, secret_ref }  # 永不直接存储密钥

# 元数据
Action: { type, target, timestamp, outcome? }
Policy: { scope, rule, enforcement }
```

### 1.3 存储

默认：`memory/ontology/graph.jsonl`（append-only，保留历史）

```jsonl
{"op":"create","entity":{"id":"p_001","type":"Person","properties":{"name":"Alice"}}}
{"op":"create","entity":{"id":"proj_001","type":"Project","properties":{"name":"Website Redesign","status":"active"}}}
{"op":"relate","from":"proj_001","rel":"has_owner","to":"p_001"}
```

### 1.4 CLI 操作

```bash
# 创建实体
python3 scripts/ontology.py create --type Person --props '{"name":"Alice","email":"alice@example.com"}'

# 查询
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'
python3 scripts/ontology.py get --id task_001
python3 scripts/ontology.py related --id proj_001 --rel has_task

# 关联实体
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001

# 验证约束
python3 scripts/ontology.py validate
```

### 1.5 约束定义

在 `memory/ontology/schema.yaml` 中定义类型约束和关系约束：

```yaml
types:
  Task:
    required: [title, status]
    status_enum: [open, in_progress, blocked, done]
  Event:
    required: [title, start]
    validate: "end >= start if end exists"

relations:
  has_owner:
    from_types: [Project, Task]
    to_types: [Person]
    cardinality: many_to_one
  blocks:
    from_types: [Task]
    to_types: [Task]
    acyclic: true
```

### 1.6 规划即图变换

多步骤计划建模为图操作序列：

```
Plan: "安排团队会议并创建后续任务"

1. CREATE Event { title: "Team Sync", attendees: [p_001, p_002] }
2. RELATE Event -> has_project -> proj_001
3. CREATE Task { title: "Prepare agenda", assignee: p_001 }
4. RELATE Task -> for_event -> event_001
5. CREATE Task { title: "Send summary", assignee: p_001, blockers: [task_001] }
```

每步执行前验证约束，违反时回滚。

### 1.7 跨 Skill 通信

```python
# Email skill 创建承诺
commitment = ontology.create("Commitment", {
    "source_message": msg_id,
    "description": "Send report by Friday",
    "due": "2026-01-31"
})

# Task skill 拾取
tasks = ontology.query("Commitment", {"status": "pending"})
for c in tasks:
    ontology.create("Task", {"title": c.description, "due": c.due, "source": c.id})
```

---

## Part 2: OWL 推理 — 领域语义

> 七阶段分层架构，为领域知识提供语义推理、SPARQL 查询和可视化。

### 2.1 架构分层

```
L4: 应用层（OpenClaw Agent）
L3: 查询层（SPARQL + 自然语言混合查询）
L2: 推理层（owlrl + 自研规则引擎）
L1: 数据层（JSONL ↔ RDF 双向转换）
L0: 抽象层（统一数据模型）
```

### 2.2 七阶段概览

| Phase | 名称 | 核心能力 | 关键文件 |
|-------|------|----------|----------|
| 0 | 抽象层 | 统一数据模型、类型注册、命名空间管理 | `phase0/models.py`, `registry.py`, `namespace.py` |
| 1 | 数据互操作 | JSONL ↔ RDF 双向无损转换 | `phase1/jsonl_to_rdf.py`, `rdf_to_jsonl.py`, `schema_mapping.py` |
| 2 | 基础推理 | owlrl 三级推理（RDFS/OWL Lite/OWL RL） | `phase2/reasoner.py`, `ontology.ttl` |
| 3 | 业务规则 | 自研规则引擎 | `phase3/rules.py`, `rule_config.json` |
| 4 | SPARQL 查询 | 直接 SPARQL 执行 + 预置模板 | `phase4/query_engine.py` |
| 5 | 混合查询 | 自然语言 → 意图分类 → SPARQL 生成 | `phase5/hybrid_query.py` |
| 6 | 可视化导出 | Turtle/RDF/XML/N-Triples + Protégé兼容 | `phase6/export.py` |

### 2.3 推理层级对比

| 层级 | 能力 | 性能 | 使用场景 |
|------|------|------|---------|
| RDFS | 类层次、属性继承 | 快 | 默认推荐 |
| OWL Lite | 简单约束、对称/传递属性 | 中 | 需要更多推理 |
| OWL RL | 完整规则推理 | 慢 | 复杂推理需求 |

### 2.4 使用方法

```python
# Phase 0: 统一数据模型
from phase0 import Entity, EntityTypeRegistry, NamespaceManager

# Phase 1: JSONL ↔ RDF
from phase1 import JsonlToRdfConverter, RdfToJsonlConverter

# Phase 2: OWL 推理
from phase2 import DomainKitReasoner
reasoner = DomainKitReasoner(reasoning_level="rdfs")

# Phase 3: 业务规则
from phase3 import BusinessRuleEngine

# Phase 4: SPARQL 查询
from phase4 import SPARQLQueryEngine

# Phase 5: 自然语言查询
from phase5 import HybridQueryEngine

# Phase 6: 导出
from phase6 import ProtegeExporter
```

### 2.5 依赖

```bash
pip install rdflib>=7.0.0 owlrl>=6.2.0
```

### 2.6 验证标准

- 双向转换：100% 无损
- 推理准确率：≥90%
- 查询性能：<500ms（100次平均）
- 自然语言→SPARQL：≥80% 准确率

---

## Part 3: 协同路由

```
用户需求 → 判断复杂度
  ├─ 轻量记忆（"记住X"/"X和Y什么关系"/"X有哪些任务"）
  │   → Part 1 通用图谱（scripts/ontology.py）
  │   → 纯 JSONL，毫秒级响应
  │
  ├─ 领域推理（"所有PLC设备"/"A依赖B依赖C的传递链"/"设备兼容性分析"）
  │   → Part 2 OWL 推理（phase0~6/）
  │   → RDF 图 + 语义推理，秒级响应
  │
  └─ 混合场景（先记忆再推理）
      → Part 1 写入实体/关系 → Part 2 L1 转换为 RDF → L2 推理 → L3 查询
```

### 数据流衔接

```
Part 1 (JSONL)
    │
    ▼ Phase 1 (jsonl_to_rdf)
Part 2 L1 (RDF Graph)
    │
    ▼ Phase 2 (reasoner)
L2 (Reasoned Graph)
    │
    ▼ Phase 3 (rules) + Phase 4/5 (query)
Query Results
    │
    ▼ Phase 6 (export)
Protégé / Turtle / RDF-XML
```

### 命名空间约定

| 前缀 | URI | 用途 |
|------|-----|------|
| dk | https://domain-kit.midea.com/ontology/ | 本体根 |
| dk-entity | .../entity/ | 实体实例 |
| dk-class | .../class/ | 实体类型/类 |
| dk-rel | .../relation/ | 关系谓词 |
| dk-prop | .../property/ | 数据属性 |

---

## 文件结构

```
knowledge-graph/
├── SKILL.md                          # 本文档
├── scripts/
│   └── ontology.py                   # 通用图谱 CRUD（21KB）
├── phase0/                           # 抽象层（统一数据模型）
├── phase1/                           # 数据互操作（JSONL ↔ RDF）
├── phase2/                           # 基础推理（owlrl + ontology.ttl）
├── phase3/                           # 自研规则引擎
├── phase4/                           # SPARQL 查询
├── phase5/                           # 混合查询（NL → SPARQL）
├── phase6/                           # 可视化导出
├── tests/                            # OWL 集成测试
├── references/
│   ├── schema.md                     # 通用图谱 Schema 参考
│   ├── queries.md                    # 通用图谱查询参考
│   └── ARCHITECTURE.md               # OWL 架构详细文档
└── requirements.txt                  # rdflib + owlrl
```

---

## 测试

```bash
# 通用图谱
python3 scripts/ontology.py validate

# OWL 集成测试
cd <skill-dir>
pytest tests/ -v
```

---

*Version 1.0.0 — 合并自 ontology v1.0.0 + domain-kit-owl v1.0.0*
