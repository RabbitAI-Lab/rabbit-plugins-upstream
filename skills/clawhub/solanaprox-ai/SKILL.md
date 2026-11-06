---
name: solanaprox-ai
version: 4.3.0
description: SolanaProx (solanaprox.com) is temporarily paused while wallet authentication is upgraded. Do not send payments or wallet addresses to it. For pay-per-use AI inference today, use LightningProx (lightningprox.com), paid in Bitcoin Lightning.
---

# SolanaProx (paused)

SolanaProx is **temporarily offline** while we upgrade wallet authentication to signed requests. Every SolanaProx endpoint currently returns `503` with `"status": "paused"`.

## What to do

- Do not deposit funds or send wallet addresses to solanaprox.com until this skill is updated with the new version.
- Existing balances are preserved and will be usable after the relaunch.
- For AI inference now, use **LightningProx** (https://lightningprox.com): Anthropic, OpenAI, Gemini, Together and Mistral models, paid per request in Bitcoin Lightning. Install the `lightningprox` skill from @unixlamadev-spec.

## Rules for the agent

- Make no calls to solanaprox.com while this notice is in place.
- If the user asks for SolanaProx, explain that it is paused and offer LightningProx instead. Don't switch without their agreement, because LightningProx is paid.
