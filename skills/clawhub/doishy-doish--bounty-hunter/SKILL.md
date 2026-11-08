---
name: bounty-hunter
description: Serial-execution toolkit for winning pay-per-merge software bounties. Pre-alert ranking, stale-ticket demotion, cross-runtime boundary guards (WASM/JS hex, Rust wildcard-Ok, mutation-before-fallible), one-shot PR preflight gate, red-test scaffolder, and the anti-slop PR checklist. Built from live bounty wins on Rust, Solidity, and TypeScript lanes.
version: 1.0.2
license: MIT
---

# Bounty Hunter

Win winner-take-all software bounties with serial execution, not parallel spray.

## Doctrine (read first: `pr-checklist.md`)

1. **One lock at a time.** Rank all alerts, lock rank 1, ignore the rest. 30-minute box: reproduce + isolate + passing test, or drop the lock.
2. **Re-verify between sprints.** Fresh competing-PR/claim check before touching ticket #2. If someone landed while you worked, kill it instantly.
3. **Max 2 consecutive sprints.** Then back to polling.
4. **Never ship a fake fix.** A dead ticket gets a one-line stale note with HEAD evidence, not a PR. Saved triage time builds maintainer credit.

## Tools

| File | Use |
|---|---|
| `pick-target.mjs` | `rankAll(alerts)` / `pickOne(alertsJson)` — repro-determinism > blast-radius (shortest-job-first) > reward density |
| `wasm-js-diff-guard.js` | Flags node-supplied hex flowing into a normalizing hash AND a raw `Buffer.from(x,"hex")` with no strict shape check and no shared try/catch |
| `wildcard-ok-guard.js` | Flags state-match `_ =>` arms returning Ok/None (swallowed variants) |
| `mutation-before-fallible-guard.js` | Flags store/cache writes preceding `?`/`await` with no restore on the error path |
| `preflight.mjs` | One-shot gate: `node preflight.mjs payload.json` — files<=3, churn<=80, regression test present, guards clean. Exit 0 = push. |
| `repro-scaffold.mjs` | Harvested `failing_assertion` → drop-in red test (`tests/repro_bounty_<id>.rs` or vitest) |
| `pr-checklist.md` | The 5-line anti-slop protocol. A PR that fails any line does not ship. |

## Bounty shape this targets

Fixer-side, pay-per-merge bounties settled in liquid rails (USDC/ETH/SOL): explicit severity tiers, first clean green PR takes the payout. Do NOT use on reservation-gated boards, house-scrip tokens, or finder-race contests — the doctrine says skip those lanes entirely.
