# Install Receipt in OpenClaw

Receipt uses OpenClaw's native remote MCP support. No custom plugin is required.

```bash
openclaw mcp set receipt '{"url":"https://receiptprotocol.com/mcp","transport":"streamable-http","auth":"oauth","supportsParallelToolCalls":false}'
openclaw mcp tools receipt --include 'receipt.*'
openclaw mcp login receipt
openclaw mcp doctor receipt --probe
```

Run login in a normal shell, not the OpenClaw TUI, and close old callback/error tabs first.
Complete OAuth in the browser. Use only the current callback, copy the fresh value between `code=`
and `&state=`, then immediately run `openclaw mcp login receipt --code '<fresh-code>'` in the same
shell. Codes are single-use and expire after 10 minutes. Never share a callback URL or code.

Do not add a static `Authorization` header or copy provider keys
into OpenClaw. Set Receipt to ask every purchase, with a per-call limit of at most $1 and a daily
limit of at most $5. Add no automatic seller rules.

Verify that OpenClaw lists exactly the eight universal tools in `SKILL.md`. If any seller-specific
tool appears, stop and remove that connection.
