# <Plan title>

The charter. A human or an agent reads this first, then works the board in
`plan.yaml`. Keep it short; the board holds the moving parts.

## North star

<The observable proof this is truly done: a passing test, a working demo, a
shipped artifact, a benchmark, a decision. If you cannot name it, you cannot
finish it.>

## Why

<One paragraph: what changes for whom when this is done.>

## Constraints

- <Non-negotiables: files to leave alone, interfaces to keep, deadlines.>

## How to run this plan

- `plandeck board .` opens the live Kanban.
- `plandeck next .` prints the single next action after a `/clear`.
- `plandeck check .` validates the plan and gates completion.
- Edit `plan.yaml` to move cards, add estimates, and record receipts. The board
  promotes a card to **Ready** the moment its dependencies are all done, lights
  up the **critical path**, and rolls up progress. You never place those by hand.
