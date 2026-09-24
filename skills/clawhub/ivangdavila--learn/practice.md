# Practice — Difficulty, Drills, and Feedback That Arrives in Time

Read before designing a drill, when sessions happen but capability does not move, and whenever there is no obvious way to know if an attempt was right. Read `errors/<topic>.md` first: the drill should come from the learner's actual mistakes, not from a generic exercise list.

**Contents:** [The Difficulty Target](#the-difficulty-target) · [Isolating a Sub-Skill](#isolating-a-sub-skill) · [Drill Types](#drill-types) · [Blocking and Interleaving](#blocking-and-interleaving) · [Feedback Latency](#feedback-latency) · [Feedback Substitutes](#feedback-substitutes) · [Building a Self-Review Rubric](#building-a-self-review-rubric) · [The Error Log](#the-error-log) · [Speed and Pressure](#speed-and-pressure) · [When Practice Is Not the Problem](#when-practice-is-not-the-problem)

## The Difficulty Target

Hold **~85% success** (Wilson's 85% rule for training difficulty). Measure it: hits over the last 20 attempts, recorded in `sessions/<year>.md`.

| Observed rate | Reading | Correction |
|---|---|---|
| >90% | Rehearsing what is known; the ceiling is not moving | Remove scaffolding, add time pressure, increase scope, or take unseen problems |
| 75-90% | On target | Change nothing |
| 50-75% | Encoding errors as often as successes | Shrink the unit — not the ambition — and add a worked example before each attempt |
| <50% | A prerequisite is missing | Stop the drill; find the missing stage (`curriculum.md`) |

The two failure modes are symmetric and both feel fine from inside: comfortable practice feels productive, and overwhelming practice feels virtuous. Only the counted rate distinguishes them.

**Worked-example fade.** Below target, do not just simplify — fade the support on a schedule: full worked example → example with the last step blank → example with the middle blank → blank problem. Fade one step per two successful attempts. Faded support is the difference between "I can follow it" and "I can start it".

## Isolating a Sub-Skill

Deliberate practice requires naming *one* thing being trained. The test: could you say, before the session, what would count as improvement in it?

1. Perform the whole task and record it (screen, audio, or the finished artefact).
2. Find where it breaks: the pause, the lookup, the re-do, the wrong branch.
3. Convert that moment into a repeatable unit that takes **under 2 minutes per rep**, so a session gets 15+ reps rather than 3.
4. Reps until the target rate holds across two sessions, then put the sub-skill back into the whole task — the reintegration step is the one usually skipped, and without it the drill improves the drill only.

Examples of correct isolation: not "practise chess" but "spot the pin in 30 seconds from 20 positions"; not "practise Spanish" but "produce the past subjunctive in 15 prompts without stalling"; not "get better at debugging" but "form a hypothesis before reading any code, 10 bugs".

## Drill Types

Pick by what is failing, not by what is pleasant. `practice_bias` sets the mix against project work.

| Failing thing | Drill |
|---|---|
| Retrieval is slow | Timed recall: 20 prompts, note which ones exceeded ~5 s and why |
| Right knowledge, wrong choice of method | **Discrimination drill**: mixed problems, and the answer required is *which method*, not the solution |
| Can follow but not start | Blank-page reproduction of something previously done with help |
| Errors cluster in one construct | Contrast pairs: two nearly identical cases with different correct answers |
| Output is correct but slow and effortful | Fluency reps at fixed short intervals until it is automatic, then stop |
| Cannot explain why it works | Teach-back to an imagined novice, out loud or written, then check against the source |
| Works in the tutorial's framing, nowhere else | Change the surface: different data, tool, key, language, or client, same underlying task |

## Blocking and Interleaving

Blocked practice (all of one type) produces better in-session performance and worse retention a week later; interleaved practice does the opposite. This is the contextual-interference result, and the in-session gain is exactly what makes learners choose wrong (Bjork's desirable difficulties).

Switch point: **~80% success on a drill within one session**, then interleave it with its neighbours. Before that threshold, interleaving is just confusion.

- Interleave things that are **confusable** — that is where discrimination is trained. Interleaving unrelated topics only costs context switches.
- Expect the success rate to fall when interleaving starts. That drop is the mechanism, not a regression; say so out loud before it happens, or the learner will revert.
- Never interleave on the day a new construct is introduced.

## Feedback Latency

Practice without correction rehearses the error at full strength.

| Practice type | Correction must arrive within | If it cannot |
|---|---|---|
| Retrieval item | Seconds | Not a valid item — it needs a checkable answer |
| Drill rep | Same minute | Add an automatic check (test, key, reference solution) |
| Exercise | Same session | Time-box it and check against a worked solution at the end |
| Project increment | ≤48 hours | Use a proxy from the list below, chosen before starting |
| Performance (talk, conversation, piece) | Same day, from a recording | Record it; memory of a performance is not evidence about it |

The rule that follows: **choose the correction path before starting the practice**, not after producing something and wondering whether it is good.

## Feedback Substitutes

Ranked by fidelity, for when there is no mentor:

1. **An executable check** — tests, a compiler, a solver, a tuner, a stopwatch. Objective, instant, unarguable. Build one where the domain allows it, even crudely.
2. **A reference solution by a strong practitioner**, diffed against yours *after* your attempt. Read the difference, not the solution.
3. **A rubric you wrote in advance** (below).
4. **A recording of yourself**, reviewed after ≥1 day so the memory of intent has faded — day-old review catches what same-day review excuses.
5. **A community or peer review** — high fidelity, high latency, and variable. Ask a specific question ("is this idiomatic?"), never "any feedback?".
6. **A paid reviewer or tutor**, for the parts where being wrong is expensive and invisible: pronunciation, technique, security, anything with an accent you cannot hear.

Anyone recurring from 5 or 6 goes to `~/Clawic/data/contacts/contacts.md` with their turnaround time — latency is the property that decides how the practice is designed around them.

## Building a Self-Review Rubric

A rubric written before the attempt is a usable substitute; a judgement made after it is self-congratulation.

1. Take three examples of good work in the domain and one of your own past work.
2. Write 5-8 binary checks that distinguish them. Binary — "uses the passive appropriately" is not checkable, "no sentence over 25 words" is.
3. Apply it cold to your attempt, ideally the next day.
4. Every time an external reviewer finds something the rubric missed, the rubric gains a line. After ~10 such lines it approximates the reviewer, which is the point.

Store a rubric worth reusing as `artifacts/rubric-<topic>.md`.

## The Error Log

The highest-value file this skill produces, and the reason `errors/<topic>.md` exists. One row per mistake, with the column that matters: **the misconception behind it**.

- "Wrong answer: 14, correct: 12" is worthless next month.
- "Multiplied before the parenthesis — treats implicit multiplication as higher precedence" is a drill specification.

Three entries with the same misconception mean a missing stage in the plan, not carelessness (`curriculum.md`). Review the log before designing any drill and before writing any transfer test — the test should target the log, not the syllabus.

## Speed and Pressure

Add pressure only after accuracy holds at target, and add exactly one kind at a time:

| Pressure | Trains | Add when |
|---|---|---|
| Time limit | Automaticity, retrieval under load | Accuracy ≥85% unhurried |
| No lookups | True unaided recall | Lookups are under ~1 per 10 attempts |
| An audience or recording | Performance under observation | The unobserved version is stable |
| Novel surface | Transfer | Application level reached (`verification.md`) |
| Fatigue (end of session) | Robustness | Only for skills that must survive it — do not train fatigue for its own sake |

## When Practice Is Not the Problem

Stop redesigning the drill if any of these is true — they need a different file:

- Nothing survives between sessions → scheduling (`schedule.md`)
- Capability exists but does not appear in real work → transfer and framing (`projects.md`, `verification.md`)
- Sessions are not happening at all → time or motivation (`time.md`, `plateaus.md`)
- The material itself is wrong or below the level → resources (`sources.md`)

Every session writes its row to `sessions/<year>.md` — minutes, hard block, success rate over attempts, what was produced — because Rule 4 needs the last 20 attempts and nobody reconstructs them a week later. Every mistake writes a row to `## Error Log` in `memory.md`, or to `errors/<topic>.md` once split, with its misconception. A rubric worth reusing goes to `artifacts/rubric-<topic>.md` with its `## Boxes` line. A recurring reviewer or tutor goes to `~/Clawic/data/contacts/contacts.md`. Formats in `memory-template.md`.
