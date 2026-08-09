---
name: prompt-archaeology
description: "Excavate forgotten solutions, code snippets, and decisions from past conversation sessions. Use when the user is re-solving a problem you've likely solved before, hunting for a lost snippet, or wants to mine session history for buried knowledge instead of starting from scratch."
version: 1.0.0
author: Denis Voronin
license: MIT
metadata:
  hermes:
    tags: [sessions, history, search, knowledge-mining, archaeology, recovery, hermes-agent]
    related_skills: []
---

# Prompt Archaeology

## Overview

**Prompt Archaeology** is the practice of excavating your own conversation history instead of re-solving problems from scratch. Every AI session is a stratum — a sedimented layer of debugging, decision-making, and discovery. Over time, valuable artifacts sink below the surface: a one-liner that fixed a gnarly race condition, a config that satisfied a finicky build, the exact incantation that convinced a model to behave. Most agents never dig for these. They re-derive, re-guess, and re-fail.

This skill turns that history into a quarryable resource. It bundles:

- **Search strategies** — keyword, semantic-adjacent, temporal, and structural queries tuned for session transcripts.
- **Relevance scoring** — a transparent, composable ranking that surfaces the one session that actually matters.
- **Knowledge extraction patterns** — recipes for pulling *decisions* and *solutions* out of a wall of chat, not just matching text.
- **Deduplication** — collapse near-duplicate fixes across sessions into a single canonical answer.
- **`excavate.py`** — a standalone Python script that crawls session logs and markdown files, ranks them, and prints the buried artifacts.

The metaphor is deliberate. An archaeologist does not grep the desert for "pottery" and ship the first hit. They survey, triangulate, carefully extract, and catalog. This skill teaches the agent to do the same with its own past.

## When to Use

- **The user is about to re-solve a known problem.** They describe a bug or task and you have a flicker of "we've done this before." Excavate before answering.
- **"Didn't we figure out...?" / "What did we land on?"** — retrieve the prior decision and its rationale, not just the outcome.
- **Hunting for a lost code snippet, config value, or command** that worked months ago.
- **Onboarding to a codebase you've touched before** — pull the architectural decisions out of old sessions.
- **Avoiding repeated dead ends** — find the approaches that were *rejected* and why, so you don't walk back into them.
- **Writing postmortems or ADRs** from scattered session evidence.

### Don't use for

- Fresh problems with no prior history — there's nothing to excavate; solve forward.
- When you already hold the answer in active context — don't pad the turn with a search.
- Sensitive retrieval across other users' private profiles unless explicitly authorized.

## The Excavation Workflow

A dig has five phases. Skipping any phase degrades result quality.

### 1. Survey — frame the query

Before searching, state **what artifact you want** and **what shape it takes**:

| Artifact you want | Query shape | Example seeds |
|---|---|---|
| A fix for a bug | error string + symptom words | the exception text, "traceback", the failing assertion |
| A decision + rationale | the option names + "decided" / "chose" / "went with" | the two libraries you were weighing |
| A config value | the key name + surrounding file | `"max_connections"`, `nginx.conf` |
| A rejected approach | the approach + "didn't work" / "gave up" / "abandoned" | the tool you tried first |
| A command / incantation | the tool + the goal verb | `ffmpeg`, "concatenate" |

Write the query down. A vague survey yields a vague dig.

### 2. Locate — run the searches

Run **multiple passes**, not one. Different phrasings live in different sessions.

- **Exact / keyword pass** — the literal error string, function name, or filename. Highest precision.
- **Semantic-adjacent pass** — paraphrase the intent. If the exact term misses, the concept might be filed under different words.
- **Temporal pass** — constrain to the window when the work happened ("sessions from the week we shipped v2").
- **Structural pass** — look for *code blocks*, *file diffs*, or *command outputs* near the topic, not just prose. Solutions often hide in fenced blocks.

`excavate.py` runs the keyword and structural passes directly; use `session_search` or a semantic tool for the semantic-adjacent pass.

### 3. Score — rank the finds

Not every hit is an artifact. Rank each located session against four signals (this is the scoring baked into `excavate.py`, in `--explain` mode):

| Signal | What it measures | Weight |
|---|---|---|
| **density** | match count relative to session length | high — a session densely packed with the term is probably *about* it |
| **recency** | newer sessions score higher (configurable) | medium — recent fixes are more likely still valid |
| **code presence** | does the session contain runnable code/commands? | high — a fix with code beats a fix with prose |
| **resolution markers** | phrases like "that fixed it", "works now", "merged" | highest — explicit success is gold |

The composite score is `density·0.25 + recency·0.15 + code·0.25 + resolution·0.35` (weights live in `excavate.py` and are tunable). Relevance is **not** raw match count — a 200-message session with one mention ranks below a 12-message session built around the topic.

### 4. Extract — pull the artifact out

Once you've found the winning session, don't dump the whole transcript. Extract the **minimal artifact**:

- **For a fix:** the failing state → the change → the success marker. Three quotes, nothing more.
- **For a decision:** the options considered → the chosen option → the stated rationale.
- **For a command:** the exact command + the one line of context that says what it does.
- **For a rejected approach:** what was tried → the observed failure → the inferred lesson.

Quote the session (`> ...`) and cite it. Extraction patterns are detailed in `references/extraction-patterns.md`.

### 5. Deduplicate — collapse the finds

The same fix often appears in three sessions (the first attempt, the retry, the "oh and also" follow-up). Deduplicate before reporting:

- **Exact-code dedup** — identical fenced blocks collapse to one.
- **Near-dup detection** — normalized text similarity > 0.85 merges into a cluster; keep the highest-scoring member as the canonical answer.
- **Variant detection** — if two snippets differ only in a version number or path, treat as the same artifact and note the latest variant.

`excavate.py --dedup` runs all three. See `references/deduplication.md`.

## Using `excavate.py`

The script lives at `scripts/excavate.py`. It has no third-party dependencies — stdlib only — so it runs anywhere Python 3.8+ does.

```bash
# Basic keyword dig over a directory of .md / .txt / .json session logs
python3 scripts/excavate.py dig ./sessions --query "kafka consumer rebalance"

# Multiple terms (AND'd within a session), show top 5 with per-session scores
python3 scripts/excavate.py dig ./sessions --query "rebalance retry backoff" --top 5 --explain

# Add a date window (ISO dates), dedup near-identical results
python3 scripts/excavate.py dig ./sessions \
  --query "connection pool exhaustion" \
  --after 2024-01-01 --before 2024-06-01 \
  --dedup

# Dump the extracted code blocks across all matching sessions
python3 scripts/excavate.py dig ./sessions --query "ffmpeg concatenate" --extract code

# Index a directory once, then query the index repeatedly (faster for large corpora)
python3 scripts/excavate.py index ./sessions --out sessions.idx
python3 scripts/excavate.py query sessions.idx --query "oauth refresh token" --top 3 --explain
```

`--explain` prints the per-signal score breakdown so you can see *why* a session ranked where it did. Full CLI reference: `references/cli-reference.md`.

### Programmatic use

```python
from excavate import ArchaeologyIndex

idx = ArchaeologyIndex()
idx.scan("./sessions")            # walk the directory once
for hit in idx.search("kafka rebalance", top=5, explain=True):
    print(hit.score, hit.path, hit.extraction)
```

The `ArchaeologyIndex` class is the stable surface; the CLI is a thin wrapper over it.

## Relevance Scoring in Depth

Scoring details, the math, and how to retune weights for your corpus are in `references/relevance-scoring.md`. Key points:

- Scores are normalized to **[0, 1]** per signal before weighting, so a corpus change doesn't silently inflate one signal.
- **Resolution markers dominate** by default — a session that explicitly says "that fixed it" beats a longer, denser session that merely mentions the term. Tune the weight down if your logs lack success markers.
- Recency is **configurable**, not gospel. For stable domains (algorithms, math) weight it low; for fast-moving domains (frontend deps) weight it high.
- The scoring is **transparent**, not learned. Every ranking is explainable; nothing is a black-box embedding. This matters when the user asks "why did you trust that session?"

## Integration with `session_search`

If you're running inside Hermes, the native `session_search` tool is your semantic-adjacent pass — it has FTS5 over the session DB. Use this skill's workflow to *decide what to search for and how to rank the results*, then let `excavate.py` handle corpora that aren't in the session DB (exported logs, markdown notes, JSONL exports, another agent's transcripts).

```text
semantic-adjacent pass  →  session_search(query="...")        # Hermes session DB
keyword + structural    →  excavate.py dig ./exported-logs    # file-based corpora
```

## Common Pitfalls

1. **Searching one query and giving up.** The single biggest failure mode. Run at least three passes (exact, semantic-adjacent, structural). Artifacts are rarely filed under the first word you reach for.

2. **Trusting match count as relevance.** A session that mentions "docker" forty times while setting up a CI pipeline is not the answer to "how did we fix the docker permissions bug." Use the composite score, not raw hits.

3. **Skipping dedup and reporting three copies of the same fix.** Always run `--dedup` when `top > 1`. The user asked for the answer, not the archaeology of the answer.

4. **Extracting the whole session.** The transcript is the *site*, not the *artifact*. Quote minimally.

5. **Retrieving a decision without its rationale.** "We chose Postgres" is useless without "because we needed strong consistency for the ledger." Resolution and rationale travel together — extract both or neither.

6. **Assuming recency equals correctness.** A two-year-old session that solved the exact algorithmic problem beats yesterday's near-miss. Recency is a *tiebreaker*, weighted low by default for a reason.

7. **Digging without a survey.** If you can't state what artifact you want and what shape it takes, your query will be too vague to rank well. Spend ten seconds on the table in Phase 1.

8. **Forgetting structural pass.** The fix is often inside a fenced code block that doesn't repeat the keyword in prose. `--extract code` exists for this reason.

9. **Treating near-dups as separate finds.** Three sessions with the same stack trace are one problem, not three. Normalize before you count.

10. **Not citing the source session.** Always cite. The user may want to open the original; future you will want to re-excavate.

## Verification Checklist

- [ ] Survey written: the artifact type and query shape are stated before searching.
- [ ] At least two query passes run (one exact/keyword, one semantic-adjacent or structural).
- [ ] Results ranked with the composite score, not raw match count (`--explain` if using the script).
- [ ] Deduplication run when multiple results are returned.
- [ ] Extraction is minimal — failing state, change, success marker — not the whole transcript.
- [ ] Source session cited (path or session id).
- [ ] Decision artifacts include rationale, not just the chosen option.
- [ ] Recency weighted appropriately for the domain (low for stable, high for volatile).

## Further Reading

- `references/search-strategies.md` — the full playbook for the Locate phase: query expansion, negation, temporal constraints, and how to pick pass order.
- `references/relevance-scoring.md` — the math behind the composite score, normalization, and how to retune weights.
- `references/extraction-patterns.md` — extraction templates for fix, decision, command, and rejection artifacts.
- `references/deduplication.md` — exact, near-dup, and variant detection in depth.
- `references/cli-reference.md` — every `excavate.py` flag and subcommand.
- `scripts/excavate.py` — the implementation. Stdlib only, single file, importable.

---

*Prompt Archaeology: don't re-derive what you've already discovered. Excavate it.*
