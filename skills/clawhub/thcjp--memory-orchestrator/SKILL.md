---
slug: "memory-orchestrator"
name: "memory-orchestrator"
version: "1.0.0"
displayName: "记忆编排器"
summary: "四层记忆架构管理系统，多模式检索与健康度仪表盘，支持并发写入冲突解决"
license: "Proprietary"
description: |-
  记忆编排器是面向 AI Agent 的智能记忆管理系统，针对分层体系不清、自动摘要质量不稳、
  并发写入冲突、缺乏健康度指标四大痛点而设计。核心能力包括：四层记忆架构（工作/短期/长期/重要，
  每层独立容量与清理策略）、三模式检索（关键词/语义/混合，混合模式算法加权打分）、
  自动摘要生成与质量评估器（信息保留率/压缩比/可读性/准确性四维指标）、
  记忆健康度仪表盘（容量/分布/命中率/陈旧度四维量化与主动告警）、
  并发写入冲突解决（乐观锁+版本合并+字段级合并策略）、过期记忆自动清理、模块化扩展接口。
  提供从存储到检索到摘要的全生命周期编排，让 Agent 记忆真正可控可观测。
  适用于长会话 Agent、聊天机器人上下文管理、多 Agent 共享记忆、客服助理上下文治理等场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tags:
  - 智能助手
---
# 记忆编排器

面向 AI Agent 的智能记忆管理系统，四层架构与多模式检索，全生命周期编排。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 记忆编排器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 记忆编排器四层记忆架构管理 | 不支持 | 支持 |
| 记忆编排器多模式检索 | 不支持 | 支持 |
| 多租户管理与权限分配 | 不支持 | 支持 |
| 操作审计与合规日志 | 不支持 | 支持 |
| 自定义仪表盘与报表 | 不支持 | 支持 |

## 核心能力

### 1. 四层记忆架构

工作/短期/长期/重要四层清晰分工，每层独立容量与清理策略。

- **参数**：`type`（working/short-term/long-term/important）、`content`、`persist`
- **用法**：添加记忆时指定类型，层级流转自动处理
- **输出**：写入确认与记忆 ID

四层架构：

| 层级 | 名称 | 容量 | 清理策略 | 适用内容 |
|---:|---:|---:|---:|---:|
| 第一层 | 工作记忆 | 上限 20 条 | 超限自动晋升短期 | 当前任务上下文 |
| 第二层 | 短期记忆 | 上限 100 条 | FIFO 淘汰，7 天未访问归档 | 当前会话上下文、近期决策 |
| 第三层 | 长期记忆 | 无上限（建议 < 10000） | 180 天未引用提示归档 | 历史交互、项目背景、领域知识 |
| 第四层 | 重要记忆 | 无上限 | 永不清理 | 用户核心偏好、关键决策、身份信息 |

层级流转规则：

```text
写入 → 工作记忆（容量 20）
         ├─ 超限 → 自动晋升到短期记忆
         └─ 标记重要 → 直接晋升到重要记忆
# ..
短期记忆（容量 100）
         ├─ 超限 → FIFO 淘汰最旧（移到长期或删除）
         ├─ 标记重要 → 晋升到重要记忆
         └─ 7 天未访问 → 自动归档到长期记忆
# ..
长期记忆
         ├─ 被引用 → 临时提升到短期（LRU）
         └─ 180 天未引用 → 提示归档/遗忘
# ..
重要记忆
         └─ 永不清理，仅可手动修改
```

### 2. 三模式检索

关键词/语义/混合三种检索模式，混合模式算法加权打分。

- **参数**：`query`（搜索关键词）、`searchMode`（keyword/semantic/hybrid）、`limit`
- **用法**：指定检索模式与查询条件
- **输出**：匹配的记忆条目列表，按相关性排序

| 模式 | 适用场景 | 优势 | 依赖 |
|:---:|:---:|:---:|:---:|
| keyword | 精确匹配、快速检索 | 零依赖、快 | 无 |
| semantic | 语义相似、模糊查询 | 召回率高 | 需向量数据库（可选） |
| hybrid | 综合检索、最佳效果 | 兼顾精确与召回 | 默认可用（语义部分降级为关键词） |

混合检索算法：

```text
score = keyword_score * 0.4 + semantic_score * 0.4 + recency_score * 0.1 + importance_score * 0.1
# ..
说明：
- keyword_score：关键词匹配（TF-IDF）
- semantic_score：语义相似度（有向量库时用 cosine，无则降级为关键词）
- recency_score：近期加权
- importance_score：重要度加权
```

### 3. 自动摘要生成与质量评估

自动生成结构化摘要，四维质量指标评估摘要效果。

- **参数**：`typeFilter`（过滤记忆类型）、`maxTokens`（摘要最大 token，默认 500）
- **用法**：`action: "summarize"` 触发摘要生成
- **输出**：结构化摘要 + 质量评估报告

摘要策略：

```text
1. 提取关键信息
   - 事件：时间、地点、参与者、结果
   - 决策：决策内容、原因、影响
   - 教训：问题、原因、规避方法
   - 待办：任务、优先级、截止时间
# ..
2. 压缩冗余
   - 去重复（相同信息只保留一次）
   - 去过程（保留结果，省略中间步骤）
   - 去客套（移除寒暄与无信息内容）
# ..
3. 结构化输出
   - 按类别分组
   - 层级列表呈现
   - 保留关键时间戳
```

质量评估指标：

| 指标 | 计算方法 | 及格线 |
|:------|------:|:------|
| 信息保留率 | 摘要含关键信息数 / 原始关键信息数 | 大于等于 90% |
| 压缩比 | 原始 token / 摘要 token | 大于等于 3 倍 |
| 可读性 | 结构化程度（标题/列表/层级） | 大于等于 0.8 |
| 准确性 | 摘要与原始内容一致性 | 大于等于 95% |

### 4. 记忆健康度仪表盘

四维量化记忆状态，主动告警异常情况。

- **参数**：`action: "health"`
- **用法**：调用健康度检查获取仪表盘数据
- **输出**：容量、分布、命中率、陈旧度四维指标与告警列表

四维健康度指标：

```json
{
  "capacity": {
    "working": { "used": 18, "limit": 20, "utilization": 0.9 },
    "short_term": { "used": 87, "limit": 100, "utilization": 0.87 },
    "long_term": { "used": 342, "limit": null, "utilization": null },
    "important": { "used": 15, "limit": null, "utilization": null }
  },
  "distribution": {
    "by_type": { "preference": 45, "decision": 30, "fact": 20, "lesson": 15 },
    "by_age": { "last_7d": 60, "last_30d": 120, "older": 200 }
  },
  "hit_rate": {
    "last_7d": 0.72,
    "last_30d": 0.65,
    "trend": "improving"
  },
  "staleness": {
    "stale_count": 23,
    "stale_ratio": 0.06,
    "oldest_unaccessed_days": 45
  },
  "alerts": [
    { "level": "warning", "message": "工作记忆使用率 90%，建议晋升到短期" },
    { "level": "info", "message": "23 条长期记忆 30 天未访问，建议归档" }
  ]
}
```

告警规则：

| 指标 | 阈值 | 告警级别 |
|---:|:---|---:|
| 工作记忆使用率 | 大于 85% | warning |
| 短期记忆使用率 | 大于 85% | warning |
| 命中率（7天） | 小于 30% | warning |
| 陈旧率 | 大于 10% | info |
| 重要记忆被修改 | 任意 | info（记录审计） |

### 5. 并发写入冲突解决

乐观锁机制 + 版本合并策略，支持多 Agent 安全并发写入。

- **参数**：写入时携带 `version` 版本号
- **用法**：读取记忆获取版本号，写入时携带版本号，不匹配则触发合并
- **输出**：写入成功或冲突解决结果

乐观锁机制：

```text
1. 读取记忆时获取版本号 version
2. 写入时携带 version
3. 若 version 与当前不匹配 → 冲突
4. 冲突时触发版本合并
```

版本合并策略：

| 冲突类型 | 合并策略 |
|:------:|--------|
| 同条目不同字段修改 | 字段级合并，各取所改 |
| 同条目同字段不同值 | 保留两版本，标记冲突，等待用户裁决 |
| 同时新增不同条目 | 无冲突，直接合并 |

### 6. 过期记忆自动清理

按层级与规则自动清理过期记忆，记录清理日志。

- **参数**：无，自动执行
- **用法**：定期触发清理或由健康度告警触发
- **输出**：清理日志记录到 `memory-cleanup.log`

| 记忆类型 | 清理规则 | 清理动作 |
|----|:--:|---:|
| 工作记忆 | 超 20 条 | 最旧的晋升到短期 |
| 短期记忆 | 超 100 条 | FIFO 淘汰，移到长期或删除 |
| 短期记忆 | 7 天未访问 | 自动归档到长期 |
| 长期记忆 | 180 天未引用 | 提示归档/遗忘 |
| 长期记忆 | 含 expires_at 且过期 | 自动归档 |
| 重要记忆 | 永不清理 | 仅可手动修改 |

### 7. 模块化扩展接口

语义检索可插拔对接向量数据库，无向量库时自动降级。

- **参数**：`action: "configure"`、`semantic.provider`（chroma/lancedb/qdrant/none）
- **用法**：配置向量数据库提供商与路径
- **输出**：配置确认

```typescript
await skills.memoryOrchestrator({
  action: "configure",
  semantic: {
    provider: "chroma",
    path: "./.chroma",
    embeddingModel: "all-MiniLM-L6-v2"
  }
});
```

无向量数据库时，semantic 模式降级为关键词检索，不影响基本功能。

#
## 使用流程

### 第一步：添加记忆

根据内容重要程度选择记忆类型，写入记忆条目。

```typescript
// 添加长期记忆
await skills.memoryOrchestrator({
  action: "add",
  content: "用户喜欢喝咖啡，不加糖，每周三下午喝奶茶",
  type: "long-term",
  persist: true
});
// ..
// 添加重要记忆（永不清理）
await skills.memoryOrchestrator({
  action: "add",
  content: "用户是项目负责人，最终决策权在用户",
  type: "important",
  persist: true
});
```

### 第二步：检索记忆

根据查询需求选择检索模式，复杂查询用混合模式。

```typescript
const result = await skills.memoryOrchestrator({
  action: "search",
  query: "用户喜好",
  limit: 3,
  searchMode: "hybrid"
});
```

### 第三步：生成摘要

对短期记忆生成压缩摘要，控制上下文体积。

```typescript
const summary = await skills.memoryOrchestrator({
  action: "summarize",
  typeFilter: "short-term",
  maxTokens: 500
});
```

### 第四步：检查健康度

定期调用健康度仪表盘，检查告警项并处理。

```typescript
const health = await skills.memoryOrchestrator({
  action: "health"
});
// 检查 alerts 列表，处理 warning 级别告警
```

### 第五步：持久化与加载

保存记忆到磁盘，重启后从磁盘加载。

```typescript
// 保存
await skills.memoryOrchestrator({
  action: "save",
  persistPath: "./my-memory.json"
});
// ..
// 加载
await skills.memoryOrchestrator({
  action: "load",
  persistPath: "./my-memory.json"
});
```

## 错误处理

| 错误类型 | 原因 | 处理方式 |
|----|----|----|
| 搜索结果不准 | 检索模式与查询需求不匹配 | 切换 searchMode，精确查询用 keyword，模糊查询用 semantic，复杂查询用 hybrid |
| 摘要丢关键信息 | 质量评估信息保留率未达标 | 检查保留率指标，补充遗漏关键信息后重新生成摘要 |
| 并发写入失败 | 多 Agent 同时写入同一记忆条目，版本号冲突 | 触发版本合并策略：不同字段各取所改，同字段冲突保留两版本等待用户裁决 |
| 工作记忆爆满 | 未及时晋升到短期记忆，超 20 条上限 | 检查健康度仪表盘，触发自动晋升，最旧的条目移到短期记忆 |
| 持久化失败 | persistPath 路径无写入权限或磁盘空间不足 | 检查 persistPath 写入权限，确认磁盘空间充足后 |
| 语义检索不工作 | 未配置向量数据库提供商 | 配置 semantic provider（chroma/lancedb/qdrant），或使用 keyword 模式作为替代 |
| 短期记忆命中率低 | 记忆陈旧未及时清理或检索策略不当 | 检查健康度命中率指标，清理过期记忆，切换为 hybrid 模式提升召回率 |
| 重要记忆误修改 | 操作失误修改了重要记忆条目 | 查看审计日志追溯修改记录，手动恢复正确内容，重要记忆仅可手动修改 |

## 示例

### 示例一：长会话上下文管理

用户会话已聊 30 轮，上下文即将超限，需要压缩短期记忆保留关键信息。

```text
用户："这个会话已经聊了 30 轮，上下文快爆了"
# ..
执行：
1. 生成短期记忆摘要：
   const summary = await skills.memoryOrchestrator({
     action: "summarize",
     typeFilter: "short-term",
     maxTokens: 500
   });
# ..
2. 压缩后的摘要替换原始短期记忆
3. 工作记忆仅保留最近 5 轮：
   const recent = await skills.memoryOrchestrator({
     action: "search",
     query: "最近讨论",
     typeFilter: "working",
     limit: 5,
     searchMode: "keyword"
   });
# ..
4. 继续会话
5. 验证效果：
   const health = await skills.memoryOrchestrator({ action: "health" });
   // 检查 short_term 容量是否下降
# ..
结果：
  原始上下文：约 15,000 token（30 轮）
  压缩后上下文：约 4,500 token（5 轮原文 + 25 轮摘要）
  token 占用减少：70%
  摘要质量：信息保留率 92%，压缩比 3.3 倍，可读性 0.88
```

### 示例二：多 Agent 共享记忆

Agent A 与 Agent B 同时操作共享记忆库，需要解决并发冲突。

```text
场景：Agent A 与 Agent B 同时更新用户偏好
# ..
执行：
1. Agent A 读取用户偏好（version=3）：
   const pref = await skills.memoryOrchestrator({
     action: "search",
     query: "用户偏好 主题色",
     searchMode: "keyword"
   });
   // 返回 version=3
# ..
2. Agent B 同时读取用户偏好（version=3）
# ..
3. Agent A 写入更新（version=3 → 4）：
   await skills.memoryOrchestrator({
     action: "add",
     content: "用户偏好深色模式",
     type: "long-term",
     version: 3
   });
   // 写入成功，version 升级为 4
# ..
4. Agent B 写入更新（version=3，冲突！）：
   await skills.memoryOrchestrator({
     action: "add",
     content: "用户偏好自动切换",
     type: "long-term",
     version: 3
   });
   // 版本不匹配，触发冲突解决
# ..
5. 冲突解决：
   - 同条目同字段不同值 → 保留两版本
   - 标记为冲突
   - 提示用户："检测到偏好冲突，请选择"
     [深色模式] [自动切换] [两者都记]
# ..
6. 用户选择后，合并完成，version 升级为 5
```

### 示例三：记忆健康度巡检

心跳任务每天检查记忆健康度，处理告警项。

```text
心跳任务：每天检查记忆健康度
# ..
执行：
1. 调用健康度仪表盘：
   const health = await skills.memoryOrchestrator({ action: "health" });
# ..
2. 检查告警项：
   - 工作记忆使用率 90%（> 85%，warning）
     → 触发晋升：最旧 5 条工作记忆移到短期
   - 短期记忆使用率 87%（> 85%，warning）
     → 触发归档：最旧 10 条短期记忆移到长期
   - 陈旧率 12%（> 10%，info）
     → 提示清理：23 条长期记忆 30 天未访问，建议归档
   - 命中率 28%（< 30%，warning）
     → 提示优化：建议切换为 hybrid 检索模式
# ..
3. 生成健康度报告：
   容量状态：工作 15/20、短期 77/100、长期 352、重要 15
   分布情况：偏好 45、决策 30、事实 20、教训 15
   命中率趋势：improving（7天 72%、30天 65%）
   陈旧情况：23 条未访问，最久 45 天
# ..
4. 处理后重新检查：
   const healthAfter = await skills.memoryOrchestrator({ action: "health" });
   // 工作记忆降至 15/20（75%），告警消除
   // 短期记忆降至 77/100（77%），告警消除
```

## FAQ

### Q1：四层架构会不会太复杂？

不会。日常使用只需指定 type（默认 short-term），层级流转自动处理。四层架构的价值在于：重要信息不被淹没（独立第四层）、短期记忆不爆（100 条上限 + FIFO 淘汰）、长期记忆可归档（180 天未引用提示）。用户无需关心层级流转细节，系统自动管理。

### Q2：没有向量数据库能用语义检索吗？

可以，但会降级。semantic 模式在无向量库时退化为关键词检索，仍可用但召回率降低。接入向量库后效果最佳。配置方式：通过 `action: "configure"` 设置 `semantic.provider`（支持 chroma/lancedb/qdrant）。无向量库时 hybrid 模式也能用，语义部分自动降级为关键词。

### Q3：并发冲突频繁怎么办？

四个策略：(1) 减少同一记忆条目的并发写入，不同 Agent 写不同条目；(2) 必要时用锁机制串行化写入；(3) 冲突后及时人工裁决，避免积压；(4) 字段级合并在大多数情况下能自动解决冲突（不同字段各取所改），只有同字段不同值才需要人工裁决。

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **运行时**：Node.js（如使用 TypeScript SDK）

### 依赖项

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| 向量数据库 | 外部依赖 | 可选 | Chroma / LanceDB / Qdrant，用于语义检索增强 |
| Embedding 模型 | 模型 | 可选 | all-MiniLM-L6-v2 等，配合向量数据库使用 |
| Node.js | 运行时 | 可选 | TypeScript SDK 场景需要 |

### API Key 配置

本技能核心功能无需额外 API Key（LLM 由 Agent 平台提供）。语义检索增强（可选）如使用云向量服务，需对应服务的 API Key。本地向量数据库（Chroma / LanceDB）无需 API Key。

### 可用性分类

- **分类**：MD+EXEC（Markdown 指令驱动，部分功能需 exec 执行持久化操作）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 管理四层记忆系统

## 已知限制

- 语义检索需配置向量数据库才能达到最佳效果，无向量库时降级为关键词检索，召回率降低
- 并发写入冲突解决中，同字段不同值的冲突需人工裁决，无法全自动合并
- 摘要质量评估器的准确性指标基于内容一致性比对，无法覆盖语义层面的偏差
- 健康度仪表盘的命中率指标依赖检索日志，首次使用时无历史数据无法计算
- 持久化文件（JSON 格式）随记忆增长会变大，超大规模记忆库（10000+ 条）可能影响加载速度
- 四层架构的容量上限（工作 20 条、短期 100 条）为固定值，暂不支持自定义调整