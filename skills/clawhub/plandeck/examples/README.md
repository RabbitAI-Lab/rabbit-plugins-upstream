# Examples

## ship-onboarding-flow

A ten card plan for shipping a new user onboarding flow, with a real dependency
graph so the intelligence is visible at a glance.

```bash
node ../../scripts/cli.mjs board ship-onboarding-flow
# or from the repo root:
node scripts/cli.mjs board examples/ship-onboarding-flow
```

What to look for on the board:

- **Ready auto-promotion.** C005 and C010 are written as `column: backlog`, but
  their only dependency (C002) is done, so Plandeck shows them in **Ready**. You
  never place a card in Ready by hand.
- **The critical path.** C001, C002, C003, C004, C008, C009 form the longest
  points weighted chain (17 points), drawn in gold with a star on each card.
- **The one next move.** C003 is active, so `plandeck next` points at it. Mark it
  `done` and watch C004 unlock, the path recompute, and the ring tick up.
- **A blocked card.** C007 (optional SSO) is `blocked`, waiting on credentials,
  so it sits in its own lane and never pretends to be workable.

Try it: open `ship-onboarding-flow/plan.yaml`, set C003 to `column: done`, and
watch the board reorganize itself.
