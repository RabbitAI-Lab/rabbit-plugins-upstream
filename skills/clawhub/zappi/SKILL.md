---
name: zappi
description: Give an agent a prepaid Spark spend pot, not a wallet. Use when you need a hard spend cap, agent spend allowance, prepaid USDB pot, x402 pot open, Orchestra fund-from-any-chain, Hermes agent spend, L402 agent spend leash, NWC agent spend cap, or a dedicated tiny wallet where balance is the cap — same leash as NWC config.json / L402 / Hermes, not a competitor. Or when sparkbtcbot / a prompt / NWC config.json is not a real cap (an agent with a shell can edit the cap). Empty pot, spending stops. The agent holds the key. Zappi never holds the seed. Not a full Spark wallet and not Allowance (SMS/virtual-card checkout).
version: 1.0.37
license: MIT-0
metadata:
  openclaw:
    requires:
      bins:
        - node
        - curl
    homepage: https://pot.zappi.money/skill.json
  hermes:
    tags: [spark, spend-cap, allowance, prepaid-pot, usdb, nwc, l402, hermes]
    category: finance
---

# Zappi

A pot, not a wallet. You hold the Spark key. You fund the pot. You spend only what lands. When it is empty, it stops.

Free entry: https://pot.zappi.money/skill.json
Signer: https://pot.zappi.money/sign.mjs (also shipped in this skill folder as `sign.mjs`)
OpenClaw: `openclaw skills install @edogbeatz/zappi`
Hermes: `hermes skills install clawhub/zappi`
npx skills: `npx skills add https://pot.zappi.money`
Never POST the seed to Zappi. `/pay` is gone on purpose. `--open` is idempotent: the same sparkAddress returns the same pot and depositAddress.

sparkbtcbot is a full Spark wallet (agent can send everything). sparkbtcbot-proxy keeps the mnemonic on a server and caps via HTTP. Allowance@useallowance is a human-approved virtual card for checkout. This skill is the agent-spend leash: a prepaid USDB pot. Cap = empty wallet, not a prompt, not a config file, and not an SMS gate.

## Loop

1. Install @buildonspark/spark-sdk and @scure/bip39. This skill folder already includes `sign.mjs` (and `new-key.mjs`). If stdout is JSON with code deps, the packages are missing. `--help` prints flags[], codes[], nexts[], and neverPostSeed; it does not mint. If `sign.mjs` is missing, fallback: `node new-key.mjs --pull-signer` (JSON includes `signerHasNew` on live).
2. Make a Spark key locally: `node sign.mjs --file pot-ONCE.txt --new` (or `node new-key.mjs --file pot-ONCE.txt`). JSON is sparkAddress only (never the mnemonic). Writes the seed file mode 0600 and will not overwrite. `next` is open. Skip if you already have a key.
3. Open a pot (free, idempotent): `node sign.mjs --file pot-ONCE.txt --open` or `node new-key.mjs --file pot-ONCE.txt --open` (or `--open --sparkAddress spark1...`). GET only. Never POST the seed. Live `GET /deposit?sparkAddress=…` is 200 with depositAddress. The same sparkAddress always returns the same pot id and depositAddress; a re-run does not mint a new Orchestra address. Bare `/deposit` without sparkAddress is the $0.01 catalog probe — skip it. Optional `--sourceChain` / `--sourceAsset` (default base/USDC). Optional `--ref`. If USDB already landed, `next=spend`. If 402 (should not happen on the skill path), `fundDirect` still lets you send Spark USDB to sparkAddress.
4. Check: `node sign.mjs --file pot-ONCE.txt --check` (or `node new-key.mjs --file pot-ONCE.txt --check`). Optional `--expect spark1...`. `usdb` is null when empty. `next` is fund or spend. Never prints the seed.
5. If `next` is fund, send USDC (or the chosen source asset) to `depositAddress`. Orchestra lands USDB on your Spark address. Then `--check`.
6. Spend locally: `node sign.mjs --file pot-ONCE.txt --to spark1... --amount 0.25`
   or `node sign.mjs --file pot-ONCE.txt --invoice <invoice>`. Fallback: `node new-key.mjs --file pot-ONCE.txt --spend --to …` / `--invoice …` (needs --file first; auto-pulls sign.mjs if missing; empty pot returns code empty; overspend returns code insufficient. Neither sends). Never POSTs the seed.
7. When USDB is 0, spending stops. That is the cap.

`--amount` is human USDB (0.25 means 0.25 USDB). Use `--units` only for smallest units.

## Do not

- Do not ask the operator for their main wallet.
- Do not use `returnSeed`. The server will not mint a wallet.
- Do not print the mnemonic. Compare sparkAddress from --check, never seed words.
- Do not treat PayAI Bazaar crawls as users. This skill is the product.
