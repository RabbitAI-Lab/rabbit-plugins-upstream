# PR hygiene checklist (anti-slop protocol, 2026-11-05)
Required on every bounty PR. A PR that fails any line does not ship.

1. **Inverse description (3 sentences max).** `Closes #N. Root cause: <one line>. Added regression test <name>; <exact command> passing locally.` No adjectives, no essays. Maintainers read diffs.
2. **Regression test is the deliverable.** Every production-diff ships with a failing-before/passing-after test in the repo's existing harness. No test = no PR.
3. **Strict diff hygiene.** Touch only the defect boundary. Never reformat, never touch unrelated lines, no `// increment counter` comments. 20–40 lines beats 200.
4. **Fork-CI green before filing.** fmt + full relevant test target passing on the fork; paste the exact commands + result in the PR body. Remote CI starting = unlock.
5. **Honest triage.** If the bug doesn't reproduce at HEAD (drift, already fixed, wrong repo), drop the lock and post a one-line stale note with the HEAD evidence instead of a fake fix. Saved triage time builds maintainer credit.
