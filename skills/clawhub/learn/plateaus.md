# Plateaus — Stalls, Motivation Collapse, and Coming Back

Read when progress has been flat for weeks, when sessions have stopped happening, and when returning after a lapse. Read `sessions/<year>.md` and the plan's `## Revisions` first: the diagnosis below depends on what actually happened, not on how it felt.

**Contents:** [The Three-Question Split](#the-three-question-split) · [Real Plateaus](#real-plateaus) · [Wrong Practice](#wrong-practice) · [Motivation Collapse](#motivation-collapse) · [Burnout](#burnout) · [The Intermediate Wall](#the-intermediate-wall) · [Relearning After a Lapse](#relearning-after-a-lapse) · [Quitting Well](#quitting-well)

## The Three-Question Split

"I'm stuck" has four different causes with opposite fixes. Ask in this order:

1. **Are sessions happening?** No → motivation or time, not learning (`time.md`, below).
2. **Is the success rate near 85%?** Far above → practice is too easy; far below → a prerequisite is missing (`practice.md`).
3. **Is anything being produced, or only consumed?** Consumption only → the stall is structural and would continue at any effort level (SKILL.md Rule 2).

Only if sessions happen, difficulty is on target, and production is real is this an actual plateau — which is the rarest of the four and the only one that resolves by continuing.

| Diagnosis | Tell | Fix |
|---|---|---|
| Real plateau | All three checks pass, results flat 3+ weeks | Change the practice dimension, keep the volume (below) |
| Wrong practice | Sessions happen, rate off target or no production | Redesign the drill (`practice.md`) |
| Motivation collapse | Sessions stopped, no fatigue, other things fine | Goal, feedback, or identity problem (below) |
| Burnout | Sessions stopped, everything else also heavy | Stop, do not restructure (below) |

## Real Plateaus

Progress is stepwise, not linear: consolidation periods look identical to failure from inside, and quitting during one is the single most common way a learning project ends.

Two mechanisms:

- **Automation**: the skill is being made cheaper, not better. Effort per unit drops while output quality is flat. Real progress, invisible on the output metric — measure speed or effort, not just quality, and it appears.
- **Restructuring**: performance is briefly *worse* while a bad method is replaced by a better one — the intermediate grip on the instrument, the new fingering, the corrected accent, the rewritten mental model. Predictable, temporary, and the point at which learners revert to the old method and cap themselves permanently.

Fixes, in order:

1. **Change the dimension, not the volume.** Flat accuracy → train speed. Flat speed → train harder material. Flat both → change the surface (`practice.md`). More hours of the same thing is the one intervention that reliably does nothing.
2. **Attack the error log, not the syllabus.** After the beginner phase, progress lives entirely in the specific failure list (`errors/<topic>.md`).
3. **Get one external evaluation.** Plateaus are frequently invisible progress or an invisible defect; both are diagnosed in an hour by someone who can see what you cannot (`practice.md`).
4. **Widen the measurement window.** Compare against three months ago, not last week. Keep a dated sample of work — the from-memory explanation or recording in `artifacts/` exists partly for this.

## Wrong Practice

The most common misdiagnosis: months of effort at a difficulty that trains nothing.

| Sign | Correction |
|---|---|
| Almost everything is correct in every session | Success rate is above target; remove supports (`practice.md`) |
| Every session covers new material, nothing is retrieved | No consolidation is happening; retrieval first (Rule 2) |
| Practice is always the same task | Automated long ago; change the dimension |
| Errors repeat across months | The error log is not feeding the drills |
| Consuming courses and calling it practice | There is no production step in the session |

## Motivation Collapse

Not a character trait. Four causes, distinguishable and separately fixable:

| Cause | Tell | Fix |
|---|---|---|
| Feedback drought | Cannot tell if there has been progress for weeks | Run a verification test; a dated result restores signal (`verification.md`) |
| The goal changed | The exit test no longer describes anything wanted | Rewrite the exit test or retire the topic. Do not push through with a dead goal |
| The plan became fiction | The schedule assumes hours that never exist | Re-size against measured hours (`curriculum.md`, `time.md`) |
| Difficulty mismatch | Sessions feel pointless or crushing | Return to the 85% band |

Two accelerants worth knowing:

- **Visible progress beats willpower.** A dated topic table, a plan with stages ticked, and a session log are motivational instruments as much as records — which is one reason they are written every session.
- **Streaks build the habit and invite the fake session.** Track a minimum quality dose (a real retrieval plus a real production step) rather than a binary day, and record it in `sessions/`. Respect `accountability` preferences: for some learners a broken streak ends the project (`config.yaml`).

## Burnout

Distinct from motivation collapse: fatigue is general, not topic-specific, and other areas of life are also heavy.

- Restructuring the plan does not help and adds guilt. Stop the topic, keep only the review queue at a reduced `daily_review_limit`, or suspend it entirely — a suspended queue survives; an abandoned one does not (`schedule.md`).
- Set a return date and put it in `## Due`. An open-ended stop becomes a silent abandonment, which taxes the next attempt.
- Mark the topic `paused <date> (<reason>)` in `## Topics`. The explicit pause is what stops it resurfacing as guilt every week.

## The Intermediate Wall

Beginners improve fast because everything is new and every hour touches something unlearned. At intermediate level, the remaining gains are narrow, unglamorous and specific — and the general resources that worked before are now entirely below level.

| Beginner phase | Intermediate phase |
|---|---|
| Any practice helps | Only targeted practice helps |
| General resources work | Resources must be specific or expert-level (`sources.md`) |
| Progress is obvious weekly | Progress needs measurement over months |
| Errors are broad | Errors are a short, stable, personal list |
| Self-teaching is efficient | External feedback becomes the bottleneck |

The transition is not a failure of effort; it is a change in what effort has to be aimed at. Learners who do not recognise it conclude they have hit their ceiling, which is almost never what happened.

## Relearning After a Lapse

Relearning is much faster than first learning — the savings effect. Restarting from the beginner course spends those savings on material already known and is the most common post-lapse error.

Protocol:

1. **Test before rebuilding.** Attempt the last stage test cold. The result, not the calendar, says where you are.
2. **Expect the split**: procedural skill largely survives; specific facts and vocabulary decay fastest (`maintenance.md`).
3. **Rebuild the queue, do not re-create it.** For a lapse over ~60 days, reset intervals rather than grading a hundred failures — a mass of `again`s destroys the ease values of items that were fine (`schedule.md`).
4. **Re-size the plan against the hours available now**, not the ones available then. The lapse usually happened because the plan was wrong for the life around it.
5. Start with production, not review. One session of doing the thing restores more than a week of queue clearing, and it restores the reason to continue.

## Quitting Well

Stopping is a legitimate outcome. Stopping *badly* is what damages the next topic.

- Retire the topic explicitly: `retired <date> (<reason>)` in `## Topics`, and archive its plan and queue rather than deleting them — the savings effect makes the record worth keeping if it is ever picked up again.
- Cancel the associated subscription in `~/Clawic/data/finances/subscriptions.md` in the same turn. This is the most common place money leaks in self-directed learning.
- Write one line on what was actually gained, as the reason clause of that `## Topics` row. Six weeks of a language that was dropped still moved something, and keeping it there stops the whole episode being filed as failure.
- A topic retired on purpose costs nothing. A topic abandoned silently taxes every future one with the belief that projects do not get finished.

Write the diagnosis, not the mood: the pause, retirement or resumption goes into the topic's row in `## Topics` with its date and reason; a re-size or a changed exit test goes into `plans/<topic>.md` as a dated revision; a return date, a reduced review cadence, or a maintenance-only mode goes into `## Due`. What broke the plateau — the dimension changed, the evaluation obtained, the method replaced — becomes `artifacts/decision-<topic>-<what>.md` with its `## Boxes` line, because the next plateau in any topic will look identical from inside. Formats in `memory-template.md`.
