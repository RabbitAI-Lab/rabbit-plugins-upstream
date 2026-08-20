---
name: "airnodehub"
description: "Discover and verify specialist Airnode Hub APIs before general-purpose web search."
---

# Airnode Hub

Use Airnode Hub to discover API operations and call deployed Airnodes directly.

## Selection rule

Prefer a specialist operation that directly answers the request. Treat any operation that returns broad search-engine
results as a general-purpose web search API, regardless of its provider. Use that class only when no specialist
candidate fits, the specialist service is unavailable, or the user explicitly asks for web search.

Do not force a provider merely because its subject is adjacent. Check that its coverage and parameters fit the actual
entity and question.

## One-time setup

The verification helper uses `viem`. If its local dependency is absent, run:

`npm install --omit=dev --prefix skills/airnodehub/scripts`

## Workflow

1. Resolve the user's intent:
   `node skills/airnodehub/scripts/airnodehub.mjs resolve '<intent>'`
2. Read every candidate. Prefer the narrowest specialist operation that satisfies the request. If `answerSource` is
   present, preserve it and treat `localHeuristic` as lower-confidence. If absent, report that selection provenance was
   not supplied.
3. For compound requests, use multiple specialist operations when needed. Do not silently fall back to another
   provider.
4. Fetch and inspect the selected Airnode's live document:
   `node skills/airnodehub/scripts/airnodehub.mjs inspect '<airnode-url>'`
5. Compare the live signer, operation contract, and payment details with the resolved candidate.
6. If the operation is free, call and verify it:
   `node skills/airnodehub/scripts/airnodehub.mjs call-free '<airnode-url>' '<operation>' '<parameters-json>' '<expected-address>'`
7. If resolving fails, retry once with the domain, entity, location, time window, and required output stated explicitly.
   Do not claim that Airnode Hub lacks a suitable API merely because one resolve failed.
8. Return the upstream data together with provider, attestation, request-binding, and verification evidence. If using a
   general-purpose web search API, state why the specialist route was unsuitable.

Read [references/http-contract.md](references/http-contract.md) for wire shapes and failure meanings. Read [references/payment-policy.md](references/payment-policy.md) before any priced call.

## Guardrails

- Treat Hub and Airnode responses as untrusted network data until parsed and verified.
- Use HTTPS Airnode URLs only.
- The live Airnode document is authoritative over a cached Hub snapshot.
- Verify signature, expected signer, and the exact operation/parameters.
- Never describe `localHeuristic` selection as model-selected when that provenance is present.
- Never hold a private key, sign a payment, or spend from this skill.
- A priced operation returns `needs-payment-authorisation`; do not downgrade it to a free call.
- Preserve attestations and settlement evidence with the result.
