# Maintenance — Keeping What Was Earned

Read when a topic passes verification, when a skill has gone rusty, and at every `## Due` maintenance touch. A verified topic without a maintenance row is a topic being deleted slowly (SKILL.md Rule 9).

**Contents:** [Setting the First Interval](#setting-the-first-interval) · [Decay by Skill Type](#decay-by-skill-type) · [What a Maintenance Touch Is](#what-a-maintenance-touch-is) · [Growing the Interval](#growing-the-interval) · [Recovering a Rusty Skill](#recovering-a-rusty-skill) · [Retiring a Skill on Purpose](#retiring-a-skill-on-purpose) · [Maintaining Many Topics](#maintaining-many-topics)

## Setting the First Interval

At the moment a topic reaches Retention level (`verification.md`), set the first maintenance touch at **the last interval that worked** — the interval the topic's items survived in the review queue, typically 30-90 days for knowledge-heavy topics and longer for procedural ones. Write it as a `## Due` row in the same turn.

Two derivations, both honest:

- The topic has queue history → use the median current interval of its items.
- It has none (a project-based skill, a physical skill) → start at **30 days**, then apply the growth rule below. Thirty days is short enough that the first failure is cheap and informative.

There is no interval that is safe for all skill types, which is why the table below exists rather than a single number.

## Decay by Skill Type

Ordered by how fast an unused skill degrades:

| Type | Decays | Practical touch interval | What survives longest |
|---|---|---|---|
| Arbitrary facts (vocabulary, dosages, shortcuts) | Fastest | 30-60 days | Nothing without retrieval |
| Domain knowledge with structure | Fast | 60-90 days | The structure; the details go first |
| Formal procedures (proofs, methods, syntax) | Medium | 90 days | The shape of the method, not its details |
| Judgement and taste | Slow | 3-6 months | Recognition of quality; production slips first |
| Motor and procedural skills | Slowest | 3-12 months | Coordination; speed and precision go first |

The two useful implications: **recognition outlives production everywhere** — a rusty learner reads before they can write and understands before they can speak — and a mixed topic decays at the rate of its fastest component, so schedule the touch against that component.

## What a Maintenance Touch Is

Not a study session. A short, cold **performance** of the exit test or a slice of it.

| Topic type | A valid touch |
|---|---|
| Language | 20 minutes of unscripted conversation or writing, no preparation |
| Programming | Solve one non-trivial problem from a blank file |
| Formal | Re-derive one central result without notes |
| Motor | Perform one piece or routine cold, recorded |
| Fact-dense | 20 items from the queue, cold, plus one structure question |
| Judgement | One brief attempted and checked against the rubric (`practice.md`) |

Rules that keep it a measurement rather than a ritual:

- **Cold, and no warm-up.** A warmed-up touch measures nothing and grows the interval on false evidence.
- **10-30 minutes.** Longer means it became a study session and will be skipped next time.
- **Record the result** in `sessions/<year>.md` and update the `## Due` row. A touch with no recorded outcome cannot grow or shrink the interval.

## Growing the Interval

Same shape as the review formula (`schedule.md`), applied to whole topics:

```
clean touch  → next interval = current × 1.5
shaky touch  → next interval = current (unchanged)
failed touch → next interval = current ÷ 2, and the topic drops a level in ## Topics
```

Worked example, a language at 60 days: clean → 90 → 135 → 200 → 300, with those touches landing on days 60, 150, 285 and 485. Two clean years leave the interval near 300 days — roughly annual, which is about the floor for anything worth having kept.

A failed touch is not a crisis: it is the interval doing its job. Drop the level in `## Topics`, halve the interval, and run one recovery session (below) rather than re-planning the whole topic.

## Recovering a Rusty Skill

Faster than first learning — the savings effect — and squandered by restarting from the beginning.

1. **Measure first.** Attempt the exit test cold, and write what specifically failed into `## Error Log` — one row per failure, with the misconception behind it. Do not read anything before this step; reading destroys the measurement.
2. **Expect the recognition/production split.** What is gone is almost always production. Train output, not input: speak, write, build, play — not re-read.
3. **Rebuild from the error list of the attempt**, not from the curriculum. Recovery is targeted or it is a re-run.
4. **Budget roughly 10-30% of the original hours** for a skill unused for a year or two, more if it was never past Application level. Say the estimate as a range, as always (Rule 8).
5. **Reset the queue rather than grading through it** if the lapse exceeded ~60 days (`schedule.md`).
6. Set a shorter maintenance interval than before on the way out — the previous one demonstrably failed.

## Retiring a Skill on Purpose

Deciding not to maintain something is a legitimate, and underused, decision.

- Mark it `retired <date> (<reason>)` in `## Topics`. Keep the plan and the queue file rather than deleting them: the savings effect makes the record valuable if it is ever picked up again.
- Remove its `## Due` row in the same turn, or it becomes a recurring reminder of a decision already made.
- Suspend rather than delete its queue items (`schedule.md`).
- Cancel the associated subscription in `~/Clawic/data/finances/subscriptions.md`.
- Write one line on what was gained, as the reason clause of the `## Topics` row — `retired <date> (<reason>)`. A retired skill is not a failed one, and that clause is what stops it being remembered that way (`plateaus.md`).

## Maintaining Many Topics

Maintenance is cheap per topic and adds up.

```
weekly maintenance load ≈ Σ (touch_minutes ÷ interval_days) × 7
```

Six topics at 20 minutes on 90-day intervals ≈ 9 minutes a week. Twelve topics at the same 20 minutes on 30-day intervals ≈ 56 minutes a week, which is a second learning project nobody planned.

Controls, in order:

1. **Grow the intervals** — the cheapest lever, and it costs nothing on clean touches.
2. **Stagger the `## Due` dates** so touches do not land in the same week. Check for clustering when adding a row.
3. **Combine touches** where topics genuinely overlap: one task that exercises two skills is one touch, not two.
4. **Retire something.** If the load competes with active learning, the honest move is a retirement, not a compressed schedule that gets skipped anyway.

Every touch writes its result to `sessions/<year>.md` and updates the interval and next date in the `## Due` row of `memory.md`; a failed touch also drops the level in `## Topics` with its date. A retirement clears the `## Due` row, sets the topic's status, and cancels any subscription row in `~/Clawic/data/finances/subscriptions.md`. Formats in `memory-template.md`.
