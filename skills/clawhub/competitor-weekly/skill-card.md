## Description:

After explicit user confirmation and pricing, this skill generates an evidence-based weekly comparison report for a primary Amazon ASIN and authorized competitors using product details, snapshots, and review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators and ecommerce teams use this skill to request a weekly AI report comparing a primary ASIN with authorized competitor products. The report summarizes available ARI evidence, competitor differences, trends, listing opportunities, and product improvement priorities after quote and confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits under account auto-confirm rules.

Mitigation: Use explicit per-action confirmations for paid operations and avoid broad standing permission for automatic spending.

Risk: The skill can change future confirmation thresholds and manage monitoring settings.

Mitigation: Review any autoconfirm or monitoring change before approval and keep confirmation thresholds aligned with account spending policy.

Risk: The skill can export reports or reviews to local files.

Mitigation: Specify expected export destinations and review exported content before sharing it outside the account context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-weekly)
- [ARI API and CLI Reference](references/reference.md)
- [Dedicated Operations Workflow](references/operation-workflow.md)
- [User Guide](使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report content with occasional JSON status data and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may return report URLs, report IDs, credits used, account status, and export file paths.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
