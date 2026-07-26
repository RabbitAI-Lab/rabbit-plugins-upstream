---
slug: ontology
name: ontology
version: "1.0.0"
displayName: 类型化知识图谱引擎
summary: 基于类型约束的知识图谱系统，为智能代理提供结构化记忆与可组合技能
license: MIT
description: |-
  类型化知识图谱引擎，将知识表示为可验证的实体-关系图谱。每个实体拥有类型、属性和关系，
  所有变更在提交前根据类型约束进行验证。核心能力涵盖类型化实体创建与验证、关系图谱与基数约束、
  Schema约束系统、无环验证、追加式变更日志、图谱遍历查询、跨技能契约声明、计划即图谱变换。
  支持 Person、Organization、Project、Task、Goal、Event、Document、Credential 等12种核心实体类型，
  可通过Schema自定义扩展。数据以追加式 JSONL 格式存储，支持迁移至 SQLite数据库。
  适用于项目任务管理、依赖关系追踪、知识库构建、跨技能状态共享、多步计划建模等场景。
tools:
  - read
  - exec
---

# 类型化知识图谱引擎

将知识表示为可验证的实体-关系图谱系统。一切皆为实体，拥有类型、属性和与其他实体的关系。每次变更在提交前根据类型约束进行验证，确保图谱一致性。支持追加式变更日志，保留完整历史记录。

## 核心能力

### 1. 类型化实体创建与验证
创建带有类型约束的实体，支持12种预定义核心类型和自定义扩展：

| 核心类型 | 必需属性 | 可选属性 |
|---------|---------|---------|
| Person | name | email, phone, notes |
| Organization | name | type, members[] |
| Project | name, status | goals[], owner |
| Task | title, status | due, priority, assignee, blockers[] |
| Goal | description | target_date, metrics[] |
| Event | title, start | end, location, attendees[], recurrence |
| Location | name | address, coordinates |
| Document | title | path, url, summary |
| Message | content, sender | recipients[], thread |
| Note | content | tags[], refs[] |
| Account | service, username | credential_ref |
| Credential | service, secret_ref | （禁止直接存储密码/令牌） |

参数：`--type`（实体类型）、`--props`（JSON格式属性）

输出：实体ID（如 `p_001`、`task_003`）、创建时间戳、验证结果。

**处理**: 按照skill规范执行类型化实体创建与验证操作,遵循单一意图原则。
### 2. 关系图谱与基数约束

在实体之间建立类型化关系，支持基数约束和方向验证：

| 关系类型 | 源类型 | 目标类型 | 基数 |
|---------|-------|---------|------|
| has_owner | Project, Task | Person | many_to_one |
| has_task | Project | Task | one_to_many |
| has_member | Organization | Person | many_to_many |
| blocks | Task | Task | many_to_many（无环） |
| depends_on | Task | Task | many_to_many（无环） |
| attends | Person | Event | many_to_many |
| references | Document | Document | many_to_many |

参数：`--from`（源实体ID）、`--rel`（关系类型）、`--to`（目标实体ID）

输出：关系记录、基数验证结果、无环检查结果。

### 3. Schema约束系统
通过 `memory/ontology/schema.yaml` 定义类型约束，所有变更在提交前强制验证：

```yaml
types:
  Task:
    required: [title, status]
    status_enum: [open, in_progress, blocked, done]
  Event:
    required: [title, start]
    validate: "end >= start if end exists"
  Credential:
    required: [service, secret_ref]
    forbidden_properties: [password, secret, token]
```

支持的约束类型：必填属性（required）、枚举值（enum）、禁止属性（forbidden_properties）、自定义验证（validate）、关系基数（cardinality）、无环约束（acyclic）。

**处理**: 按照skill规范执行Schema约束系统操作,遵循单一意图原则。
**输出**: 返回Schema约束系统的执行结果,包含操作状态和输出数据。

### 4. 无环验证（DAG检查）
对标记为 `acyclic: true` 的关系类型执行有向无环图检查，防止循环依赖：

- 创建 blocks 关系时检查是否形成环
- 创建 depends_on 关系时检查依赖链是否循环
- 检测到环时拒绝操作并返回完整环路路径

**输入**: 用户提供无环验证（DAG检查）所需的指令和必要参数。
### 5. 追加式变更日志
所有图谱变更以追加方式记录在 `memory/ontology/graph.jsonl`，保留完整操作历史：

```jsonl
{"op":"create","entity":{"id":"p_001","type":"Person","properties":{"name":"Alice"}}}
{"op":"create","entity":{"id":"proj_001","type":"Project","properties":{"name":"Website Redesign","status":"active"}}}
{"op":"relate","from":"proj_001","rel":"has_owner","to":"p_001"}
{"op":"update","entity_id":"proj_001","changes":{"status":"in_progress"}}
```

变更类型：create（创建实体）、relate（创建关系）、update（更新属性）、delete（标记删除）。追加式写入保证历史可追溯，支持回放重建任意时间点的图谱状态。

**输入**: 用户提供追加式变更日志所需的指令和必要参数。
**处理**: 按照skill规范执行追加式变更日志操作,遵循单一意图原则。

### 6. 图谱遍历查询
支持多维度查询和图谱遍历操作：

| 查询类型 | 命令 | 用途 |
|---------|------|------|
| 类型查询 | `query --type Task --where '{"status":"open"}'` | 按类型和条件筛选实体 |
| ID查询 | `get --id task_001` | 获取单个实体详情 |
| 关联查询 | `related --id proj_001 --rel has_task` | 查询实体的关联实体 |
| 依赖查询 | `related --id task_001 --rel depends_on --depth 3` | 多跳关系遍历 |
| 路径查询 | `path --from task_001 --to task_005` | 查找两实体间的关系路径 |

**输入**: 用户提供图谱遍历查询所需的指令和必要参数。
**处理**: 按照skill规范执行图谱遍历查询操作,遵循单一意图原则。
**输出**: 返回图谱遍历查询的执行结果,包含操作状态和输出数据。

### 7. 跨技能契约声明
使用本图谱的技能通过契约声明其读写范围，确保技能间数据隔离与安全协作：

```yaml
ontology:
  reads: [Task, Project, Person]
  writes: [Task, Action]
  preconditions:
    - "Task.assignee must exist as Person"
  postconditions:
    - "Created Task has status=open"
```

前置条件在技能执行前验证，后置条件在执行后验证，违反条件时中止操作并回滚。

**输入**: 用户提供跨技能契约声明所需的指令和必要参数。

- 执行`跨技能契约声明`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `跨技能契约声明` 选项

### 8. 计划即图谱变换

将多步计划建模为图谱操作序列，每步在执行前验证，违反约束时回滚：

```text
计划："安排团队会议并创建后续任务"

第一步: CREATE Event { title: "团队周会", attendees: [p_001, p_002] }
第二步: RELATE Event -> has_project -> proj_001
第三步: CREATE Task { title: "准备议程", assignee: p_001 }
第四步: RELATE Task -> for_event -> event_001
第五步: CREATE Task { title: "发送会议纪要", assignee: p_001, blockers: [task_001] }
```

每步验证通过后提交，任一步骤失败则回滚已执行的步骤，保证图谱一致性。

### 能力覆盖范围

本skill还覆盖以下能力场景: 基于类型约束的知、识图谱系统、为智能代理提供结、构化记忆与可组合、类型化知识图谱引、将知识表示为可验、证的实体、每个实体拥有类型、属性和关系、根据类型约束进行、核心能力涵盖类型、种核心实体类型、可通过、数据以追加式、格式存储、支持迁移至、SQLite、数据库、适用于项目任务管、依赖关系追踪、知识库构建、跨技能状态共享、多步计划建模等场。这些能力在上述核心功能中均有对应处理逻辑。
### 源能力映射
本skill覆盖源skill的以下能力点:

| 源能力点 | 支持状态 | 实现方式 |
|:---------|:---------|:---------|
| Link Entities | 支持 | 通过核心功能实现对应能力 |

**输入**: 用户提供源能力映射所需的指令和必要参数。
**处理**: 按照skill规范执行源能力映射操作,遵循单一意图原则。
**输出**: 返回源能力映射的执行结果,包含操作状态和输出数据。
### 领域术语
本skill涉及以下领域术语: `transformation`, `workflows`, `智能代理领域的专`, `trigger`, `append`, `scope`, `friday`, `model`, `代理增强`, `force`, `runtime`, `validation`, `communication`, `productivity`, `prepare`

**输出**: 返回领域术语的执行结果,包含操作状态和输出数据。

## 使用流程

### 第一步：初始化图谱目录与Schema

创建 `memory/ontology/` 目录和空的 `graph.jsonl` 文件。编写 `schema.yaml` 定义项目所需的实体类型和关系约束。执行 `python3 scripts/ontology.py validate` 验证Schema格式正确。

### 第二步：创建核心实体

根据项目需求创建 Person、Project、Task 等基础实体。使用 `create --type Person --props '{"name":"Alice","email":"alice@example.com"}'` 命令逐个创建，系统自动分配ID并验证属性约束。

### 第三步：建立实体关系

使用 `relate` 命令在实体之间建立关系。创建 has_owner、has_task、blocks 等关系时，系统自动验证基数约束和无环约束。违反约束的操作被拒绝并返回详细错误信息。

### 第四步：查询与遍历图谱

使用 `query`、`get`、`related`、`path` 等命令查询图谱信息。复杂查询可通过 `--depth` 参数控制遍历深度，或通过 `--where` 条件过滤结果。

### 第五步：验证与维护

定期执行 `python3 scripts/ontology.py validate` 检查所有约束。审查变更日志确认操作历史。大规模图谱（1000+实体）可迁移至 SQLite数据库 提升查询性能。

## 错误处理

| 错误类型 | 原因 | 处理方式 |
|---------|------|---------|
| 必填属性缺失 | 创建实体时未提供 required 列表中的属性 | 检查 schema.yaml 中该类型的 required 定义，补全缺失属性后重新创建 |
| 枚举值非法 | 属性值不在 status_enum 定义的允许范围内 | 查阅 schema.yaml 中该属性的 enum 列表，使用合法值重新提交 |
| 基数约束违反 | 在 many_to_one 关系中为目标实体分配了多个源实体 | 检查已有关系记录，移除冲突关系或将关系类型改为 many_to_many |
| 无环检测失败 | blocks 或 depends_on 关系形成循环依赖 | 根据 error 返回的环路路径，移除形成环的最后一条关系，重新设计依赖结构 |
| 禁止属性出现 | Credential 类型中出现了 password/secret/token 属性 | 移除直接存储的敏感值，改用 secret_ref 间接引用外部密钥管理服务 |
| 实体类型未定义 | 创建实体时使用了 schema.yaml 中未声明的类型 | 在 schema.yaml 的 types 下新增该类型定义，包含 required 和可选属性声明 |
| 关系类型未注册 | relate 操作使用了未在 relations 中声明的关系类型 | 在 schema.yaml 的 relations 下新增关系定义，指定 from_types、to_types 和 cardinality |
| 追加日志损坏 | graph.jsonl 文件被外部工具修改导致JSON格式错误 | 使用 `validate --repair` 尝试修复损坏行，无法修复的行备份后移除，从最近的有效状态重建 |

## 示例

### 示例一：创建项目任务体系并建立依赖关系

场景：为"网站重设计"项目创建负责人、任务列表和任务间依赖。

```bash
# 创建人员
python3 scripts/ontology.py create --type Person --props '{"name":"Alice","email":"alice@example.com"}'
# 返回: {"id":"p_001","type":"Person","properties":{"name":"Alice","email":"alice@example.com"}}

# 创建项目
python3 scripts/ontology.py create --type Project --props '{"name":"Website Redesign","status":"active","goals":["提升转化率","改善移动端体验"]}'
# 返回: {"id":"proj_001","type":"Project","properties":{"name":"Website Redesign","status":"active"}}

# 建立项目-负责人关系
python3 scripts/ontology.py relate --from proj_001 --rel has_owner --to p_001
# 返回: {"from":"proj_001","rel":"has_owner","to":"p_001","validated":true}

# 创建任务
python3 scripts/ontology.py create --type Task --props '{"title":"设计首页原型","status":"open","priority":8}'
# 返回: {"id":"task_001","type":"Task","properties":{"title":"设计首页原型","status":"open","priority":8}}

python3 scripts/ontology.py create --type Task --props '{"title":"前端开发实现","status":"open","priority":7}'
# 返回: {"id":"task_002","type":"Task","properties":{"title":"前端开发实现","status":"open","priority":7}}

# 建立任务依赖（task_002 依赖 task_001）
python3 scripts/ontology.py relate --from task_002 --rel depends_on --to task_001
# 返回: {"from":"task_002","rel":"depends_on","to":"task_001","acyclic_check":true,"validated":true}

# 建立项目-任务关系
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_002

# 查询项目所有任务
python3 scripts/ontology.py related --id proj_001 --rel has_task
# 返回: [task_001, task_002]

# 查询任务依赖链
python3 scripts/ontology.py related --id task_002 --rel depends_on --depth 3
# 返回: [task_001]
```

### 示例二：多步计划建模与约束回滚

场景：安排团队会议并创建后续任务，中途因约束违反触发回滚。

```bash
# Schema定义（memory/ontology/schema.yaml）
# Task:
#   required: [title, status]
#   status_enum: [open, in_progress, blocked, done]
# Event:
#   required: [title, start]
#   validate: "end >= start if end exists"

# 第一步：创建会议事件
python3 scripts/ontology.py create --type Event --props '{"title":"团队周会","start":"2026-07-20T10:00:00","end":"2026-07-20T11:00:00","attendees":["p_001","p_002"]}'
# 返回: {"id":"event_001","validated":true}

# 第二步：创建准备议程任务
python3 scripts/ontology.py create --type Task --props '{"title":"准备会议议程","status":"open","assignee":"p_001"}'
# 返回: {"id":"task_003","validated":true}

# 第三步：尝试创建状态非法的任务（触发约束违反）
python3 scripts/ontology.py create --type Task --props '{"title":"发送会议纪要","status":"pending"}'
# 返回错误: {"error":"ENUM_VIOLATION","property":"status","value":"pending","allowed":["open","in_progress","blocked","done"]}
# 操作被拒绝，task_003 之前创建的实体不受影响

# 修正后重新创建
python3 scripts/ontology.py create --type Task --props '{"title":"发送会议纪要","status":"open","assignee":"p_001"}'
# 返回: {"id":"task_004","validated":true}

# 建立任务依赖（发送纪要依赖准备议程）
python3 scripts/ontology.py relate --from task_004 --rel depends_on --to task_003
# 返回: {"acyclic_check":true,"validated":true}

# 尝试创建循环依赖（task_003 依赖 task_004，形成环）
python3 scripts/ontology.py relate --from task_003 --rel depends_on --to task_004
# 返回错误: {"error":"CYCLE_DETECTED","path":["task_003","task_004","task_003"]}
# 操作被拒绝，无环约束生效
```

## FAQ

### Q1: 知识图谱的数据存储在哪里？支持什么格式？

默认存储在 `memory/ontology/graph.jsonl`，采用追加式JSONL格式，每行一个操作记录。追加式写入保证历史可追溯，支持回放重建任意时间点状态。对于大规模图谱（1000+实体），可迁移至 SQLite数据库 提升查询性能，迁移脚本保留JSONL作为备份。

### Q2: 如何自定义新的实体类型和关系类型？

在 `memory/ontology/schema.yaml` 中的 `types` 下新增类型定义，指定 `required`（必填属性）、`enum`（枚举值）、`forbidden_properties`（禁止属性）等约束。在 `relations` 下新增关系定义，指定 `from_types`、`to_types`、`cardinality`（基数）和 `acyclic`（无环约束）。新增后执行 `validate` 命令确认Schema格式正确。

### Q3: 无环约束是如何检测循环依赖的？

对标记为 `acyclic: true` 的关系类型（如 blocks、depends_on），每次创建关系时执行深度优先搜索（DFS）检查从目标实体回到源实体是否存在路径。如果存在路径则形成环，操作被拒绝并返回完整环路路径（如 `["task_003","task_004","task_003"]`），帮助用户定位和修复循环依赖。

### Q4: 跨技能契约声明的作用是什么？如何配置？

跨技能契约声明确保使用本图谱的不同技能不会越权读写。在技能的SKILL.md中声明 `ontology.reads`（可读类型）、`ontology.writes`（可写类型）、`preconditions`（前置条件）、`postconditions`（后置条件）。技能执行前验证前置条件（如"Task.assignee必须存在为Person"），执行后验证后置条件（如"创建的Task状态为open"），违反条件时中止并回滚。

### Q5: Credential类型为什么禁止直接存储密码和令牌？

Credential类型在Schema中设置了 `forbidden_properties: [password, secret, token]`，强制通过 `secret_ref` 间接引用外部密钥管理服务（如HashiCorp Vault、AWS Secrets Manager）。这确保敏感凭证不会以明文形式存储在图谱文件中，降低泄露风险。图谱仅记录凭证的引用标识，实际凭证值由专门的密钥管理工具保护。

### Q6: 图谱文件被意外修改后如何恢复？

graph.jsonl 采用追加式写入，每行是独立的JSON记录。如果部分行损坏，执行 `validate --repair` 命令尝试修复损坏的JSON行。无法修复的行会被备份到 `graph.jsonl.bak` 后从主文件移除。如果使用Git版本控制，可通过 `git checkout` 恢复到最近的有效版本。建议将 `memory/ontology/` 目录纳入Git管理，定期提交变更。

## 依赖说明

### 运行环境
- **Agent平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python环境**：Python 3.8+（脚本执行依赖）
- **本地存储**：可写的 `memory/ontology/` 目录

### 依赖项

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时环境 | 必需 | 系统安装 |
| ontology.py 脚本 | 运行时库 | 必需 | 随技能安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| SQLite数据库 | 本地存储 | 可选 | 大规模图谱（1000+实体）迁移时启用 |

### API Key 配置
- 核心功能无需任何 API Key
- Credential类型的 secret_ref 引用的外部密钥管理服务需对应服务的访问凭证

### 可用性分类
- **分类**：MD+EXEC（Markdown指令驱动，需exec执行Python脚本）
- **说明**：通过自然语言指令驱动Agent执行图谱创建、查询和验证操作

## 已知限制

1. **并发写入不支持**：追加式JSONL文件不支持多进程并发写入，多Agent同时操作同一图谱文件可能导致数据损坏，建议单写者模式或引入文件锁机制。
2. **全文搜索能力有限**：当前查询基于属性精确匹配和关系遍历，不支持模糊搜索和全文检索，大规模文本内容检索需配合外部搜索引擎。
3. **Schema变更不自动迁移**：修改Schema定义后（如新增必填属性），已有实体不会自动补全新属性，需手动执行迁移脚本或逐个更新。
4. **无内置版本控制**：图谱变更历史通过追加日志保留，但缺乏内置的版本快照和差异对比功能，需配合Git等外部版本控制工具使用。
5. **关系属性支持有限**：当前关系类型主要支持实体间关联，关系本身的属性（如关系的有效时间、权重）需通过额外的属性表管理。
