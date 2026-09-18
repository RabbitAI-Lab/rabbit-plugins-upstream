## Description:

A free local checker for mall concession rent worksheets that recalculates line items, reconciles totals, detects duplicate, blank, and negative-value issues, and cites source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations employees use this skill during monthly close, reconciliation, or inventory checks to verify mall concession rent worksheets against the values provided in the input. It is useful for line-by-line arithmetic, total cross-checks, duplicate and blank detection, and insufficient-input reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious because the documentation steers users toward unpinned remote installation and purchase steps outside the reviewed artifact.

Mitigation: Use the free local checker only with inputs you are comfortable processing locally; do not run the unpinned npx installer or load external onboarding content unless you independently verify the package, source, and purchase flow.

Risk: The free checker intentionally omits several paid-tier checks, so a clean result does not cover all reconciliation scenarios named in the artifact.

Mitigation: Treat results as limited to the listed free checks and review omitted checks against the contract and accounting controls before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/mall-concession-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or structured JSON from a local Node.js CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include source row references; insufficient input returns missing fields instead of conclusions.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
