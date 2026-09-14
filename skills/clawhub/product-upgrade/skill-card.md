## Description:

Plans Amazon product upgrade directions and validation questions from product details and review evidence; it is not for sales forecasting, purchasing, or automatic listing changes, and it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product managers, and operators use this skill to turn Amazon product details and review samples into prioritized upgrade directions and validation questions after checking available data and quoted ARI costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that CLI overrides may allow broader paid ARI product-operations behavior than the product-upgrade description promises.

Mitigation: Review before installing if a strictly fixed product-upgrade-only tool is required; avoid workflow or focus overrides unless broader ARI product operations are intentional.

Risk: The skill uses an ARI API key and can submit paid collection or analysis operations.

Mitigation: Use only a trusted ARI account and key, inspect the quote before execution, and require explicit confirmation before paid runs.

## Reference(s):

- [Amazon Product Upgrade Workflow](references/operation-workflow.md)
- [Amazon Product Upgrade API Reference](references/reference.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/product-upgrade)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with CLI command snippets and ARI-generated product-upgrade report content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection and analysis should run only after quote review and explicit confirmation.]

## Skill Version(s):

1.4.11 (source: server release, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
