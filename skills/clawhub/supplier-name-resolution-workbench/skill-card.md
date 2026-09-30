## Description:

Reconcile supplier names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Purchasing and accounts teams use this skill to compare supplier names using supplied matching guidance and review the resulting match and local report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect supplier match could mislead reconciliation decisions.

Mitigation: Provide structured matching guidance for important work and review the match result before relying on it.

Risk: The local CSV report may contain supplier information.

Mitigation: Choose an appropriate output directory and review the report before sharing it.

## Reference(s):

- [Supplier Reconciliation Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-name-resolution-workbench)

## Skill Output:

**Output Type(s):** [Structured match result, Local CSV report]

**Output Format:** [JSON match_result object and CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a match decision, normalized supplier names, and a score; writes a CSV report under the chosen output directory.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
