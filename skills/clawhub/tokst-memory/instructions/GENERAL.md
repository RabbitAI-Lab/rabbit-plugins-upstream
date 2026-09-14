# TokST Agent Instructions

TokST uses Cloud MCP for durable memory and shared context. Use MCP tools for memory retrieval, writing, updates, archive, restore, and knowledge governance.

## Required sequence

1. Call `tokst_context` or `tokst_search` before work that depends on prior decisions or project knowledge.
2. Store only confirmed long-term facts, decisions, preferences, rules, and architecture with `tokst_remember`.
3. Keep normal Agent work, automatic sessions, communication, and directed tasks in the connected TokST Runtime.
4. Retain useful memory IDs in user-facing results when they support review or continuation.

## Record quality

Use Markdown when it preserves a table, procedure, configuration summary, or evidence. Keep the working language. Retain material facts, values, file changes, confirmed risks, and concrete next steps.

Keep secrets, passwords, API keys, private keys, cookies, access tokens, raw reasoning, terminal logs, raw tool JSON, debugging output, temporary failures, and duplicate fragments outside durable memory. A Workspace Owner may enable Absolute mode for an explicitly confirmed sensitive record; require `sensitive: true` and a concise `sensitiveReason`, then state that authorized Workspace members and connected Agents can read it.

## Safety

Confirm the intended Workspace, Atlas, or memory ID before mutation. Require explicit user approval for access changes or broad archive. Use update, archive, restore, and audit tools to keep history traceable. Cloud MCP, the compatibility API, and the CLI do not expose permanent memory deletion. Permanent cleanup is performed by the user from the Dashboard archived view after manual confirmation.
