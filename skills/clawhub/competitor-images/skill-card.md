## Description:

Compares a primary ASIN with an authorized competitor's product-page image fields, visible listing information, and review feedback to identify image expression gaps and shooting notes; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and their agents use this skill to compare a product ASIN against an authorized competitor and turn image, listing, and review evidence into a concise image-gap report. It is intended for product-page image review and listing improvement, not advertising execution, inventory, order, or sales forecasting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is presented as an image-comparison skill, but security evidence says it includes broader ARI account, billing-enabled analytics, monitoring, export, and account-management capabilities.

Mitigation: Install it only when that broader ARI assistant scope is expected, and keep routine use constrained to the documented image comparison workflow unless the user explicitly asks for another ARI task.

Risk: The skill uses a local ARI API key and authenticated account or review queries.

Mitigation: Use a dedicated ARI key, do not paste secrets into chat or reports, revoke unused keys, and keep custom API base URLs disabled unless the user explicitly controls the environment.

Risk: Some commands can spend credits through explicit confirmation or account auto-confirm rules.

Mitigation: Use explicit 'only quote, do not execute' wording for pricing checks, verify quoted cost and balance before confirmed runs, and consider turning auto-confirm off for review-before-spend workflows.

Risk: Monitoring, schedule changes, and local exports can persist data access patterns or create shareable files.

Mitigation: Require clear user approval before creating or changing monitoring and review export contents before sharing or uploading generated files.

## Reference(s):

- [Dedicated Operations Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-images)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report text with supporting CLI JSON, command guidance, and optional local CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid operations require quote and confirmation unless the user's account auto-confirm rules apply.]

## Skill Version(s):

1.4.7 (source: server release, SKILL.md frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
