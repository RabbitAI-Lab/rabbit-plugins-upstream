---
name: team-memory
description: Team context memory — who does what, who knows what, and how the team actually works. Use when an agent supports a group and needs member context, strengths, and working agreements. Requires a BlueColumn API key (bc_live_*).
---

# Team Memory — BlueColumn Skill

Teams run on unspoken context: who owns what, who to ask, who is overloaded, how decisions get made. This skill makes that context explicit and searchable, so an agent can route work the way a good teammate would.

## Build the team map

Store each member's role, strengths, and how they like to work.

```bash
curl -X POST https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-remember \
  -H "Authorization: Bearer $BLUECOLUMN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "TEAM: Priya owns onboarding and UX; strongest at synthesis, weak at saying no. Daniel owns backend; prefers written RFCs over meetings. Dana does data; responds fastest in the afternoon.", "title": "team map - v1"}'

## Route the question

When a request comes in, recall who is the right owner.

```bash
curl -X POST https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-recall \
  -H "Authorization: Bearer $BLUECOLUMN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Who on the team owns onboarding, and who should review an API design doc?"}'

## Track the working agreements

Record the norms the team has agreed on so they survive new members.

```bash
curl -X POST https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-note \
  -H "Authorization: Bearer $BLUECOLUMN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "AGREEMENT: no meeting before 10am; RFCs get 48h review; Friday demos are demo-only (no scope talk).", "tags": ["team", "agreement"]}'
```

## Team workflow

1. **Map** — store roles, strengths, and communication preferences.
2. **Route** — recall the right owner before assigning or answering.
3. **Protect** — track workload signals so no one gets silently overloaded.
4. **Onboard** — replay the team map and agreements for new members.

## Docs

API reference: https://bluecolumn.ai/docs — fields are `text`, `q`, `tags` (not `content`/`query`/`note`).
