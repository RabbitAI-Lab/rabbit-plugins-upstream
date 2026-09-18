## Description:

A free deterministic checker for Chinese freight monthly statements that verifies line-item arithmetic, totals, duplicate waybills, and blanks while citing source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, warehouse, and operations staff use this skill to reconcile freight monthly statements before settlement by checking arithmetic, totals, duplicate waybills, and missing values. It reports missing input instead of making unsupported conclusions when the statement cannot be parsed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a prompt that can lead an assistant into an unpinned package installation and payment flow for a separate paid skill.

Mitigation: Use this release only for local freight-statement checks unless the package source, version, and payment flow are independently verified and the paid skill is intentionally being installed.

Risk: The free release does not execute every freight-reconciliation check described for the paid version.

Mitigation: Treat the results as covering only the declared free checks and review the listed withheld and out-of-scope checks before relying on the reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/freight-reconciliation-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON reconciliation report with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided statement text; insufficient input returns missing fields and advice instead of conclusions.]

## Skill Version(s):

1.1.7 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
