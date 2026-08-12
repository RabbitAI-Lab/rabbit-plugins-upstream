# Time — Fitting Learning Into a Week That Is Already Full

Read when sessions are not happening, when the plan assumes hours that do not exist, and when deciding what to cut. Read `sessions/<year>.md` first: the measured hours are the input to everything here, and they are almost always lower than the declared `weekly_hours`.

**Contents:** [Measure Before Planning](#measure-before-planning) · [Frequency Beats Duration](#frequency-beats-duration) · [The Minimum Effective Dose](#the-minimum-effective-dose) · [Session Sizing](#session-sizing) · [What to Cut First](#what-to-cut-first) · [Energy, Not Just Hours](#energy-not-just-hours) · [Sleep and Consolidation](#sleep-and-consolidation) · [Learning Around a Job](#learning-around-a-job) · [Restarting the Habit](#restarting-the-habit)

## Measure Before Planning

Plans fail against the imagined week, not the real one.

```
measured_weekly_hours = Σ minutes in sessions/<year>.md over the last 4 weeks ÷ 4 ÷ 60
```

- If measured is under **60% of declared** for two cycles, the declared number is wrong. Change `weekly_hours` to the measured figure and re-size the plan (`curriculum.md`). Exhortation has a zero success rate here and costs the plan's credibility.
- Count only sessions with a retrieval step and a production step. An hour of watching is not an hour of the budget the plan was sized against.
- Two weeks of honest measurement before committing to a long plan is the cheapest possible insurance against a six-month plan that fails in month two.

## Frequency Beats Duration

Four 45-minute sessions beat one 3-hour session at equal total time, and the gap widens with time between the session and the test. Three reasons, all mechanical:

1. **Spacing.** Four sessions give three overnight gaps; one session gives none, so almost nothing is spaced (`schedule.md`).
2. **Startup cost is real but small** — roughly 5 minutes per session to reload context, and it shrinks when the next session's first item was named at the previous close (Session Shape, `SKILL.md`).
3. **Consolidation happens between sessions**, not within them, and is sleep-dependent for motor skills especially (`domains.md`).

The practical consequence: when the week collapses, cut session **length**, never session **count**. Five 15-minute sessions preserve the schedule; one 75-minute session on Sunday does not.

## The Minimum Effective Dose

The smallest session that still counts, by purpose:

| Purpose | Minimum | What it contains |
|---|---|---|
| Keep a queue alive | 5-10 min | Due reviews only, up to `daily_review_limit` |
| Keep a topic warm | 15 min | Retrieval of last session + one production attempt |
| Make progress | 30-45 min | The full Session Shape |
| Deep or messy work (projects, proofs, composition) | 60-90 min | The above, plus room for a real block of the hard thing |

Above ~90 minutes, returns fall off sharply for most learners and error rates rise; if a longer block exists, break it with a real gap rather than pushing through.

**The 10-minute rule for bad days**: do the minimum dose, mark it in `sessions/<year>.md`, and stop. Its value is not the practice — it is that the schedule never becomes something being recovered from.

## Session Sizing

The Session Shape in `SKILL.md` is proportional, so it resolves against `session_minutes`:

| `session_minutes` | Warm retrieval | Reviews | Hard block | Production | Close |
|---|---|---|---|---|---|
| 20 | 3 min | 3 min | — | 12 min | 2 min |
| 45 | 5 min | 7 min | 22 min | 9 min | 2 min |
| 90 | 9 min | 14 min | 45 min | 18 min | 4 min |

At 20 minutes or under, drop the hard block and keep retrieval plus production (the 20-minute row above). The order of cuts is fixed and non-obvious: **cut new material first, production last.** Production is what transfers, and it is what gets sacrificed by default because it is the uncomfortable part.

## What to Cut First

When the week shrinks, cut in this order and stop as soon as the plan fits:

1. New material intake (and the new-item rate in the queue with it — Rule 3's ratio works in both directions).
2. Session length.
3. Secondary topics — down to maintenance mode, not to zero (`maintenance.md`).
4. Project scope, to the thinnest usable version (`projects.md`).
5. Session frequency. Last, and only to a floor of 2-3 per week; below that a topic is in maintenance whether or not it is labelled so.

Never cut: due reviews (they compound into a backlog) and the production step (it is the learning).

## Energy, Not Just Hours

Hours are not fungible. Match the slot to the work:

| Slot quality | Suited to |
|---|---|
| Best 60-90 min of the day | New difficult material, projects, anything requiring a model to be built |
| Medium | Drills, exercises, structured practice |
| Low (tired, fragmented, commuting) | Due reviews, listening input, re-listening, passive exposure in a language |

Two rules that survive contact with real weeks:

- **Protect one good slot, not five mediocre ones.** The best slot is usually early and is usually the first thing given away.
- **Attach the session to an existing anchor** — after the same daily event, in the same place. Decisions about when to practise consume more of the budget than the practice does.

## Sleep and Consolidation

- Consolidation happens during sleep; a session followed by a short night gives back part of what it built. This is a scheduling constraint, not wellness advice: studying until 2 a.m. is a false economy that shows in the next day's review failures.
- Reviewing material shortly before sleep is a favourable slot for declarative material, and one of the few genuinely free wins available.
- Motor and procedural skills show measurable between-session improvement (`domains.md`), which is the mechanical reason daily short practice dominates weekly blocks for instruments and sport.

## Learning Around a Job

- **Aim the topic at the job where honest.** A topic that overlaps work gets practice, feedback and spacing for free, and the hours stop competing.
- **Mornings survive; evenings get taken.** If evening sessions have failed twice, that is data about the slot, not about discipline.
- **The commute and the queue are a natural pair** — reviews and listening input fit fragmented low-energy time, which frees the good slot for the hard block.
- **Expect quarterly interruptions** — deadlines, travel, illness. Build them into the range (Rule 8) instead of treating each one as a failure. A plan that assumes no interruptions is a plan with one life.
- Where the employer funds learning, the subscription still belongs in `~/Clawic/data/finances/subscriptions.md` with its renewal date: reimbursed and forgotten is the same leak as paid and forgotten.

## Restarting the Habit

After a lapse of any length:

1. **Restart at the minimum dose**, for one week. Restarting at the old volume fails within days and confirms the story that it cannot be sustained.
2. Do the **production step first** on day one — one real thing done beats a session of queue clearing for restoring the reason to continue (`plateaus.md`).
3. Re-anchor the slot before increasing the volume. Consistency first, duration second, intensity third — in that order, never in parallel.
4. Re-size the plan against the hours that exist now, and write the new range into `plans/<topic>.md`.

Log every session in `sessions/<year>.md` — including the 10-minute ones, which are exactly the data that shows a habit surviving a bad month. Any agreed cadence (review day, weekly retro, plan review, a return date after a pause) becomes a row in `## Due`. A changed `weekly_hours` or `session_minutes` is a declaration and goes in `config.yaml`, not in `memory.md`, with the plan re-sized in the same turn. Formats in `memory-template.md`.
