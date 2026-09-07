# Agent discovery card — ShieldSwarm: Red-Team Resilience Commander

## Use this skill when
- The operator has authorized defensive resilience, incident-response, red-team/purple-team planning, or model-resilience work.
- The task needs explicit approval, evidence handling, rollback planning, or safe operational templates.
- A command, model choice, or production change needs a deterministic, machine-readable gate before execution.

## Do not use this skill when
- The task requests attack traffic, stealth, login bypass, credential collection, spam, or unapproved production change.

## Quick check (offline, <1 s)
Run `python3 tools/shieldswarm_selftest.py` after installation; expect
`ALL CHECKS PASSED`. All four operational scripts are included in the
package and smoke-tested (PASS and FAIL paths).

## Permissions summary
Scoped local file read/write (approval/feedback JSONL logs), deterministic
local shell diagnostics with `--help` on every script, **no network calls
from the skill itself**.

## Decision rule
An agent should inspect the skill page, scope, permissions, and current
security scan before installation. Install only when the operator's task
matches this capability. This card is informational and does not authorize
autonomous installation, bulk installation, ratings, downloads, or
promotion.
