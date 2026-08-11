---
name: mobile-agent
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

# Mobile Agent Skill

Bridges the Mobile AI Agent running in the browser via a local MCP Server, allowing OpenClaw to remotely control a real phone — no extra code needed, just describe the task in natural language.

## When to Use This Skill

- The user asks to operate a real phone (open apps, tap, input, swipe)
- The user asks to view the current phone screen (screenshot)
- The user asks to query device information (model, OS version)
- The user asks to run a multi-step AI automation task on the phone
- The user asks to query/abort a running Agent task

## Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────┐
│                        External AI Agent                             │
│              (OpenClaw / Qoder / Claude Desktop / Chrome AI)         │
└───────────┬──────────────────────────────────────────┬───────────────┘
            │ Channel A: stdio JSON-RPC 2.0            │ Channel B: document
            ▼                                          │   .modelContext
┌───────────────────────────────┐                      │   .callTool()
│  mcp-server/dist/server.js    │                      ▼
│  (Node.js McpServer)          │      ┌───────────────────────────────┐
│  6 Tools registered on stdio  │      │   Chrome WebMCP Runtime       │
└───────────┬───────────────────┘      │   (#enable-webmcp-testing)    │
            │ WebSocket                └───────────────┬───────────────┘
            │ ws://localhost:7788                      │ execute()
            ▼                                          ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    Browser Page (Mobile AI Use)                       │
│   McpRelayClient (Channel A)    WebMcpService (Channel B)            │
│                └────────────┬────────────┘                           │
│                             ▼  McpServiceContext (shared)             │
│            Plan-and-Resolve Agent / ReAct Agent                      │
└─────────────────────────────┬────────────────────────────────────────┘
                              │  Web ADB
                              ▼
┌──────────────────────────────────────────────────────────────────────┐
│                       Android / iOS Device                           │
└──────────────────────────────────────────────────────────────────────┘
```

## Installation/Setup

### 1. Start the Local MCP Server

```bash
cd <project-root>/mcp-server
npm install      # Install dependencies on first run
npm run build    # Compile TypeScript
npm start        # Start the server (listens on stdio + WebSocket :7788)
```

### 2. Open the Mobile AI Agent Page

Navigate to https://mobile-ai-use.xyz/mobileAi — the **Relay** indicator in the top-right corner of the page header turning green indicates a successful connection.

### 3. Connect the Phone

Connect an Android device via USB; the page should display "Connected".

### 4. Configure OpenClaw (add to `openclaw.json`)

```json5
{
  mcp: {
    servers: {
      "mobile-agent": {
        command: "node",
        // Replace <PROJECT_ROOT> with the actual absolute path
        args: ["<PROJECT_ROOT>/mcp-server/dist/server.js"],
        env: {
          // Optional: change the WebSocket port (default 7788)
          PHONE_AGENT_WS_PORT: "7788"
        }
      }
    }
  }
}
```

You can also configure via CLI:

```bash
openclaw mcp set mobile-agent --command node --args "<PROJECT_ROOT>/mcp-server/dist/server.js"
```

## Usage

Simply describe the task in natural language — no coding required:

> Open WeChat, find the conversation with Zhang San, and send a "Hello" message

> Take a screenshot to see what's currently on the phone screen

> Open phone Settings and check the system version information

> Abort the currently running task

> What was the result of the most recent Agent task

## Tool Reference

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `run_agent_task` | Run a multi-step AI automation task on the phone | `goal` (required), `timeoutMs` (default 1200s) |
| `abort_task` | Abort the currently running task | — |
| `take_screenshot` | Capture the phone screen, returns a PNG image | — |
| `get_device_status` | Query device model, OS version, and other info | — |
| `get_task_result` | Query detailed task results by taskId | `taskId` (required), `includeSteps` (default true) |
| `get_latest_task` | Get the result of the most recent task | — |

## Full Call Chain

```
OpenClaw Agent
    │ stdio JSON-RPC 2.0
    ▼
mcp-server/dist/server.js  (Node.js MCP Server)
    │ WebSocket ws://localhost:7788
    ▼
Browser Page AiChatPanel (McpRelayClient)
    │ McpServiceContext
    ▼
PlanResolveAgent / ReAct Agent
    │ Web ADB
    ▼
Phone
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Relay indicator is red | Confirm `npm start` is running in the mcp-server directory |
| Tool call times out | An Agent task is still running — wait or call `abort_task` |
| Phone not responding | Check the ADB connection; the page should show the device as "Connected" |
| Port 7788 is occupied | Set `PHONE_AGENT_WS_PORT=7789` and update the MCP configuration accordingly |
