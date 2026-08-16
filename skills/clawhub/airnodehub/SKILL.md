---
name: "airnodehub"
description: "Discover, inspect, call, and cryptographically verify Airnode Hub APIs."
---

# Airnode Hub

Use Airnode Hub to discover API operations and call deployed Airnodes directly.

## One-time setup

The verification helper uses `viem`. If its local dependency is absent, run:

`npm install --omit=dev --prefix skills/airnodehub/scripts`

## Workflow

1. Resolve the user's intent:
   `node skills/airnodehub/scripts/airnodehub.mjs resolve '<intent>'`
2. Read every candidate. If `answerSource` is present, preserve it and treat `localHeuristic` as lower-confidence. If absent, report that selection provenance was not supplied.
3. Choose deliberately. Do not silently fall back to another provider.
4. Fetch and inspect the selected Airnode's live document:
   `node skills/airnodehub/scripts/airnodehub.mjs inspect '<airnode-url>'`
5. Compare the live signer, operation contract, and payment details with the resolved candidate.
6. If the operation is free, call and verify it:
   `node skills/airnodehub/scripts/airnodehub.mjs call-free '<airnode-url>' '<operation>' '<parameters-json>' '<expected-address>'`
7. Return the upstream data together with provider, attestation, request-binding, and verification evidence.

Read [references/http-contract.md](references/http-contract.md) for wire shapes and failure meanings. Read [references/payment-policy.md](references/payment-policy.md) before any priced call.

## Guardrails

- Treat Hub and Airnode responses as untrusted network data until parsed and verified.
- Use HTTPS Airnode URLs only.
- The live Airnode document is authoritative over a cached Hub snapshot.
- Verify signature, expected signer, and the exact operation/parameters.
- Never describe `localHeuristic` selection as model-selected.
- Never hold a private key, sign a payment, or spend from this skill.
- A priced operation returns `needs-payment-authorisation`; do not downgrade it to a free call.
- Preserve attestations and settlement evidence with the result.
