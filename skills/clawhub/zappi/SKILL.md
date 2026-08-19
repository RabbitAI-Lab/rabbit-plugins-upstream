---
name: zappi
description: Give an agent a prepaid Spark spend pot, not a wallet. Use when you need a hard spend cap, agent spend allowance, prepaid USDB pot, x402 pot open, Orchestra fund-from-any-chain, or when sparkbtcbot / a prompt / NWC config.json is not a real cap (an agent with a shell can edit the cap). Empty pot, spending stops. The agent holds the key. Zappi never holds the seed. Not a full Spark wallet and not Allowance (SMS/virtual-card checkout).
version: 1.0.10
license: MIT-0
metadata:
  openclaw:
    requires:
      bins:
        - node
        - curl
    homepage: https://pot.zappi.money/skill.json
  hermes:
    tags: [spark, spend-cap, allowance, prepaid-pot, usdb]
    category: finance
---

# Zappi

A pot, not a wallet. You hold the Spark key. You fund the pot. You spend only what lands. When it is empty, it stops.

Free entry: https://pot.zappi.money/skill.json
Signer: https://pot.zappi.money/sign.mjs
OpenClaw: `openclaw skills install @edogbeatz/zappi`
Hermes: `hermes skills install clawhub/zappi`
Never POST the seed to Zappi. `/pay` is gone on purpose.

Do not install from https://pot.zappi.money/SKILL.md until `/.well-known/agent-skills/index.json` is live. That file is stale (no new-key.mjs). This ClawHub folder is the skill.

sparkbtcbot is a full Spark wallet (agent can send everything). sparkbtcbot-proxy keeps the mnemonic on a server and caps via HTTP. Allowance@useallowance is a human-approved virtual card for checkout. This skill is the agent-spend leash: a prepaid USDB pot. Cap = empty wallet, not a prompt, not a config file, and not an SMS gate.

## Loop

1. Install @buildonspark/spark-sdk and @scure/bip39, then run this skill new-key.mjs. If stdout is JSON with code deps, the packages are missing.
2. Make a Spark key locally: node new-key.mjs --file pot-ONCE.txt
   JSON stdout is ok/mode/sparkAddress/file/open/signer. `open` is the /deposit URL with your sparkAddress filled in. Writes the seed file mode 0600 and will not overwrite. Never print the file. Skip if you already have one.
3. Download the signer: `curl -fsSL https://pot.zappi.money/sign.mjs -o sign.mjs`
4. Check the address and whether USDB landed: `node new-key.mjs --file pot-ONCE.txt --check` (or `node sign.mjs --file pot-ONCE.txt --check` after you download the signer). Optional `--expect spark1...` refuses to continue if the file opens a different wallet. JSON is ok/mode/sparkAddress/usdb/balances/next, same USDB shape as the live signer. `usdb` is null when the pot is empty. `next` is open (after mint), fund (empty), or spend (USDB landed). Never prints the seed.
5. Open a pot (paid step, $0.01 USDC on Base): GET the `open` URL from stdout (or `https://pot.zappi.money/deposit?sparkAddress=spark1...&sourceChain=base&sourceAsset=USDC`).
6. Pay the 402, retry, get `depositAddress`.
7. Send USDC (or the chosen source asset) to `depositAddress`. Orchestra lands USDB on your Spark address.
8. Spend locally: `node sign.mjs --file pot-ONCE.txt --to spark1... --amount 0.25`
   or `node sign.mjs --file pot-ONCE.txt --invoice <invoice>`
9. When USDB is 0, spending stops. That is the cap.

`--amount` is human USDB (0.25 means 0.25 USDB). Use `--units` only for smallest units.

## Do not

- Do not ask the operator for their main wallet.
- Do not use `returnSeed`. The server will not mint a wallet.
- Do not print the mnemonic. Compare sparkAddress from --check, never seed words.
- Do not treat PayAI Bazaar crawls as users. This skill is the product.
