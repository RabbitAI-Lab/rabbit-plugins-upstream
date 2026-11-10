# Coding Agent — 标准化编程代理定义

> 借鉴 Claude Code 代理定义 + Codex YAML 格式，为 OpenClaw 提供可配置的编程代理。

## 代理定义规范

每个代理使用 YAML 文件定义，存放于 `agents/` 目录：

```yaml
# 必填字段
name: agent-id              # 唯一标识符
display_name: "显示名称"     # 中文友好名称
description: "职责描述"      # 一句话说明代理做什么
model: sonnet               # 推荐模型（sonnet/opus/haiku）
color: green                # UI 显示颜色

# 工具权限
tools:                      # 允许使用的工具列表
  - Read
  - Grep
  - exec

# 触发条件
trigger_examples:           # 触发此代理的用户消息示例
  - "示例消息1"
  - "示例消息2"

# 系统提示
system_prompt: |
  详细的系统提示文本...
```

## 代理调度逻辑

当用户发起编程相关请求时，按以下流程选择代理：

1. **关键词匹配**：将用户消息与 `trigger_examples` 比对
2. **文件类型匹配**：根据涉及的文件类型选择（如 `.test.` → test-engineer）
3. **任务类型匹配**：根据任务性质选择（审查/安全/测试）
4. **默认回退**：无明确匹配时使用 code-reviewer

调度优先级：security-auditor > test-engineer > code-reviewer

## 与 sessions_spawn 集成

```
用户请求 → coding-agent 识别任务类型
  → 加载对应 agents/*.yaml
  → sessions_spawn(
      model: agent.model,
      system_prompt: agent.system_prompt,
      task: 用户请求 + 上下文
    )
  → 等待子代理返回
  → 格式化输出给用户
```

### spawn 参数映射

| YAML 字段 | spawn 参数 |
|-----------|-----------|
| model | model |
| system_prompt | system_prompt |
| tools | tools（白名单过滤） |
| name | 子代理标识 |

## 输出格式规范

所有代理输出遵循统一格式：

```markdown
## [代理名称] 审查结果

### 概要
一句话总结发现。

### 详细发现
1. **[严重程度]** 问题描述
   - 位置：文件:行号
   - 建议：修复方案

### 评分
- 整体评分：X/10
- 置信度：X%
```

## 预置代理

| 代理 | 职责 | 触发场景 |
|------|------|----------|
| code-reviewer | 代码质量审查 | "审查代码"、"review"、"代码质量" |
| security-auditor | 安全漏洞扫描 | "安全检查"、"漏洞"、"security" |
| test-engineer | 测试用例生成 | "写测试"、"覆盖率"、"test" |

## 自定义代理

在 `agents/` 下创建新的 `.yaml` 文件即可。遵循代理定义规范，确保：
- `name` 唯一
- `system_prompt` 足够详细（包含角色、约束、输出格式）
- `trigger_examples` 覆盖常见触发场景
- `tools` 最小权限原则

## 文件结构

```
coding-agent/
├── SKILL.md                       # 本文件
├── agents/
│   ├── code-reviewer.yaml         # 代码审查代理
│   ├── security-auditor.yaml      # 安全审计代理
│   └── test-engineer.yaml         # 测试工程代理
└── references/
    └── agent-definition-spec.md   # 代理定义完整规范
```
