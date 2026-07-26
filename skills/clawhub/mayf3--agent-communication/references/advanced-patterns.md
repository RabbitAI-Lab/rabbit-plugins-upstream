# Agent Communication — Advanced Patterns

## Circuit Breaker

Prevent cascading failures when a target agent is down:

```javascript
let failureCount = 0;
const MAX_FAILURES = 3;

async function communicateWithBreaker(sessionKey, message) {
  if (failureCount >= MAX_FAILURES) {
    throw new Error("Circuit breaker open — target may be down");
  }
  try {
    const result = await sessions_send({ sessionKey, message, timeoutSeconds: 30 });
    failureCount = 0; // Reset on success
    return result;
  } catch (error) {
    failureCount++;
    throw error;
  }
}
```

## Message Queuing

For high-volume or batched communication:

```javascript
const queue = [];

function enqueue(sessionKey, message) {
  queue.push({ sessionKey, message });
}

async function flush() {
  while (queue.length > 0) {
    const { sessionKey, message } = queue.shift();
    await sessions_send({ sessionKey, message, timeoutSeconds: 30 });
  }
}
```

## Async Pattern (Long-Running Tasks)

For operations that take > 120s:

```javascript
// Step 1: Fire-and-forget with task ID
const taskId = Date.now().toString(36);
await sessions_send({
  sessionKey: "agent:worker-agent:main",
  message: `TASK: ${taskId}\nWORK: process-large-dataset`,
  timeoutSeconds: 0
});

// Step 2: Poll for results later
async function checkResults(taskId) {
  const result = await sessions_send({
    sessionKey: "agent:worker-agent:main",
    message: `CHECK: ${taskId}`,
    timeoutSeconds: 30
  });
  return result;
}
```

## Integration Examples

### Research Coordination

Agent A delegates research to Agent B:

```javascript
const result = await sessions_send({
  sessionKey: "agent:research-agent:main",
  message: "请研究 OpenClaw Skills 的最佳实践",
  timeoutSeconds: 120
});
```

### Task Delegation to Todo Hub

```javascript
await sessions_send({
  sessionKey: "agent:todo-agent:main",
  message: `TODO_HUB: CREATE\nAGENT: ${currentAgent}\nTASK: 完成代码审查\nPRIORITY: 1`,
  timeoutSeconds: 30
});
```

### Result Sharing

```javascript
await sessions_send({
  sessionKey: "agent:reporting-agent:main",
  message: `REPORT: Daily summary\nCompleted: 5 tasks\nPending: 2 tasks`,
  timeoutSeconds: 10
});
```

## Error Handling

### Session Not Found
- Verify target agent is running: use `sessions_list`
- Check session key format: `agent:<name>:main`
- Check OpenClaw gateway logs

### Timeout
- Increase `timeoutSeconds` for complex tasks
- Check if target agent is overloaded
- Consider async pattern with polling

### Malformed Response
- Verify protocol version matches
- Add response validation
- Log raw response for debugging

## Best Practices

1. **Use standard protocols** — Agents like Todo Hub define their own message format (TODO_HUB: CREATE/READ/UPDATE). Follow them.
2. **Set appropriate timeouts** — Match timeout to operation complexity
3. **Handle responses gracefully** — Check for success/error indicators (✅/❌)
4. **Log communications** — `console.log("[Agent Comm] To:", sessionKey, "Msg:", message.substring(0,50))`
5. **Use descriptive messages** — Structured fields instead of free-form text

## Migration from `cross-group-messaging` (Legacy)

**Old (deprecated):**
```javascript
message({ action: "send", channel: "feishu", target: "oc_xxx", message: "内容" });
```

**New:**
```javascript
sessions_send({ sessionKey: "agent:<name>:main", message: "内容", timeoutSeconds: 30 });
```

**Benefits**: Bidirectional, synchronous, direct agent-to-agent, no Feishu dependency.
