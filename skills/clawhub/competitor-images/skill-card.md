## Description:

Compares a main ASIN with an authorized competitor's Amazon product-page images, visible product information, and review feedback to identify image-expression gaps and shooting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators and ecommerce analysts use this skill to compare a primary ASIN with an authorized competitor ASIN, inspect product-page image coverage alongside review feedback, and produce practical image-content gap notes. It is scoped to image information review and not to ad deployment, sales forecasting, inventory, orders, or automated publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the package is broader than the advertised image-gap task and can read account, product, and review data.

Mitigation: Install only if that broader ARI Amazon operations scope is acceptable, and review the skill's account, product, review, export, and monitoring behavior before use.

Risk: Paid ARI reports or operations may run under account auto-confirm rules.

Mitigation: Set auto-confirm off or use quote-only requests when paid work should require explicit approval.

Risk: The skill requires an ARI API key and may export files locally.

Mitigation: Use the documented browser authorization or environment variable flow, avoid sharing keys in chat or reports, and review exported files before redistributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-images)
- [README](README.md)
- [User guide](使用说明.md)
- [Operation workflow reference](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and natural-language summaries, with structured command output, report links, and optional local CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some ARI collection, analysis, report generation, monitoring, leaderboard, and advice workflows can involve credits or plan-gated features.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
