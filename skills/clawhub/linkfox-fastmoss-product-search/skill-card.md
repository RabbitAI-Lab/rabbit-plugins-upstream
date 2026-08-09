## Description:

Searches and filters FastMoss TikTok Shop product data across supported markets, including sales, GMV, pricing, ratings, commission rates, creator promotion counts, and shop information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and commerce researchers use this skill to search TikTok Shop product data, compare sales and GMV signals, and identify products by keyword, category, market, shop type, commission rate, and creator activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls external LinkFox and FastMoss services and uses LinkFox API credentials.

Mitigation: Install only when those external calls are acceptable, keep endpoint environment variables pinned to official LinkFox hosts, and avoid exposing API keys in prompts or logs.

Risk: The onboarding flow can guide phone/SMS login, API-key creation, and paid recharge orders.

Mitigation: Do not share SMS codes unless intentionally onboarding, and require explicit user confirmation before account setup or payment-related steps.

Risk: Full product-search responses are stored locally and may contain commercially sensitive research results.

Mitigation: Store results only in appropriate workspaces and delete saved JSON files when they are no longer needed.

Risk: The security scan verdict is suspicious because the skill includes account setup, payment flows, feedback reporting, external calls, and persistent data storage.

Mitigation: Review the skill, its configured endpoints, and its credential and billing behavior before installation or deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-fastmoss-product-search)
- [FastMoss-TikTok商品搜索 API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown summaries and tables, JSON API responses, shell commands, and local JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product-search script writes full responses under the current workspace and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
