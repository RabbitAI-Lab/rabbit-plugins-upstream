# What The Agent Remembers — Written, Indexed, Read

Scope: the notes, memory, and state files the agent keeps *for the user* across sessions. This is the audit of someone else's memory system; the files this skill writes for itself are described in `memory-template.md`.

**Before this pass**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for the recorded memory roots and last measured size, and `## Accepted` for directories the user has already declared intentionally messy.

**Contents:** [The Three Failures](#the-three-failures) · [Is The Read Order Real](#is-the-read-order-real) · [Index Drift](#index-drift) · [Contradictions](#contradictions) · [Growth And Consolidation](#growth-and-consolidation) · [Declared Versus Observed](#declared-versus-observed) · [Retrieval Test](#retrieval-test) · [Privacy Of Remembered Content](#privacy-of-remembered-content) · [Repair Order](#repair-order) · [Write It Down](#write-it-down)

## The Three Failures

Every "the agent forgot" complaint is exactly one of these. Diagnose in order; each test is one command.

| Failure | Test | Fix |
|---|---|---|
| **Not written** | Grep the memory tree for the fact. Absent | The instruction that should have produced it says "remember/track/note" without naming a destination file. Name the file. |
| **Written, not indexed** | Present in a file; the file is not in the index and nothing points to it | Add the index line — with a read condition, not just a path |
| **Indexed, not read** | Present and indexed; the instruction to read it is conditional or missing | Make the read order unconditional (below) |

The third is the expensive one because everything looks correct: the data is there, the index is there, and it is never opened.

## Is The Read Order Real

An instruction to read stored data is only real if the agent can evaluate its condition at the top of a session with no prior context. Test each read instruction against that bar:

| Instruction | Verdict |
|---|---|
| "Read `state.md` at the start of every session" | Real — unconditional |
| "Read `state.md`, then open whatever its index names when that line's condition applies" | Real, and it survives files created after the instruction was written |
| "On first use, read the setup notes" | Dead from session two — the agent cannot tell that this is not the first use |
| "If you already know the user, skip this" | Dead — unevaluable |
| "When relevant, check the notes" | Dead — relevance is decided by what is in the notes, which have not been read |
| A list of specific filenames to read | Half dead — every file created after the list was written is invisible |

Findings here are WARNING at least, and CRITICAL when the unread data is what prevents a destructive mistake (a "never touch X" note, a client constraint, an allergy, a deployment gotcha).

Second-level reads have the same defect: a file reachable only from another file is read only when the intermediate was read. Point at it from the entry point instead (`workspace.md`).

## Index Drift

Two set differences over the memory tree, in both directions:

- Files present but not indexed → orphans. Rank by size and by recency: a note written yesterday and never indexed is a fresh failure of the writing rule, not old debris.
- Index lines whose file is missing → dangling. Every one is listed in full.
- Index lines with no read condition → present but useless: a pointer nobody knows when to open. Report as INFO, action "add the condition".

Detection is a listing versus a grep of the index file; it costs nothing and it is the single highest-yield check in this file.

## Contradictions

Two entries about the same subject with different values (a preference, a threshold, a name, an address). The agent will read one of them. Find them by taking the keys the memory claims to hold and counting distinct values per key.

Resolution rule: newest wins, the older line is deleted rather than annotated, and if both are recent, ask once — this is one of the few places a single question is cheaper than a wrong guess. Never leave both.

A special case worth its own check: an **observation contradicting a declaration**. What the user stated (a preference, a rule) outranks what the agent inferred, always. An inferred value sitting in a config-shaped file is a finding on its own — it moves to the observation side and the declaration is restored.

## Growth And Consolidation

| Signal | Threshold | Action |
|---|---|---|
| Total memory tree | `memory_budget_mb` (default 5 MB), or doubling since the last baseline | Consolidate before archiving; archiving unread duplicates preserves the mess |
| Date-named files | more than ~30 unconsolidated | Summarize into the durable file, then archive the raw ones; keep raw for 30 days |
| A single section inside one file | ~40 lines or ~15 entries of real content | Split into its own file with identical headings, delete the section, add the index line |
| Repetition | the same fact restated in 3+ places | One canonical home, pointers elsewhere (`workspace.md`) |
| Entries with no date | any | Undatable entries cannot be aged out, so they never leave |

Consolidation is lossy on purpose: a summary keeps the fact and drops the narration. The test for a good consolidation is whether the next session can act on the summary without opening the raw file.

## Declared Versus Observed

A healthy memory system separates them, and the audit checks that the wall is intact:

- **Declared** — what the user said they want. Lives in a config file, changed only by the user, never overwritten by an inference.
- **Observed** — what the agent noticed. Lives in the memory file, freely rewritten.

Findings: preferences recorded in the memory file (they will be rewritten away), inferences recorded in the config file (they will outrank a real preference), and any place where the agent overwrote a stated preference with an observation. That last one is WARNING minimum — it is the mechanism by which a system slowly stops doing what it was told.

## Retrieval Test

The functional check, cheaper than any structural one: take three facts the memory claims to hold — one recent, one old, one from a file that is deep in the tree — and verify each is reachable from the entry point by following only unconditional instructions and index lines with conditions that today's context satisfies. Any fact that is not reachable is a finding whose evidence is the path that ran out.

Report as `3/3 reachable` or name the ones that failed and where the chain broke. This is the sentence a user actually understands.

## Privacy Of Remembered Content

Memory files accumulate whatever passed through, which means they inherit two rules:

- Credentials: a memory tree is one of the highest-yield places to scan, because the agent writes there by default (`secrets.md`).
- Sensitive personal content: health, financial, or third-party personal data stored in a general notes file, unencrypted and backed up wherever the workspace goes. Report as a WARNING naming the file and the category — never quote the content — with the action of moving it to the box that owns that data class or dropping it.

## Repair Order

1. Fix the read order first. Everything else is invisible until something reads it.
2. Repair dangling references; they are cheap and each is a broken read.
3. Resolve contradictions; wrong data is worse than missing data.
4. Index the orphans that matter, delete the ones that do not.
5. Consolidate and archive last — it is the only step that destroys evidence for the previous four.

## Write It Down

Same turn as the pass:

- Memory roots, entry point, index location, measured size, retrieval-test result → `## System Baseline` in `memory.md`.
- Broken read order, dangling references, contradictions, unindexed recent notes → `## Open Findings`, each with the file and the failing chain.
- A directory the user keeps unindexed on purpose → `## Accepted` with a path glob and a review date.
- A consolidation or migration procedure that worked → `~/Clawic/data/analysis/artifacts/memory-repair-<kebab>.md`, plus its `## Boxes` line.
