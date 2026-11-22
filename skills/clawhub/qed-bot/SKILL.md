---
name: qed-bot
description: Look up what AI has actually done in mathematics, and how well each claim is evidenced, on qed.bot, a public register of AI claims on math problems (Erdős problems, Millennium problems, record bounds, formalised theorems). Each claim is graded for autonomy, evidence and fidelity, and cited Lean proofs are rebuilt rather than taken on report. Use when your owner asks whether AI solved a problem, how strong a claimed AI proof is, which open problems have AI work on them, who holds a record bound, how much an announcement disclosed, or wants a Lean proof file checked for sorry and nonstandard axioms, or wants to send the register a paper, a claim or a correction for review.
---

# qed.bot

Site: `https://qed.bot` · MCP: `https://qed.bot/mcp` · For agents: `https://qed.bot/agents`

qed.bot is a register of claims of AI work in mathematics. Each claim is recorded with its sources
and graded; it is assembled from public sources, refreshed every hour, and published under
CC BY 4.0. It grades the evidence attached to a claim. It never rules on whether a proof is correct,
so report its grades as grades, not as verdicts.

## Ways in

- **MCP** (easiest): add the remote server `https://qed.bot/mcp` (Streamable HTTP, no account).
  ```json
  { "mcpServers": { "qed": { "type": "http", "url": "https://qed.bot/mcp" } } }
  ```
  Reading tools: `search_statements`, `get_statement`, `search_targets`, `get_target`,
  `open_problems`, `list_collections`, `list_systems`, `benchmarks`, `disclosure`,
  `search_formalisations`, `get_formalisation`, `compare_registries`, `registry_positions`,
  `list_evaluators`.
  Paid tools: `check_proof`, `get_check` (see "Checking a Lean proof").
  Submitting: `submit_lead`, `submit_claim`, `flag_record`, `get_submission` (see "Telling the
  register what it is missing").
  Building a proof or scoring a construction runs its author's code, so `verify_proof`,
  `submit_proof` and `submit_construction` are only on the local server
  (`python -m mcp_server.server` from the repository).
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

Without a key, where agent payments are open, you can pay for one check yourself in USDC on Base
over x402 ($1.30 public, $2.60 private; `GET https://qed.bot/api/checks/packs` shows `agents.open`
and the prices). `POST https://qed.bot/api/checks` with `{"url", "theorem"}` answers `402` with a
`PAYMENT-REQUIRED` header (base64 JSON naming the amount, the USDC contract and `payTo`); an x402
client signs the authorization and retries with `PAYMENT-SIGNATURE`, and the check comes back queued
with the settlement in `PAYMENT-RESPONSE`. Over MCP, `check_proof` without a key returns the payment
asked for and takes it in `params._meta["x402/payment"]`. A private check returns a `qedc_` token,
shown once, which `get_check` (or `?token=`) needs to read it. Spend only a wallet you have been
given for this and within the limit you were given, and never pay for a check that is already
public: that result is returned free.

## Telling the register what it is missing

When your owner points at AI work the register lacks or gets wrong, you can send it for review with
an API key from `https://qed.bot/check` (free; submitting costs no credits). Ask your owner before
submitting under their account: it is public, under their handle.

- `submit_lead` with a `url` and optional `note`: a paper, repository, post or announcement. Use it
  when you are unsure which record it belongs to.
- `submit_claim` with `node`, `systems`, `outcome`, `sources`, and where known `humans`, `date`, a
  Lean `proof_url` at a commit and its `theorem`.
- `flag_record` with `node`, `what` is wrong, and `sources`.

The same work over HTTP: `POST https://qed.bot/api/submissions` with the key. Each submission is
public at once and waits for an administrator; nothing in the register changes until it is accepted,
and grades are never bought. Poll `get_submission` (no key) with the id you got back: its `stage`
is `received`, `in_review`, `accepted` or `declined` (with the reason in `review_note`). Each
account may send five a day; a repeated lead is answered with the first one.

## Following changes

- **Webhooks** (with Pro): register an HTTPS endpoint for nodes, AI systems, labs, followed problems
  and watched papers or phrases, and qed.bot POSTs signed JSON when something happens
  (`node.event`, `signal.seen`). `POST https://qed.bot/api/webhooks` with the key; the secret is shown
  once. Details: `https://qed.bot/agents#webhooks`.
- **Allowances**: every keyed request and every `/api/v1` request is metered (30 a minute without a
  key, 120 with a free key, 1,200 with Pro), reported in `x-ratelimit-*` headers; a refusal is a 429
  with `retry-after`.
- **Pro** is £10 a month at `https://qed.bot/pro`, bought by your owner. It buys delivery and
  volume, never a grade.
