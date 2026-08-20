## Description:

Uses SellerSprite data to search, filter, and analyze Amazon products across supported marketplaces by price, sales, BSR, margin, ratings, fulfillment, seller, brand, and related product attributes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace analysts, and ecommerce operators use this skill to run product-level SellerSprite searches for product discovery, competitor analysis, BSR review, sales filtering, and margin screening. It helps agents prepare structured search parameters, call the product-search API, and present concise product-analysis results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and may guide users through account login or API-key generation.

Mitigation: Use secure secret storage, avoid entering verification codes on shared machines, and review credential setup before running the scripts.

Risk: The skill uses a paid credit-based service and can initiate billing or payment onboarding when credits are unavailable.

Mitigation: Review payment plans and QR codes before paying, and confirm with the user before additional searches that may consume credits.

Risk: The security summary flags account login, API-key generation, billing, persistent credential setup, and automatic feedback reporting as behaviors that need review.

Mitigation: Inspect the onboarding and feedback behavior before installation, and only install when these account, billing, credential, and reporting flows are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-product-search)
- [SellerSprite product-search API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, configuration, JSON, markdown, files]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, API responses, tabular summaries, and saved JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product-search calls consume paid credits, use API-key authentication, cache identical parameters for 24 hours, and save full responses under a linkfox session data directory while summarizing large responses.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
