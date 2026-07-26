# true402-token-safety — OpenClaw skill

Rug-check any Base token before trading, from inside [OpenClaw](https://openclaw.ai): a **real buy/sell honeypot simulation** (proves the token is sellable, not just a static scan) plus liquidity and ownership checks, returning one `AVOID / CAUTION / OK` verdict.

Powered by [true402.dev](https://true402.dev) — pay-per-call over [x402](https://x402.org), no accounts, no API keys. The first few checks each day are **free, no wallet needed**.

## Install

```bash
openclaw skills install true402-token-safety
```

or copy this directory to `~/.openclaw/workspace/skills/true402-token-safety/`.

## Use

Ask your agent things like:

> "Is 0x532f…42E4 safe to buy?"
> "Rug-check this token before you snipe it."

The agent runs `npx -y @true402.dev/rugcheck 0x…` and gates on the verdict (non-zero exit on AVOID).

## Optional: unlimited checks

Set `PAYER_PRIVATE_KEY` to a Base wallet holding a little USDC to pay ~$0.005–0.01 per check over x402 (gas sponsored — the wallet needs no ETH). The key signs locally and is never sent anywhere; the client refuses to sign any single charge above **$0.10**. Without a key, the free daily trial applies.

## Links

- Live in-browser check: https://true402.dev/check
- API reference: https://true402.dev/docs/api
- OpenAPI: https://true402.dev/openapi.json
- MCP server (all stalls as agent tools): `npx @true402.dev/mcp-server`

## License

MIT-0 (per ClawHub policy).
