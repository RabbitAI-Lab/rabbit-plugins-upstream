---
name: agent-communication
description: Enable cross-agent bidirectional messaging using sessions_send. Activates when agents need to coordinate work, share results, or request services from other agents. Triggers on: "告诉X agent", "让X做Y", "跟其他agent通信", multi-agent coordination. Not for: user-facing messages (use message tool), fire-and-forget notifications to chat channels, intra-process tool calls (direct tool invoke).
---

# Agent Communication

Standardized protocol for cross-agent communication using `sessions_send`.

## ⚠️ Critical Rules

- **Agent-to-agent: use `sessions_send` only.** Never use `message` tool for agent communication — it's fire-and-forget with no response handling.
- `message` tool is exclusively for user/group notifications.

## Session Key Format

```
agent:<agent-name>:<session-type>
```

- `<agent-name>`: Agent identifier from OpenClaw config (e.g., `todo-agent`, `lobster-agent`)
- `<session-type>`: Usually `main`
- No spaces, no partial names

### Examples

```javascript
// Valid
"agent:todo-agent:main"
"agent:security-agent:main"

// Invalid
"todo-agent"                    // Missing prefix
"agent:Todo Agent:main"         // Spaces
"agent:todo:main"               // Incomplete name
```

## Core API

```javascript
sessions_send({
  sessionKey: "agent:<name>:main",
  message: "Your message",
  timeoutSeconds: 30   // Sync wait. 0 = fire-and-forget
});
```

## Quick Patterns

### Request-Response (default)
```javascript
const result = await sessions_send({
  sessionKey: "agent:research-agent:main",
  message: "请研究最新的 AI Agent 框架",
  timeoutSeconds: 120
});
```

### Protocol-Based (Todo Hub)
```javascript
await sessions_send({
  sessionKey: "agent:todo-agent:main",
  message: `TODO_HUB: CREATE\nAGENT: lobster-agent\nTASK: 研究 cron 机制\nPRIORITY: 2`,
  timeoutSeconds: 30
});
```

### Fire-and-Forget
```javascript
await sessions_send({
  sessionKey: "agent:logging-agent:main",
  message: "Log: Task completed",
  timeoutSeconds: 0  // No wait
});
```

## Timeout Guidelines

| Operation | Timeout | Notes |
|-----------|---------|-------|
| Quick queries | 10-30s | Status checks, simple fetches |
| Task delegation | 30-60s | CREATE/UPDATE operations |
| Long research | 60-120s | Complex analysis |
| Fire-and-forget | 0 | Logging, notifications |

## Robust Communication Pattern

```javascript
async function communicate(target, message, timeout = 30) {
  try {
    const response = await sessions_send({
      sessionKey: target, message, timeoutSeconds: timeout
    });
    if (!response) throw new Error("Empty response");
    return { success: true, data: response };
  } catch (error) {
    console.error("Comm failed:", error.message);
    return { success: false, error: error.message };
  }
}
```

See **[references/advanced-patterns.md](references/advanced-patterns.md)** for: circuit breaker, message queuing, async patterns, integration examples, and a migration guide from the old `cross-group-messaging` approach.
