## Description:

Retrieves structured Amazon product details by ASIN through the LinkFox Keepa product request API, including pricing, title, images, listing date, product attributes, FBA fees, sales rank, current monthly sales, and optional 12-month sales history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce analysts, and developers use this skill to look up one or more known ASINs across supported Amazon marketplaces and summarize product attributes, prices, sales metrics, category data, dimensions, fees, and sales trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ASIN query data and API credentials to LinkFox-operated services.

Mitigation: Install and use it only when the user accepts LinkFox as a trusted service provider; store API keys in environment variables and avoid exposing keys in chat or logs.

Risk: Authentication recovery and onboarding can involve phone-based login, OTP handling, API-key generation, and payment setup.

Mitigation: Ask the user to confirm the trust boundary before providing OTPs or API keys, and have the user explicitly approve plan selection, payment method, and any generated payment flow.

Risk: Keepa product requests consume LinkFox credits and may incur unexpectedly high cost for some queries.

Mitigation: State the marketplace, ASIN count, history setting, and cost warning before issuing paid requests, and avoid repeated retries or parameter changes without user consent.

Risk: Full API responses are persistently saved to a local linkfox session directory.

Mitigation: Tell users where response files are written when results may contain sensitive business research, and avoid adding those files to commits or shared artifacts without review.

Risk: The artifact describes automatic feedback reporting when user sentiment or skill issues are detected.

Mitigation: Avoid sending feedback content externally unless the user consents to sharing the relevant interaction details with LinkFox.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-request)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Keepa product detail API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, shell command examples, JSON request examples, product summary tables, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries are limited to 5 ASINs per request; full API responses are saved under a local linkfox session directory, with stdout summarized for responses over 8 KB unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
