# 代理定义规范（Agent Definition Specification）

## 概述

本文档定义 OpenClaw 编程代理的标准格式，用于创建可复用的、可配置的编程子代理。

## YAML Schema

### 必填字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 唯一标识符，仅允许 `[a-z0-9-]` |
| `display_name` | string | 中文友好名称 |
| `description` | string | 一句话职责描述（≤50字） |
| `model` | string | 推荐模型：sonnet/opus/haiku |
| `system_prompt` | string | 完整系统提示（支持多行） |

### 可选字段

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `color` | string | blue | UI 显示颜色 |
| `tools` | list | [] | 允许使用的工具白名单 |
| `trigger_examples` | list | [] | 触发此代理的消息示例 |
| `max_tokens` | number | 4096 | 最大输出 token 数 |
| `temperature` | number | 0.3 | 生成温度（越低越确定） |
| `timeout_seconds` | number | 300 | 执行超时时间 |

### 工具白名单

可用工具列表：

| 工具 | 说明 |
|------|------|
| `Read` | 读取文件内容 |
| `Write` | 创建/写入文件 |
| `Edit` | 编辑文件 |
| `Grep` | 搜索代码模式 |
| `Glob` | 文件匹配查找 |
| `exec` | 执行 shell 命令 |
| `web_search` | 搜索网络 |
| `web_fetch` | 获取网页内容 |

## 系统提示编写指南

### 结构模板

```
你是一个专业的[角色名称]。你的职责是[一句话职责]。

## [维度1名称]
[具体检查项/工作内容]

## [维度2名称]
[具体检查项/工作内容]

## 输出格式
[明确的输出模板]

## 约束
[行为边界和限制]
```

### 最佳实践

1. **角色明确**：开头定义清晰的角色身份
2. **维度具体**：列出 3-6 个具体工作维度
3. **格式统一**：提供输出模板，确保结果可预测
4. **约束清晰**：明确什么能做、什么不能做
5. **示例驱动**：在 system_prompt 中包含输入输出示例

## 触发匹配算法

```
用户消息 → 预处理（小写化、去标点）
  → 遍历所有 agents/*.yaml
    → 提取 trigger_examples
    → 计算关键词匹配分数
  → 选择分数最高的代理
  → 分数相同则按优先级：security > test > review
  → 无匹配则使用 code-reviewer（默认）
```

## 代理组合模式

### 串行模式

一个代理的输出作为另一个代理的输入：

```
code-reviewer → security-auditor → test-engineer
```

适用场景：完整的代码提交流程

### 并行模式

多个代理同时处理同一输入：

```
         ┌→ code-reviewer    ─┐
输入 ────┼→ security-auditor  ─┼→ 汇总
         └→ test-engineer    ─┘
```

适用场景：multi-agent-review 的并行审查

## 扩展代理

创建新代理的步骤：

1. 在 `agents/` 下创建 `your-agent.yaml`
2. 填写所有必填字段
3. 编写详细的 system_prompt
4. 添加 3-5 个 trigger_examples
5. 测试触发匹配是否正常工作
