## Description:

A free local Node.js checker for chain-store settlement tables that recalculates row arithmetic, totals, duplicate rows, blanks, and negative amounts, with source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill during monthly settlement, reconciliation, or inventory-close workflows to check chain-store settlement tables before payment or follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may assume the free version covers every settlement-table issue even though several checks are intentionally omitted.

Mitigation: Review the reported checks_not_run list and manually assess omitted items or use the complete product where those checks are required.

Risk: Settlement tables can contain sensitive commercial or franchise data.

Mitigation: Run the local Node.js checker only in an approved environment and avoid sharing input files outside the intended workspace.

Risk: The interface and expected settlement-table labels are primarily Chinese, which can lead to missing or misread inputs for other users.

Mitigation: Confirm required column labels and inspect missing-input guidance before relying on the findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/chain-store-settlement-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or structured JSON containing executed checks, findings, missing-input guidance, and checks not run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; accepts JSON or pasted table text and reports the free-version scope.]

## Skill Version(s):

1.0.52 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
