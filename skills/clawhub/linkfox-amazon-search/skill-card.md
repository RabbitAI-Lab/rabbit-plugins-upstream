## Description:

Simulates Amazon storefront searches to retrieve real-time search results data, including product rankings, prices, ratings, review counts, brands, delivery details, and sponsored placement signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce analysts use this skill to inspect live Amazon search result pages for keyword ranking, competitor discovery, price comparison, sponsored product analysis, and new product monitoring. It is intended for current SERP inspection rather than historical trend, campaign, sales, or inventory analysis.

### Deployment Geography for Use:

Global, across the supported Amazon marketplaces documented by the skill.

## Known Risks and Mitigations:

Risk: Search terms, optional ZIP or location parameters, onboarding phone-login data, feedback text, and API-authenticated billing requests may be sent to LinkFox services.

Mitigation: Use the skill only when that data sharing is acceptable, avoid sensitive search or business data when possible, and review the LinkFox onboarding terms before account setup.

Risk: Endpoint override environment variables can redirect API, login, or billing traffic.

Mitigation: Use default endpoints unless you control and trust the override destination.

Risk: API keys may appear in onboarding output or shell configuration instructions.

Mitigation: Treat API keys as secrets, avoid sharing logs or screenshots containing keys, and rotate credentials if exposure is suspected.

Risk: Full search results and payment-related QR artifacts may persist in local linkfox output or cache directories.

Mitigation: Review and delete local linkfox output or cache directories when results or onboarding artifacts contain sensitive information.

## Reference(s):

- [亚马逊前端搜索模拟 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-search)

## Skill Output:

**Output Type(s):** [markdown, text, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, shell commands, configuration snippets, and JSON API response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The search script saves full JSON responses under a local linkfox session data directory, uses a 24-hour local cache by default, and may summarize large responses instead of printing them inline.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
