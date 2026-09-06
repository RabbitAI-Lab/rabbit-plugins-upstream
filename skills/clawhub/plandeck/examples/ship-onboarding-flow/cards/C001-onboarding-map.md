# C001 — Map the current onboarding

A long receipt lives here when it does not fit on the card. The card in
`plan.yaml` points at it with `receipt: { note: cards/C001-onboarding-map.md }`,
and the board shows it in the card's detail view.

## What is live

- `/v1/register` is the only signup path that reaches production (`src/auth/register.ts`).
- Two legacy paths (`/signup`, `/onboard`) still have routes but 404 behind the gateway.

## What is missing

- No email verification step exists anywhere.
- Analytics fires on zero onboarding events, so activation is unmeasurable today.

## Evidence

- `src/auth/register.ts:41` handles the one live path.
- `src/onboarding/` has UI shells but no wired backend.

## Verification path for the north star

`npm run test:e2e -- onboarding` is the command that will prove the full flow
once C004, C005, and C008 are done.
