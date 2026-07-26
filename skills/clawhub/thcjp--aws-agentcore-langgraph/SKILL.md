---
slug: "aws-agentcore-langgraph"
name: "aws-agentcore-langgraph"
version: 1.0.3
displayName: "AgentCore LangGraph"
summary: "AWS Bedrock AgentCore 与 LangGraph 多智能体编排部署助手"
license: "Proprietary"
description: |-
  基于 AWS Bedrock AgentCore Runtime 与 LangGraph 的多智能体系统构建与部署助手.
  覆盖智能体编排(Orchestrator + Specialists)、跨会话记忆(STM/LTM)、
  Gateway 工具集成(Lambda/MCP/REST)、容器化部署全流程.
  适用于需要在 AWS 上构建可扩展多智能体应用的开发团队,支持客户服务、电商、
  医疗、金融等领域的专家智能体协同。提供从本地开发到生产部署的完整 CLI 工作流,
  含状态图设计(StateGraph)、工具路由(tools_condition)、记忆持久化、
  MCP 工具转换等核心模式。不适用于需要 100% 确定性的关键决策场景.
tags:
  - Agents
  - Operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# aws-agentcore-langgraph

Multi-agent systems on AWS Bedrock AgentCore with LangGraph orchestration. 

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AgentCore LangGraph处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| AgentCore LangGraph多智能体编排 | 不支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |

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
- **AgentCore Memory**: 托管式跨会话/跨智能体记忆,支持 STM 与 LTM
- **LangGraph Routing**: `tools_condition` 负责智能体到工具的路由,`ToolNode` 负责执行
- **AgentCore Gateway**: 将 API/Lambda 转换为带鉴权的 MCP 工具
### AgentCore Runtime

针对AgentCore Runtime,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供AgentCore Runtime相关的配置参数、输入数据和处理选项.
**输出**: 返回AgentCore Runtime的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Runtime`的配置文档进行参数调优
### AgentCore Memory

针对AgentCore Memory,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供AgentCore Memory相关的配置参数、输入数据和处理选项.
**输出**: 返回AgentCore Memory的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Memory`的配置文档进行参数调优
### LangGraph Routing

针对LangGraph Routing,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供LangGraph Routing相关的配置参数、输入数据和处理选项.
**输出**: 返回LangGraph Routing的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`LangGraph Routing`的配置文档进行参数调优
#
## CLI 命令

| 命令 | 用途 |
|---:|---:|
| `agentcore configure -e agent.py --region us-east-1` | 初始化配置 |
| `agentcore configure -e agent.py --region us-east-1 --name my_agent --non-interactive` | 脚本化配置 |
| `agentcore launch --deployment-type container` | 容器模式部署 |
| `agentcore launch --disable-memory` | 部署时禁用记忆子系统 |
| `agentcore dev` | 热重载本地开发服务器 |
| `agentcore invoke '{"prompt": "Hello"}'` | 测试调用 |
| `agentcore destroy` | 清理资源 |

## 核心模式

### 多智能体编排

- Orchestrator 将任务委托给专家智能体(客户服务、电商、医疗、金融等)
- 专家智能体可为内联函数或独立部署的智能体,均通过 `session_id` 共享上下文

### 记忆系统 (STM/LTM)

```python
from bedrock_agentcore.memory import MemoryClient
memory = MemoryClient()
memory.create_event(session_id, actor_id, event_type, payload)  # 写入
events = memory.list_events(session_id)  # 读取(返回列表)
```

- **STM(短期记忆)**: 会话内逐轮对话
- **LTM(长期记忆)**: 跨会话/跨智能体的事实与决策
- 写入后约 10 秒最终一致性延迟

### Gateway 工具

```bash
python -m bedrock_agentcore.gateway.deploy --stack-name my-agents --region us-east-1
```

```python
from bedrock_agentcore.gateway import GatewayToolClient
gateway = GatewayToolClient()
result = gateway.call("tool_name", param1=value1, param2=value2)
```

- 传输方式: 本地 Fallback Mock、本地 MCP 服务器、生产 Gateway(Lambda/REST/MCP)
- 部署后自动配置 `BEDROCK_AGENTCORE_GATEWAY_URL` 环境变量

## 决策树

```text
多智能体协同?        → Orchestrator + Specialists 模式
需要跨会话持久记忆?   → AgentCore Memory(非 LangGraph checkpoints)
需调用外部 API/Lambda? → AgentCore Gateway
单智能体简单场景?     → 快速开始示例
复杂多步逻辑?        → StateGraph + tools_condition + ToolNode
```

## 命名规则

- 以字母开头,仅含字母/数字/下划线,长度 1-48 字符
- 正确: `my_agent`  错误: `my-agent`

## 适用场景

| 场景 | 输入 | 输出 |
|:---:|:---:|:---:|
| 多智能体编排部署 | 编排器与专家智能体定义 | 容器化部署的多智能体服务,共享 session_id |
| 跨会话持久记忆 | session_id、actor_id、事件数据 | STM 逐轮记忆与 LTM 跨会话事实存储 |
| Gateway 工具集成 | Lambda/REST API 定义与鉴权配置 | 转换为 MCP 工具并自动配置 Gateway URL |

**不适用于**: 需要 100% 确定性的关键决策场景、纯本地无网络环境.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
4. 运行 `agentcore configure` 初始化部署配置(注意命名规则)
5. 运行 `agentcore launch --deployment-type container` 部署
6. 使用 `agentcore invoke` 测试,完成后 `agentcore destroy` 清理

#
## 案例展示

### 案例1: 多智能体编排(客服 + 电商)

```python
# Orchestrator 委托给客服专家与电商专家,共享 session_id
def orchestrator(state):
    if "订单" in state["messages"][-1].content:
        return {"next": "ecommerce_specialist"}
    return {"next": "customer_service"}
# ...
builder.add_conditional_edges("orchestrator", orchestrator)
builder.add_node("customer_service", cs_agent)
builder.add_node("ecommerce_specialist", eco_agent)
# 两个专家通过同一 session_id 访问共享记忆
```

### 案例2: 跨会话持久记忆

```python
memory = MemoryClient()
# 写入 LTM 事实
memory.create_event(
    session_id="sess_001",
    actor_id="user_123",
    event_type="preference",
    payload={"language": "zh", "timezone": "Asia/Shanghai"}
)
# 等待约 10 秒后读取
import time; time.sleep(10)
events = memory.list_events("sess_001")
# event['payload'] 是列表,需按索引取值
```

### 案例3: Gateway 工具集成

```bash
# 部署 Gateway,将 Lambda 转为 MCP 工具
python -m bedrock_agentcore.gateway.deploy --stack-name my-agents --region us-east-1
# 部署后自动设置 BEDROCK_AGENTCORE_GATEWAY_URL
```
```python
gateway = GatewayToolClient()
result = gateway.call("search_products", query="laptop", limit=10)
# Lambda 端需从 bedrockAgentCoreToolName 中去除 ___ 前缀
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| `on-demand throughput isn't supported` | 使用了不支持按需吞吐的推理配置 | 改用 `us.anthropic.claude-*` 推理配置文件 |
| `Model use case details not submitted` | 未提交 Anthropic 模型用例申请 | 在 Bedrock 控制台填写 Anthropic 用例表单 |
| `Invalid agent name` | 智能体名称含连字符等非法字符 | 使用下划线而非连字符,如 `my_agent` |
| 写入后记忆为空 | 约 10 秒最终一致性延迟未完成 | 写入后等待约 10 秒再读取 |
| 容器未读取 .env 文件 | 容器运行时不加载 .env | 在 Dockerfile 中用 `ENV` 设置环境变量 |
| 部署后记忆不工作 | 部署时记忆子系统未启用 | 检查日志中 "Memory enabled/disabled" 信息 |
| `list_events` 返回空 | actor_id 或 session_id 不匹配 | 核对 actor_id/session_id;`event['payload']` 是列表 |
| Gateway 报 "Unknown tool" | Lambda 未去除工具名前缀 | Lambda 需从 `bedrockAgentCoreToolName` 中去除 `___` 前缀 |
| Platform mismatch warning | 本地与目标平台架构不一致 | 正常现象,CodeBuild 会处理 ARM64 跨平台构建 |
| 端口 8080 被占用 | 本地已有进程占用 8080 | 停止占用进程或修改 BedrockAgentCoreApp 端口 |

## 常见问题

### Q1: STM 与 LTM 何时分别使用?
A: STM 用于单次会话内的逐轮对话上下文;LTM 用于跨会话、跨智能体持久化的事实与决策。需要长期记住用户偏好或历史决策时用 LTM.
### Q2: 多个专家智能体如何共享上下文?
A: 所有专家智能体使用同一个 `session_id`,通过 AgentCore Memory 读写共享事件。编排器在委托任务时传递 session_id.
### Q3: 何时用 Gateway 而非内联工具?
A: 需要鉴权、生产级可靠性、多智能体共享工具时用 Gateway;本地开发或简单场景可用内联函数或 Fallback Mock.
### Q4: 如何部署不带记忆子系统的智能体?
A: 使用 `agentcore launch --disable-memory`。适用于无状态工具型智能体,可降低成本与延迟.
### Q5: tools_condition 路由如何工作?
A: `tools_condition` 是 LangGraph 预置的条件边函数,根据智能体节点输出中是否包含工具调用,自动路由到 `ToolNode` 执行或到 `END` 结束.
### Q6: 跨平台 ARM64 构建出现警告怎么办?
A: Platform mismatch warning 属正常现象。CodeBuild 会自动处理 ARM64 跨平台构建,无需手动干预.
## 已知限制

- 依赖 AWS 云服务,需要网络连接与有效的 AWS 凭证
- 记忆系统存在约 10 秒最终一致性延迟,不适合强一致即时读取
- Bedrock 模型需在控制台提前申请用例并配置推理配置文件
- 智能体名称受 1-48 字符及字母/数字/下划线限制

## 参考

- [agentcore-cli.md](references/agentcore-cli.md) - CLI 命令、部署、生命周期
- [agentcore-runtime.md](references/agentcore-runtime.md) - 流式、异步、可观测性
- [agentcore-memory.md](references/agentcore-memory.md) - STM/LTM 模式与 API
- [agentcore-gateway.md](references/agentcore-gateway.md) - 工具集成、MCP、Lambda
- [langgraph-patterns.md](references/langgraph-patterns.md) - StateGraph 设计与路由

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AgentCore LangGraph处理结果",
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
