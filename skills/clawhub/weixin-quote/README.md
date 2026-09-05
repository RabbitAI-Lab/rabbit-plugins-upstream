# weixin-quote

**Type:** setup/enabler skill — when the agent runs it, WeChat "quote-as-context" is
installed and verified on this OpenClaw (quoting a bot reply injects the full quoted text).

## How it gives you the capability

Installing alone adds nothing; the agent following `SKILL.md` performs real enablement:

1. Ensures the WeChat channel is the ClawBot fork plugin
   (`clawhub:@yechang1450/openclaw-weixin-clawbot`, which records server message ids and
   resolves quotes by id proximity ≤1000), replacing the stock plugin if needed;
2. Restarts the gateway;
3. Verifies via logs: `[send-resp]` on send and `[quote-hit] method=id …` when you quote a
   fresh bot reply.

Idempotent: on an already-configured machine it only verifies.

## Usage (fresh machine)

```bash
openclaw skills install @yechang1450/weixin-quote
# then tell ClawBot: 启用引用 / 引用没生效
```

The agent asks before installing the plugin package if approval is required.

## Trigger words

启用引用 / 引用没生效 / 引用追问 / quote.

Files: `SKILL.md` (execution), `README.md` / `README-zh.md`, `LICENSE` (MIT).
