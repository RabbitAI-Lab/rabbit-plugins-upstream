## Description:

Plans Amazon product upgrade directions and validation questions from product details and review evidence; it is not for sales forecasting, procurement, purchasing, or automatic listing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and product teams use this skill to plan Amazon product upgrade opportunities from product detail and review evidence. It helps frame upgrade priorities and validation questions after checking available data and quote details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI exposes configurable paid operation workflow fields beyond the documented fixed product-upgrade planner scope.

Mitigation: Approve paid runs only after confirming the quote, ASIN, site, requestId, workflow, and focus match the intended product/upgrade analysis.

Risk: The skill requires an ARI API key and can spend ARI credits after explicit confirmation.

Mitigation: Use quote and profile checks before execution, require explicit user confirmation for --confirm, and use status with the original requestId after interruptions instead of rerunning.

## Reference(s):

- [ClawHub listing: product-upgrade](https://clawhub.ai/funewa/skills/product-upgrade)
- [Amazon product upgrade workflow](artifact/references/operation-workflow.md)
- [Amazon product upgrade API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized ARI CLI results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid runs.]

## Skill Version(s):

1.4.13 (source: server release evidence, CHANGELOG, _meta.json, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
