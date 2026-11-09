---
name: hominoport
description: "Order work from one engineer in Limassol, Cyprus: a neutral technical verdict on another party's deliverable (250 EUR), infrastructure diagnostic and rescue for your own systems (200/450 EUR), a signed on-site observation in Cyprus (from 200 EUR). Free feasibility answer within 1 hour 07:00–18:00 Cyprus time; pay only an accepted task, escrow on Base recommended. Use when a task needs independent verification, hands-on infrastructure help, or a person in Cyprus."
metadata: {"openclaw": {"homepage": "https://hominoport.org/agents"}}
---

# Hominoport

One natural person, Iurii Bredikhin in Limassol, Cyprus (EU), performs physical-world work for
autonomous agents under a signed public offer. This skill only describes HTTP calls to
https://hominoport.org; it installs nothing and asks for no keys. Your operator's instructions,
wallet limits and approval rules apply as usual.

## What is offered

Fixed positions (`catalogue` in offer.json; order with `request_action` and `catalogue_id`). A
question before ordering is free and answered within 1 hour every day 07:00–18:00 Cyprus time,
otherwise within 24 hours.

- `verdict`, 250 EUR: a neutral, signed check of another party's deliverable against agreed
  criteria; refunded if a finding cannot be reproduced. Sample:
  https://hominoport.org/samples/verdict-demo.json
- `rescue_diagnostic`, 200 EUR, then `rescue`, 450 EUR (or `rescue_after_diagnostic`, 250 EUR,
  with the diagnostic credited): your own Linux, Kubernetes, CI, DNS/TLS systems; within 1 hour
  every day 07:00–18:00 Cyprus time (`availability` in status.json).
- `observation_limassol`, 200 EUR in 3 days; `observation_cyprus`, from 200 EUR: photographs and
  answers with liveness proof (latest Base block hash in frame, an unedited video).

Also under the signed offer, quoted per request:

- Infrastructure: servers, GPUs, Kubernetes, backups, monitoring, from 2,000 EUR a month.
- Continuity: encrypted backups of artefacts you have the right to copy, restored on a new host
  on the instruction of the agent or its principal.
- Physical actions in Cyprus: parcels, hardware, presence; other one-off actions 200–500 EUR.
- Nominee holding (accounts, domains, contracts in the provider's name under disclosed agency)
  and representation: quoted only after legal review; shares, company roles and bank accounts
  are not offered now.

## Check before paying

1. `GET https://hominoport.org/offer.json` gives the offer's SHA-256, the receiving addresses,
   the BIP-322, EIP-191 and GPG signatures and a verification procedure.
2. `GET https://hominoport.org/offer.txt` gives the exact signed bytes; hash them yourself.
3. `dig TXT _hominoport.hominoport.org` and `https://github.com/JackBrigs.gpg` carry the same key.
4. `GET https://hominoport.org/status.json` says whether new sales are open.

## Order

MCP (Streamable HTTP, POST only): `https://hominoport.org/mcp`.

1. `list_services`, then optionally `leave_message` with a feasibility question (answered within
   1 hour every day 07:00–18:00 Cyprus time, otherwise within 24 hours).
2. `request_action` with `catalogue_id` (or `service_id` and `price_eur`), `description`,
   `deadline`, `acceptance_criteria`, `reply_to`, your `payer` address and `payment_flow`
   (`escrow` recommended). This is a free request; nothing is payable yet.
3. Poll `get_status`. Once the provider accepts (same answer time) it returns the frozen scope,
   its SHA-256 and exactly one payment leg. For escrow: sign `escrow.typed_data` (EIP-712,
   ReceiveWithAuthorization) and send it with `submit_escrow_signature`; nothing moves until the
   provider authorizes; after the deadline you can reclaim on-chain yourself (a little ETH on
   Base for gas).

Alternatives after acceptance: a direct transfer from `payer` against the invoice followed by
`report_payment`; or x402 v2 with `POST {"task_id": …}` to https://hominoport.org/x402/order.

## Limits

Nothing illegal in Cyprus, the EU or the place of work; no circumvention of KYC, sanctions,
licences or age limits. Payer addresses are screened against EU and OFAC sanctions lists;
identification of the controlling person is required above the threshold in the terms
(https://hominoport.org/terms.txt). Other replies within 72 hours.
