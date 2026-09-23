# Learning Next to an Agent — Without Hollowing It Out

Read when an agent is in the loop, when `hint_policy` is being set, and when the learner performs well with assistance and badly without it. This file governs the agent's own conduct during a session as much as the learner's habits.

**Contents:** [The Core Failure](#the-core-failure) · [hint_policy](#hint_policy) · [What the Agent Must Not Do](#what-the-agent-must-not-do) · [What an Agent Is Uniquely Good At](#what-an-agent-is-uniquely-good-at) · [The Offload Boundary](#the-offload-boundary) · [Prompts That Teach vs Prompts That Answer](#prompts-that-teach-vs-prompts-that-answer) · [Verifying What the Agent Says](#verifying-what-the-agent-says) · [Detecting Assisted Competence](#detecting-assisted-competence)

## The Core Failure

Retrieval builds memory; being told does not. An agent's defining property is that it removes the retrieval attempt faster than any book, search engine or teacher ever could — the answer arrives before the reconstruction that would have built the memory (SKILL.md Rule 2).

The result is **assisted competence**: real, measurable performance that exists only while the assistant is present, and that the learner cannot distinguish from their own capability, because from the inside both feel like understanding.

The correction is structural, not motivational: put the attempt before the answer, every time, by policy rather than by intention.

## hint_policy

The `config.yaml` variable that decides when the answer is allowed to appear.

| Value | Behaviour | Fits |
|---|---|---|
| `on-request` | Answer whenever asked | Orientation, exploring a new field, time pressure with no learning goal |
| `after-attempt` (default) | Nothing until the learner has produced something, even a wrong something | Every active learning session |
| `never` | Hints only after the learner asks twice, and the answer only after a stated attempt plus a stated reason | Verification, exam-like practice, the topic the learner keeps leaning on |

Under `after-attempt`, the escalation ladder — one rung at a time, and never skipped:

1. "What have you tried?"
2. Restate the problem in different terms.
3. Name the *area* the answer lives in.
4. A leading question that makes the next step visible.
5. The first step, worked, and back to the learner.
6. The whole answer, plus one item added to the queue.

Rung 6 always costs a queue item. That is what makes handing over the answer honest rather than free.

## What the Agent Must Not Do

- **Answer before the learner has produced anything** when `hint_policy` is `after-attempt` or `never`.
- **Write the artefact the learner is practising producing.** Writing the code, the essay, the translation or the proof for them replaces the practice with a demonstration.
- **Grade the learner's answer generously.** "Almost — you had the right idea" on a wrong answer breaks calibration, which is the instrument the whole system depends on (`verification.md`).
- **Reveal the answer while asking for a confidence rating.** The rating must precede the reveal or the column carries no information.
- **Let recognition pass as recall**, by phrasing questions so that the answer appears among the options or inside the question.
- **Turn a verification test into a teaching session.** During verification, the agent grades and says nothing else until the test is over.
- **Silently expand scope** — answering the interesting adjacent question instead of the one asked spends the session's budget on the agent's interest.

## What an Agent Is Uniquely Good At

The other side, and the reason to have one in the loop at all:

| Capability | Why it is unmatched | Where it plugs in |
|---|---|---|
| Unlimited generated items at a chosen difficulty | Endless unseen problems calibrated to the 85% band | `practice.md` |
| Instant feedback at any hour | Collapses the latency budget for exercises to near zero | Rule 7 |
| Socratic questioning at scale | Can ask "why" ten times without impatience | This file |
| Marking a boundary condition | "Name a case where this is wrong" is cheap to pose and hard to fake | `verification.md` |
| Rephrasing at a different level | Same idea from three angles, on demand | `learning` skill |
| Simulating an interlocutor | Conversation partner, interviewer, code reviewer, opponent | `domains.md` |
| Keeping the system | The queue, the plan, the error log, the cadences — the part learners abandon | `memory-template.md` |

The last row is where an agent adds the most durable value and the least risk: nothing about maintaining the system substitutes for the learner's own retrieval.

## The Offload Boundary

Deciding what may be delegated permanently. One question: **is this in the exit test?**

| In the exit test | Not in the exit test |
|---|---|
| Never delegate. Practise it unaided until verified | Delegate freely; it is not what is being learned |
| Example: writing the SQL, if the goal is SQL | Example: formatting the output table |
| Example: forming the sentence, if the goal is the language | Example: looking up a place name |

Two boundary cases worth naming:

- **Scaffolding is delegation with a removal date.** The agent may carry a sub-skill while another is being trained, but the date it stops is written in the plan (`projects.md`, rung ladder).
- **The gap log applies to every generated line accepted without understanding.** An agent's output is a tutorial's output with better ergonomics; the same rule catches it (`projects.md`).

## Prompts That Teach vs Prompts That Answer

| Instead of | Ask |
|---|---|
| "How do I do X?" | "I tried this and got that. What is wrong with my model?" |
| "Explain X" | "Here is my explanation of X. Where is it wrong or incomplete?" |
| "Write me a Y" | "Here is my Y. Diff it against how a strong practitioner would do it, and tell me why each difference matters" |
| "Give me practice problems" | "Give me 10 problems at ~85% expected success, mixed types, and do not say which method each needs" |
| "Is this right?" | "Grade this against these criteria, strictly, and do not soften it" |
| "Summarise this chapter" | "Quiz me on this chapter without showing me the content first" |

The pattern in all six rows: the learner produces first, and the agent operates on the production. A prompt that starts with the learner's own artefact cannot be answered by handing over a finished one.

## Verifying What the Agent Says

An agent is a confident, fluent source with a non-zero error rate, and a learner cannot detect the errors precisely in the domain they are learning.

- **Anchor to a primary source for anything load-bearing**: the specification, the documentation, the textbook, the standard. Items entering the queue from an agent's answer are checked once against a primary source before they are added — a wrong item drilled to fluency is expensive to remove.
- **Highest risk zones**: exact numbers, version-specific behaviour, citations and attributions, and anything where a plausible answer exists next to the true one.
- **Lowest risk zones**: generating practice problems, rephrasing, asking questions, and critiquing the learner's own output against criteria the learner supplied.
- Disagreement between the agent and a primary source is resolved for the source, and the correction goes to `## Error Log` — it is exactly as informative as any other misconception.

## Detecting Assisted Competence

| Test | Passing means |
|---|---|
| Same task, no assistant, cold | The capability is the learner's |
| Explain the produced work line by line | It was understood, not accepted |
| The same problem with a small twist, unaided | It is a model, not a memorised session |
| Reproduce it a week later | It survived, which assistance can hide indefinitely |

Run at least one of these before any promotion in `## Topics`. Assisted work is never evidence for a mastery level — a promotion must come from an unassisted, cold test (`verification.md`).

Set `hint_policy` in `config.yaml` the moment the learner states a preference about being given answers, and apply it from then on. Every answer delivered at rung 6 adds its item to `## Review Queue` in the same turn. An agent correction the learner accepted without understanding is a gap-log row and, if it was a misconception, a row in `## Error Log`. A prompt pattern that works especially well for this learner belongs in `artifacts/` with its `## Boxes` line. Formats in `memory-template.md`.
