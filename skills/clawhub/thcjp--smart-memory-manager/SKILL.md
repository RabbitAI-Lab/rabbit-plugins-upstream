---
slug: smart-memory-manager
name: smart-memory-manager
version: "1.0.1"
displayName: smart-memory-manager
summary: Intelligent memory management for agents with short/long-term memory layering,
  semantic search, a...
license: MIT-0
description: |-
  Intelligent memory management for agents with short/long-term memory
  layering, semantic search, a...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: memory, intelligent, manager, smart-memory-manager, agents, management, smart
tags:
- Agents
tools:
- read
- exec
---

# smart-memory-manager

## 核心亮点

1. 📚 **分层记忆体系**：短期/长期/重要记忆三层架构，自动清理过期记忆，解决上下文溢出问题
2. 🔍 **多模式检索**：支持关键词/语义/混合三种检索模式，快速召回相关记忆，提升RAG准确率
3. 📝 **自动摘要能力**：一键生成记忆摘要，支持长会话上下文压缩，token占用减少70%
4. 💾 **持久化支持**：支持内存/磁盘持久化，重启后记忆不丢失

## 🎯 适用场景

* 长会话Agent、聊天机器人
* RAG应用的记忆层
* 需要长期记忆的任务型Agent
* 客服、助理类Agent的上下文管理

## 📝 参数说明

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | 操作类型：add/search/summarize/clear/list/load/save |
| content | string | 否 | add操作必填，记忆内容 |
| type | string | 否 | add操作可选，记忆类型：short-term/long-term/important，默认short-term |
| query | string | 否 | search操作必填，搜索关键词 |
| limit | number | 否 | search/list操作可选，返回结果数量，默认5/20 |
| typeFilter | string | 否 | 所有操作可选，过滤记忆类型，默认all |
| persist | boolean | 否 | add操作可选，是否持久化存储，默认false |
| persistPath | string | 否 | load/save操作可选，持久化文件路径，默认./memory-store.json |

## 💡 开箱即用示例

### 添加记忆

```typescript
// 添加长期记忆
await skills.smartMemoryManager({
  action: "add",
  content: "用户喜欢喝咖啡，不加糖，每周三下午喝奶茶",
  type: "long-term",
  persist: true
});
```

### 搜索记忆

```typescript
const result = await skills.smartMemoryManager({
  action: "search",
  query: "用户喜好",
  limit: 3,
  searchMode: "hybrid" // 关键词+语义混合检索
});
```

### 生成会话摘要

```typescript
const summary = await skills.smartMemoryManager({
  action: "summarize",
  typeFilter: "short-term",
  maxTokens: 500
});
```

### 持久化与加载

```typescript
// 保存所有记忆到磁盘
await skills.smartMemoryManager({
  action: "save",
  persistPath: "./my-memory.json"
});

// 从磁盘加载记忆
await skills.smartMemoryManager({
  action: "load",
  persistPath: "./my-memory.json"
});
```

## 🔧 技术实现说明

* 内置记忆自动清理机制，短期记忆最多保留100条，避免内存溢出
* 模块化设计，可轻松对接向量数据库实现语义检索
* 全链路类型安全，参数自动校验
* 轻量无外部依赖，开箱即用，也支持自定义扩展

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
