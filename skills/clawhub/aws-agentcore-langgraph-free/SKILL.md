---
slug: "aws-agentcore-langgraph-free"
name: "aws-agentcore-langgraph-free"
version: "1.0.0"
displayName: "AgentCore 免费"
summary: "AWS Bedrock AgentCore 与 LangGraph 基础智能体部署助手"
license: "MIT"
description: |-
  基于 AWS Bedrock AgentCore Runtime 与 LangGraph 的基础智能体构建助手(免费版).
  覆盖单智能体 StateGraph 定义、工具路由(tools_condition)、容器化部署基础流程.
  适用于快速搭建单智能体原型与本地开发验证。不含多智能体编排、Gateway 工具集成、
  跨会话 LTM 记忆等高级功能。如需完整能力请升级付费版.
  不适用于需要 100% 确定性的关键决策场景.
tags:
  - Agents
  - Operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# aws-agentcore-langgraph (免费版)

基于 AWS Bedrock AgentCore 与 LangGraph 的基础智能体部署助手.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AgentCore 免费处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 安装

```bash
pip install bedrock-agentcore langgraph
# 安装 agentcore CLI
```

## 快速开始

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
app = BedrockAgentCoreApp()  # 端口 8080,提供 /invocations 与 /ping
@app.entrypoint
def invoke(payload, context):
    result = graph.invoke({"messages": [("user", payload.get("prompt", ""))]})
    return {"result": result["messages"][-1].content}
app.run()
```

## 核心能力
- **AgentCore Runtime**: 端口 8080 的 HTTP 服务,处理 `/invocations` 与 `/ping` 端点
- **LangGraph Routing**: `tools_condition` 负责智能体到工具的路由,`ToolNode` 负责执行
- **AgentCore Memory**: 托管式跨会话记忆(免费版仅支持基础 STM,不含 LTM)
### AgentCore Runtime

针对AgentCore Runtime,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供AgentCore Runtime相关的配置参数、输入数据和处理选项.
**输出**: 返回AgentCore Runtime的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Runtime`的配置文档进行参数调优
### LangGraph Routing

针对LangGraph Routing,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供LangGraph Routing相关的配置参数、输入数据和处理选项.
**输出**: 返回LangGraph Routing的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`LangGraph Routing`的配置文档进行参数调优
### AgentCore Memory

针对AgentCore Memory,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供AgentCore Memory相关的配置参数、输入数据和处理选项.
**输出**: 返回AgentCore Memory的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Memory`的配置文档进行参数调优
#
## CLI 命令

| 命令 | 用途 |
|:-----|:-----|
| `agentcore configure -e agent.py --region us-east-1` | 初始化配置 |
| `agentcore launch --deployment-type container` | 容器模式部署 |
| `agentcore dev` | 热重载本地开发服务器 |
| `agentcore invoke '{"prompt": "Hello"}'` | 测试调用 |
| `agentcore destroy` | 清理资源 |

## 命名规则

- 以字母开头,仅含字母/数字/下划线,长度 1-48 字符
- 正确: `my_agent`  错误: `my-agent`

## 适用场景

| 场景 | 输入 | 输出 |
|---:|---:|---:|
| 单智能体部署 | 智能体定义与工具列表 | 容器化部署的 HTTP 智能体服务 |

**不适用于**: 多智能体编排、跨会话 LTM 记忆、Gateway 工具集成(需升级付费版).
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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
## 使用流程

1. 安装 `bedrock-agentcore`、`bedrock-agentcore`、`langgraph`
2. 使用 `StateGraph` 定义智能体图,通过 `tools_condition` 与 `ToolNode` 配置工具路由
3. 用 `BedrockAgentCoreApp()` 包装为 HTTP 服务
4. 运行 `agentcore configure` 初始化配置(注意命名规则:下划线而非连字符)
5. 运行 `agentcore launch --deployment-type container` 部署
6. 使用 `agentcore invoke` 测试,完成后 `agentcore destroy` 清理

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 案例展示

### 案例1: 单智能体工具调用

```python
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from bedrock_agentcore.runtime import BedrockAgentCoreApp
# ...
# 定义工具
def search_tool(query: str) -> str:
    return f"搜索结果: {query}"
# ...
tools = [search_tool]
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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| `on-demand throughput isn't supported` | 使用了不支持按需吞吐的推理配置 | 改用 `us.anthropic.claude-*` 推理配置文件 |
| `Model use case details not submitted` | 未提交 Anthropic 模型用例申请 | 在 Bedrock 控制台填写 Anthropic 用例表单 |
| `Invalid agent name` | 智能体名称含连字符等非法字符 | 使用下划线而非连字符,如 `my_agent` |
| 容器未读取 .env 文件 | 容器运行时不加载 .env | 在 Dockerfile 中用 `ENV` 设置环境变量 |
| 端口 8080 被占用 | 本地已有进程占用 8080 | 停止占用进程或修改 BedrockAgentCoreApp 端口 |
| Platform mismatch warning | 本地与目标平台架构不一致 | 正常现象,CodeBuild 会处理 ARM64 跨平台构建 |

## 常见问题

### Q1: tools_condition 路由如何工作?
A: `tools_condition` 是 LangGraph 预置的条件边函数,根据智能体节点输出中是否包含工具调用,自动路由到 `ToolNode` 执行或到 `END` 结束.
### Q2: 智能体名称为何报 Invalid agent name?
A: 名称必须以字母开头,仅含字母/数字/下划线,长度 1-48 字符。使用 `my_agent` 而非 `my-agent`.
### Q3: 免费版与付费版有何区别?
A: 免费版仅支持单智能体部署与基础 STM 记忆;付费版增加多智能体编排、跨会话 LTM、Gateway 工具集成(Lambda/MCP)、完整错误诊断与案例库.
### Q4: 如何部署不带记忆的智能体?
A: 使用 `agentcore launch --disable-memory`。适用于无状态工具型智能体,可降低成本与延迟.
## 已知限制

- 仅支持单智能体部署,不支持多智能体编排(Orchestrator + Specialists)
- 不含跨会话 LTM 记忆,仅支持基础会话内 STM
- 不含 Gateway 工具集成,无法将 Lambda/REST 转为 MCP 工具
- 依赖 AWS 云服务,需要网络连接与有效的 AWS 凭证
- Bedrock 模型需在控制台提前申请用例并配置推理配置文件

## 升级提示

> 本免费版提供基础单智能体部署能力。如需多智能体编排、跨会话 LTM 记忆、
> Gateway 工具集成(Lambda/MCP/REST)、完整错误诊断(10+ 场景)与 3 个
> 进阶案例,请升级至 **AgentCore LangGraph 付费版**.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AgentCore 免费处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "aws-agentcore-langgraph"
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
