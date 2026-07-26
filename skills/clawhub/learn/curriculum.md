# Curriculum — Building a Path Nobody Is Grading

Read before starting a topic, whenever scope moves, and at every `plan_review_weeks` check. The output of this file is one `plans/<topic>.md`.

**Contents:** [The Exit Test](#the-exit-test) · [Working Backwards](#working-backwards) · [Sequencing](#sequencing) · [Sizing Against a Real Week](#sizing-against-a-real-week) · [What to Cut](#what-to-cut) · [Borrowed Syllabi](#borrowed-syllabi) · [The Plan Review](#the-plan-review) · [Multiple Topics at Once](#multiple-topics-at-once)

## The Exit Test

A goal is a performance with conditions. Four slots, all required: **what is produced · from what starting state · under what constraints · judged how**.

| Vague goal | Exit test |
|---|---|
| "Learn Spanish" | Hold a 20-minute unscripted conversation with a stranger about my work, no English, no lookups, understood without repetition |
| "Get good at SQL" | Rewrite five reporting queries with window functions from the schema alone, correct on first run |
| "Understand machine learning" | Take a raw CSV to a validated model with a written error analysis, no template repo |
| "Learn guitar" | Play three songs start to finish at tempo, from memory, for someone in the room |

Tests for the test: could a stranger grade it without asking follow-up questions? Could you attempt it *today* and fail cleanly? If the answer to either is no, the goal is still a topic, not a target.

**Level check.** An exit test set at a level far above the current one produces a plan of unknown length. If the honest range (below) exceeds ~6 months, split the test into a first milestone you can reach in 4-8 weeks and keep the far target as a line in the plan, not as the thing being scheduled.

## Working Backwards

1. Write the exit test.
2. Perform it now, badly, and write what stopped you into `plans/<topic>.md` as the blocker list. This is the fastest curriculum-generation move available and almost nobody does it — the failure list is a syllabus produced in an hour, specific to this learner.
3. Group the blockers into 4-8 capabilities. Each becomes a stage.
4. Give every stage **its own test**, at the same standard as the exit test. A stage without a test cannot be finished, only abandoned.
5. Order by dependency, then by unlock value (below).
6. Name what is being cut, and why (`## What to Cut`).

## Sequencing

- **Hard dependencies first, and only hard ones.** Most claimed prerequisites are conventions of textbook order, not requirements. Test the claim: can the later thing be attempted at all without the earlier one? If yes, it is a preference.
- **Unlock value beats logical order.** Prefer the stage that makes the largest number of real tasks attemptable. In a language that is ~1,000 high-frequency words and the present tense; in a codebase it is the build and the test command; in music it is four chords and a strum.
- **Front-load the thing that will be used every day.** Anything used daily gets its spacing for free from use, which is review you never have to schedule.
- **Put the intimidating stage third, not last.** Last means never: momentum is highest early, and the stage everyone defers is usually the one the exit test depends on.
- **One stage in flight.** Two half-finished stages produce no verified capability and hide which one is stalled.

## Sizing Against a Real Week

```
hours_needed  = Σ (stage estimates)
weeks         = hours_needed ÷ weekly_hours
quoted range  = weeks  to  2 × weeks
```

Quote the range, never a date (SKILL.md Rule 8). The upper end is not slowness: it is missed weeks, illness, work, and the stage that turns out to be two stages. State that assumption out loud, once, when the range is given.

- **`weekly_hours` is what happened last month, not what is intended.** If there is a `sessions/<year>.md`, sum it — the measured number is almost always lower than the declared one, and planning against the declared one is how month two fails.
- Stage estimates come from the resource where possible (chapters × observed hours per chapter after the first two), never from the resource's own marketing ("learn X in 10 hours").
- Under 3 h/week, cut the exit test rather than extending the calendar: a plan longer than ~6 months at that budget will not survive the first interruption (`time.md`).

## What to Cut

Write the cut list into the plan explicitly. An unwritten cut is not a decision — it is a thing that comes back as guilt every session.

| Cut candidate | Keep it only if |
|---|---|
| History and origin of the subject | The exit test involves arguing about design choices |
| Advanced features encountered in blog posts | A stage test needs them |
| The tool's full API or the language's full grammar | The exit test is breadth itself (rare) |
| A second language, framework or instrument in parallel | The two are being interleaved deliberately (`domains.md`), not both being started |
| Note-taking systems, setup, and tooling research | The setup blocks the first session and only then, timeboxed to one session (`sources.md`) |

## Borrowed Syllabi

Do not invent a sequence when a good one exists. Sources, ranked by how well they match a self-directed learner:

1. **A practitioner job description or a real task list** — reverse-engineers exactly the capability set that is used, with no academic padding.
2. **The table of contents of the two most-recommended books**, intersected. The intersection is consensus core; anything in only one is optional.
3. **A certification or exam objectives list**, used as a coverage map and then trimmed against the exit test — exam boards optimise for testability, not for capability.
4. **An open university course outline** — good ordering, usually heavy on theory the exit test does not need.

Then trim: borrowed syllabi are written for a cohort with an assessor, and typically contain 30-50% material a specific exit test does not require.

## The Plan Review

Runs every `plan_review_weeks` (default 4), as a `## Due` row. Five questions, in order:

1. **Hours**: actual hours from `sessions/<year>.md` versus `weekly_hours`. If actual is under 60% of the declared figure for two cycles, the number is wrong — re-size the plan, do not exhort.
2. **Stage tests passed** since the last review. Zero for two cycles means the stage is too big, not that the learner is failing.
3. **Error log themes** (`errors/<topic>.md`): three or more entries with the same misconception is a missing stage, not a careless streak.
4. **Exit test still wanted?** Motivation collapse is frequently a goal that stopped being the goal two months ago (`plateaus.md`).
5. **Range still honest?** Recompute from remaining stages and the measured weekly hours, and say the new range out loud.

Each review writes a dated line into the plan's `## Revisions`. Silent edits destroy the only record that could show whether estimates are improving.

## Multiple Topics at Once

- Two topics is the practical ceiling below ~10 `weekly_hours`; the second topic costs more than half the time because context reloading is not free.
- Pair topics that are **unrelated** if both are in an early stage — similar material learned simultaneously produces interference, and the learner blames memory rather than the pairing.
- Pair topics that are **related** only once one is at Application level or above; then the interleaving is a feature (`practice.md`).
- A topic in maintenance costs almost nothing (`maintenance.md`) and does not count against the ceiling.

Write the plan to `~/Clawic/data/learn/plans/<topic>.md` and its row to `## Topics` in `memory.md`, both in the turn it is agreed; add the `plan_review_weeks` row to `## Due`. Every revision appends a dated line to the plan's `## Revisions`. Format in `memory-template.md`. A plan that lives only in the conversation is re-invented, slightly differently, in three weeks.
