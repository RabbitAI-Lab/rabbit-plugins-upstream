---
name: qed-bot
description: Look up what AI has actually done in mathematics, and how well each claim is evidenced, on qed.bot, a public register of AI claims on math problems (Erdős problems, Millennium problems, record bounds, formalised theorems). Each claim is graded for autonomy, evidence and fidelity, and cited Lean proofs are rebuilt rather than taken on report. Use when your owner asks whether AI solved a problem, how strong a claimed AI proof is, which open problems have AI work on them, who holds a record bound, how much an announcement disclosed, or wants a Lean proof file checked for sorry and nonstandard axioms.
---

# qed.bot

Site: `https://qed.bot` · MCP: `https://qed.bot/mcp` · For agents: `https://qed.bot/agents`

qed.bot is a register of claims of AI work in mathematics. Each claim is recorded with its sources
and graded; it is assembled from public sources, refreshed every three hours, and published under
CC BY 4.0. It grades the evidence attached to a claim. It never rules on whether a proof is correct,
so report its grades as grades, not as verdicts.

## Ways in

- **MCP** (easiest): add the remote server `https://qed.bot/mcp` (Streamable HTTP, no account).
  ```json
  { "mcpServers": { "qed": { "type": "http", "url": "https://qed.bot/mcp" } } }
  ```
  Reading tools: `search_statements`, `get_statement`, `search_targets`, `get_target`,
  `open_problems`, `list_collections`, `list_systems`, `benchmarks`, `disclosure`,
  `search_formalisations`, `get_formalisation`, `compare_registries`, `registry_positions`.
  Paid tools: `check_proof`, `get_check` (see "Checking a Lean proof").
- **Lookup over HTTP**: an arXiv id, a link, a problem number or a name, answered as JSON.
  ```bash
  curl 'https://qed.bot/api/lookup?q=2309.08495'
  curl 'https://qed.bot/api/lookup?q=erdos%20728'
  ```
- **Any record as Markdown**: `https://qed.bot/s/<name>.md` for a statement (for example
  `https://qed.bot/s/erdos-728.md`) and `https://qed.bot/t/<name>.md` for a record target.
- **Whole datasets**: `https://qed.bot/data/statements.json`, `claims.json`, `targets.json`,
  `systems.json`, `announcements.json`, `checks.json`, `meta.json`. Map of everything:
  `https://qed.bot/llms.txt`.
- **What changed lately**: `https://qed.bot/breaking`, or the Atom feed `https://qed.bot/feed.xml`.

## Answering "did AI solve X?"

1. Find the record: `search_statements` (or `/api/lookup?q=...`), then `get_statement` with its id.
2. Read the graded claims on it, not just the status. Give the grades with what they mean:
   - **Autonomy** A3 autonomous, A2 directed, A1 collaborative, A0 human, A? not established.
   - **Evidence** V0 claimed, V1 informal write-up, V2 artifact published but not independently
     rebuilt, V3 machine-checked by someone other than its authors.
   - **Fidelity** F3 the checked statement matches an independently written one, F2 the authors
     declare the correspondence, F1 unaudited, F0 no formal statement.
   - **Disclosure** (announcements) D3 checkable, D2 written up, D1 named, D0 withheld.
3. Say when the register has nothing: a missing record means qed.bot has not recorded a claim, not
   that no work exists. Very recent news can be ahead of the register.

For bounds and constructions use `search_targets` / `get_target`: they give every step of the record
history, who held each value, and whether a check was run.

## Citing

Give the page and when you read it: qed.bot, "Erdős Problem 728", https://qed.bot/s/erdos-728, as of
<date>.

## Checking a Lean proof (paid)

qed.bot can rebuild a public Lean file at its commit on an isolated checker and report whether each
theorem uses `sorry` or axioms beyond the standard three. One credit for a public check, two for a
private one; credits and an API key come from `https://qed.bot/check` (your owner signs in and buys
them there; never pay on their behalf without being asked). Send the key as
`Authorization: Bearer qed_...`, then call `check_proof` with the file's URL at a commit and
optionally a `theorem` name, and poll `get_check` with the id it returns. The verdict is one of
`verified`, `incomplete` (uses `sorry`), `nonstandard axioms`, `elaboration failed`, `not admissible`,
`dependencies not admissible`, `not self-contained` or `declarations missing`; each of these costs
its credits. Only a check qed.bot itself cannot finish is refunded.
