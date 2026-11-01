# Security and Permissions

Resources use `action(target)`. Evaluation order is `deny`, then `ask`, then `allow`. `deny` beats `ask`. `ask` beats `allow`.

Change rules in `/permissions` or `/config`. Edit `~/.gemini/antigravity-cli/settings.json` only for a file-level change. Defaults and the v1.4.4 sandbox fallback: `references/command-reference.md`.

## Presets

- `request-review` (default): prompt for write, bash, web, and MCP unless an allow rule matches.
- `proceed-in-sandbox`: run a terminal command without a prompt when the sandbox is on and the command stays inside it. v1.4.4+: behaves like `request-review` when the sandbox is unavailable.
- `always-proceed`: run commands, web, and MCP without a prompt unless an ask or deny rule matches. Trusted, low-risk context only.
- `strict`: prompt before every tool action, including file reads, even when an allow rule matches.

Deny rules apply in every mode. `auto` mode is Preview (v1.3.5+ macOS/Linux, v1.4.4+ Windows), needs the terminal sandbox, and is not available for business or enterprise accounts.

## Sandbox

```json
{
  "enableTerminalSandbox": true
}
```

Linux uses namespace/cgroup isolation. macOS uses a native sandbox policy. Windows uses AppContainer-style isolation.

With the sandbox on, a prompt can offer one run without sandbox restrictions. With it off, a prompt can offer one run inside the sandbox.

## Risk

- Unfamiliar repo: `request-review` or `strict`.
- `--dangerously-skip-permissions`: only when the user explicitly requests it and the workspace is trusted.
- Repeated bounded automation: `proceed-in-sandbox`, not `always-proceed`.
- Widen filesystem, URL, or MCP access only when the user intent needs it.
- Deny sensitive paths, production secrets, destructive commands, and remote endpoints that must stay untouched.
