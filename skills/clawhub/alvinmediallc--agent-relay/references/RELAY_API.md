# Agent Relay API Reference

Agent Relay is a bridge between an AI agent and its human user's phone. With it you can:

- Send messages that appear in the user's chat and push a notification
- Read messages the user sends back
- Push standalone notifications (e.g. reminders) without adding to the chat

## 1. Connecting

Two things needed:

- **Base URL**: `<BASE_URL>/api`
  - Dev: `https://<dev-subdomain>.replit.dev/api`
  - Prod: `https://<app>.replit.app/api`
- **API key**: Created in the Agent Relay app, shown once. Send as `Authorization: Bearer <KEY>` header on every request.

### Option A — MCP (preferred for MCP clients)
Connect to `<BASE_URL>/mcp` as a Streamable HTTP MCP server with the Bearer header. Three tools: `send_message`, `get_user_messages`, `notify_user`.

### Option B — REST

| Action | Method & path | Body |
|--------|--------------|------|
| Confirm connection | `GET /relay/whoami` | — |
| Read new messages | `GET /relay/inbox` | — |
| Send a message | `POST /relay/messages` | `{ "text": "..." }` |
| Push a notification | `POST /relay/notify` | `{ "title": "...", "body": "..." }` |

### Option C — Push (webhook)

When Instant delivery is enabled, the server POSTs each new message to a configured webhook address immediately.

**Payload format** (Content-Type: application/json):

```json
{
  "source": "agent-relay",
  "agentName": "My Agent",
  "message": {
    "id": "msg_123",
    "text": "Can you check the deploy?",
    "createdAt": "2026-06-29T12:00:00.000Z",
    "attachment": {
      "url": "https://…",
      "type": "image/png",
      "name": "screenshot.png"
    }
  }
}
```

- `attachment` is `null` when the message has no file
- `url` is a time-limited download link
- Test ping adds `"test": true` and a placeholder message
- Shared secret (if set) arrives in `X-Webhook-Secret` header

**Behavior:**
- HTTPS only, public host required
- Respond 2xx quickly; real work afterward
- Non-2xx or timeout (~10s) = failure, retried over ~30s
- Failed deliveries remain in `GET /relay/inbox`
- At-least-once delivery — deduplicate by `message.id`
- Polling inbox remains a safe fallback

## 2. Capabilities

### Send a message
- MCP: `send_message` — input `{ text }`
- REST: `POST /relay/messages` — body `{ "text": "..." }`

Text appears in chat and triggers push notification.

### Read messages
- MCP: `get_user_messages` — no input
- REST: `GET /relay/inbox`

Returns unseen messages. Each message returned only once. Images delivered inline (base64 over MCP); other files as download URL.

### Push notification
- MCP: `notify_user` — input `{ title, body }`
- REST: `POST /relay/notify` — body `{ "title": "...", "body": "..." }`

Push notification only — no chat message. Use for reminders/nudges.

## 3. Behavior Guidelines

- Check for new messages at startup and periodically while active
- Each message arrives once — persist what you need
- Use message for conversation, notification for quick heads-up
- Keep it short — phone screen
- Never put API key in messages or notifications
- 401 = key missing/wrong/rotated — ask user for fresh key
