# Automation And Handoff

## Runner Contract

An outer runner may invoke one bounded loop repeatedly.

Each run must:

1. acquire a single-writer lock;
2. load state from disk;
3. validate authorization and budgets;
4. execute one loop;
5. append a loop record;
6. release the lock;
7. stop on any state other than `In Progress`.

The runner must not:

- construct new scope;
- auto-answer Owner decisions;
- retry the same failure indefinitely;
- run concurrent writers;
- accept governed work;
- hide failed verification.

## Budgets

Enforce:

- maximum ten stages;
- stage time ceiling by size;
- two consecutive core failures without progress;
- context file/size budget;
- optional cost or tool-call budget.

Budget exhaustion is a stop, not evidence of completion.

## Handoff

Prefer the Active Packet plus loop log over a new handoff file. Create a separate handoff only when a different team/agent cannot safely resume from those files.

A handoff must include:

- packet ID and stage;
- current execution and alignment states;
- last useful change;
- verification passed and failed;
- root cause when known;
- files changed;
- blockers and Owner decisions;
- exactly one next action;
- evidence paths.

Do not include a transcript or hidden reasoning.

## Multiple Agents

- Use one writer at a time.
- Give each agent a disjoint Work Order when parallel work is necessary.
- Merge and integration require a separate authorized stage.
- A reviewer should receive raw task artifacts and evidence, not the Developer's desired verdict.
- Do not let one agent silently switch from Developer to QA in governed work.
