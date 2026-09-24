# Sources — Choosing Material and Stopping the Search

Read when a topic starts, when three resources are open at once, when a resource is not working, and before buying anything. The output is a `## Resources` row per verdict and, when the search is over, one primary resource named in the plan.

**Contents:** [One Primary, Everything Else Lookup](#one-primary-everything-else-lookup) · [Matching Format to Stage](#matching-format-to-stage) · [Evaluating a Resource in 20 Minutes](#evaluating-a-resource-in-20-minutes) · [The Abandon Rule](#the-abandon-rule) · [Reading Technique by Material](#reading-technique-by-material) · [Paying for Material](#paying-for-material) · [Free Sources That Beat Paid Ones](#free-sources-that-beat-paid-ones) · [Resource Hoarding](#resource-hoarding)

## One Primary, Everything Else Lookup

Exactly one resource is the spine of a stage. Every other resource is demoted to lookup: consulted when the primary is unclear, never worked through in parallel.

- Three parallel resources is not triple coverage; it is triple context-switching, three sequencings that disagree, and no finished anything.
- The primary gets a **dated finish line** in the plan ("Rust Book ch. 1-10 by 2026-05-30"). Without a date, the primary silently becomes optional.
- A demoted resource goes on the lookup shelf with its verdict, so it is not re-evaluated as a candidate every quarter (`memory-template.md`).
- Switching primaries is allowed once per stage, and only against the abandon rule below. Twice means the problem is the level, not the book.

## Matching Format to Stage

| Stage | Format that fits | Why |
|---|---|---|
| Orientation (first 2-5 h) | One overview: a long article, a talk, chapter 1 of two books | Builds the map cheaply; wrong choices here cost hours, not weeks |
| Foundations | A book or a structured course with exercises | Sequencing and completeness are the value; video without exercises is orientation, not foundations |
| Practice | Exercise sets, katas, problem books, graded readers | Volume of feedback per hour is what matters |
| Building | Official docs plus reference implementations | Tutorials stop matching real requirements here |
| Depth | Papers, source code, specifications, a mentor | Nothing summarised is precise enough at this level |
| Maintenance | Whatever is shortest | Its job is contact, not coverage (`maintenance.md`) |

Video is the highest-comprehension, lowest-retrieval format: excellent for orientation and for anything physical where seeing the motion is the content, weak as a foundation because it invites passive consumption at 1.5× speed with no production step.

## Evaluating a Resource in 20 Minutes

Do not read the reviews; run the test.

1. **Jump to a topic you already partly know.** If the treatment is confused or hand-waves where you know detail exists, everything you cannot check is equally unreliable.
2. **Count the exercises.** A foundations resource without a way to produce and check answers is a reading list.
3. **Read one paragraph aloud.** Density and clarity are stable across a book; one paragraph predicts the rest.
4. **Check the date against the field's volatility.** A 2015 Java book is fine; a 2015 JavaScript tooling book is a trap.
5. **Check the prerequisites of chapter 3, not chapter 1.** Chapter 1 is written for everyone; chapter 3 reveals who the book is actually for.
6. **Look for the errata page.** A maintained errata list is a strong quality signal; its absence in a technical book of any age is a weak negative.

## The Abandon Rule

Abandon a primary resource when one of these holds, and not for any other reason:

| Condition | Threshold |
|---|---|
| Level mismatch upward | Two consecutive sections need external explanation to be usable |
| Level mismatch downward | Three consecutive sections contain nothing new |
| No production path | 20% in, and there is still nothing to produce or check |
| Factually unreliable | Two errors found in material you can verify |
| Stale for a volatile field | Its instructions no longer run, and the fix is not obvious |

Boredom, difficulty at target, and slow progress are **not** abandon conditions — they are the normal texture of learning, and treating them as signals to switch is the mechanism of resource hoarding.

Write the verdict to `## Resources` when abandoning: which condition fired. "Abandoned" without a reason gets re-bought.

## Reading Technique by Material

| Material | Technique |
|---|---|
| Textbook chapter | Read the summary and exercises **first**, then the chapter, then do the exercises without looking back |
| Documentation | Never linear. Enter from a task, read the surrounding section, leave. Docs are a reference that occasionally contains a tutorial |
| Paper | Abstract → figures → conclusion → method, in that order; stop at any point where it stops being relevant |
| Source code | Start from an entry point and follow one path to the end, ignoring everything off it. Reading a codebase breadth-first is how people conclude they cannot read code |
| Reference book | Do not read it. Answer questions with it (`capture.md` turns the answers into items) |
| Long-form video | Watch at normal speed with the production step attached: pause, predict, then continue. At 2× with no pauses, retention is close to zero |

Applies across all six: **stop and produce something every ~20 minutes of input**, or the session becomes consumption with a feeling of progress (SKILL.md Rule 2).

## Paying for Material

Ranked by value per unit currency for a self-directed learner:

1. **A few hours of a good practitioner's time**, spent on the parts where being wrong is invisible to you — pronunciation, technique, security, taste. Highest return, lowest uptake.
2. **A book.** Density per unit cost is unmatched; the good one in most fields costs less than a month of any subscription.
3. **A problem set or exercise platform** with automated checking — buys feedback latency, which is the scarce resource (`practice.md`).
4. **A structured course**, if the sequencing problem is real and the course has graded work.
5. **A subscription platform.** Weakest, because the recurring cost survives the motivation. If bought, put it in `~/Clawic/data/finances/subscriptions.md` with a review date — the abandoned-but-still-billing subscription is the single most common learning expense.

Cost is not a proxy for quality anywhere in this list, and paying is a well-documented way to purchase the feeling of commitment instead of the commitment.

## Free Sources That Beat Paid Ones

- Official documentation and specifications, in mature ecosystems.
- University course pages with problem sets and solutions.
- The exercises at the end of the standard textbook, which most learners skip entirely — the largest free source of graded practice in existence.
- Open-source codebases as reference implementations for the Building stage.
- Community forums for feedback, with a specific question (`practice.md`).

## Resource Hoarding

Symptom: a growing library, a stable capability. It is the most comfortable failure mode in self-directed learning because acquiring feels like progress and has no failure state.

Counters, in order of effect:

1. **A one-in-one-out rule**: nothing new is started until the current primary hits its finish line or fires an abandon condition.
2. **Buy at the point of need**, never at the point of interest.
3. **Ration the search.** Choosing a resource is timeboxed to one session; the third-best book finished beats the best book unstarted.
4. **Count finished, not owned.** The `## Resources` table makes the ratio visible, which is most of the cure.

Write a row to `## Resources` in `memory.md` (or `~/Clawic/data/learn/resources.md` once split) whenever a resource becomes primary, is finished, is abandoned, or is demoted to lookup — with the verdict and the condition that fired, in one clause. A recurring paid platform or tutor also goes to `~/Clawic/data/finances/subscriptions.md` with its currency and renewal date, and is deleted from that table on cancellation. Formats in `memory-template.md`.
