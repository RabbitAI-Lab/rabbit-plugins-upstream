# Channel and routing checklist

Use this checklist for each OpenClaw agent/channel binding.

## Account

- Account ID: `<non-secret-id>`
- Platform: `<discord|telegram|slack|other>`
- Owning agent: `<agent-id>`
- Intended channels or chats: `<allow-list>`
- Credential source: `<interactive|environment|secret-file>`
- Credential owner and rotation date: `<operator/date>`

Do not record the credential value here.

## Least privilege

- Bot is present only in required servers/workspaces.
- Channel access is allow-listed.
- Administrative, member-management, and unrelated message-history permissions
  are disabled.
- Privileged deployment or payment tools are unavailable to public intake.
- The agent workspace contains only the context required for its role.

## Configure

```bash
openclaw channels add
openclaw channels list
openclaw agents bind --agent <agent-id> --bind <channel>:<account-id>
openclaw agents bindings
openclaw config validate
```

## Verify

- A harmless test message reaches exactly one expected agent.
- The reply returns through the expected account.
- An unauthorized channel cannot invoke the agent.
- Secrets do not appear in the config output, logs, workspace, or shell history.
- `openclaw channels status --deep` reports the account healthy.
