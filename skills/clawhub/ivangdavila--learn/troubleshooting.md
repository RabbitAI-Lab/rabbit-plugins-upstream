# Troubleshooting — Symptom to Cause

Read when the complaint does not map cleanly onto one of the other files. Read `memory.md` first — `## Topics`, `## Error Log` and the last rows of `sessions/<year>.md` usually name the cause before any question is asked.

**Contents:** [The Five Places](#the-five-places) · [Symptom Table](#symptom-table) · [Contradictions Worth Resolving](#contradictions-worth-resolving) · [Questions That Locate the Fault](#questions-that-locate-the-fault) · [When Nothing Is Actually Wrong](#when-nothing-is-actually-wrong)

## The Five Places

Every learning failure sits in exactly one of these. Name it before proposing anything.

| Place | Question that tests it | Fix lives in |
|---|---|---|
| 1. The goal was never testable | Could a stranger grade "done" today? | `curriculum.md` |
| 2. The material was never retrieved | Was anything produced from memory before being seen? | `capture.md`, `schedule.md` |
| 3. The practice was too easy | What is the success rate over the last 20 attempts? | `practice.md` |
| 4. The feedback arrived too late | How long between the attempt and knowing it was wrong? | `practice.md` |
| 5. The schedule was fiction | What do the measured hours say? | `time.md` |

Working the wrong place is why "just study more" fails: more hours against a place-1 or place-4 fault changes nothing and costs the learner their confidence.

## Symptom Table

| Symptom | Place | Cause | First move |
|---|---|---|---|
| "I read it and understood it, then could not do it" | 2 | Recognition mistaken for capability | Cold production attempt now, then convert the failures into items (`capture.md`) |
| "I know it during the session, forget it by next week" | 2 | No spacing; everything massed | Queue with expanding intervals; first review within 24 h (`schedule.md`) |
| "My reviews take an hour and I have started skipping them" | 2 | Intake above the sustainable ratio | Suspend new items, drain by the backlog formula, cap intake at `daily_review_limit ÷ 10` |
| "One card has beaten me eight times" | 2 | Leech — malformed item, not weak memory | Split into atomic items or drop it (`schedule.md`) |
| "I can do the exercises but not the real thing" | 3 | Exercises are pre-decomposed; reality is not | Discrimination drills and whole-task practice (`practice.md`) |
| "Every session feels good and nothing improves" | 3 | Success rate above 90% | Count it; remove scaffolding or raise scope (Rule 4) |
| "It is so hard I dread starting" | 3 | Success rate below 75%, or a missing prerequisite | Shrink the unit, add worked-example fade (`practice.md`) |
| "I have done 12 tutorials and cannot start a blank file" | 3 | Never left rung 1 of the scaffolding ladder | Blank-file rebuild of the last project, timed (`projects.md`) |
| "I do not know if my answer is any good" | 4 | No correction path was chosen before practising | Pick a feedback substitute now, by latency (`practice.md`) |
| "I only find out I was wrong weeks later" | 4 | Latency exceeds the budget for that practice type | Automate a check, or write the rubric (`practice.md`) |
| "I keep planning and not starting" | 1 | The goal has no performance in it | Write the exit test; perform it badly today (`curriculum.md`) |
| "I do not know what to learn first" | 1 | No exit test, so nothing can be ordered or cut | Exit test, then blockers, then stages (`curriculum.md`) |
| "How long will this take?" | 1 | — | Range from `weekly_hours`, never a date (Rule 8) |
| "I have five books open and no progress" | 1 | Resource hoarding replacing the primary | One primary with a dated finish line (`sources.md`) |
| "I planned 15 hours a week and did 3" | 5 | Plan sized against an imagined week | Re-size against measured hours (`time.md`) |
| "I keep missing sessions and then giving up for a week" | 5 | No minimum dose, so a bad day breaks the schedule | 10-minute rule; cut length, never frequency (`time.md`) |
| "I stopped for two months and everything is gone" | 5 | Normal decay plus a restart error | Test before rebuilding; reset the queue, do not grade through it (`plateaus.md`) |
| "Flat for six weeks despite steady work" | 3 | Plateau vs wrong practice vs burnout | Run the three-question split (`plateaus.md`) |
| "I do not care about this any more" | 1 | The goal changed, or feedback drought | Verification test for signal, then rewrite or retire the exit test (`plateaus.md`) |
| "I was fine and now I am worse" | 3 | Restructuring — a better method mid-installation | Expected and temporary; do not revert (`plateaus.md`) |
| "I am great with the AI and useless alone" | 2 | Assisted competence; retrieval was offloaded | `hint_policy: after-attempt` or `never`, then an unassisted cold test (`ai-assisted.md`) |
| "I can read the language but not speak it" | 3 | Production never trained; four separate skills | Output drills with constraints from week one (`domains.md`) |
| "I passed the course and cannot do the job" | 1 | Completion measured attendance | Run the exit test; the certificate is not evidence (`verification.md`) |
| "I learned it last year and it is gone" | 5 | No maintenance interval was ever set | Recovery protocol, then a `## Due` row (`maintenance.md`) |
| "I am learning three things and none is moving" | 5 | Above the topic ceiling for the hours available | Two topics maximum below ~10 `weekly_hours` (`curriculum.md`) |
| Anything else | — | Locate it in the five places above and work that file | — |

## Contradictions Worth Resolving

Situations where two of this skill's own rules appear to conflict. The resolution is fixed, so it is not re-litigated each time.

| Apparent conflict | Resolution |
|---|---|
| "Retrieve before re-exposure" vs a topic the learner has never seen | Retrieval applies to material already encountered. First exposure is input; the retrieval starts at the first interrupt, 3-4 items in (Rule 5) |
| "Interleave" vs "one stage in flight" | Stages are sequenced; drills within a stage are interleaved. Different levels of granularity |
| "85% success" vs "desirable difficulties feel worse" | 85% is measured accuracy, not perceived comfort. Interleaving lowers comfort while accuracy stays in band |
| "Cap new items" vs a fixed deadline | With a real deadline this is the wrong skill — `studying` handles a date-driven plan. If the deadline stays here, raise intake knowingly and accept the post-deadline collapse of the queue |
| "Do not delete a backlog" vs "the queue is not a completeness obligation" | Never delete in bulk during a backlog. Retire items deliberately, one at a time, when they are no longer used |
| "Projects first" vs "fundamentals first" | Project-first with a gap log. The log is what makes the position defensible (`projects.md`) |

## Questions That Locate the Fault

Six questions that resolve most cases faster than a discussion, in order:

1. "What would count as done, and could I grade it today?" → place 1
2. "In the last session, what did you produce before seeing any answer?" → place 2
3. "Out of your last 20 attempts, how many were right?" → place 3
4. "How do you find out you were wrong, and how long does that take?" → place 4
5. "How many hours did you actually do last week?" → place 5
6. "When did you last do the whole thing, cold, unaided?" → verification, and usually the answer to "am I stuck"

## When Nothing Is Actually Wrong

Three patterns that are frequently reported as problems and should be left alone:

- **Performance drops when interleaving or when a method is being replaced.** Expected, temporary, and the mechanism working (`plateaus.md`).
- **Slower progress at intermediate level.** The remaining gains are narrower, not smaller. Measure over months, not weeks.
- **Forgetting between reviews.** The schedule is designed to catch material just as it becomes hard to retrieve — retrieving something with effort is the review doing its job, not evidence of failure.

Whatever the diagnosis, write it: the place identified and the correction applied go into `## Error Log` when they came from a specific mistake, into the topic's row in `## Topics` when they changed its level or status, and into `plans/<topic>.md` as a dated revision when they changed the plan. A diagnosis repeated across topics — the same fault twice in two subjects — belongs in `## How They Learn`, which is what stops the third occurrence. Formats in `memory-template.md`.
