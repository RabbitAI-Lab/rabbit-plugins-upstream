---
name: phone-agent
description: >-
    Control a real phone from OpenClaw via a local MCP relay. Use when the user asks to
    operate a phone (open apps, tap, input, take screenshots), run an AI automation task
    on a connected Android/iPhone device, check the current phone screen or device info,
    or query/abort a running phone agent task.
version: 1.0.0
metadata:
    openclaw:
        requires:
            bins:
                - node
        envVars:
            - name: PHONE_AGENT_WS_PORT
              required: false
              description: WebSocket relay port between the MCP server and the browser page (default 7788).
        emoji: "📱"
---

# Phone Agent Skill

通过本地 MCP Server 桥接浏览器中运行的 Mobile AI Agent，让 OpenClaw 可以远程控制手机——无需额外代码，直接用自然语言描述任务即可。

## 何时使用本技能

- 用户要求操控真实手机（打开应用、点击、输入、滑动）
- 用户要求查看手机当前界面（截图）
- 用户要求查询设备信息（型号、系统版本）
- 用户要求在手机上执行多步骤 AI 自动化任务
- 用户要求查询/中断正在运行的 Agent 任务

## 架构概览

```
┌──────────────────────────────────────────────────────────────────────┐
│                        External AI Agent                             │
│              (OpenClaw / Qoder / Claude Desktop / Chrome AI)         │
└───────────┬──────────────────────────────────────────┬───────────────┘
            │ 通道 A：stdio JSON-RPC 2.0                │ 通道 B：document
            ▼                                          │   .modelContext
┌───────────────────────────────┐                      │   .callTool()
│  mcp-server/dist/server.js    │                      ▼
│  (Node.js McpServer)          │      ┌───────────────────────────────┐
│  6 Tools 注册于 stdio 传输      │      │   Chrome WebMCP Runtime       │
└───────────┬───────────────────┘      │   (#enable-webmcp-testing)    │
            │ WebSocket                └───────────────┬───────────────┘
            │ ws://localhost:7788                      │ execute()
            ▼                                          ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        浏览器页面（Mobile AI Use）                     │
│   McpRelayClient(通道 A)        WebMcpService(通道 B)                 │
│                └────────────┬────────────┘                           │
│                             ▼  McpServiceContext（共用）              │
│            Plan-and-Resolve Agent / ReAct Agent                      │
└─────────────────────────────┬────────────────────────────────────────┘
                              │  Web ADB
                              ▼
┌──────────────────────────────────────────────────────────────────────┐
│                       Android / iOS Device                           │
└──────────────────────────────────────────────────────────────────────┘
```

## Installation/Setup

### 1. 启动本地 MCP Server

```bash
cd <项目根目录>/mcp-server
npm install      # 首次运行需安装依赖
npm run build    # 编译 TypeScript
npm start        # 启动服务（监听 stdio + WebSocket :7788）
```

### 2. 打开 Mobile AI Agent 页面

访问 https://mobile-ai-use.com/mobileAi ，页面 header 右上角的 **Relay** 指示器变绿即表示连接成功。

### 3. 连接手机

通过 USB 连接 Android 设备，页面显示"已连接"。

### 4. 配置 OpenClaw（在 `openclaw.json` 中添加）

```json5
{
  mcp: {
    servers: {
      "phone-agent": {
        command: "node",
        // 将 <PROJECT_ROOT> 替换为实际绝对路径
        args: ["<PROJECT_ROOT>/mcp-server/dist/server.js"],
        env: {
          // 可选：修改 WebSocket 端口（默认 7788）
          PHONE_AGENT_WS_PORT: "7788"
        }
      }
    }
  }
}
```

也可以通过 CLI 配置：

```bash
openclaw mcp set phone-agent --command node --args "<PROJECT_ROOT>/mcp-server/dist/server.js"
```

## Usage

直接描述任务，无需写代码：

> 打开微信，找到和张三的对话，发送一条"你好"

> 截个屏看看手机当前界面是什么

> 打开手机设置，查看系统版本信息

> 中断正在执行的任务

> 最近一次 Agent 任务的结果是什么

## 工具说明

| 工具 | 说明 | 主要参数 |
|------|------|---------|
| `run_agent_task` | 在手机上执行多步骤 AI 自动化任务 | `goal`（必填）、`timeoutMs`（默认 1200s）|
| `abort_task` | 中断当前正在运行的任务 | — |
| `take_screenshot` | 截取手机屏幕，返回 PNG 图像 | — |
| `get_device_status` | 查询设备型号、系统版本等信息 | — |
| `get_task_result` | 按 taskId 查询任务详细结果 | `taskId`（必填）、`includeSteps`（默认 true）|
| `get_latest_task` | 获取最近一次任务的执行结果 | — |

## 完整调用链

```
OpenClaw Agent
    │ stdio  JSON-RPC 2.0
    ▼
mcp-server/dist/server.js  (Node.js MCP Server)
    │ WebSocket  ws://localhost:7788
    ▼
浏览器页面 AiChatPanel  (McpRelayClient)
    │ McpServiceContext
    ▼
PlanResolveAgent / ReAct Agent
    │ Web ADB
    ▼
手机
```

## 故障排查

| 问题 | 解决方法 |
|------|---------|
| Relay 指示器为红色 | 确认 `npm start` 已在 mcp-server 目录运行 |
| 工具调用超时 | Agent 任务执行中，等待或调用 `abort_task` |
| 手机不响应 | 检查 ADB 连接，页面需显示设备"已连接" |
| 端口 7788 被占用 | 设置 `PHONE_AGENT_WS_PORT=7789` 并同步更新 MCP 配置 |
