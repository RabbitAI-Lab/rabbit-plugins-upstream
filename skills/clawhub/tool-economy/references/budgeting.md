# Tool Budgeting

A *tool budget* is a soft estimate of how many tool calls a task should cost.
You set it before starting, compare against it while working, and reconcile at
the end.

## Estimating a Budget

Break the task into sub-goals and count expected calls per sub-goal:

| Sub-goal                  | Typical cost |
|---------------------------|--------------|
| Read N files (batched)    | 1 call       |
| Search codebase           | 1 call       |
| Edit a file               | 1 call       |
| Run tests / build         | 1 call       |
| Create a file             | 1 call       |
| Verify result             | 1 call       |

Add them up. That is your budget. Example: "refactor function X and update tests"
might budget as:

```
read file(s)      : 1   (batched)
patch source      : 1
patch tests       : 1
run tests         : 1
verify            : 1
--------------------
total             : 5 calls
```

If you find yourself at call 8 and not done, **stop and replan** — something is
wrong (you're re-reading, serializing, or using weak commands).

## Tracking During the Task

Keep a mental or explicit tally:

- **Under budget** → proceed normally.
- **At budget, not done** → audit for waste before continuing.
- **Over budget** → stop; run `analyze_session.py` on the log so far, find the
  leak, then replan the remaining work.

## Reconciling After the Task

Run the analyzer on the full session:

```bash
python3 scripts/analyze_session.py scripts/sample_session.json
```

Key metrics:

- **Redundant calls** — exact duplicates within a window (default 10 calls).
  Each is pure waste.
- **Serializable-but-parallel** — independent calls issued in separate turns.
  Each adds ~1 extra round-trip of latency.
- **Overhead** — estimated extra round-trips × a per-call latency constant
  (default 300ms, configurable).
- **Score** — 100 minus penalties, clamped to [0, 100].

### Score Bands

| Score | Meaning                                    |
|-------|--------------------------------------------|
| 90+   | Excellent — nearly zero waste              |
| 70–89 | Good — minor batching/caching gaps         |
| 50–69 | Fair — several wasteful patterns present   |
| <50   | Poor — re-architect the workflow           |

## Adjusting the Budget Over Time

Keep a note of *actual* vs *budgeted* calls for recurring task types. If a kind
of task consistently runs 2× over, either the budget was naive or the workflow
has a structural inefficiency. Fix the workflow, not the budget.
