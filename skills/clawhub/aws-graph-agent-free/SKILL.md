---
slug: "aws-graph-agent-free"
name: "aws-graph-agent-free"
version: "1.0.0"
displayName: "AWS Graph LITE"
summary: "Bedrock AgentCore与LangGraph基础代理编排,提供StateGraph状态图与容器部署能力。"
license: "MIT"
description: |-
  AWS Bedrock AgentCore与LangGraph基础代理编排工具（免费版）。提供StateGraph状态图编排与
  AgentCore Runtime容器部署两大基础能力。支持 tools_condition 自动路由与 ToolNode 工具执行器，
  可将代理封装为 8080 端口 HTTP 服务.
  适用于单一代理的快速部署和工具调用场景。如需持久记忆、Gateway工具集成、多代理协调等高级功能，
  请升级至 aws-graph-agent 付费版.
tags:
  - 智能代理
  - 云计算
  - AWS
  - 通用办公
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# AWS Graph LITE

基于 AWS Bedrock AgentCore 与 LangGraph 的基础代理编排工具。通过 StateGraph 状态图定义代理工作流，AgentCore Runtime 封装为 HTTP 服务.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AWS Graph LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. StateGraph 状态图编排
使用 LangGraph StateGraph 定义代理工作流，支持 `tools_condition` 自动路由（代理 → 工具或 END）、`ToolNode` 预置工具执行器，实现工具调用与自动路由.
**输入**: 用户提供StateGraph 状态图编排所需的指令和必要参数.
**输出**: 返回StateGraph 状态图编排的处理结果,包含执行状态码、结果数据和执行日志.
### 2. AgentCore Runtime HTTP 封装
将代理封装为 8080 端口 HTTP 服务，处理 `/invocations`（调用）与 `/ping`（健康检查）端点，支持容器模式部署.
**输入**: 用户提供AgentCore Runtime HTTP 封装所需的指令和必要参数.
**输出**: 返回AgentCore Runtime HTTP 封装的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Runtime HTTP 封装`的配置文档进行参数调优
### 3. agentcore CLI 基础管理
`configure`（配置）→ `launch`（部署）→ `dev`（本地开发）→ `invoke`（测试调用）→ `destroy`（清理资源）.
> **升级提示**: 跨会话持久记忆（STM/LTM）、Gateway 外部 API/Lambda 工具集成、多代理协调（编排器+专家模式）、记忆一致性验证逻辑等高级功能仅在 [aws-graph-agent 付费版] 中提供.
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|---:|---:|---:|
| 单一代理部署 | "部署一个带工具调用的代理到 8080 端口" | 容器部署+健康检查 | Runtime + CLI |
| 工具调用代理 | "代理自动判断是否调用工具" | tools_condition 自动路由 | StateGraph |
| 本地开发调试 | "热重载本地开发代理" | agentcore dev 热重载 | CLI |

**不适用于**: 需要跨会话持久记忆的场景（需付费版），需要外部 API/Lambda 工具集成的场景（需付费版），多代理协调的复杂业务系统（需付费版），未完成 Bedrock 模型审批的账户.
## 使用流程

### Step 1: 安装依赖
```bash
pip install bedrock-agentcore bedrock-agentcore-starter-toolkit langgraph
uv tool install bedrock-agentcore-starter-toolkit  # 安装 agentcore CLI
```

### Step 2: 预检清单
| 检查项 | 要求 | 不满足的后果 |
|:---:|:---:|:---:|
| 模型使用审批 | 在 Bedrock Console 填写 Anthropic 表单 | `Model use case details not submitted` |
| 推理配置 | 使用 `us.anthropic.claude-*` 推理配置文件 | `on-demand throughput isn't supported` |
| 代理命名 | 字母开头，仅字母/数字/下划线，1-48 字符 | `Invalid agent name` |
| 环境变量 | 容器中在 Dockerfile 设置 ENV，非 .env | 容器不读取 .env |

### Step 3: 编写代理代码
```python
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from typing import Annotated
from typing_extensions import TypedDict
# ...
class State(TypedDict):
    messages: Annotated[list, add_messages]
# ...
builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge(START, "agent")
graph = builder.compile()
# ...
app = BedrockAgentCoreApp()
@app.entrypoint
def invoke(payload, context):
    result = graph.invoke({"messages": [("user", payload.get("prompt", ""))]})
    return {"result": result["messages"][-1].content}
app.run()
```

### Step 4: 配置与部署
```bash
agentcore configure -e agent.py --region us-east-1
agentcore launch --deployment-type container
```

### Step 5: 测试与清理
```bash
agentcore dev                              # 热重载本地开发
agentcore invoke '{"prompt": "Hello"}'    # 测试调用
agentcore destroy                          # 清理资源避免持续计费
```

#
## 案例展示

### 案例1: 带工具调用的代理部署
**场景**: 部署一个简单代理，用户输入后自动判断是否调用工具

```python
# 用户输入 → 代理节点 → tools_condition → ToolNode → 回到代理
#                                → END（无需工具）
builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_conditional_edges("agent", tools_condition)  # 自动路由
builder.add_edge(START, "agent")
graph = builder.compile()
```

**部署命令**:
```bash
agentcore configure -e agent.py --region us-east-1
agentcore launch
agentcore invoke '{"prompt": "查询北京今天天气"}'
```

**分析**: `tools_condition` 自动判断代理输出是否包含工具调用请求。包含则路由到 `ToolNode` 执行工具后返回代理节点；不包含则直接路由到 END。部署后可通过 8080 端口的 `/invocations` 端点调用，`/ping` 端点检查健康状态。测试完成后务必执行 `agentcore destroy` 清理资源，避免持续计费。本地开发可使用 `agentcore dev` 热重载，无需每次重新部署容器.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 推理配置不支持 | `on-demand throughput isn't supported` | 未使用跨区域推理配置文件 | 改用 `us.anthropic.claude-*` 推理配置文件 |
| 模型审批未提交 | `Model use case details not submitted` | 未在 Bedrock Console 填写使用表单 | 进入 Bedrock Console 填写 Anthropic 模型使用审批表单 |
| 代理名称无效 | `Invalid agent name` | 名称含连字符或非法字符 | 改用下划线，字母开头，1-48 字符（如 `my-agent` → `my_agent`） |
| 容器不读取 .env | 环境变量未生效 | 容器模式不支持 .env 文件 | 在 Dockerfile 中用 `ENV` 指令设置环境变量 |
| 平台不匹配警告 | ARM64 跨平台构建警告 | 本地与目标平台架构不同 | 正常现象，CodeBuild 会自动处理，无需操作 |

## 常见问题

### Q1: 收到 "on-demand throughput isn't supported" 错误？
A: 使用 `us.anthropic.claude-*` 推理配置文件替代按需吞吐量。这是区域和模型组合的限制，跨区域推理配置文件可自动路由到容量充足的区域.
如仍报错，确认所选区域（如 us-east-1）支持 AgentCore 与 Bedrock 模型，并检查账户是否已开通对应模型的访问权限.
### Q2: 代理名称无效如何修改？
A: 代理名称必须字母开头，仅含字母/数字/下划线，1-48 字符。将连字符改为下划线（如 `my-agent` → `my_agent`），避免使用特殊符号和中文.
### Q3: 容器无法读取 .env 文件怎么办？
A: 容器模式下 .env 文件不会被自动读取。在 Dockerfile 中使用 `ENV` 指令设置环境变量，而非依赖 .env 文件。这是容器模式与本地开发习惯的主要差异.
### Q4: 免费版和付费版有什么区别？
A: 免费版（LITE）包含 StateGraph 状态图编排和 AgentCore Runtime 容器部署两大基础功能。付费版（AWS Graph Agent）额外提供：
- 跨会话持久记忆（STM/LTM）与一致性验证逻辑（指数退避）
- Gateway 外部 API/Lambda 工具集成（三种传输模式）
- 多代理协调（编排器+专家模式，共享 session_id）
- 更多案例展示（3 个完整案例 vs 1 个基础案例）
- 更详细的异常处理（9 种 AgentCore 特定错误 vs 5 种基础错误）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **功能限制**: 仅支持 StateGraph 基础编排与容器部署，不支持持久记忆、Gateway 工具集成、多代理协调（需升级付费版）
- **依赖 Bedrock 模型审批**: 未在 Bedrock Console 填写 Anthropic 表单则无法部署
- **代理命名规则严格**: 仅字母/数字/下划线，1-48 字符，连字符不被接受
- **容器模式不支持 .env**: 必须在 Dockerfile 中用 ENV 设置环境变量

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AWS Graph LITE处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "aws-graph-agent"
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
