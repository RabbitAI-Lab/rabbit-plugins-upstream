# Zappi

A pot, not a wallet. Prepaid Spark USDB spend cap for AI agents.

The agent holds the key. Zappi never holds the seed. Empty pot, spending stops.

## Install

OpenClaw / ClawHub:

```
openclaw skills install @edogbeatz/zappi
```

Hermes:

```
hermes skills install clawhub/zappi
```

agentskills / `npx skills add`:

```
npx skills add edogbeatz/zappi-skill
```

Live skill JSON: https://pot.zappi.money/skill.json

Do not `npx skills add https://pot.zappi.money/SKILL.md` until well-known discovery is live. That file is stale.

## Loop

1. `node new-key.mjs --file pot-ONCE.txt` (prints sparkAddress and an `open` deposit URL)
2. Open a pot at that `open` URL ($0.01 USDC on Base)
3. Fund the deposit address. `node new-key.mjs --file pot-ONCE.txt --check` reports `usdb` (null if empty). Spend with `/sign.mjs`.

Do not POST the seed to Zappi. Do not use `returnSeed`. Cap = empty wallet.

This folder is the ClawHub skill. The pot server stays private at edogbeatz/zappi-pot.
