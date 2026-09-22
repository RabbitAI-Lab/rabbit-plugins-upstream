# Changelog

All notable changes to Engram. This project follows [semantic versioning](https://semver.org).

## 1.2.0 — 2026-09-21

### Fixed

- **Every fresh install of v1.1.x crashed on its first recall.** `CREATE TABLE` did not
  declare the `last_touched` and `touch_count` columns on `nodes` or `strength` on
  `associations`. `ensure_dynamics_columns()` adds them, but nothing called it before
  `cmd_recall` selected `a.strength`, so a brand-new database raised
  `sqlite3.OperationalError: no such column: a.strength` on the first question asked of it.
  Databases created before the bug never saw it, which is why it survived from 2026-07-05
  to 2026-09-18. The columns are now declared in `CREATE TABLE`;
  `ensure_dynamics_columns()` stays as the upgrade path for existing databases, and
  `CREATE TABLE IF NOT EXISTS` makes the change invisible to them.
- The seeded battery scored a dead engine as a partial pass. It discarded stderr and the
  exit code, and counted an empty result as a *passing* negative control, so an engine that
  could not start reported 3/23 with three green ticks. Both batteries now fail the whole
  run on any non-zero exit or traceback, and a negative control passes only when the engine
  ran and gave an explicit abstain. The 90% gate rounds up instead of truncating.
- `install.sh` wrote `semantic_mode: onnx` even when the preflight had just found no numpy
  and no onnxruntime, so the first recall died on an import. It now writes what the
  preflight found.
- `install.sh` skipped missing engine files silently. A missing file is now fatal.
- The daemon socket and pid file moved from `/tmp` into `engram/`, so two workspaces on one
  machine no longer collide.
- **Two unrelated notes could silently supersede each other, and one of them vanished from
  recall.** Auto-supersede fires on a fuzzy name match above 0.85, and the fuzzy score added
  `0.3 + 0.2 × shared words` — counting *every* shared word, stop words included. "RULE:
  Always write the changelog entry in the same commit as the version bump" and "RULE: Every
  promise becomes a ticket in the same turn it is made" share `rule:`, `the`, `in` and
  `same`: four words, score 1.1, and the first rule was marked superseded by the second and
  hidden from every query. Anything that prefixes names with a type — which is every
  workspace built by the markdown migration — was exposed. Overlap is now counted on
  distinctive words only and the score is capped at 1.0.
- **The name-match channel was silently dead on every graph smaller than about 8,000
  nodes**, which means on every fresh install. Its evidence bar was an absolute IDF sum of
  9.0, but the largest IDF possible on a 28-node database is log(28) = 3.3, so no name hit
  could ever clear it. The same arithmetic applied to the abstention gate's IDF-mass bar.
  Both bars are now expressed as a fraction of log(corpus size), and reproduce their
  calibrated values exactly on the graph they were measured on.

### Added

- **Aliases** — a node may carry `props.aliases`, a list of the words a person would
  actually use for it. Full-text search picks them up free (the `props` column is already
  indexed), the vector index embeds them with the name, and the name channel treats each one
  as an alternative name — which makes an aliased node pin-eligible whatever its type. This
  is the only general fix for the vocabulary gap: "owner contact details" and a node called
  "Alice Johnson" share no word in any channel, so no amount of ranking reaches it.
  `engram-aliases.py` writes a curated spec and re-embeds just those nodes;
  `aliases.example.json` is the template.
- **Rare tags act as names.** A tag on a handful of nodes is as distinctive as a proper noun
  and is the word people actually type. A tag below a document-frequency cap can now pin its
  nodes into the candidate pool — gated on the corpus frequency of the tag *word*, not of the
  tag, because a tag is often rare only because nobody reused it. Tag pins never vouch for
  the answer: letting them satisfy the abstention gate cost the negative class 39 points.
- **Lexical evidence on the abstention gate.** The cross-encoder's absolute score is ~0.000
  for a genuine paraphrase *and* for an unanswerable question, so it cannot separate them.
  The gate now has a second, independent way to be satisfied: does a top-ranked candidate
  contain the query's rarest term, or enough IDF mass across the terms it does contain. This
  is what took `msgctx` abstention from 15% to 62%.
- **`engram-hygiene.py`** — `tier`, `merge` and `link` as three separately runnable,
  separately reversible steps. Counts only unless given `--apply`, and a dry run opens the
  database read-only. Merging is not idempotent, so each applied step leaves a marker in
  `config` and refuses to repeat itself without `--force`. Duplicate groups need identical
  normalised name and type, or cosine ≥ 0.97 *and* name-token Jaccard ≥ 0.6 *and* content
  lengths within 20% — anything looser destroys facts, so ambiguous pairs go to a review
  file for a human instead.
- **`engram-maintenance.py`** — the weekly health job: junk nodes, type casing, stale
  vectors, orphans, duplicates, integrity, hot-node cache.
- **`--no-llm` on `engram-sleep.py`** — skip every LLM call and write the deterministic
  digests. Measured over 75 nights on a live graph: 314 of 340 segments distilled to
  nothing, at about 2.5 minutes of local GPU each. The deterministic night finishes in under
  a second.
- **Task ledger** — `engram task add|list|show|update|done|probe`. A durable record of work
  that outlives a session: each task carries a brief that can respawn it, an evidence
  command whose exit code decides whether it is really done, a status and a staleness
  clock. `task done` refuses to close a task whose evidence command fails.
- **IDF gate on `msgctx`** — the Strategy-2 OR search now requires a rare term before it
  fires, instead of matching on whatever common word the message happened to contain.
- **`build.py`** — five engine files are now generated from their upstream sources by a
  rename map, replaced regions and a leak gate that refuses to write if a private name,
  path, email, id or internal document reference survives. `--check` fails when a
  checked-in file is stale, `--list` prints what comes from where. Until now the engine was
  a hand-maintained copy that had drifted from its upstream since 2026-07-05; everything in
  this release arrived through the build, not by hand-copying.
- **CI** — `ci/make-fixture.sh` builds a throwaway synthetic workspace under `/tmp`;
  `ci/run-battery.sh` runs four gates: build freshness, migrate plus every shipped tool, a
  first recall on a brand-new database, and the seeded battery. Gate 3 exists because gate 4
  used to lie. Both fresh-install bugs above were found by this gate, not in review.
- `install.sh` smoke stage: stores one node and recalls it before touching any markdown.
  It catches the class of bug above at install time rather than at first use.

### Changed

- `SKILL.md` and `README.md` rewritten. They described a hand-maintained engine and a flow
  that no longer matched the installer.
- **Retrieval quality, measured on 74 hand-labelled questions mined from 60 days of real
  agent traffic against a 19,000-node workspace — same questions, same database, before and
  after.** Full method and the parts that do not flatter Engram:
  [docs/measurement.md](docs/measurement.md).

  | `engram recall`, hit@3 | 1.1.x | 1.2.0 |
  |---|---|---|
  | paraphrased questions | 58% | **81%** |
  | all classes | 74% | **86%** |
  | headline (paraphrase weighted 2×) | 70% | **85%** |
  | tokens per query | 1426 | **1421** |

  No class regressed, and the accuracy is not paid for in tokens. (The paraphrase figure is
  the shipped configuration's own gate run; on the same workspace after its duplicate-merge
  pass the same battery gives 77% and an 83% headline, because merging duplicates changes
  what a question competes against. Re-running the previous engine on that same post-merge
  graph reproduces the lower number case for case, so it is a data effect, not a code one.) `msgctx` abstention on
  unanswerable questions went from 15% to **62%** and its hit@3 from 53% to **62%**, at 92
  tokens per query instead of 115. Association expansion, measured by ablation on the
  shipped graph, is worth **+2 points of hit@3 and +3 of headline** — it was +0.0 in 1.1.x.
- **Graph hygiene on the measured workspace**: orphan nodes (no edge at all) fell from 23.2%
  to **2.4%**, duplicate groups from 124 to **5**. This is where the last 7 points of
  paraphrase accuracy came from, after the ranking work had run out.
- The weekly duplicate warning was a false alarm by construction: it grouped on the first
  three words of a name, which reported 304 groups on the measured graph, 132 of them daily
  reflections that share a prefix and nothing else. It now uses the same three guards as the
  merge, and warns above 20 groups instead of 5.

### Known

- **Tiering ships switched off, and is experimental.** `nodes.tier`, the archive rule and
  `recall --all` are all in this release, but nothing marks a node `archive`, so the filter
  is a no-op. Turning it on costs 16 points of recall headline, because the ranking constants
  (`NAME_MATCH_MAX_DF`, `GATE_EVIDENCE_DF_MAX`, the IDF floors) count document frequency over
  `nodes_fts`, which indexes archived nodes too — so archiving half the graph changes what
  every threshold means without changing any threshold. **Whoever turns tiering on must make
  document frequency tier-aware first**: a tier-filtered FTS index, or df computed over the
  visible corpus. On the measured workspace 65% of the graph is transport exhaust, which
  makes this the largest remaining token win and the reason it ships off rather than not at
  all.
- `msgctx` abstains on 62% of questions that have no answer in memory, up from 15%. It still
  answers the rest with about 92 tokens of irrelevance, and it is the one path that runs on
  every message. Largest known defect.
- Every retrieval gain in this release lands hardest on `recall`: +12 points of hit@3 against
  `msgctx`'s +9. `recall` is not the path in production.
- The association channel adds +2 points at hit@3 for 234 extra tokens per query — it earns
  its keep now, narrowly. See [docs/measurement.md](docs/measurement.md).
- `engram-sleep.py` and the other engine files without an upstream twin are still maintained
  by hand. `build.py --list` shows which five are generated; the rest are the remaining
  drift surface.

## 1.1.2 — 2026-07-05

- Migration parses per bullet; explicit type markers win over inferred types.

## 1.1.1 — 2026-07-05

- First public release.
