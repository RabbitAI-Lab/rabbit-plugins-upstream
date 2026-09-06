# weixin-debounce20s

**Type:** setup/enabler skill — when the agent runs it, 20s WeChat burst debouncing is
installed and verified on this OpenClaw.

## How it gives you the capability

Installing this skill alone does not add transport behavior. Running it (the agent follows
`SKILL.md`) performs the real enablement automatically:

1. Ensures the WeChat channel is the ClawBot fork plugin
   (`clawhub:@yechang1450/openclaw-weixin-clawbot`, which contains the 20s debounce merge
   + quote injection), replacing the stock npm plugin if needed;
2. Sets `messages.inbound` window to `20000` ms;
3. Restarts the gateway;
4. Verifies via logs (`debounce: buffered … windowMs=20000`) and a live burst test.

Idempotent: on an already-configured machine it only verifies.

## Usage (fresh machine)

```bash
openclaw skills install @yechang1450/weixin-debounce20s
# then tell ClawBot (WeChat or CLI): 启用防抖 / 防抖没生效
```

The agent asks before installing the plugin package if approval is required.

## Trigger words

启用防抖 / 防抖没生效 / 连发合并 / debounce.

Files: `SKILL.md` (execution), `README.md` / `README-zh.md`, `LICENSE` (MIT).
