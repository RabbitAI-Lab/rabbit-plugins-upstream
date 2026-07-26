# Projects — Learning By Building Something Real

Read when the learner can follow along but cannot start alone, when choosing what to build, and when a project has stalled. Read the plan's exit test first: a project that does not move it is recreation, which is fine but must be labelled.

**Contents:** [The Scaffolding Ladder](#the-scaffolding-ladder) · [Choosing the Project](#choosing-the-project) · [Sizing](#sizing) · [The Gap Log](#the-gap-log) · [Tutorial Hell](#tutorial-hell) · [When a Project Stalls](#when-a-project-stalls) · [Finishing and Shipping](#finishing-and-shipping) · [Non-Software Projects](#non-software-projects)

## The Scaffolding Ladder

The mechanism that converts following into doing. Each rung removes one support; skipping rungs is what produces the freeze at the blank file.

| Rung | What happens | Move up when |
|---|---|---|
| 1. Copy | Reproduce the tutorial exactly, typed not pasted | It runs and every line can be explained |
| 2. Modify | Change three things the tutorial did not cover | All three work and the failures were diagnosed unaided |
| 3. Extend | Add a feature the tutorial never mentions | It works without re-reading the tutorial |
| 4. Rebuild | Same project, blank file, notes allowed | Completed within ~2× the original time |
| 5. Blank | A different project of the same class, no notes, no reference implementation | Completed. This is Application level (`verification.md`) |

Two rules: **one rung per project**, and **the rung is declared before starting**. "I'll see how far I get" defaults to rung 1 every time, because rung 1 is the comfortable one.

Time-box each rung. If rung 4 is not done in 2× the original build time, the gap is specific and findable — go to the gap log rather than restarting the tutorial.

## Choosing the Project

| Property | Why | Bad example |
|---|---|---|
| Exercises the exit test's capabilities | Otherwise it trains something else convincingly | Building a portfolio site to learn data modelling |
| You want the output to exist | Motivation survives week three on this alone | The to-do app nobody wants, including you |
| Failure is visible | An invisible failure teaches nothing | A project with no test, no audience, no run |
| Smaller than it feels | See sizing below | "A clone of X" |
| Not a rewrite of an existing tool for its own sake | Rewrites hide behind familiar requirements | — |

The strongest source of projects: **a real annoyance in your own week**. Requirements are known, the finish line is unarguable, and the thing gets used, which surfaces the failures a demo never would.

## Sizing

```
first_project_hours ≈ weekly_hours × 2
```

Two weeks of budget, so a bad choice costs two weeks and not two months. Scale up only after one project has actually finished. The dominant sizing error is not ambition — it is invisible scope: authentication, deployment, data, and error handling each cost more than the feature they surround.

Cut to the **thinnest version that is genuinely used once**: one user, one path, no configuration, ugly. Everything else is a second project, and it should be, because a finished small thing produces more learning than an abandoned large one.

## The Gap Log

The single practice that makes project-first learning work rather than produce confident copy-paste.

Every time you copy a line, accept an autocomplete, or make it work without knowing why: write one row.

| Date | What I copied / did not understand | Resolved? |
|---|---|---|

Then, the same day: each unresolved row becomes a queue item, a drill, or a five-minute read. This is the fundamentals-first material arriving exactly when it is needed, which is why the project-first position is defensible at all (SKILL.md, Where Experts Disagree).

The log is working state, not a box of its own: it lives inside the project file at `~/Clawic/data/projects/<project>.md` while the project runs, and is deleted with the project's closing status. What outlives it are the rows it fed — queue items in `## Review Queue`, mistakes in `## Error Log`.

An unlogged gap does not stay neutral: it becomes a permanent hole that the next project routes around, and the routing hardens into a ceiling.

## Tutorial Hell

Symptom: many completed tutorials, no ability to start from nothing. Cause: rung 1 repeated, never rung 4 or 5.

| Sign | Fix |
|---|---|
| A new tutorial is started whenever the last one ends | Ban new tutorials for one project; take the current one to rung 4 |
| Following works, blank file produces paralysis | Rebuild the last tutorial project from a blank file, notes allowed, timed |
| Every error is solved by searching for the exact message | Predict the cause before searching; a wrong prediction is a row in `## Error Log`, with the misconception, not just the fix |
| Nothing is ever finished, only followed | Ship the thinnest usable version of one thing, to one real user |

The blank-file rebuild is uncomfortable in a specific and diagnostic way: the discomfort is the boundary of actual capability, and it is the first time it has been visible.

## When a Project Stalls

Classify before acting — the four causes have opposite fixes:

| Cause | Tell | Fix |
|---|---|---|
| Scope grew | The finish line moved twice | Freeze scope at today's state; the additions become project two |
| A blocking gap | Same problem three sessions running | Stop building; drill the sub-skill for one session (`practice.md`) |
| No feedback | Nobody has run it, no tests | Get it in front of a person or a test suite this week (Rule 7) |
| Motivation gone | The output stopped being wanted | Kill it and say so — a project retired on purpose costs nothing; one abandoned silently taxes every future one (`plateaus.md`) |

## Finishing and Shipping

- **Define done before starting**, in one sentence, in the project file. Without it, projects end by exhaustion rather than by completion, which teaches the wrong lesson about your capacity.
- Shipping to **one real user** — including yourself, in real use — surfaces the class of failure that only appears outside the author's assumptions.
- Do a short retrospective at the end: what took longest, what was copied without understanding, what would be done differently. Three lines, in the project file. This is the highest-value 10 minutes of the whole project.
- A finished project is evidence for Application level, not for Transfer. Transfer needs a *different* project of the same class (`verification.md`).

## Non-Software Projects

The ladder is domain-independent; only the artefacts change.

| Domain | Rung 1 | Rung 5 |
|---|---|---|
| Music | Play a piece from the score | Play a new piece of the same difficulty, unassisted; or improvise in that idiom |
| Language | Reproduce a dialogue | Hold an unscripted conversation on a chosen topic |
| Writing | Imitate a passage's structure | Write your own piece to the same standard, cold |
| Design | Recreate an existing layout | Design for an unseen brief and defend the choices |
| Cooking | Follow the recipe exactly | Cook the dish from the ingredients without it |
| Maths | Work the solved example | Solve an unseen problem and prove the result |

A build-to-learn project goes to `~/Clawic/data/projects/<project>.md` — goal, status, milestones, and a pointer back to `plans/<topic>.md` — because other skills track work in that same box and the project must be findable from outside this topic; identity is the file name, retirement is `status: done | cancelled — <date>` inside the file, never a deletion. The plan holds only the project's name. Gap-log rows that survive the session become queue items in `## Review Queue` and, where they were mistakes, rows in `## Error Log`. The retrospective goes in the project file. Formats and the write protocol in `memory-template.md`.
