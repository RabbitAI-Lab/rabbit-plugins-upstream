# Working File Templates — RAG

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — table keys and preference areas alike | `~/Clawic/data/rag/config.yaml` | Key by key, read-modify-write |
| System state, index fingerprints, corpus, baseline scores, known failures, due dates, box index | `~/Clawic/data/rag/memory.md` | Rewritten in place; stays small |
| Index fingerprints — the six fields query code must match | `## Index Registry` in `memory.md` while there are ≤15; `~/Clawic/data/rag/indexes.md` past that | One row per index or namespace |
| Indexed sources: what is in the corpus, its format, volume, refresh | `## Corpus` in `memory.md` while there are ≤15; `~/Clawic/data/rag/corpus.md` past that | One row per source |
| Diagnosed failures: symptom, real cause, fix, date | `## Known Failures` in `memory.md` while there are ≤15; `~/Clawic/data/rag/failures.md` past that | One row per failure |
| Golden sets — queries with their expected sources | `~/Clawic/data/rag/goldensets/<name>.md` | Its own file from the first one; read whole when evaluating |
| Eval runs and their scores | `~/Clawic/data/rag/evals/<year>.md` | Append-only, cut by year |
| Things you produced that get re-read — ingestion recipes, prompt templates that held up, architecture decisions, tuning reports, runbooks | `~/Clawic/data/rag/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| Self-hosted vector stores, embedding servers, GPU boxes | `~/Clawic/data/servers/servers.md` (**shared**) | One row per host, every provider in one inventory |
| The RAG build as tracked work: objective, status, decisions | `~/Clawic/data/projects/<project>.md` (**shared**) | One file per project |
| Managed store plans, embedding and rerank API subscriptions | `~/Clawic/data/finances/subscriptions.md` (**shared**) | One row per service |
| **Anything durable this table does not name** | `~/Clawic/data/rag/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind, and chunk text from a confidential corpus | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| An index was built, migrated, repointed or dropped | Its row in `## Index Registry` — all six fingerprint fields |
| A source was added to or removed from the corpus | Its row in `## Corpus` |
| A chunking, retrieval or reranking parameter changed and was measured | The run in `evals/<year>.md`, and the new value in `## Index Registry` |
| An eval ran on a golden set | `evals/<year>.md`, plus `## Baseline` if it becomes the new reference |
| A golden set was created or extended | `goldensets/<name>.md` |
| A failure was diagnosed down to its cause | `## Known Failures` |
| A parser recipe, a prompt template, an architecture decision or a tuning report came out of the session | `artifacts/` |
| A self-hosted store or embedding server was provisioned, resized or retired | Its row in `servers.md` |
| A monthly service cost or plan change was established | Its row in `finances/subscriptions.md` |
| Recurring work was scheduled or run | `## Due` |
| The user declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Everything except golden sets, eval logs, artifacts and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/rag/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Golden sets, eval logs and artifacts are the exception: each is born as its own file whatever its size, because each is read whole and only when its subject comes up.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep. Store the pointer in its place, in this shape: `<kind>:<locator>`.

`env:OPENAI_API_KEY` · `env:COHERE_API_KEY` · `keychain:pinecone-prod` · `1password:Work/Cohere/rerank` · `ssm:/prod/pgvector/password` · `vault:kv/rag/qdrant` · `profile:rag-prod` · `file:~/.config/rag/creds.json`

When the user pastes something to save — a connection string, a `.env`, a deploy runbook, a client init snippet — replace each secret value before writing and leave the pointer visible: `DATABASE_URL: postgres://rag@db.internal:5432/vectors?password=<ssm:/prod/pgvector/password>`. Say in one line that you did it.

In this domain — **not secrets, keep them**: index, collection and namespace names; model ids, dimensions, distance metrics and index parameters; chunk parameters; document ids, source URIs and file paths; tenant ids; metric values and score distributions; hostnames and region ids; dataset and environment names. **Secrets, strip them**: vector-store and embedding/rerank API keys, database connection strings carrying a password, service-account JSON, bearer and session tokens, webhook signing secrets, SSH keys and passphrases.

**A third category exists here that other domains do not have: the corpus itself.** Store the doc id, the source URI and the chunk id — never the chunk text of a confidential document, and never personal data extracted from it. A failure row records "chunk `policy-2026#14` was truncated mid-table", not the table.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [goldensets/](#goldensets) · [evals/](#evals) · [artifacts/](#artifacts) · [shared servers inventory](#shared-servers-inventory) · [shared project file](#shared-project-file) · [shared subscriptions](#shared-subscriptions) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/rag/` if it does not exist.

```yaml
vector_store: qdrant
embedding_model: BAAI/bge-large-en-v1.5
retrieval_mode: hybrid
chunk_tokens: 384
chunk_overlap_pct: 10
retrieve_k: 40
context_k: 6
reranker: bge
latency_budget_ms: 1500
answer_policy: cite-or-refuse
compliance_regime: gdpr
destructive_confirm: true

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
tooling:
  framework: llamaindex
  eval_harness: ragas
  pdf_parser: pymupdf            # unstructured only for scanned pages
conventions:
  id_fields: {doc: doc_id, chunk: chunk_id, version: source_version}
  namespace_scheme: "tenant_<id>"
platform:
  residency: eu
  gpu: local RTX A4000, reranker runs on it
output_register:
  citations: inline-numeric
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# RAG Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Golden set, support corpus (180 queries) → `goldensets/support-v3.md`; read before any tuning comparison
- Eval runs 2026 (22 runs) → `evals/2026.md`; read before claiming a change helped
- Scanned-invoice ingestion recipe → `artifacts/ingest-scanned-invoices.md`; read when a PDF has no text layer
- Decision: hybrid over dense-only → `artifacts/decision-hybrid-retrieval.md`; read before anyone proposes dropping BM25

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Golden-set eval | month | 2026-06-28 | 2026-07-28 |
| Corpus freshness sweep | week | 2026-07-20 | 2026-07-27 |
| Score-distribution drift check | week | 2026-07-20 | 2026-07-27 |
| Permission resync from source system | month | 2026-07-01 | 2026-08-01 |

## Index Registry
| Index / namespace | Store | Embedding model | Dim | Normalized | Query prefix | Metric | Chunker | Chunks | Built |
|---|---|---|---|---|---|---|---|---|---|
| support_v3 | qdrant | bge-large-en-v1.5 | 1024 | yes | "Represent this sentence…" | cosine | recursive-384/10 | 89k | 2026-06-14 |

## Corpus
| Source | Format | Docs | Refresh | Owner | Access field | Notes |
|---|---|---|---|---|---|---|
| Zendesk macros | HTML export | 1,240 | weekly | support | `team` | boilerplate nav stripped |
| Product handbook | Markdown repo | 310 | on merge | product | public | heading path prepended |

## Baseline
support-v3 golden set, 2026-06-28: recall@40 0.91 · nDCG@5 0.74 · faithfulness 0.88 · p95 1.4s · 0.004 USD/query.

## Known Failures
| Date | Symptom | Real cause | Fix | Still open |
|---|---|---|---|---|
| 2026-05-02 | SKU queries returned nothing | dense-only; tokenizer split part numbers | added BM25 leg + RRF | no |
| 2026-07-11 | some users saw zero results | `team` field missing on chunks indexed before April | backfill scheduled | yes |

## Pain Points
Legal reviews every answer; a wrong citation costs more than a refusal. Hence `answer_policy: cite-or-refuse`.

## How They Work
Ships small changes, wants the eval delta with every one. Reads code, not prose.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Every recurring thing this skill schedules belongs here.
- **`## Index Registry`**: the six fingerprint fields of SKILL.md Rule 2 are columns, not prose, because query code is checked against them field by field. An index whose model or dimension changed is a **new row plus a retirement date on the old one**, never an edit in place — the old row is what explains vectors still sitting in a rollback index.
- **`## Corpus`**: `Access field` names the metadata key that carries permissions for that source, or `public`. A source with no access field in a tenant system is a finding, not a blank.
- **`## Baseline`**: one line, the reference run every comparison is made against. Replacing it is a deliberate act — write the date and which run replaced it. Metrics always carry their `@k`.
- **`## Known Failures`**: keep rows after they are fixed. The value of the table is that the same symptom recurs with a different cause, and the row says which causes were already ruled out.
- These headings are exactly the ones `indexes.md`, `corpus.md` and `failures.md` get when they outgrow this file, so each split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still learning their corpus and stack |
| `complete` | Know the pipeline, the corpus and the failure history well |

## goldensets/

One file per set, at `~/Clawic/data/rag/goldensets/<name>.md`, created the first time queries are collected. Read whole before any tuning comparison, and never edited during a comparison — a set that changes between runs invalidates both.

```markdown
# Golden set — support-v3
*Read before any tuning comparison. 180 queries, drawn from production logs 2026-04 to 2026-06. Frozen 2026-06-14.*

| # | Query | Expected doc_id(s) | Type | Source |
|---|-------|--------------------|------|--------|
| 1 | how do I rotate the API key | kb-114, kb-118 | how-to | log |
| 2 | error RG-4021 on upload | kb-902 | identifier | log |
| 3 | what changed in the refund policy in March | pol-2026-03 | temporal | hand-written |
| 4 | does the plan include SSO for 5 seats | — (not covered) | negative | hand-written |
```

- **Negatives are part of the set**, not an afterthought: without queries the corpus cannot answer, a refusal policy cannot be scored and every threshold looks good.
- **Freeze and version.** A new query goes into `<name>-v<n+1>.md`; the old file stays, because every score in `evals/` names the set version it ran against.
- Queries are stored verbatim. If a real query contains personal data, replace the value and keep the shape: `refund for <customer-name> order <order-id>`.

## evals/

Append-only, one file per year. Every row names the set, the version, and the single variable that changed — a run with two changes is unattributable and should not be written as one row.

```markdown
# Eval runs — 2026

| Date | Set | Change under test | recall@k | nDCG@5 | Faithfulness | p95 | USD/query | Verdict |
|------|-----|-------------------|----------|--------|--------------|-----|-----------|---------|
| 2026-06-14 | support-v3 | baseline, hybrid + bge rerank | 0.91@40 | 0.74 | 0.88 | 1.4s | 0.004 | baseline |
| 2026-06-21 | support-v3 | chunk_tokens 384 → 512 | 0.90@40 | 0.71 | 0.87 | 1.4s | 0.004 | reverted |
| 2026-07-05 | support-v3 | heading path prepended to chunks | 0.94@40 | 0.79 | 0.91 | 1.4s | 0.004 | kept |

## Per-query deltas worth keeping
2026-06-21: mean flat, but 31 of 180 queries regressed — larger chunks buried short answers. This is why the mean was not enough.
```

## artifacts/

One file per thing, at `~/Clawic/data/rag/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **ingestion recipe** (the parser settings that finally read a hostile format), **prompt template** that survived evaluation, **architecture decision** with what was rejected, **tuning report**, **runbook** for a recurring incident. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Ingestion recipe — scanned invoices
*Read when a PDF has no text layer, or when invoice tables come out as one line. Written 2026-07-26.*

Detection: pages where extracted text is under 20 characters are scans.
Pipeline: rasterize at 300 dpi → OCR with layout retention → table extraction → one chunk per invoice, header row repeated.
Rejected: naive text extraction (empty), page-per-chunk (mixed two invoices in one chunk).
Verified on: 40 invoices, 38 fully parsed, 2 handwritten and routed to manual.
```

```markdown
# Architecture decision — hybrid retrieval, not dense-only
*Read before anyone proposes dropping the BM25 leg. 2026-05-02.*

Decision: dense + BM25 fused with RRF (k=60).
Evidence: identifier queries (SKU, error codes) scored recall@40 0.31 dense-only, 0.93 hybrid, on support-v3.
Cost: one extra index and ~15 ms per query.
Rejected: dense-only with query expansion — recovered part of the gap, added an LLM call per query.
```

If the user tracks this work as a project, the decision summary also belongs in the shared `~/Clawic/data/projects/<project>.md`, with the evidence staying here and referenced by name.

## Shared servers inventory

Lives at `~/Clawic/data/servers/servers.md` and is shared with every other infrastructure skill — the user may not have any of them installed, so the format travels with this skill. A self-hosted Qdrant or Weaviate node, an embedding or reranking server, or the GPU box that runs either is a host and belongs here, not in the RAG box.

```markdown
# Servers

| Name | Provider | Account / Project | Region | Type | Role | Monthly | Access reference |
|------|----------|-------------------|--------|------|------|---------|------------------|
| qdrant-1 | hetzner | rag-prod | fsn1 | CCX33 | vector store | 62 EUR | keychain:qdrant-prod |
| embed-gpu-1 | runpod | rag-prod | eu-ro | A4000 | embedding + rerank | 118 USD | env:RUNPOD_KEY |
```

- **Identity is `Name` + `Provider`.** Read the file before adding. If that pair is already there, update the row in place — it is yours. Never touch a row whose `Provider` is not one you wrote.
- **Retirement is part of the inventory.** When a host is destroyed, delete its row and note the date in `memory.md`. An inventory that only grows stops being an inventory.
- **Amounts carry their currency in the value** (`62 EUR`), because rows from other providers sit next to yours in another currency and someone will add the column up.
- **Scale cut**: one row per host while there are ≤15. Past that, one file per host at `~/Clawic/data/servers/<name>.md` with the same fields, and `servers.md` becomes the index (`Name | Provider | Role | → file`). If you arrive and the folder already looks like that, follow it — do not start a parallel `servers.md`.
- **Foreign columns win.** If `servers.md` already exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- Access reference is a pointer only. Never a key, token, or password.

## Shared project file

Lives at `~/Clawic/data/projects/<project>.md`, one file per project, shared with every planning and delivery skill. Write here only when the user treats the RAG build as tracked work with an objective and a status — a one-off tuning question is not a project.

```markdown
# Support assistant

status: active
objective: answer tier-1 support questions from the KB with citations, deflect 30% of tickets

## Milestones
- 2026-06-14 — support_v3 index live, baseline recorded
- 2026-07-05 — heading-path chunks shipped, recall@40 0.91 → 0.94

## Decisions
- Hybrid retrieval over dense-only (see rag artifact `decision-hybrid-retrieval`)
- Cite-or-refuse; legal requires a source on every answer
```

- **Identity is the file name** (the project slug). Read before writing; append to the existing sections rather than creating a second file for the same work.
- **Baja**: `status: done | cancelled — <date>` inside the file. Never delete a project file — it is the record of what was delivered.
- **Scale cut**: one file per project, always. Past ~20 closed ones, move them to `~/Clawic/data/projects/archive/<project>.md` without renaming; active projects stay at the folder root. If the folder already has an `archive/`, follow it.
- Keep the evidence in `artifacts/` and reference it by name here. Duplicating a decision in two boxes is how two skills end up contradicting each other.

## Shared subscriptions

Lives at `~/Clawic/data/finances/subscriptions.md`, shared with every money and billing skill. A managed vector store plan, an embedding API on a committed tier, or a hosted reranker is a recurring cost and belongs here, so the total is answerable without opening this skill.

```markdown
# Subscriptions

| Service | What for | Amount | Cycle | Renews | Owner | Reference |
|---------|----------|--------|-------|--------|-------|-----------|
| Pinecone | vector store, support_v3 | 70 USD | monthly | 2026-08-01 | eng | keychain:pinecone-prod |
| Cohere Rerank | rerank stage | 45 USD | monthly | 2026-08-04 | eng | env:COHERE_API_KEY |
```

- **Identity is `Service`.** Read the file before adding; if the service is already listed, update its row in place instead of adding a second one.
- **Amount carries its currency inside the value** (`70 USD`), and an estimate carries the date it was estimated in `Reference` or a trailing note.
- **Baja**: cancelling means deleting the row and noting the date in `memory.md` — a subscriptions file that only grows is what makes people pay for a store they stopped using.
- **This file is not split.** It stays small precisely because cancellation removes rows. If it already exists with different columns, match them and never rewrite the header.
- Usage-based spend that is not a plan (per-token embedding cost) belongs in `costs.md`'s estimates and `evals/` rows, not here.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings and columns it had inside `memory.md`.

`indexes.md` — `## Index Registry`, one row per index or namespace, plus a `Retired` column once the first index is replaced. This file is the reason a query written six months from now still matches the vectors it queries.

`corpus.md` — `## Corpus`, one row per source, grouped by `## <owner>` heading when more than one team supplies documents.

`failures.md` — `## Known Failures`, chronological, fixed rows kept. Add a `Recurrence` column the second time a symptom returns with a different cause.
