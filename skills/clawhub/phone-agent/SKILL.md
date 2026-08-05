---
name: phone-agent
description: 通过本地 MCP Server 调用 Mobile AI Agent，在已连接的手机上执行自动化任务（截图、操作手机、查询任务状态等）
tools:
  - mcp__phone-agent__run_agent_task
  - mcp__phone-agent__abort_task
  - mcp__phone-agent__take_screenshot
  - mcp__phone-agent__get_device_status
  - mcp__phone-agent__get_task_result
  - mcp__phone-agent__get_latest_task
---

# Phone Agent Skill

通过本地 MCP Server 桥接浏览器中运行的 Mobile AI Agent，让 OpenClaw / Qoder 可以远程控制手机——无需额外代码，直接用自然语言描述任务即可。

## 前提条件

1. **启动本地 MCP Server**：
   ```bash
   cd <项目根目录>/mcp-server
   npm install      # 首次运行需安装依赖
   npm run build    # 编译 TypeScript
   npm start        # 启动服务（监听 stdio + WebSocket :7788）
   ```

2. **打开 Mobile AI Agent 页面**（https://mobile-ai-use.com/mobileAi）  
   页面 header 右上角的 **Relay** 指示器变绿即表示连接成功。

3. **连接手机**：通过 USB 连接 Android 设备，页面显示"已连接"。

## 配置 OpenClaw（在 `openclaw.json` 中添加）

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

## 配置 Qoder（在 `.qoder/mcp.json` 或全局 MCP 配置中添加）

```json
{
  "mcpServers": {
    "phone-agent": {
      "command": "node",
      "args": ["<PROJECT_ROOT>/mcp-server/dist/server.js"],
      "env": {
        "PHONE_AGENT_WS_PORT": "7788"
      }
    }
  }
}
```

## 使用方式

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
OpenClaw / Qoder Agent
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
