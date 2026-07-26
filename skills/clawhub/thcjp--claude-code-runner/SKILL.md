---
slug: "claude-code-runner"
name: "claude-code-runner"
version: 0.1.1
displayName: "ai-assistant Code Ru"
summary: "经PTY调用Claude Code执行编程任务,搞定非TTY环境"
license: "Proprietary"
description: |-
  Execute programming tasks via ai-assistant Code using PTY-based invocation。Handles non-TTY environment。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# ai-assistant Code Ru

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

- Claude Code Runner 结果导出 - 生成生成内容
- Claude Code Runner 实时监控 - 遵循专业风格规范
- Claude Code Runner 错误重试 - 支持多种变体等多种变体
- Claude Code Runner 多格式支持 - 自动适配多种场景
#
## 适用场景

### 1. Automated Code Review

```python
result = run_claude_code(
    workdir='/root/repo/project',
    prompt='Review this codebase and identify potential bugs or improvements'
)
```

### 2. Refactoring Tasks

```python
result = run_claude_code(
    workdir='/root/repo/legacy-app',
    prompt='Refactor the database layer to use SQLAlchemy ORM instead of raw SQL'
)
```

### 核心能力(补充)

```python
result = run_claude_code(
    workdir='/root/repo/api-service',
    prompt='''
    Add a new REST endpoint for user profile management:
    - GET /api/users/{id}/profile
    - PUT /api/users/{id}/profile
    - Include validation and error handling
    - Add unit tests
    '''
)
```

### 4. Bug Fixes

```python
result = run_claude_code(
    workdir='/root/repo/web-app',
    prompt='Fix the memory leak in the WebSocket connection handler'
)
```

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | claude-code-runner处理的内容输入 |,  |
| content | string | 否 | claude-code-runner处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "runner 相关配置参数",
    result: "runner 相关配置参数",
    result: "runner 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 输入content为空 | 用户未提供必要信息 | 提示用户提供content, 并给出示例格式 |
| 输入内容过长(>5000字) | 超出单次处理能力 | 建议分段处理, 每段不超过2000字 |
| 风格参数不识别 | 传入不支持的风格 | 列出支持的风格选项, 使用默认风格 |
| 生成内容不达标 | 质量校验未通过 | 自动1次, 仍不达标则标注问题返回 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Claude Code Runner？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

* Requires Unix-like environment (uses PTY)
* Requires root/sudo for user switching
* ai-assistant Code must be installed separately
* May not handle all edge cases of interactive prompts
