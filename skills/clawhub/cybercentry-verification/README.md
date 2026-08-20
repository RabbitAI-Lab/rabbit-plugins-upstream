# Cybercentry Verification — ClawHub skill

The ClawHub package for [Cybercentry](https://centry.cybercentry.co.uk):
security verification for wallets, tokens, smart contracts, AI agents and web
applications, paid per call in USDC over x402.

- `SKILL.md` — the instructions an OpenClaw agent loads
- `skill-card.md` — the listing card shown on ClawHub

## Publishing

```bash
npm i -g clawhub
clawhub login --device
clawhub skill publish . \
  --slug cybercentry-verification \
  --name "Cybercentry Verification" \
  --tags "latest,x402,mcp,security,blockchain,wallet" \
  --changelog "..." \
  --dry-run
```

Drop `--dry-run` to publish for real.

## Keeping it honest

`SKILL.md` names ten paid tools and a $1.00 price. Both come from the live
catalogue at `lib/catalog.ts` in the seller app, and `list_services` is the
authoritative source at runtime — the skill says so, so an agent that reads it
will not act on a stale price here. If the catalogue changes, republish.
