# OpenClaw Hooks Configuration — Agent Relay Push Webhook

Place this configuration in your `openclaw.json` under the `hooks` key.
Merge with any existing hooks config you have.

```json
{
  "hooks": {
    "enabled": true,
    "token": "<GENERATE_A_SECURE_RANDOM_TOKEN>",
    "path": "/hooks",
    "defaultSessionKey": "hook:relay",
    "allowRequestSessionKey": false,
    "allowedAgentIds": ["main"],
    "allowedSessionKeyPrefixes": ["hook:"],
    "transformsDir": "<YOUR_HOME>/.openclaw/hooks/transforms",
    "mappings": [
      {
        "id": "agent-relay",
        "match": {
          "path": "agent-relay"
        },
        "action": "agent",
        "agentId": "main",
        "wakeMode": "now",
        "name": "Agent Relay",
        "sessionKey": "hook:relay",
        "messageTemplate": "--- Message from User via Relay ({{message.id}}) ---\n{{message.text}}\n--- End relay ---\n\nProcess this as a full agent turn. Reply with:\n  relay send \"<reply>\"\n\nETIQUETTE: Short (1-3 lines), direct, no fluff, no sign-offs.",
        "deliver": false,
        "transform": {
          "module": "agent-relay.mjs"
        }
      }
    ]
  }
}
```

## What to fill in

1. **`token`** — Generate a secure random token (e.g., `openssl rand -hex 32`).
   This is the bearer token that authenticates webhook POSTs.
   Use a different token than your Gateway auth token.

2. **`transformsDir`** — Absolute path to your hooks/transforms directory.
   Example: `/home/agent/.openclaw/hooks/transforms`

3. **`messageTemplate`** — Update `<YOUR_WORKSPACE>` in the relay path.

## Caddy reverse proxy (or nginx)

If your gateway is behind a reverse proxy, add:

```
handle /hooks/* {
  reverse_proxy localhost:18789 {
    header_up Authorization "Bearer <YOUR_HOOK_TOKEN>"
  }
}
```

## Setting up the webhook in the Relay app

1. Open the Agent Relay app on your phone
2. Go to Connect → Instant delivery
3. Enter your webhook URL: `https://your-domain.com/hooks/agent-relay`
4. Optionally set a shared secret (arrives as `X-Webhook-Secret` header)
5. Tap "Send test ping" to verify connectivity
6. You should get back `{"ok":true}`

## Inbox fallback (recommended)

Even with push webhooks working, set up inbox polling as a fallback.
Add a cron job that runs `scripts/poll-inbox-fallback` every 2 minutes.
Failed webhook deliveries are retried by the relay server, then if still failing,
left in the inbox for the fallback poller to catch.
