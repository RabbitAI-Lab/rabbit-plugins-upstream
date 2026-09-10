## Description:

Analyzes Amazon bestseller reviews to identify customer pain points, purchase drivers, trend signals, competitor differences, and Listing improvement opportunities from ARI review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product operators, and marketplace researchers use this skill to analyze collected Amazon review data, compare competitors, validate product opportunities, and turn customer feedback into Listing and product-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable ARI review workflows may spend account credits automatically under the account's confirmation rules.

Mitigation: Before analysis, ask the agent to quote only or to ask before every credit deduction, and review the returned credit cost and balance before authorizing paid commands.

Risk: The skill can change future confirmation behavior, which may allow later runs to proceed with less friction.

Mitigation: Use explicit confirmation settings such as requiring approval before each credit deduction, and review any confirmation-rule changes the agent reports.

Risk: Recurring monitoring can create ongoing review-collection costs.

Mitigation: Enable schedules only after the cadence and cost are clear, and periodically inspect monitored ASINs and account billing.

Risk: Interrupted paid workflows may already have charged credits or generated reports before the local connection fails.

Mitigation: Check existing reports or workflow status before retrying a paid command to avoid duplicate generation.

Risk: Review conclusions may be incomplete when ARI has limited samples, short time windows, or uncertain variant coverage.

Mitigation: Require outputs to state the sample range, review window, and known coverage limits, and validate product decisions against additional evidence when stakes are high.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/hot-review)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Account and Authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown reports with occasional shell commands, report links, and export guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Outputs may include review summaries, VOC reports, trend and keyword interpretations, competitor comparisons, Listing suggestions, account status notes, credit-use notices, report URLs, and export instructions.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
