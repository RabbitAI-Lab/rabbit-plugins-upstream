## Description:

查询1688商品热销榜单数据，用于货源发现和批发选品调研。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, sourcing teams, and agents use this skill to query 1688 weekly or monthly bestseller rankings, compare wholesale suppliers, and identify product sourcing opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle phone numbers, SMS verification codes, API keys, and billing flows.

Mitigation: Use it only when the user intends to use LinkFox account and billing services, and do not share credentials or verification codes in untrusted environments.

Risk: The skill can create unpaid payment orders and render payment QR codes.

Mitigation: Confirm plan, price, payment method, and user intent before initiating any payment order.

Risk: The skill can send feedback content to a separate LinkFox feedback endpoint.

Mitigation: Avoid including sensitive business, account, or personal data in feedback content.

Risk: Endpoint base URLs are configurable through environment variables.

Mitigation: Run the skill only where LinkFox endpoint environment variables are trusted and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-dld-product-billboard)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The billboard script saves full JSON responses locally and may summarize large responses inline.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
