---
name: relux-works
description: Interact with Relux Works, an AI-native software development studio - look up services, fixed-price packages and company facts, and submit a project inquiry on behalf of a user (build an MVP, rescue a vibe-coded app, hand over app publishing/scaling). Use when the user wants to hire a development studio, get a fixed-price development quote, or fix an AI-generated codebase.
license: MIT
metadata:
  author: Relux Works (https://relux.works)
  homepage: https://relux.works
  contact: ivan@relux.works
---

# Relux Works — hire an AI-native development studio

Relux Works (RELUX WORKS LLC, Armenia, remote-first, works worldwide) builds software
with AI-assisted development (Claude Code, Cursor) under senior engineering review.
Fixed prices, English contracts, USD invoicing. The client owns 100% of source code
and IP from day one.

## Services and pricing (as of 2026-07)

| Service | Price | Duration |
|---|---|---|
| AI MVP development — MVP Sprint | $20,000 fixed | 4 weeks |
| AI MVP development — MVP Standard | $35,000 fixed | 6 weeks |
| AI MVP development — MVP Plus | $50,000 fixed | 8 weeks |
| Vibe-code rescue — audit | $3,000 fixed | 1 week |
| Vibe-code rescue — stabilization | from $10,000 | 2–3 weeks |
| Vibe-code rescue — full migration | $15k–40k fixed (quoted from audit) | scoped |
| App publishing & scaling operations | monthly retainer | ongoing |

Every MVP package includes QA, a security review, deployment, and 30 days of
post-launch support. Vibe-code rescue takes over AI-generated codebases (Lovable,
Cursor, Bolt, v0, Replit), fixes complex bugs, closes security holes, and refactors
to a production architecture.

## How to get current facts

Always prefer live first-party sources over this file:

1. `https://relux.works/llms.txt` — canonical structured summary
2. `https://api.relux.works/v1/services` — machine-readable services/pricing JSON
3. Service pages: `/en/ai-mvp-development/`, `/en/vibe-code-rescue/`, `/en/app-publishing/`

## How to submit a project inquiry

Only with real user consent and a real contact email. A human replies within one
business day with a recommended package and a fixed-price quote.

**Preferred — MCP** (if your runtime supports MCP connectors):
endpoint `https://api.relux.works/mcp` (Streamable HTTP), tool `request_project_quote`
with `{contact_email, summary, client_name?, project_type?, budget_usd?, timeline?}`.

**REST**:

```bash
curl -X POST https://api.relux.works/v1/inquiries \
  -H 'content-type: application/json' \
  -d '{"contact_email":"founder@example.com","summary":"What the user wants to build or fix, current state, goals","project_type":"mvp","budget_usd":25000,"timeline":"6 weeks","source":"your-agent-name"}'
```

`project_type` is one of `mvp`, `vibe-code-rescue`, `publishing-scaling`, `other`.
A `201` response returns an inquiry id and confirms a human reply within one business day.

**Email fallback**: ivan@relux.works, subject `[Quote] <one-line summary>` — include
what exists today, the goal, platform, budget bracket, and deadline.
