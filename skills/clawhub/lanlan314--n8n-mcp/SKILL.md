---
name: n8n-mcp
description: 通过 n8n MCP server (http://localhost:5678/mcp-server/http) 用 n8n Workflow SDK 创建/校验/发布/管理工作流
version: 1.0.0
---

# n8n MCP 连接与工作流管理

通过 n8n 官方 MCP server 以编程方式创建、校验、发布和管理这台 Mac mini 上的 n8n 工作流。

## 连接信息
- **MCP 端点**：`http://localhost:5678/mcp-server/http`
- **认证**：HTTP header `Authorization: Bearer <token>`（n8n MCP 访问令牌，用户从 n8n 设置中获取并配置）
- **协议**：MCP over HTTP（JSON-RPC 2.0 + SSE）。用 curl POST，`Content-Type: application/json`，`Accept: application/json, text/event-stream`
- **本机 n8n**：版本 2.20.9，Homebrew 安装（`/opt/homebrew/lib/node_modules/n8n`），跑在 `:5678`，服务名 `com.n8n.server`
- **Token 存哪**：用户在 n8n 的 MCP 配置中生成并提供

## 关键 MCP 工具
| 工具 | 用途 |
|------|------|
| `search_workflows` | 搜索已有工作流（按 name/description/projectId 过滤） |
| `get_workflow_details` | 查看工作流详情、输入 schema、节点结构 |
| `create_workflow_from_code` | **用 n8n Workflow SDK 代码创建工作流**（核心） |
| `update_workflow` | 更新已有工作流 |
| `validate_workflow` | 校验工作流代码（创建前必须先 validate） |
| `publish_workflow` / `unpublish_workflow` | 激活 / 停用定时触发的正式版 |
| `execute_workflow` | 执行工作流（manual / production，支持 chat/webhook/form 输入） |
| `test_workflow` | 测试工作流 |
| `get_node_types` | 获取某节点类型的 TS 类型定义（版本+参数），用于写 SDK 代码 |
| `search_nodes` | 搜索可用节点类型 |
| `archive_workflow` | 归档工作流 |

## 调用格式（curl）
```bash
TOKEN="<n8n-mcp-token>"
curl -s -X POST http://localhost:5678/mcp-server/http \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"<TOOL>","arguments":{...}}}'
```
- 列工具：`method:"tools/list"`
- 返回是 SSE 流，每行 `data: {jsonrpc...}`。解析 `data:` 后 JSON 的 `result.content[0].text` 拿实际内容。

## 创建工作流标准流程
1. **设计**：定触发（Schedule Trigger 定时 / Manual / Webhook）、数据源（HTTP Request）、处理（Code / AI 节点）、输出（飞书 / 数据表 / 日志）。
2. **查类型**：用 `get_node_types` 拿所需节点 TS 定义（如 `n8n-nodes-base.scheduleTrigger`、`n8n-nodes-base.httpRequest`、`n8n-nodes-base.code`、`@n8n/n8n-nodes-langchain.openAi` 等），按其 Params 接口写代码。
3. **写代码**：用 n8n Workflow SDK（TypeScript）写完整工作流对象（nodes + connections + settings + name）。
4. **校验**：`validate_workflow` 传 code，通过后创建。
5. **创建**：`create_workflow_from_code` 带 code，可选 name/description/projectId/folderId。
6. **激活**：`publish_workflow` 使定时时序生效；调试用 `test_workflow` / `execute_workflow`(manual)。
7. **查看**：`get_workflow_details` 确认节点与 schema。

## 实践注意
- **优先走 MCP**：干净、无需进界面手动改。
- **本机页面 vs API**：`http://localhost:5678` 页面免登录；但 REST API 需要 `X-N8N-API-KEY` header（与 MCP token 不同）。
- 工作流持久化在 `~/.n8n/database.sqlite`；除非必要否则别直接改库，走 MCP。
- **其他服务的 MCP**（如博客平台 halo_create_post/halo_search_content 等）与 n8n 的 MCP 端点不同，注意区分。
- 定时默认建议每天 08:00 跑一次。
- 聚合多个热点源可用公开接口：知乎热榜、百度热搜、微博要闻榜、今日头条（多需带 UA，注意反爬可能变更）。

## 相关记忆
- 本机 n8n 曾做「AI 智能工单处理系统」「视频制作工单系统」；n8n form 访问路径为 `/webhook/{路径}/n8n-form`。
