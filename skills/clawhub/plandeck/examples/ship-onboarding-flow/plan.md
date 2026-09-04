# Ship the new onboarding flow

The charter for this sample plan. The board lives in `plan.yaml`; this file is
the human-readable context an agent reads first.

## North star

A new user can sign up, verify their email, and reach the welcome screen, proven
by a green end to end test (`npm run test:e2e -- onboarding`).

## Why

The current onboarding has three legacy signup paths and fires no analytics. One
clean, verified flow replaces them so activation is measurable and the next
feature ships on a foundation instead of on guesses.

## Constraints

- Do not touch billing or the existing `/v1/register` path until the new flow is green.
- SSO is optional and must not block the core flow.

## How to run this plan

- `plandeck board .` opens the live board. C005 and C010 sit in Ready because
  their only dependency (C002) is done; C003 is the active card and the gold
  chain through C001, C002, C003, C004, C008, C009 is the critical path.
- `plandeck next .` prints the single next move.
- `plandeck check .` gates completion against the north star.
