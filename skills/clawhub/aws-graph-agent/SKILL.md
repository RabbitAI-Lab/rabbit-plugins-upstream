---
slug: "aws-graph-agent"
name: "aws-graph-agent"
version: 1.0.1
displayName: "AWS Graph Agent"
summary: "Bedrock AgentCore与LangGraph多代理编排,覆盖状态图、Runtime、记忆、网关、CLI全生命周期。"
license: "Proprietary"
description: |-
  AWS Bedrock AgentCore与LangGraph多代理部署编排工具。提供StateGraph状态图编排、AgentCore Runtime HTTP封装（8080端口）、
  Memory跨会话STM/LTM持久记忆、Gateway外部API/Lambda工具集成、CLI全生命周期管理五大核心能力.
  适用于多代理协调的复杂业务系统、跨会话持久记忆代理、外部API集成到代理工具链、生产级AI代理部署.
tags:
  - 智能代理
  - 云计算
  - AWS
  - 多代理系统
  - 通用办公
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# AWS Graph Agent

基于 AWS Bedrock AgentCore 与 LangGraph 编排的多代理系统。通过 StateGraph 状态图定义代理工作流，AgentCore Runtime 封装为 HTTP 服务，Memory 管理持久记忆，Gateway 集成外部工具.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AWS Graph Agent处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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
使用 LangGraph StateGraph 定义多代理工作流，支持 `tools_condition` 自动路由（代理 → 工具或 END）、`ToolNode` 预置工具执行器、条件边实现复杂多步逻辑（planner → executor → reviewer 循环）.
**输入**: 用户提供StateGraph 状态图编排所需的指令和必要参数.
**输出**: 返回StateGraph 状态图编排的处理结果,包含执行状态码、结果数据和执行日志.
### 2. AgentCore Runtime HTTP 封装
将代理封装为 8080 端口 HTTP 服务，处理 `/invocations`（调用）与 `/ping`（健康检查）端点，支持容器模式部署.
**输入**: 用户提供AgentCore Runtime HTTP 封装所需的指令和必要参数.
**输出**: 返回AgentCore Runtime HTTP 封装的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Runtime HTTP 封装`的配置文档进行参数调优
### 3. AgentCore Memory 持久记忆
管理跨会话/跨代理的 STM（短期记忆，会话内逐轮）与 LTM（长期记忆，跨会话/跨代理），配套一致性处理模式（写入后约 10s 最终一致，含等待+验证+重试逻辑）.
**输入**: 用户提供AgentCore Memory 持久记忆所需的指令和必要参数.
**输出**: 返回AgentCore Memory 持久记忆的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Memory 持久记忆`的配置文档进行参数调优
### 4. AgentCore Gateway 工具集成
将 API/Lambda 转化为带认证的 Agent 工具接口，支持 Fallback Mock（本地开发）、Local 工具协议、Production Gateway（生产）三种传输模式.
**输入**: 用户提供AgentCore Gateway 工具集成所需的指令和必要参数.
**处理**: 解析AgentCore Gateway 工具集成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回AgentCore Gateway 工具集成的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`AgentCore Gateway 工具集成`的配置文档进行参数调优
### 5. agentcore CLI 全生命周期管理
`configure`（交互式/脚本化配置）→ `launch`（容器部署）→ `dev`（热重载本地开发）→ `invoke`（测试调用）→ `destroy`（清理资源避免持续计费）.
**输入**: 用户提供agentcore CLI 全生命周期管理所需的指令和必要参数.
**输出**: 返回agentcore CLI 全生命周期管理的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|:---:|:---:|:---:|:---:|
| 多代理客服系统 | "按意图路由到客服/计费专家" | 编排器+专家模式部署，共享 session_id | StateGraph + Memory |
| 跨会话持久记忆 | "记住用户偏好和历史决策" | LTM 写入与一致性验证逻辑 | Memory |
| 外部 API 工具集成 | "将订单查询 Lambda 集成为代理工具" | Gateway 注册+三种传输模式 | Gateway |
| 生产级代理部署 | "部署带工具调用的代理到 8080 端口" | 容器部署+健康检查 | Runtime + CLI |
| 复杂多步逻辑 | "planner→executor→reviewer 循环" | 条件边+ToolNode 状态图 | StateGraph |

**不适用于**: 未完成 Bedrock 模型使用审批的账户，不需要多代理协调的简单单一代理场景，非 AWS 平台部署需求.
## 使用流程

### Step 1: 安装依赖
```bash
pip install bedrock-agentcore bedrock-agentcore-starter-toolkit langgraph
uv tool install bedrock-agentcore-starter-toolkit  # 安装 agentcore CLI
```

### Step 2: 预检清单（部署前必读）
| 检查项 | 要求 | 不满足的后果 |
|:------|------:|:------|
| 模型使用审批 | 在 Bedrock Console 填写 Anthropic 表单 | `Model use case details not submitted` |
| 推理配置 | 使用 `us.anthropic.claude-*` 推理配置文件 | `on-demand throughput isn't supported` |
| 代理命名 | 字母开头，仅字母/数字/下划线，1-48 字符 | `Invalid agent name` |
| 区域选择 | 选择支持 AgentCore 的区域（如 us-east-1） | 部署失败 |
| 环境变量 | 容器中在 Dockerfile 设置 ENV，非 .env | 容器不读取 .env |
| 记忆开关 | 确认是否需要记忆子系统 | 记忆功能不可用 |

### Step 3: 编写代理代码（StateGraph + Runtime）
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
# 交互式配置
agentcore configure -e agent.py --region us-east-1
# 脚本化配置（CI/CD）
agentcore configure -e agent.py --region us-east-1 --name my_agent --non-interactive
# 容器模式部署（生产）
agentcore launch --deployment-type container
# 无记忆部署（无状态代理）
agentcore launch --disable-memory
```

### Step 5: 测试与开发
```bash
agentcore dev                              # 热重载本地开发
agentcore invoke '{"prompt": "Hello"}'    # 测试调用
```

### Step 6: 按决策树选择多代理模式
```text
多代理协调? → 编排器+专家模式（编排器根据意图路由到专家，共享 session_id）
跨会话持久记忆? → AgentCore Memory（非 LangGraph checkpoints）
外部 API/Lambda? → AgentCore Gateway
单一代理简单? → 快速开始模板
复杂多步逻辑? → StateGraph + tools_condition + ToolNode
```

### Step 7: 清理资源（避免持续计费）
```bash
agentcore destroy
```

#
## 案例展示

### 案例1: 带工具调用的代理部署（StateGraph 基础模式）
**场景**: 部署一个简单代理，用户输入后自动判断是否调用工具

```python
# 最简模式：用户输入 → 代理节点 → tools_condition → ToolNode → 回到代理
#                                    → END（无需工具）
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

**分析**: `tools_condition` 自动判断代理输出是否包含工具调用请求。包含则路由到 `ToolNode` 执行工具后返回代理节点继续处理；不包含则直接路由到 END 返回结果.
### 案例2: 记忆系统写入与一致性验证（指数退避）
**场景**: 写入长期记忆并确保跨会话可读，处理约 10s 最终一致性延迟

```python
from bedrock_agentcore.memory import MemoryClient
import time
# ...
memory = MemoryClient()
memory.create_event(session_id, actor_id, event_type, payload)  # 写入
# ...
# 最终一致性验证（指数退避：2s→4s→8s→16s→30s，最多 5 次）
def verify_with_backoff(memory, session_id, actor_id, event_type, payload,
                        base=2, max_wait=30, max_retries=5):
    for attempt in range(max_retries):
        time.sleep(min(base * (2 ** attempt), max_wait))  # 指数退避+上限
        if memory.list_events(session_id):
            return  # 一致性达成
        if attempt < max_retries - 1:
            memory.create_event(session_id, actor_id, event_type, payload)  # 重写
    raise RuntimeError(f"记忆一致性验证失败：{max_retries} 次重试后仍为空")
# ...
verify_with_backoff(memory, session_id, actor_id, event_type, payload)
# 注意：event['payload'] 是列表类型；确认 actor_id 和 session_id 匹配
```

**分析**: 记忆写入后存在约 10 秒最终一致性延迟，立即查询会返回空。指数退避策略（2→4→8→16→30s）在保证最终一致的同时避免频繁轮询。重试时重新写入确保事件不被丢失.
### 案例3: 多代理协调（编排器+专家模式）端到端
**场景**: 客服系统按意图路由到客服专家/计费专家，共享 session_id 跨专家记忆

```python
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
# ...
class State(TypedDict):
    messages: list
    expert: str
# ...
def orchestrator(state):
    intent = classify(state["messages"][-1])  # 意图分类
    return {"expert": {"投诉": "cs_expert", "账单": "billing_expert"}[intent]}
# ...
def cs_expert(state):
    return {"messages": [handle_cs(state)]}      # 客服专家处理
# ...
def billing_expert(state):
    return {"messages": [handle_billing(state)]}  # 计费专家处理
# ...
builder = StateGraph(State)
builder.add_node("orchestrator", orchestrator)
builder.add_node("cs_expert", cs_expert)
builder.add_node("billing_expert", billing_expert)
builder.add_edge(START, "orchestrator")
builder.add_conditional_edges("orchestrator", lambda s: s["expert"])
builder.add_edge("cs_expert", END)
builder.add_edge("billing_expert", END)
graph = builder.compile()
```

**部署命令**:
```bash
agentcore configure -e agent.py --region us-east-1
agentcore launch
```

**分析**: 两个专家共享同一 `session_id`，通过 AgentCore Memory 实现跨专家记忆传递（编排器写入意图，专家读取上下文），避免用户重复陈述。`conditional_edges` 根据 `expert` 字段动态路由到对应专家节点.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---:|:---|---:|---:|
| 推理配置不支持 | `on-demand throughput isn't supported` | 未使用跨区域推理配置文件 | 改用 `us.anthropic.claude-*` 推理配置文件 |
| 模型审批未提交 | `Model use case details not submitted` | 未在 Bedrock Console 填写使用表单 | 进入 Bedrock Console 填写 Anthropic 模型使用审批表单 |
| 代理名称无效 | `Invalid agent name` | 名称含连字符或非法字符 | 改用下划线，字母开头，1-48 字符（如 `my-agent` → `my_agent`） |
| 记忆写入后为空 | `list_events` 返回空列表 | 最终一致性延迟约 10s | 等待 10s 后重新查询；检查日志 "Memory enabled/disabled" |
| 容器不读取 .env | 环境变量未生效 | 容器模式不支持 .env 文件 | 在 Dockerfile 中用 `ENV` 指令设置环境变量 |
| 部署后记忆不可用 | 记忆功能缺失 | 部署时使用了 `--disable-memory` | 重新部署不带 `--disable-memory` 参数 |
| actor_id 不匹配 | `list_events` 返回空但记忆已写入 | actor_id/session_id 与写入时不一致 | 确认 ID 匹配，注意 payload 是列表类型 |
| Gateway 未知工具 | `Unknown tool` | Lambda 未去除工具名前缀 | 从 `bedrockAgentCoreToolName` 去除 `___` 前缀 |
| 平台不匹配警告 | ARM64 跨平台构建警告 | 本地与目标平台架构不同 | 正常现象，CodeBuild 会自动处理，无需操作 |

## 成本优化策略

- 无状态部署用 `--disable-memory` 节省记忆存储成本
- 测试后立即 `agentcore destroy` 避免持续运行成本
- 生产用容器模式、开发用 `agentcore dev`
- 选择低成本区域（如 us-east-1）
- 使用 `us.anthropic.claude-*` 推理配置降低吞吐量成本

## 常见问题

### Q1: 部署后记忆为空怎么办？
A: 记忆写入后有约 10 秒最终一致性延迟。等待 10 秒后用 `list_events` 重新查询。如仍为空，检查日志中是否显示 "Memory enabled"，确认部署时未使用 `--disable-memory`.
### Q2: 容器无法读取 .env 文件怎么办？
A: 容器模式下 .env 文件不会被自动读取。在 Dockerfile 中使用 `ENV` 指令设置环境变量，而非依赖 .env 文件。这是容器模式与本地开发习惯的主要差异.
### Q3: 收到 "on-demand throughput isn't supported" 错误？
A: 使用 `us.anthropic.claude-*` 推理配置文件替代按需吞吐量。这是区域和模型组合的限制，跨区域推理配置文件可自动路由到容量充足的区域.
### Q4: 代理名称无效如何修改？
A: 代理名称必须字母开头，仅含字母/数字/下划线，1-48 字符。将连字符改为下划线（如 `my-agent` → `my_agent`），避免使用特殊符号和中文.
### Q5: Gateway 返回 "Unknown tool" 如何排查？
A: Lambda 函数必须从 `bedrockAgentCoreToolName` 参数中去除 `___` 前缀。检查 Lambda 代码中的工具名处理逻辑，确认注册时使用的名称与代理调用时一致.
### Q6: 多代理如何共享记忆？
A: 多个专家代理共享同一 `session_id`，通过 AgentCore Memory 的 `create_event` 写入、`list_events` 读取。编排器写入意图后，专家节点读取上下文，避免用户重复陈述。注意使用指数退避验证一致性.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **记忆最终一致性延迟约10秒**：写入后不能立即可读，需等待+验证+重试机制，不适合强一致性场景
2. **依赖 Bedrock 模型审批**：未在 Bedrock Console 填写 Anthropic 表单则无法部署，审批流程不可跳过
3. **代理命名规则严格**：仅字母/数字/下划线，1-48 字符，连字符等常见命名方式不被接受
4. **容器模式不支持 .env**：必须在 Dockerfile 中用 ENV 设置环境变量，与本地开发习惯不同
5. **Gateway 工具名需去前缀**：Lambda 的 `bedrockAgentCoreToolName` 必须去除 `___` 前缀，否则返回 "Unknown tool"

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AWS Graph Agent处理结果",
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
