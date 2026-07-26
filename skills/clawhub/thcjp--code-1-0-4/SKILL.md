---
slug: code-1-0-4
name: code-1-0-4
version: "1.0.0"
displayName: Code 1.0.4
summary: Coding workflow with planning, implementation, verification, and testing
  for clean software devel...
license: MIT
description: |-
  Coding workflow with planning, implementation, verification, and testing
  for clean software devel。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Development
tools:
  - - read
- exec
---
# Code 1.0.4

## 核心能力

- Coding workflow with planning, implementation, verification, and testing
  for clean software devel
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、需要代码生成、编程辅助、调试测试、开发部署时使用、不适用于无明确技、术栈的模糊需求。这些能力在上述核心功能中均有对应处理逻辑。
### 源能力映射
本skill覆盖源skill的以下能力点:

| 源能力点 | 支持状态 | 实现方式 |
|:---------|:---------|:---------|
| Verify Everything | 支持 | 通过核心功能实现对应能力 |
| Check Memory First | 支持 | 通过核心功能实现对应能力 |
| Task breakdown | 支持 | 通过核心功能实现对应能力 |
| Memory setup | 支持 | 通过核心功能实现对应能力 |
| After | 支持 | 通过核心功能实现对应能力 |
| UI changes | 支持 | 通过核心功能实现对应能力 |
| Multi-task state | 支持 | 通过核心功能实现对应能力 |

**处理**: 按照skill规范执行源能力映射操作,遵循单一意图原则。
**输出**: 返回源能力映射的执行结果,包含操作状态和输出数据。
### 领域术语
本skill涉及以下领域术语: `accesses`, `before`, `sent`, `ignoring`, `execution.md`, `scope`, `deliver`, `memory-template.md`, `delivering`, `provides`, `state.md`, `planning.md`, `verification.md`, `modification`, `action`

**处理**: 按照skill规范执行领域术语操作,遵循单一意图原则。
**输出**: 返回领域术语的执行结果,包含操作状态和输出数据。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 常见问题

### Q1: 如何开始使用Code 1.0.4？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Code 1.0.4有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
