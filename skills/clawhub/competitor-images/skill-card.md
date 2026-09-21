## Description:

Compares a primary Amazon ASIN with authorized competitor product pages to identify image-field, visible-information, and review-backed expression gaps for image review and shoot planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to compare a target Amazon listing against authorized competitors and produce image-gap findings, review-backed evidence, and practical shooting notes. It is scoped to product image information review and excludes ad deployment, sales forecasting, inventory, orders, and automatic publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can check account and billing status, collect review data, and spend ARI credits after confirmation.

Mitigation: Review the quoted cost and requestId before execution, and run paid operations only after explicit user confirmation.

Risk: Security evidence says the CLI can run broader paid product-operation workflows than the advertised image-gap scope.

Mitigation: Use the documented page_compare/images workflow and treat direct workflow or focus overrides as outside the advertised scope unless the publisher tightens or documents them.

## Reference(s):

- [Amazon Competitor Image Gap API Reference](artifact/references/reference.md)
- [Dedicated Operations Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/competitor-images)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise findings and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis steps require a quote and explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: server release, artifact _meta.json, CHANGELOG, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
