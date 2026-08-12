## Description:

友鹰-Shopee商品搜索 helps agents query and filter Shopee product data across 11 marketplaces for product discovery and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agent users use this skill to search and filter Shopee product listings by marketplace, keyword, price, sales, ratings, category, shop, and listing recency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopee search queries and API credentials are sent to LinkFox services.

Mitigation: Install and use the skill only when sharing those queries and credentials with LinkFox is acceptable; avoid custom LinkFox endpoint environment variables unless the destination is trusted.

Risk: The onboarding flow can request phone/SMS verification and expose paid credit purchase flows.

Mitigation: Confirm costs, selected plans, and payment methods with the user before initiating purchases or follow-up billing actions.

Risk: The scripts write full API responses and cache data under LinkFox, home, workspace, or temporary directories.

Mitigation: Review saved files after use and remove local response or cache data that should not persist.

Risk: Automatic feedback reporting can send user-visible feedback about skill behavior to the publisher.

Mitigation: Avoid including sensitive business details, credentials, or private user data in feedback content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-youying-shopee-get-product-infos)
- [友鹰-Shopee 商品选品 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under LinkFox session data directories; large responses print summaries unless inline output is requested; repeated parameter combinations may use a 24-hour cache.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
