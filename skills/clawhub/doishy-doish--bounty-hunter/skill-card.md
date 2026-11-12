## Description:

Serial-execution toolkit for winning pay-per-merge software bounties. Pre-alert ranking, stale-ticket demotion, cross-runtime boundary guards (WASM/JS hex, Rust wildcard-Ok, mutation-before-fallible), one-shot PR preflight gate, red-test scaffolder, and the anti-slop PR checklist. Built from live bounty wins on Rust, Solidity, and TypeScript lanes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doishy-doish](https://clawhub.ai/user/doishy-doish)

### License/Terms of Use:

MIT-0

## Use Case:

Developers pursuing eligible pay-per-merge software bounties use this toolkit to rank alerts, prioritize reproducible work, inspect selected diffs for common boundary errors, and prepare focused regression tests and pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The preflight gate and generated test scaffolds may give incomplete assurance because checks can be unavailable or tests can still contain placeholders.

Mitigation: Repair preflight issues, make unavailable guards fail explicitly, replace placeholders with real assertions, and independently confirm failure before the fix and success afterward.

## Reference(s):

- [Bounty Hunter on ClawHub](https://clawhub.ai/doishy-doish/skills/bounty-hunter)

## Skill Output:

**Output Type(s):** [Code, Analysis, Guidance]

**Output Format:** [JavaScript modules, ranked alert objects, guard findings, test scaffolds, and Markdown checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test scaffolds include placeholders that must be completed with real assertions.]

## Skill Version(s):

1.0.2 (source: frontmatter, package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
