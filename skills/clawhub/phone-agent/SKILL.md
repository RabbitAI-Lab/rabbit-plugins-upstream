---
name: phone-agent
description: >-
    Control a real phone from OpenClaw via a local MCP relay. Use when the user asks to
    operate a phone (open apps, tap, input, take screenshots), run an AI automation task
    on a connected Android/iPhone device, check the current phone screen or device info,
    or query/abort a running phone agent task. WARNING: This skill can modify device state
    and perform actions on behalf of the user — see the Safety Notice section before use.
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

## ⚠️ 安全须知 —— 使用前必读

**本技能会在真实设备上执行实际操作。** Agent 可以打开应用、点击界面元素、输入文本、发送消息、更改设置，以及运行多步骤自动化流程——这些操作可能不可逆地改变设备状态或产生现实后果。

### 潜在影响

| 操作类别 | 示例 | 风险等级 |
|---------|------|--------|
| **消息发送** | 代发微信 / 短信 / 邮件 | 🔴 高 —— 接收方会实际收到消息 |
| **购买与支付** | 在应用中下单、确认付款 | 🔴 高 —— 可能产生实际费用 |
| **设置变更** | 开关 Wi-Fi、蓝牙、系统偏好设置 | 🟡 中 —— 设备行为将发生变化 |
| **应用数据** | 删除联系人、清除缓存、移除文件 | 🟡 中 —— 数据丢失可能不可恢复 |
| **导航浏览** | 打开应用、搜索、浏览内容 | 🟢 低 —— 本质为只读操作 |

### 用户同意要求

1. **明确确认**：在执行任何可能发送消息、触发购买或修改关键设置的任务之前，Agent **必须**向用户确认操作意图并等待明确批准。
2. **任务范围清晰**：用户应精确描述任务。模糊的指令（如“清理我的手机”）可能导致非预期操作。
3. **建议在旁监督**：首次使用或高风险操作时，请在旁观察 Agent 通过投屏实时执行的过程。
4. **可随时中止**：如 Agent 开始非预期操作，可随时调用 `abort_task` 立即停止。

### AI Agent 调用本技能的最佳实践

- 在调用 `run_agent_task` 执行涉及发送消息、购买、删除数据或更改系统设置的目标之前，**务必先征得用户确认**。
- **优先使用只读操作**：先用 `take_screenshot` 和 `get_device_status` 检查当前状态，再执行写入操作。
- **涉及金融交易或不可逆操作的失败任务，未经用户重新确认不得自动重试**。

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
| `run_agent_task` | ⚠️ **写入** — 在手机上执行多步骤 AI 自动化任务（可能修改设备状态） | `goal`（必填）、`timeoutMs`（默认 1200s）|
| `abort_task` | 中断当前正在运行的任务 | — |
| `take_screenshot` | 只读 — 截取手机屏幕，返回 PNG 图像 | — |
| `get_device_status` | 只读 — 查询设备型号、系统版本等信息 | — |
| `get_task_result` | 只读 — 按 taskId 查询任务详细结果 | `taskId`（必填）、`includeSteps`（默认 true）|
| `get_latest_task` | 只读 — 获取最近一次任务的执行结果 | — |

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
