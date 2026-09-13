## Description:

Invoice Risk Scan screens invoice tax IDs, amounts, and dates before reimbursement or bookkeeping and flags anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and agent operators use this skill to run a deterministic local pre-screen of invoice fields before reimbursement or bookkeeping. Results are preliminary and should be reviewed by a qualified human for compliance decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install path uses an unpinned npx installer and can install mutable repository content globally into agent skill directories.

Mitigation: Install only from a reviewed commit or signed release, and avoid the global -g install path unless the skill should be active across agent projects.

Risk: PASS results are a preliminary invoice field check and the bundled validation has known edge cases.

Mitigation: Treat results as a screening aid and require qualified human review for compliance or bookkeeping decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/invoice-risk-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [CLI PASS/FAIL text or machine-readable JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes rc=0 for pass, rc=1 for issues found, and rc=2 for usage errors; local execution with no external runtime dependencies.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
