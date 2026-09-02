# Task: <one line>

> Read BRIEFING.md at the repo root before starting (stack rationale / naming conventions / known traps / forbidden zones).

## Goal
<what "done" looks like, one paragraph>

## Explicitly not doing
<scope fence: which files not to touch, which interfaces not to change, which dependencies not to introduce>

## Must comply with
<interface signatures / type definitions / error-handling conventions — paste the actual code. Findings from an exempted spike go here too.>

## Constraints
<performance, compatibility, style — the hard requirements>

## Allowed paths
<whitelist of directories this task may modify. Delivery is bounds-checked against the real diff; out of bounds is rejected and redispatched serialized>
<⚠ The measuring instruments (tests / assertions / CI config) are protected: your diff must not touch them. Touching them is an automatic rejection.>

## Acceptance criteria
<one checkable item per line. Verify them yourself before delivering.>

## Verification commands
<must pass before you deliver. Tag each one persistent | one_shot;
 anything with side effects (migrations/seeds/tokens) must NOT run in your self-check — mark it "CI only" and use a side-effect-free preflight variant instead>

## Delivery header (required, ≤300 token JSON)
{"commands": [...], "exit_codes": [...], "passed": N, "first_failure": "...", "log_path": "..."}
