# Token Spend — Where It Goes And What Actually Reduces It

**Before answering any spend question**, read `## Spend` in `~/Clawic/data/analysis/memory.md` — or `spend-log.md` if the `## Boxes` index points there. A current number with no prior month is not an answer, and "it feels expensive" is not a baseline.

**After any spend review**, write the month row back in the same turn: the amount with its currency, the `As of` date, the top three drivers, and any saving that landed (`memory-template.md`).

**Contents:** [The Four Terms](#the-four-terms) · [The Quadratic Term](#the-quadratic-term) · [Cache Invalidation](#cache-invalidation) · [Tool Output Dumps](#tool-output-dumps) · [Fan-Out](#fan-out) · [Anomaly Detection](#anomaly-detection) · [Reduction Ladder](#reduction-ladder) · [Per-Run Budgets](#per-run-budgets) · [Model Routing](#model-routing) · [Sweep](#sweep) · [Write It Down](#write-it-down)

## The Four Terms

Nearly all spend is one of four things, and they respond to completely different fixes. Attribute before optimizing.

| Term | Grows with | Cheapest lever |
|---|---|---|
| Always-loaded context | bytes × turns | Trim the set (SKILL.md Rule 8) |
| Conversation history | turns² | End sessions; start fresh for a new task |
| Tool output pulled into context | bytes returned | Filter at the source: grep and head instead of whole files |
| Parallel or nested runs | fan-out × everything above | Bound depth and breadth (`sessions.md`) |

Output tokens are usually the smallest term by count and the most expensive per token; input dominates by volume in agentic work. Say which term you measured before recommending anything — a suggestion to "write shorter answers" against a quadratic-history problem changes nothing.

## The Quadratic Term

In a linear conversation the whole history is resent on every turn. If each turn adds `t` tokens:

```
total input over N turns ≈ t × N² / 2
```

At `t = 1,500` and `N = 50` that is about **1.9 million input tokens** for one session. Doubling the session length quadruples the input. This is why "one long session per day" costs several times what the same work costs split into task-sized sessions, and it is the single largest avoidable term in most setups.

Caching changes the *price* of those tokens, never the count — and only while the prefix stays identical, which is the next section.

## Cache Invalidation

Prefix caching pays only when the beginning of the context is byte-for-byte identical between turns. One volatile line at the top of an always-loaded file — a timestamp, today's date, a counter, a "last updated" stamp, a random session id — invalidates the whole prefix on every single turn, and the bill rises with no change in behavior.

- **Signature**: spend up sharply, usage flat, cache-hit ratio near zero on a workspace nobody restructured.
- **Fix**: make the prefix stable. Volatile content moves to the end of the context or out of the always-loaded set entirely; dates get injected at the point of use, not at the top of an instruction file.
- **Check it directly**: diff the assembled always-loaded content between two turns. Any difference that is not user content is the leak.

## Tool Output Dumps

A tool result enters the context and stays there for the rest of the session, so a single 200 KB file read costs its ~50k tokens once and then pays the history tax on every subsequent turn.

| Habit | Cost | Instead |
|---|---|---|
| Reading a whole file to check one value | Whole file, forever | Grep for the line, read a window around it |
| Listing a large tree | Thousands of paths | Filter by name or depth first |
| Dumping raw command output | Whatever it printed | Pipe through a filter; keep the shape, drop the volume |
| Re-reading a file already in context | Twice the bytes, plus confusion about which copy is current | Reference the earlier read |

The re-read case doubles as a `performance.md` finding: the same file read three or more times in one session is both a latency and a spend signal.

## Fan-Out

Nested runs multiply every term above. Cost scales with `breadth ^ depth`, so three subagents at depth 2 is nine runs, each carrying its own context. Findings: unbounded depth, spawns with no completion condition (`sessions.md`), and fan-out inside a scheduled job — which multiplies again by runs per day.

## Anomaly Detection

A threshold on absolute spend fires constantly in a growing setup and never in a shrinking one. Use dispersion instead, on daily totals:

```
MAD = median(|xᵢ − median(x)|)     over the trailing 14 days
alert when today > median + 3 × MAD
```

MAD survives the few huge days that would wreck a mean-and-standard-deviation rule. With very stable spend, MAD can approach zero and everything alerts — floor the threshold at `median × 1.5` to prevent that. Both numbers go next to the month row in `## Spend`, because a threshold nobody wrote down is re-derived differently every quarter.

Investigate an anomaly in this order: a new always-loaded file (Rule 8), a broken cache prefix, a new or more frequent schedule, a fan-out, a runaway session. The first two explain most of them.

## Reduction Ladder

Cheapest and most reversible first. Stop when the number is acceptable — beyond that, the optimizing costs more than it saves.

1. **End long sessions.** Free, immediate, attacks the quadratic term.
2. **Trim the always-loaded set.** Move rarely-needed depth behind an explicit read; every KB removed is paid back on every turn of every session.
3. **Stabilize the cache prefix.** No behavior change at all, and it can move the bill by a large fraction where caching applies.
4. **Filter tool output at the source.** Grep instead of read, head instead of cat, targeted listings.
5. **Lower schedule frequency, or make jobs exit early.** `runs_per_day = 1440 / interval_minutes` multiplies whatever a run costs (`scheduled.md`).
6. **Bound fan-out.** Depth 2 by default.
7. **Route small work to a smaller model.** Real savings, real quality risk; last because it is the only step that changes output.

## Per-Run Budgets

Unattended work needs a ceiling or a loop will find the limit for you. Derive it rather than guessing: `per_run_ceiling = monthly_budget / runs_per_month`, then set the actual limit at two to three times the measured p95 of a healthy run — if that number exceeds the ceiling, the schedule is unaffordable at that frequency and the frequency is the finding, not the run.

## Model Routing

Where several models are available, the audit checks that the routing that was decided is the routing that happens: a rule that says "small model for classification" is only real if the classification path cannot silently escalate. Findings: a routing rule with no enforcement point, an expensive model used for mechanical work (reformatting, extraction, greppable lookups), and a cheap model used where a mistake is expensive. Route by *consequence of being wrong*, not by how interesting the task looks.

## Sweep

| Check | Passing looks like |
|---|---|
| Month row current with `As of` date | Amount with currency, top three drivers |
| Always-loaded set measured | Under the recorded baseline, or the growth explained |
| Cache prefix stable | No volatile line above user content |
| Session length habit | Task-sized sessions, not one all-day thread |
| Schedules costed | runs/day × per-run cost recorded per job |
| Fan-out bounded | Depth and breadth limits on record |
| Anomaly threshold recorded | Median and MAD from the trailing 14 days |
| Per-run ceiling on unattended work | Derived from the budget, not guessed |

## Write It Down

Same turn as the pass:

- Month row: amount with currency, `As of` date, top three drivers → `## Spend` in `memory.md` (splits to `spend-log.md`; re-checking the current month **overwrites** its row, never adds a second).
- Anomaly baseline (median, MAD, floor) and the measured always-loaded size → `## System Baseline`.
- Each saving with its date and estimated monthly effect → the optimization rows of `## Spend`. Without it, the same trim is rediscovered every quarter and nobody can say what the last one was worth.
- Paid external services → the shared `~/Clawic/data/finances/subscriptions.md`, amount with currency.
- Overspend that is not yet fixed → `## Open Findings`; a deliberate expensive habit the user defends → `## Accepted` with a review date.
