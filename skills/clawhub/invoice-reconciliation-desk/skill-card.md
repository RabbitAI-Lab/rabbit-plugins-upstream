## Description:

Derives an invoice-match threshold and builds an invoice reconciliation summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance operations staff and developers use this skill to derive a match threshold from a reconciliation rule and summarize matching invoices from local records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream operation writes a reconciliation-summary JSON file to a local directory.

Mitigation: Choose a dedicated writable output directory and review the returned receipt path.

## Reference(s):

- [Invoice Reconciliation Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-reconciliation-desk)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and, for downstream use, a local reconciliation-summary JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream use returns an effect receipt identifying the saved file.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
