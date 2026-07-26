---
name: knowledge-router
version: 1.0.0
description: "知识查询统一入口。根据问题类型自动选择最优查询路径，覆盖 wiki-kb（编译知识库）、memory-tencentdb（对话记忆）、Ontology（知识图谱）、memorySearch（向量搜索）、domain-kit（领域知识本体）。触发词：'查询知识'、'知识搜索'、'帮我找'、'XX是什么'、'XX怎么回事'、'上次说了什么'、'XX和XX什么关系'。"
---

# Knowledge Router — 知识查询统一入口

作为所有知识查询的入口，根据问题类型自动选择最优查询路径，避免漏查或重复查询。

## 知识源清单

| 知识源 | 工具/路径 | 知识粒度 | 特点 | 优先级 |
|--------|-----------|----------|------|--------|
| **wiki-kb** | `wiki-kb/wiki/index.md` → 主题文章 | 编译后的主题知识 | 高可靠、人工审核、主动编译 | 最高 |
| **memory-tencentdb** | `tdai_memory_search` / `tdai_conversation_search` | 对话片段 | 自动捕获、实时、细粒度 | 高 |
| **Ontology** | `memory/ontology/graph.jsonl` | 实体+关系 | 结构化、可推理 | 中 |
| **domain-kit** | `skills/domain-kit-owl/` | 领域本体 | 结构化知识（设备/协议/约束） | 中 |
| **memorySearch** | 内置向量搜索 | 文本块 | 语义匹配、**仅当 tdai 无结果时启用** | 低（fallback） |

> **注意**：`memorySearch` 是 `tdai_memory_search` 的 fallback，两者不并列使用。只有当 tdai 搜索无结果或结果不佳时，才降级到 memorySearch。

## 问题分类规则

根据用户问题，判断属于以下哪一类：

### 类型 A：领域知识查询

**特征**：询问技术概念、方案、方法论、行业知识
- "XX 技术怎么回事"
- "XX 方案怎么做"
- "XX 的原理是什么"
- "有没有 XX 的最佳实践"

**查询路径**：
1. `wiki-kb/wiki/index.md` → 定位相关主题文章 → 读取文章
2. `domain-kit` → 查询领域本体（设备/协议/约束）
3. `Ontology` → 查询实体关系
4. `tdai_memory_search` → 搜索结构化记忆
5. （fallback）`memorySearch` → 仅当 tdai 无结果时启用

**停止条件**：在任一步骤获得充分答案后，可跳过后续步骤。

### 类型 B：对话回忆查询

**特征**：询问之前聊过什么、做过什么决定
- "上次我们聊了什么"
- "我之前提过 XX 吗"
- "XX 是什么时候决定的"
- "帮我回忆一下 XX"

**查询路径**：
1. `tdai_conversation_search` → 搜索原始对话
2. `tdai_memory_search` → 搜索结构化记忆
3. （fallback）`memorySearch` → 仅当 tdai 无结果时启用

**停止条件**：在任一步骤获得充分答案后停止。

### 类型 C：关系查询

**特征**：询问实体之间的关系、谁负责什么
- "XX 和 XX 什么关系"
- "谁负责 XX 项目"
- "XX 项目涉及哪些人"
- "XX 的上游是什么"

**查询路径**：
1. `Ontology` → `memory/ontology/graph.jsonl` 查询实体关系
2. `domain-kit` → 查询领域本体中的关系
3. `tdai_memory_search` → 搜索结构化记忆
4. `wiki-kb` → 检查是否有相关文章提及
5. （fallback）`memorySearch` → 仅当 tdai 无结果时启用

**停止条件**：在任一步骤获得充分答案后停止。

### 类型 D：综合查询

**特征**：需要全面信息的复杂问题
- "帮我整理一下 XX 的全部信息"
- "XX 项目的完整情况"
- "关于 XX，我知道什么"

**查询路径**（按优先级依次执行）：
1. `wiki-kb` → 编译后的主题知识
2. `Ontology` → 结构化实体关系
3. `domain-kit` → 领域本体知识
4. `tdai_memory_search` → 结构化记忆
5. （fallback）`memorySearch` → 仅当 tdai 无结果时启用

**输出**：综合所有来源，按主题组织输出。

## 查询执行流程

```
用户提问
  │
  ├─ 1. 判断问题类型（A/B/C/D）
  │
  ├─ 2. 按类型对应的查询路径依次查询
  │     - 每个来源查询后评估：是否已充分回答？
  │     - 是 → 停止，进入输出阶段
  │     - 否 → 继续下一个来源
  │
  ├─ 3. 综合输出
  │     - 标注信息来源（wiki-kb / Ontology / memory / domain-kit）
  │     - 如有冲突，标注冲突并说明各来源的说法
  │
  └─ 4. 如果所有来源都无结果
        - 明确告知"未找到相关信息"
        - 建议用户：是否需要从某个来源开始积累？
```

## 输出格式

### 单来源命中

```
## 查询结果

{答案内容}

**来源**：{wiki-kb / Ontology / memory / domain-kit}
**置信度**：高 / 中 / 低
```

### 多来源综合

```
## 查询结果

### {主题 1}
{内容}
> 来源：wiki-kb

### {主题 2}
{内容}
> 来源：Ontology + memory

### 冲突/补充
- {来源 A} 说：...
- {来源 B} 说：...
```

### 无结果

```
## 查询结果

未找到与「{关键词}」相关的信息。

**建议**：
- 是否需要将相关资料 ingest 到 wiki-kb？
- 或者从对话记忆中提取？
```

## 特殊规则

### 优先级原则

**编译过的 > 结构化的 > 语义搜索的 > 原始对话**

- wiki-kb（编译后）优先级最高
- Ontology / domain-kit（结构化）次之
- memorySearch（语义搜索）再次
- tdai_conversation_search（原始对话）最低

### Fallback 机制

如果某个查询工具报错或返回空：
1. 记录错误/空结果
2. 继续下一个来源
3. 在输出中说明哪个来源不可用

### 缓存策略

对于同一 session 内的重复查询：
- 如果问题完全相同，复用上次结果
- 如果问题相似但关键词不同，部分复用（已查过的来源跳过）

## 与其他 Skill 的协作

| Skill | 协作方式 |
|-------|----------|
| `karpathy-llm-wiki` | 当用户说"加入知识库"时，触发 wiki-kb 的 Ingest 流程 |
| `domain-kit-owl` | 当查询涉及设备/协议/约束时，调用 domain-kit 查询 |
| `daily-agent` | 当查询后需要执行任务时，路由到 daily-agent |

## 示例

### 示例 1：领域知识查询

**用户**：WCS 系统的架构是什么？

**执行**：
1. 判断类型：A（领域知识）
2. 查 wiki-kb → 找到 `wiki-kb/wiki/logistics/wcs-architecture.md`
3. 读取文章 → 获得完整架构描述
4. 输出结果，来源标注 wiki-kb

### 示例 2：对话回忆查询

**用户**：上次关于前端技术路线我们讨论了什么？

**执行**：
1. 判断类型：B（对话回忆）
2. 查 tdai_conversation_search → 找到相关对话
3. 查 tdai_memory_search → 补充结构化记忆
4. 综合输出，标注来源

### 示例 3：关系查询

**用户**：王攀负责哪些项目？

**执行**：
1. 判断类型：C（关系查询）
2. 查 Ontology → 找到"王攀"实体及其关系
3. 输出结果，标注来源 Ontology

### 示例 4：综合查询

**用户**：帮我整理一下智能巡检项目的全部信息

**执行**：
1. 判断类型：D（综合查询）
2. 查 wiki-kb → 找到相关文章
3. 查 Ontology → 找到相关实体
4. 查 domain-kit → 找到相关设备/协议
5. 查 memorySearch → 语义搜索补充
6. 查 tdai_memory_search → 结构化记忆补充
7. 综合所有来源，按主题组织输出
