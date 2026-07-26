---
slug: "knowledge-ontology"
name: "knowledge-ontology"
version: 2.0.1
displayName: "知识本体"
summary: "类型化知识图谱：约束校验+模式演进+图遍历规划，让Agent记忆结构化可验证。"
license: "Proprietary"
description: |-
  面向AI Agent的类型化知识图谱系统，提供实体关系建模、约束校验引擎、模式演进管理、图遍历规划四大核心能力.
  内置15+实体类型与7类约束规则，支持append-only历史保留与三步迁移法，确保模式变更不破坏旧数据.
  将多步计划建模为图操作序列，每步执行前自动校验约束，违反约束自动回滚.
  适用于需要结构化查询的Agent记忆、多实体关系管理、依赖追踪与影响分析、多步计划建模场景.
  避免扁平文件记忆难查询、约束缺失数据脏、模式演进破坏旧数据等问题.
  支持Skill契约声明，明确跨Skill通信边界与读写权限.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 智能助手
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 知识本体

一切皆实体，一切变更皆受约束。将Agent记忆从扁平文件升级为类型化可验证的知识图谱，支持图遍历查询、模式演进、多步规划建模，让知识结构化、可查询、可信任.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 知识本体处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 知识本体约束校验 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

- **类型化实体与关系系统**：内置 Person/Organization/Project/Task/Goal/Event/Location/Document/Message/Thread/Note/Account/Device/Credential/Action/Policy 共15+实体类型。每个实体遵循标准结构 `{"id":"ent_001","type":"Project","properties":{...},"relations":[...],"created":"2026-01-15T10:00:00Z","updated":"2026-01-15T10:00:00Z"}`。支持 has_owner/has_task/depends_on/blocks/relates_to 等关系类型，关系建立前自动校验类型兼容性.
- **约束校验引擎**：支持7类约束规则——required（必填属性，如 Task 必须有 title 和 status）、enum（枚举值，如 status 只能是 open/in_progress/done/blocked）、forbidden_properties（禁止属性，如 Credential 禁止 password 和 api_key）、cardinality（关系基数，如 Project 最多1个 has_owner）、acyclic（无环校验，如 blocks 关系不能成环）、validate（自定义表达式，如 priority 必须1-5之间）、defaults（默认值，如 status 默认 open）。执行 `python3 （请参考skill目录中的脚本文件） validate` 输出校验报告.
- **模式演进管理**：采用 append-only 历史保留策略，schema 变更通过三步法执行：第一步追加新 schema 节点（不删除旧 schema）→ 第二步编写迁移脚本补充默认值 → 第三步执行迁移并运行校验。确保任何模式变更不破坏已有数据，可通过历史记录回滚到任意时间点.
- **图遍历规划**：将多步计划建模为图操作序列（CREATE/RELATE/UPDATE/DELETE），每步执行前校验约束，违反约束自动回滚到上一步。支持依赖分析（正向遍历 depends_on 关系链）、影响分析（反向遍历找出所有受影响的实体）、循环依赖检测（`cycle-check --rel blocks` 定位环路）.
- **Skill契约声明**：使用本体的Skill声明 reads/writes 边界与前后置条件。例如Skill A声明 `reads: [Project, Task]` `writes: [Task]`，任一步骤违反契约自动回滚，明确跨Skill通信边界，避免并发写入冲突.
### 类型化实体与关系系统

针对类型化实体与关系系统,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供类型化实体与关系系统相关的配置参数、输入数据和处理选项.
**输出**: 返回类型化实体与关系系统的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`类型化实体与关系系统`的配置文档进行参数调优
### 约束校验引擎

针对约束校验引擎,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供约束校验引擎相关的配置参数、输入数据和处理选项.
**输出**: 返回约束校验引擎的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`约束校验引擎`的配置文档进行参数调优
### 模式演进管理

针对模式演进,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供模式演进管理相关的配置参数、输入数据和处理选项.
**输出**: 返回模式演进管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`模式演进管理`的配置文档进行参数调优
#
## 使用流程

### 第一步：初始化目录与schema

创建图谱存储目录并写入初始schema定义。执行以下命令完成初始化：

```bash
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl
python3 （请参考skill目录中的脚本文件） schema-append --data '{
  "types": {
    "Task": { "required": ["title", "status"], "defaults": {"status": "open"}, "enum": {"status": ["open","in_progress","done","blocked"]} },
    "Project": { "required": ["name"] },
    "Person": { "required": ["name"] }
  },
  "relations": {
    "has_owner": { "from_types": ["Project"], "to_types": ["Person"], "cardinality": "1:1" },
    "has_task": { "from_types": ["Project"], "to_types": ["Task"], "cardinality": "1:N" },
    "depends_on": { "from_types": ["Task"], "to_types": ["Task"], "cardinality": "N:N", "acyclic": true },
    "blocks": { "from_types": ["Task"], "to_types": ["Task"], "cardinality": "N:N", "acyclic": true }
  }
}'
```

### 第二步：创建实体与关系

使用 create 命令追加实体到图谱文件末尾，绝不覆盖已有内容。然后使用 relate 命令建立关系，关系建立前自动校验类型与基数约束.
```bash
python3 （请参考skill目录中的脚本文件） create --type Person --props '{"name":"Alice","role":"architect"}'
python3 （请参考skill目录中的脚本文件） create --type Project --props '{"name":"支付模块重构","status":"active","priority":2}'
python3 （请参考skill目录中的脚本文件） relate --from proj_001 --rel has_owner --to p_001
python3 （请参考skill目录中的脚本文件） relate --from proj_001 --rel has_task --to task_001
```

### 第三步：查询与图遍历

按类型与条件查询实体，执行关联查询与图遍历分析.
```bash
python3 （请参考skill目录中的脚本文件） query --type Task --where '{"status":"open"}'
python3 （请参考skill目录中的脚本文件） related --id proj_001 --rel has_task
python3 （请参考skill目录中的脚本文件） traverse --id task_001 --rel depends_on --direction outgoing
python3 （请参考skill目录中的脚本文件） traverse --id task_001 --rel depends_on --direction incoming
python3 （请参考skill目录中的脚本文件） cycle-check --rel blocks
```

### 第四步：模式演进（不破坏旧数据）

当需要新增字段或修改约束时，按三步法执行模式演进.
```bash
python3 （请参考skill目录中的脚本文件） schema-append --data '{"types":{"Task":{"required":["title","status","priority"]}}}'
python3 （请参考skill目录中的脚本文件） migrate --script 001_add_priority_to_tasks.py
python3 （请参考skill目录中的脚本文件） validate
```

### 第五步：多步规划建模

将复杂工作流建模为图变换序列，每步自动校验约束，失败自动回滚.
```bash
python3 （请参考skill目录中的脚本文件） plan --file plan.yaml --validate-each --rollback-on-fail
```

#
## 错误处理

| 错误类型 | 原因 | 处理方式 |
|---:|---:|---:|
| 校验失败：缺必填属性 | 实体未提供 required 字段，如 Task 缺少 status | 按提示补全属性后重新提交；或使用 defaults 配置自动填充默认值 |
| 校验失败：含禁止属性 | Credential 实体写入了 password 或 api_key 等敏感字段 | 拒绝存储；改为 secret_ref 字段间接引用外部密钥库，如 `"secret_ref":"vault://secrets/stripe_key"` |
| 关系创建失败：类型不匹配 | relate 命令的 from/to 类型与 schema 中 from_types/to_types 声明不符 | 检查 schema 中该关系的类型约束声明，确认实体类型后再建立关系 |
| 循环依赖报错 | blocks 或 depends_on 关系形成环，违反 acyclic 约束 | 执行 `cycle-check --rel blocks` 定位环路，打破环中一条边后重新校验 |
| 查询无结果 | 实体不存在、类型名拼写错误或 where 条件过严 | 执行 `list --type Project` 确认实体存在；检查 where 条件中的属性名与值 |
| 文件过大性能下降 | JSONL 全量扫描，实体数超过10000条 | 执行 `migrate --from jsonl --to sqlite` 迁移到SQLite数据库；或定期 compact 合并旧操作记录 |
| 迁移失败：脚本错误 | 迁移脚本语法错误或数据类型冲突 | 逐步调试迁移脚本；校验迁移前后数据完整性；append-only 历史保留可回滚到迁移前状态 |
| 多Skill写入冲突 | 多个Skill并发写入同一JSONL文件 | 声明Skill契约界定读写边界；使用文件锁或队列串行化；复杂场景迁移到SQLite数据库利用事务机制 |
| 模式演进破坏旧数据 | 直接修改schema未走三步法，旧实体不符合新约束 | 必须按"追加新schema → 编写迁移脚本 → 执行+校验"流程操作，append-only保留完整历史 |

## 示例

### 示例1：项目依赖管理与拓扑排序

**输入：** 用户问"重构支付模块需要先完成哪些任务？"

**执行：**
1. 查询支付模块相关 Project：`query --type Project --where '{"name":"支付模块重构"}'`
2. 遍历 has_task 关系找到所有 Task：`related --id proj_001 --rel has_task`
3. 遍历 blocks 关系找到阻塞链：`traverse --id task_001 --rel blocks --direction outgoing`
4. 拓扑排序输出执行顺序

**输出：**
```
执行顺序（拓扑排序）：
1. 设计支付接口（task_001）— 无阻塞，可立即开始
2. 实现支付网关（task_002）— blocked by task_001
3. 集成测试（task_003）— blocked by task_002
4. 上线部署（task_004）— blocked by task_003
# ...
关键路径：task_001 → task_002 → task_003 → task_004
预计总工期：12个工作日
```

### 示例2：影响分析（反向遍历）

**输入：** 用户问"如果推迟数据库迁移任务，影响哪些任务？"

**执行：**
1. 找到数据库迁移 Task：`query --type Task --where '{"title":"数据库迁移"}'` 返回 task_015
2. 反向遍历 depends_on 关系：`traverse --id task_015 --rel depends_on --direction incoming`
3. 找出所有依赖该任务的下游 Task

**输出：**
```
影响范围（3个任务受影响）：
- task_022: API部署（directly depends on task_015）
- task_031: 性能测试（depends on task_022）
- task_045: 生产上线（depends on task_031）
# ...
建议：级联调整 task_022、task_031、task_045 的截止日期，延期天数 = 迁移推迟天数
```

### 示例3：凭证安全存储

**输入：** 用户说"记住我的 Stripe API Key"

**执行：**
1. 检查 Credential 类型约束 → forbidden_properties: [api_key, secret, password]
2. 拒绝直接存储敏感字段
3. 创建间接引用实体

**输出：**
```json
{
  "id": "cred_001",
  "type": "Credential",
  "properties": {
    "service": "stripe",
    "secret_ref": "vault://secrets/stripe_key",
    "created_by": "Alice",
    "expires_at": "2026-12-31"
  },
  "created": "2026-07-21T08:00:00Z"
}
```
输出说明：已记录 Stripe 凭证引用（密钥本身存储在密钥库，未写入图谱）.
## FAQ

**Q1：JSONL存储和SQLite数据库怎么选？**
A：实体数小于1000条时用JSONL（简单无依赖，纯文本可读）；实体数超过10000条或需要频繁复杂查询时迁移到SQLite数据库（性能更优，支持事务）。中间区间看查询模式，简单类型查询JSONL够用，多跳遍历查询建议SQLite数据库.
**Q2：append-only策略会不会让文件越来越大？**
A：会持续增长，但历史完整可追溯。可通过 `compact` 命令合并旧操作记录（仅保留最终状态），但会丢失变更历史。建议保留append-only模式，对高频查询字段建立索引加速.
**Q3：约束校验会不会拖慢写入性能？**
A：单次校验是毫秒级操作。批量写入时先校验全部再统一提交。校验失败的代价远低于脏数据清理成本，建议始终保持校验开启.
**Q4：模式演进如何保证不破坏旧数据？**
A：三步法——第一步追加新schema节点（不删除旧schema）→ 第二步编写迁移脚本为旧实体补充默认值 → 第三步执行迁移并运行validate校验。详见使用流程第四步.
**Q5：多个Skill同时写入图谱会冲突吗？**
A：会。建议每个Skill声明契约（reads/writes边界），通过文件锁或队列串行化写入。复杂场景迁移到SQLite数据库利用事务机制保证原子性.
**Q6：Credential类型为什么不直接存储密码？**
A：知识图谱文件以明文JSONL存储，直接写入敏感信息存在泄露风险。通过 forbidden_properties 约束强制使用 secret_ref 间接引用外部密钥库，密钥本身不进入图谱文件.
## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Python 3.8+ | 运行时 | 必需 | 系统安装Python 3.8或更高版本 |
| PyYAML | Python包 | 必需 | 执行 `pip install pyyaml` 解析schema定义文件 |
| SQLite数据库 | 数据库 | 可选 | Python内置sqlite3模块，实体数超过10000条时启用 |
| Agent平台 | 运行环境 | 必需 | 支持SKILL.md的任意AI Agent平台 |

**API Key配置：** 本Skill无需任何API Key，纯本地文件操作，无网络请求。凭证等敏感信息强制间接引用，不存储在图谱中.
**可用性分类：** MD+EXEC（Markdown指令 + exec命令行执行）。核心实体与关系概念纯Markdown可理解；创建、查询、校验等操作需Python脚本执行.
## 已知限制

1. **默认JSONL存储不适合超大规模**：实体数超过10000条需手动迁移到SQLite数据库，迁移过程需停服或锁写，期间无法正常查询.
2. **append-only文件持续增长**：不主动compact会越来越大，compact会丢失变更历史，需用户在历史完整性与文件大小间权衡.
3. **并发写入支持弱**：JSONL存储无事务机制，多Skill并发写入需外部文件锁或队列串行化，复杂场景需迁移到SQLite数据库.
4. **不存储敏感信息原文**：Credential类型强制间接引用（secret_ref），用户需自行管理外部密钥库的生命周期与权限.
5. **校验引擎覆盖有限**：支持7类约束规则，但不支持跨实体的多字段联合业务逻辑校验（如"Task的owner必须是Project的member"），需在迁移脚本中自行实现.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "知识本体处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "knowledge-ontology"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
