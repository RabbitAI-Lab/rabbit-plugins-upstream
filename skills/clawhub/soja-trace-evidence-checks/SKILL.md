---
name: soja-trace-evidence-checks
description: Use when an agent or operator needs a bounded, read-only comparison of supplied trace/link evidence or reconciliation of supplied evaluation-cost events. No endpoint, installation, payment, or automatic invocation is available.
version: 0.1.2
---

# SOJA Trace Evidence Checks

## Scope

This public descriptor covers two bounded resources:

1. **Trace-integrity verifier** — compares an operator-supplied expected trace/link manifest against operator-supplied observed evidence. It reports missing/non-provable entries. Absence of supplied evidence is not proof of runtime failure.
2. **Evaluation cost-reconciliation sentinel** — deduplicates identical supplied trace-cost events, flags conflicting trace IDs, and excludes conflicts from its reconciled total for human review.

## Access state

- **Discovery:** this descriptor and `resource.json` are public.
- **Evaluation / invocation:** not publicly available. A human operator must authorize any local, supplied-input evaluation.
- **Payment:** unavailable. C$15 per verified environment check and C$5 per evaluation-run check are proposed validation hypotheses only, not active charges.
- **Delivery:** no hosted endpoint, MCP server, API, integration, automated delivery, telemetry, source download, or checkout is offered.

## Data and safety boundary

Do not submit secrets, credentials, customer data, production traces, or other payloads. The public request route is for a concise trigger, current workaround, recurrence, and pricing/budget/evaluation interest only.

## Request access

Email [soja.validation@proton.me](mailto:soja.validation@proton.me) with the non-sensitive fields described in `REQUEST_ACCESS.md`.

## Evidence boundary

A page retrieval, crawl, view, download, generic compliment, self-test, controlled agent, owner-controlled agent, internal simulation, bot, or coordinated test is not commercial evidence. A qualifying external request must be independently generated and identify a real use trigger plus credible price, budget, procurement, or delegated-evaluation authority.
