# Goal Discovery

Use when the user has a concept, pain point, direction, or desired result but does not know the implementation path.

## Low-Burden Interview

Ask at most three questions per round. Ask only questions that materially change:

- desired outcome;
- primary user or situation;
- minimum useful workflow;
- legal, privacy, safety, data, budget, or environment boundary;
- observable success;
- an expensive or irreversible choice.

Do not ask the user to choose a framework, database, API style, hosting platform, test framework, or architecture unless that choice has a user-visible tradeoff.

When the user says "I do not know":

1. Give two or three plain-language options.
2. Explain the practical difference in one sentence each.
3. Recommend one default.
4. Label the recommendation as an assumption that can be changed.

Do not repeat questions already answered by the conversation, repository, or current project state.

## Interpret The Request

Restate the user's input using:

```text
Desired outcome:
Who benefits:
Current problem:
Simplest useful result:
Known constraints:
Confirmed facts:
AI inferences:
Items to confirm:
```

Never present an inference as confirmed fact.

## Readiness Ladder

| State | Required understanding | Next action |
| --- | --- | --- |
| `Concept` | Broad idea or pain point | Clarify outcome and beneficiary |
| `Direction` | Outcome and primary use | Propose simplest useful workflow |
| `Ready for Planning` | MVP boundary and success evidence | Size the goal |
| `Ready for Execution` | Scope, acceptance, constraints, authority | Dispatch execution |
| `Owner Decision Required` | Consequential choice cannot be inferred | Present options and stop on that decision |

Do not block on reversible uncertainty. Record it and choose the safest low-cost default.

## Intent Brief

Use `{baseDir}/templates/en/INTENT_BRIEF.md`. Keep it in chat by default. Persist one canonical copy only when the user asks, planning begins, or another agent needs a handoff.

The brief must distinguish:

- Must work now.
- Useful later.
- Explicitly out of scope.
- Assumptions.
- Evidence that would prove usefulness.

## Recommend One Next Step

End with one recommended action, why it is first, and what evidence it should produce. Choose one:

- clarify one blocking decision;
- observe the current workflow;
- inspect an existing repository;
- validate a user flow without code;
- build a low-cost prototype;
- define acceptance examples;
- size the goal;
- create the Active Packet;
- begin authorized execution;
- simplify, pause, or reject the idea because value or feasibility is weak.

Do not give an undifferentiated backlog.
