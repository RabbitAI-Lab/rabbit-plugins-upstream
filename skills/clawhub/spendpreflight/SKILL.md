---
name: spendpreflight
description: Preflight an x402 payment or screen a public payee with SpendPreflight. Use only preflight_payment and check_payee. Defaults to offline hold with no signer; paid API calls require explicit human approval.
metadata:
  openclaw:
    requires:
      bins: [node, npm]
    homepage: https://docs.spendpreflight.com/mcp/
---

# SpendPreflight

Use exactly two existing SpendPreflight MCP tools: `preflight_payment` for an actual x402 challenge/cart, or `check_payee` for a public wallet, name or domain. Do not select other tools as a fallback.

The skill is free and licensed MIT-0. **SpendPreflight is our external paid x402 API**, paid in USDC; each call can incur a separate fee. Check the current quoted fee and payment requirements before requesting a paid call. A trial is not assumed or automatically requested. API pricing and service terms are unchanged by this skill.

## Default: offline hold, no signer

The included helper uses the published `spendpreflight@0.4.0` SDK Spend Policy without a remote transport. It never makes a network request, signs, pays, loads credentials or authorizes payment. A valid local policy preview remains **hold** because remote evidence is absent. `check_payee` offline returns unknown screening status, never a fabricated sanctions non-match.

Read [usage and one offline example](references/usage.md). Run the helper only on public identifiers and supplied payment requirements. Never provide wallet keys, seed phrases, tokens, customer lists or private URLs. Do not install dependencies or configure accounts without the operator's permission.

## When a human requests an online check

1. Use an already configured SpendPreflight MCP connection at `https://api.spendpreflight.com/mcp`. If no connection or suitably bounded x402 transport exists, return hold and explain what is missing. This skill supplies no signer or payment client.
2. Choose `preflight_payment` for a supplied, actual challenge/cart. Preserve the exact selected amount, network, asset, payee and resource. Apply SDK 0.4.0 Spend Policy locally first; a local block stops this workflow. Use `check_payee` instead for standalone public `address`, `domain` and/or `name` screening. Do not invent a challenge for a payee check.
3. Before any call that may spend, show the human the selected tool, public input, service recipient, network/asset, exact quoted fee or hard maximum, and whether a trial applies. Obtain explicit approval for that call and fee. A previous approval or a policy preview is not approval for a new charge. If fee/recipient/input changes, obtain a new approval. The external transport must enforce the approved cap before signing. Without that capability, hold.
4. Invoke only the chosen tool once. Do not auto-retry a failed, timed-out or unknown paid call. Preserve unknown outcomes and ask for direction only if a new action is needed.
5. Report the actual result and its timestamp, reasons, scope and unknowns. `hold` needs human review; `block` means stop. An `allow` is a screening decision within the approved policy, **not permission to sign or pay the target merchant**. Any target payment is a separate human-authorized action outside this skill.

Payee non-match is not sanctions clearance, identity verification or a safety guarantee. Preflight does not establish paid delivery or perform the separate wallet-binding check. Do not claim receipt signatures were verified unless independent verification was actually performed.

Only the skill files are MIT-0. The separate SDK retains its own license, and SpendPreflight's API pricing and terms remain in force.
