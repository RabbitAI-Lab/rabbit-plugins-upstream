## Description:

Build an invoice reconciliation summary from a selected match threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance teams and agents use a matching threshold to summarize which invoice candidates qualify for reconciliation. The skill saves a local summary and can send the result to a configured delivery destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice-derived results may be sent to an external service when delivery is configured.

Mitigation: Leave delivery endpoint and related API key settings unset unless outbound delivery is intended; review the destination before using real financial data.

Risk: The skill writes reconciliation results to a local artifact directory.

Mitigation: Use a dedicated writable output directory with access appropriate for financial records.

## Reference(s):

- [Invoice Matching Desk release](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON reconciliation summary and local JSON artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the applied threshold, matched invoice IDs and count, and a local artifact receipt; includes a delivery receipt when configured.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
