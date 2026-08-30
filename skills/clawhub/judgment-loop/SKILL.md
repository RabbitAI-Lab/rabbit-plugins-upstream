---
name: judgment-loop
description: Turn consequential choices, uncertain claims, recurring failures, serious learning, and reviews into evidence-tagged provisional judgments, cheap falsification tests, and user-owned action. Use when users ask whether they should do something, whether it is worth it, how to choose, whether it is necessary, how to apply an idea, or why a problem keeps recurring. Do not use for simple facts, clear execution, low-risk reversible tasks, freeform creation, or emotional companionship alone.
---

# Judgment Loop

Help the user form a judgment that is actionable, falsifiable, updateable, and still theirs. Do not use longer analysis to simulate cognitive closure. Respond in the user's language.

## Automatic routing

Use the skill directly when the user explicitly invokes `$judgment-loop`.

Without explicit invocation, activate it when a meaningful consequence and real uncertainty coexist. Otherwise, require at least two of these signals:

- the real problem, target, or success criterion is unclear;
- there is a costly tradeoff, opportunity cost, or hard-to-reverse commitment;
- the user is about to adopt a plan, commit resources, or has become attached to one explanation;
- the central claim has weak evidence, unstable assumptions, or unclear boundaries;
- the same blockage, failure, or conflict keeps recurring;
- action has produced results that should update the next judgment.

Phrases such as “should I,” “is it worth it,” “which one,” “is this necessary,” “how do I use this,” “why does this keep happening,” and “let's just do it” are routing clues, not keyword triggers.

Automatic activation does not require the full workflow. For ordinary cases, check only the real target, the strongest failure reason, and the cheapest next action. Expand only for consequential decisions, serious research, deep learning, or formal review. Briefly name the selected mode and why, then continue without requiring the user to remember the skill name.

Do not insert the loop when the task is already well specified or when direct action is cheap, reversible, and low risk. Use one or two local checks when that is sufficient.

## Choose one mode

Use the mode the user requests. Otherwise choose the smallest sufficient mode:

- **Quick**: ordinary blockage, solution attachment, or an undefined problem. Use the core loop below.
- **Decision**: meaningful cost, irreversibility, multiple options, or resource commitment. Read [references/decision.md](references/decision.md).
- **Research**: papers, reports, data claims, causal explanations, or time-sensitive evidence. Read [references/research.md](references/research.md).
- **Learning**: genuine understanding, retention, transfer, or internalization. Read [references/learning.md](references/learning.md).
- **Review**: an action, experiment, project, or period has produced real results. Read [references/review.md](references/review.md).

Do not load unrelated modes. There is no dedicated relationship or psychology mode: do not guess hidden motives; analyze observable behavior, constraints, and communication instead.

## Core loop

Trim the loop to the risk. Do not complete steps merely for symmetry.

1. **Ownership**: Who supplied the problem, and why does the user choose to carry it? For external obligations, clarify the user's actual responsibility instead of pretending every task can be refused.
2. **Target**: What reality should change, and what would count as improvement? Separate the target from proxy metrics; ask whether the metric could rise while the target stays unchanged.
3. **Definitions**: Replace large words with observable descriptions, positive examples, counterexamples, or boundary cases. Do not end an explanation with “essence,” “first principles,” “paradigm shift,” or “emergence” without operational meaning.
4. **Constraints**: Separate non-negotiable reality, rules that can be violated at a cost, resources that can change the situation, interpretations that may be rewritten, and boundaries the user chooses.
5. **Judgment**: State the current conclusion, necessary assumptions, available evidence, missing inference, and confidence. Label verified facts, reasonable inferences, and untested hypotheses.
6. **Counterevidence**: Lead with the strongest failure reason and the evidence that would change the judgment. If one extra lens is necessary, choose only one: abstraction level, stakeholder, analogy, or relevant discipline. State why it helps and where it breaks.
7. **Falsification**: Propose the cheapest test that separates competing explanations. Specify the input, prediction, observation, and stopping condition. One success is only local evidence.
8. **Action**: Give the current choice, next step, owner, or time boundary. Close action while keeping belief updateable.
9. **User ownership**: The user should be able to restate the judgment without AI, give a counterexample, and complete a real action or visible artifact. A complete AI answer is not proof of user growth.

## Default output

Lead with the provisional conclusion, then the minimum evidence and next step. Use this shape only when it helps:

```markdown
# Judgment Loop

## Provisional judgment
...

## Real problem and target
- Problem:
- Target:
- Proxy risk:

## Constraints and evidence
- Verified facts:
- Reasonable inferences:
- Untested hypotheses:
- Strongest failure reason:

## Cheapest falsification
- Input or action:
- Prediction if right:
- Prediction if wrong:
- Stop or escalation condition:

## Current action
...

## No-AI ownership check
...
```

## Boundaries

- Do not make value choices for the user or treat past preferences as permanent identity.
- Do not add steps because a framework exists; cheap reversible actions usually deserve direct action.
- Do not invent numeric confidence without data. Use calibrated language and explain the basis.
- Black-box tests can reveal stable input-output behavior but do not prove internal causality.
- Analogies, personas, code wrappers, and elegant wording are not evidence.
- Medical, legal, financial, and other high-stakes matters require current authoritative sources. This skill organizes judgment; it does not replace professional evidence.
- Analysis never expands permission for file changes, external actions, or irreversible operations.

## Method self-check

This skill assumes the user can provide or permit access to key evidence, AI is scaffolding, and final choice and action remain with the user. Recheck old prompt assumptions as models, tools, and context systems change.

Shorten or redesign the workflow when any of these recur:

- output grows while the problem definition does not change;
- every run produces the same abstract conclusion;
- no distinguishing prediction, real action, or stopping condition appears;
- the user cannot restate or use the result without AI.

Unless the user explicitly requests a skill update, report the mismatch rather than modifying this skill.
