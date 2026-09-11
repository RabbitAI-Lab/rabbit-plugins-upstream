## Description:

Extracts evidence-backed product differentiation opportunities from a primary Amazon ASIN and authorized competitor product details, images, and review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and ecommerce teams use this skill to compare a primary ASIN against approved competitors, validate differentiation opportunities, and identify follow-up questions before changing listings or products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI workflows can spend account credits, and some small paid actions may run with reduced confirmation under account rules.

Mitigation: Use explicit quote-only wording when pricing information is needed without execution, and set autoconfirm off when every paid action should require confirmation.

Risk: Monitoring or billing-confirmation settings can affect future credit use.

Mitigation: Require clear user approval before changing schedule or autoconfirm settings, and state the returned cost or confirmation rule after any change.

Risk: The skill needs access to an ARI API key and Amazon product, competitor, review, and report data.

Mitigation: Use the browser authorization flow or environment variable support, avoid exposing the API key in chat or reports, and install only when that data access is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/differentiation)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)
- [Operation workflow reference](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [Usage guide](使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text guidance, with optional inline shell commands for setup, quoting, and confirmed ARI operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ARI account authorization and Amazon product, competitor, and review evidence; excludes market-size, sales, ads, inventory, purchasing, and order decisions.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
