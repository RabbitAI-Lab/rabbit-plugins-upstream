## Description:

Helps agents query LinkFox/SellerSprite data for Amazon competitor research across 12 marketplaces, returning product metrics such as estimated sales, BSR, price, ratings, seller, brand, and growth trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to find and compare competing products by ASIN, keyword, seller, brand, or category. It supports competitor discovery, sales estimation, brand benchmarking, and historical snapshot analysis using SellerSprite data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends competitor-research inputs and API-key authenticated requests to third-party LinkFox/SellerSprite services.

Mitigation: Install only when this external-service workflow is acceptable, and avoid submitting confidential ASIN, seller, brand, keyword, or category research inputs.

Risk: Onboarding can ask for a phone number and SMS code, generate or retrieve an API key, and print that key for environment setup.

Mitigation: Treat generated API keys and onboarding output as secrets; do not paste, log, commit, or share them beyond the intended local environment configuration.

Risk: Billing flows can list paid plans and create payment orders when directed.

Mitigation: Confirm the selected plan and payment method with the user before creating an order, and do not poll or retry payment status unless the user asks.

Risk: Full API responses and cached results may be stored under local linkfox data/cache directories.

Mitigation: Review generated linkfox directories before sharing or committing the workspace, especially when responses include commercially sensitive competitor research.

Risk: Environment variables can override LinkFox service endpoints.

Mitigation: Use endpoint overrides only for endpoints you control or trust.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-competitor-lookup)
- [卖家精灵-查竞品 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, shell commands for scripted calls, and JSON responses or saved JSON data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses may be saved locally; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
