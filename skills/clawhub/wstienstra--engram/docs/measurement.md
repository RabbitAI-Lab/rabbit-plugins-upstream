# How the numbers were measured

Measured 2026-09-18. Everything on this page comes from a four-arm battery over 74 labelled
questions against a real workspace of about 19,000 nodes and 22,000 associations, built up
over roughly a year of daily use. Two numbers are given throughout: the **baseline** is the
engine as v1.1.x shipped it, the **1.2.0** column is what this release does on the same
questions and the same database.

## Where the questions came from

Not from the database. A battery that generates its questions out of its own node names
measures whether full-text search can find a string it was just handed; that is how the
older seeded battery reported 95% while paraphrased questions failed.

These 74 questions were mined from session transcripts — every `recall` and `msgctx` query
a live agent or its owner really ran over 60 days — then labelled by hand with the node
that should have answered them. The classes:

| class | n | what it tests |
|---|---|---|
| `name_lookup` | 15 | the question names the thing |
| `nl_paraphrase` | 26 | same intent, different words from the stored text |
| `property_lookup` | 10 | a distinctive value: an address, a port, an email |
| `procedural` | 10 | how a task was done last time |
| `negative` | 13 | the answer is not in memory; the right reply is silence |

`nl_paraphrase` is the interesting class and it is weighted 2× in the headline. A memory
that only answers when you already know the name of the thing is an index, not a memory.

## The four arms

| arm | what it does |
|---|---|
| `engram_recall` | `engram recall "<q>" --compact` — the deep lookup |
| `engram_msgctx` | `engram msgctx "<q>"` — the per-message hook, the path in production |
| `md_bm25` | top-3 paragraphs from `MEMORY.md` + `memory/**/*.md`, IDF-weighted overlap |
| `md_naive` | what most agents do today: inject the whole of `MEMORY.md` every turn |

`hit@3` means an expected node appears in the arm's top three results. `tok` is characters
divided by four — what the arm would inject into the prompt. `tok/hit` is tokens spent per
useful fact recalled.

## Results

1.2.0, hit@3, all four arms:

```
arm             class             n   hit@1   hit@3     tok   tok/hit
---------------------------------------------------------------------
engram_recall   ALL              74     69%     86%    1421      1643
engram_msgctx   ALL              74     49%     62%      92       149
md_bm25         ALL              74     39%     49%     236       484
md_naive        ALL              74     31%     31%    1445      4649

headline (nl_paraphrase weighted 2x, hit@3):
  engram_recall    85.0%
  engram_msgctx    55.0%
  md_bm25          48.0%
  md_naive         31.0%
```

What 1.2.0 changed, per class, on the arm that answers questions:

| `engram_recall` hit@3 | baseline | 1.2.0 | `md_bm25` |
|---|---|---|---|
| `name_lookup` | 87% | **93%** | 47% |
| `nl_paraphrase` | 58% | **81%** | 46% |
| `property_lookup` | 70% | **80%** | 60% |
| `procedural` | 90% | **100%** | 40% |
| `negative` (abstains) | 85% | **85%** | 54% |
| **ALL** | 74% | **86%** | 49% |
| headline | 70% | **85%** | 48% |
| tokens per query | 1426 | **1421** | 236 |

Nothing regressed, and the gain is not paid for in tokens: the answer got 12 points better
at the same 1,421 tokens per query. The paraphrase class — the one that decides whether this
is a memory or an index — went from missing four questions in ten to missing two.

The per-message hook moved on the number that matters most for it:

| `engram_msgctx` | baseline | 1.2.0 |
|---|---|---|
| abstains on an unanswerable question | 15% | **62%** |
| ALL hit@3 | 53% | **62%** |
| tokens per query | 115 | **92** |

### One caveat on the paraphrase number

The table above is the shipped configuration's own measurement run — the code as it is
released, on the graph as it was when the gates were scored. The same battery re-run on that
workspace *after* its duplicate-merge pass had been applied gives 77% on paraphrase and 83%
headline instead of 81% and 85%: one paraphrase question out of 26 flipped, because merging
duplicates changes which nodes a question competes against even when it does not touch the
answering node itself. Re-running the battery with the previous engine on the same
post-merge graph reproduces that lower number exactly, case for case, so this is the effect
of a data change, not of a code change. It is reported here because a number that moves when
you clean the graph is a number a reader should know moves.

### Where the gain came from

Three changes, each measured on its own, each kept only because it paid:

* **Aliases and rare tags as name surfaces.** A node may carry `props.aliases`; a tag on a
  handful of nodes is treated like a name. "owner contact details" and a node called
  "Alice Johnson" share no word in any channel, so no amount of ranking reaches it. One
  alias does. This is the largest single share of the paraphrase gain.
* **A lexical-evidence bar on the abstention gate.** The cross-encoder's absolute score is
  ~0.000 for a genuine paraphrase *and* for an unanswerable question, so it cannot separate
  them. The gate now also asks whether a top candidate carries the query's rarest term.
  That is what took `msgctx` abstention from 15% to 62%.
* **Graph hygiene.** Orphan nodes — nodes with no edge at all — fell from 23.2% to 2.4% of
  the graph, and duplicate groups from 124 to 5. Hygiene is not cosmetic: it is what the
  last 7 points of paraphrase accuracy came from, after the ranking work had run out.

### The association channel

Ablation on the shipped graph, association expansion off against on:

| | assoc off | assoc on |
|---|---|---|
| ALL hit@3 | 84% | **86%** |
| headline | 82% | **85%** |
| tokens per query | 1187 | 1421 |

+2 points of hit@3 and +3 of headline, for 234 extra tokens. In 1.1.x the same ablation
measured **+0.0** — the graph was carrying no weight at all. It does now, but it is still
the least profitable part of the system per token, and saying so is the point of this page.

## What this says, including the parts that do not flatter Engram

1. **`recall` beats grep on hit rate by 25 points at hit@3** (74% against 49%), and by 50
   points on procedural questions.
2. **`msgctx` is 2.2× more token-efficient than grep** per useful fact: 218 tokens against
   484. Against the file-dump default it is 21× better — 218 against 4,649.
3. **`recall` buys its accuracy at 6× the token cost** of a markdown search: 1,426 tokens
   per query against 236. Nothing in 1.2 lets you spend `recall` accuracy at `msgctx`
   prices. That gap is the next release's job.
4. **`msgctx` is level with grep on hit rate**: 53% against 49%, inside the noise. Its win
   is efficiency, not accuracy.
5. **`msgctx` abstains on 62% of unanswerable questions**, up from 15%, and `recall` on
   85%. Better, not solved: the hook still answers about four unanswerable questions in ten
   with roughly 92 tokens of irrelevance. It is the largest known defect in 1.2.0.
6. **`msgctx` hit@3 gained 9 points and `recall` gained 12.** Every retrieval improvement in
   this release lands hardest on `recall`, and `recall` is not the path that runs on every
   message. Closing that gap is the next release's job.
7. **The association channel adds +2 points at hit@3**, for 234 extra tokens per query. It
   was +0.0 in 1.1.x. The graph now earns its keep, narrowly.
8. `md_naive` is flattered here. The arm injects `MEMORY.md` and `memory/**/*.md` only —
   1,445 tokens. A real agent's per-turn markdown load in the measured workspace was about
   41 KB, roughly 7× more.

## Reproducing this

The battery harness and its 74 labelled questions are not in this repository. The questions
are real messages from a private workspace, and the labels point at nodes in that
workspace's database; publishing either would publish the memory itself.

The method is the whole of this page and it is portable: mine your own agent's recall
queries, label the node that should answer each one, and run the four arms. The two Engram
arms are single CLI calls; the two markdown arms are twenty lines of scoring each.

What does ship, and what you can run today:

- `engine/engram-seed-battery.py` — mines 20 cases from your own migrated content, adds 3
  negative controls, gates at 90% plus 3/3. This is install verification, not a quality
  measurement: its questions come from the database, so it flatters keyword matching.
- `engine/engram-battery.py` — the larger battery, with mined and adversarial classes and
  per-class scoring.
- `ci/run-battery.sh` — build freshness, fixture, every shipped tool, first recall on a new
  database, battery.
- `engine/engram-hygiene.py` — the orphan and duplicate counts above, on your own graph.
  Dry-run by default, on a read-only connection.

Both batteries fail with exit 1 if the engine crashes rather than scoring the crash as a
miss. That was not true before 1.2.0, and it is the reason the fresh-install crash above
shipped.
