## Description:

Uses ARI Amazon review data to generate listing optimization guidance, including titles, bullet points, A+ copy, VOC reports, competitor comparisons, alerts, exports, and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to analyze collected customer reviews, identify pain points and buying motives, and turn those signals into Listing copy, product improvement priorities, reports, and monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI workflows can spend credits automatically under server-side auto-confirm rules.

Mitigation: Use quote-only requests when pricing is needed without execution, and set ARI confirmation mode to always ask before running paid workflows.

Risk: The skill sends product and review data to ari.funewa.com for analysis and reporting.

Mitigation: Install only when this data sharing is acceptable for the user's ARI account and product-review data.

Risk: Interrupted paid workflows may already have consumed credits and produced a report.

Mitigation: Check existing reports or operation status before retrying a paid command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/listing-optimizer)
- [ARI CLI and API reference](references/reference.md)
- [ARI user guide](使用说明.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Natural-language guidance, Markdown reports, JSON CLI responses, and CSV/Markdown/HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ARI authorization; outputs may include report links, sample scope, credits used, and account-specific status.]

## Skill Version(s):

1.4.13 (source: server evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
