---
name: tokst-memory
description: Use TokST Cloud MCP for durable memory, shared context, and governed knowledge.
description_zh: 使用 TokST 云端 MCP 管理长期记忆、共享上下文和知识治理。
description_en: Use TokST Cloud MCP for durable memory, shared context, and governed knowledge.
display_name: TokST
display_name_en: TokST
category: tools
slug: tokst-memory
displayName: TokST
version: 0.9.0
author: TokST
summary: Cloud MCP memory and shared context for people and AI agents.
license: MIT
---

# TokST Memory

TokST gives the connected Agent durable memory across conversations, devices,
and authorized workspaces. Use the TokST Cloud MCP connection for all memory
operations. The MCP endpoint is:

https://api.tokst.com/mcp

## Connection

Configure this URL in an MCP client that supports Streamable HTTP. Complete the
browser authorization requested by the client. Static or headless deployments
may use a TokST API key as a Bearer token.

The connected client exposes TokST tools directly. Use those tools; do not ask
the user to install a CLI for memory retrieval or memory writes.

Useful references:

- Documentation: https://tokst.com/docs
- MCP guide: https://tokst.com/docs/mcp
- Agent guide: https://tokst.com/llms.txt
- Full agent context: https://tokst.com/llms-full.txt
- MCP discovery: https://api.tokst.com/.well-known/mcp

## Daily memory workflow

1. At the start of substantial work, call tokst_context or tokst_search.
2. Search before repeating a decision, implementation, preference, or policy.
3. Write only confirmed long-term facts, decisions, preferences, rules, and architecture with tokst_remember.
4. Update or archive superseded records with their existing memory ID.
5. Keep task execution results in TokST Runtime; extract long-term knowledge separately.

Use the narrowest Workspace and Atlas that matches the user’s request. The
service applies the authenticated user and Agent identity; clients must not
invent an authoritative identity.

## What belongs in durable memory

| Type | Store |
|---|---|
| fact | Stable project, user, infrastructure, or operational facts |
| decision | Approved choices, rationale, and constraints |
| preference | Durable user or team preferences |
| architecture | Components, data flow, interfaces, and operational constraints |
| note | Reusable context outside the typed categories |
| task | Historical compatibility records only; use a formal task for assigned work |

Use Markdown when it preserves important structure such as a table, numbered
procedure, or configuration summary. Preserve the working language. Retain
material facts, values, file changes, confirmed risks, and concrete next steps.

## Data quality rules

Store a record after the result is confirmed. A good record states the result,
the scope, the supporting evidence, and the effective constraint.

Keep these categories outside durable memory:

- Secrets, passwords, API keys, private keys, cookies, and access tokens.
- Raw chain-of-thought, full terminal logs, raw tool JSON, and debug traces.
- Transient network failures, quota errors, retries, and duplicate output.
- Guesses presented as confirmed facts.

When a source contains sensitive content, preserve a safe summary whenever it
remains useful. The default Workspace policy blocks secrets, passwords, API
keys, private keys, cookies, and access tokens. A Workspace Owner can enable
**Absolute mode** in Dashboard Settings for an explicit exception. In that
mode, require the user's confirmation, set `sensitive: true`, provide a concise
`sensitiveReason`, and warn that authorized Workspace members and connected
Agents can read the record. Sensitive records skip embeddings and automatic
capture. Keep secret-manager references as the preferred durable record.

## Connected Runtime

Tasks, automatic sessions, Agent communication, handoffs, endpoint health, and
execution results use the TokST CLI and its authenticated WSS Runtime. The MCP
connection stores and retrieves durable knowledge for that work.

## Safe mutation rules

Read and search before modifying existing records. Confirm the intended
Workspace, Atlas, or memory ID before a broad archive operation.

Use update, archive, restore, and audit tools to preserve traceability. Cloud
MCP, the compatibility API, and the CLI do not expose permanent memory
deletion. Permanent cleanup is performed only by the user from the Dashboard
archived view after manual confirmation.

## Error recovery

| Condition | Agent action |
|---|---|
| OAuth authorization required | Present the MCP client authorization step and wait for completion. |
| Invalid or expired credential | Ask the user to reconnect or refresh the credential. |
| Permission rejection | Confirm Workspace, Atlas, role, and target resource. |
| Rate limit or temporary server failure | Respect Retry-After when present; retry one safe read once. |
| Interrupted write | Search the target knowledge base first; avoid duplicate writes. |

Return concise, user-facing outcomes. Include relevant memory or evidence IDs
when they help the user inspect the work.
