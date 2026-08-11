## Description:

Queries and filters Etsy products by keyword or product URL, price, sales, favorites, reviews, listing date, category, product type, and marketplace labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Etsy sellers, marketplace researchers, and agent users use this skill to find and compare Etsy listings by commercial signals such as price, sales, favorites, reviews, listing time, category, and product labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Etsy search inputs and API credentials are sent to LinkFox services.

Mitigation: Use the skill only when the user is comfortable sharing those inputs and credentials with LinkFox.

Risk: The artifact includes account login, API-key generation, and payment-order flows beyond product search.

Mitigation: Prefer the self-service LinkFox account page for account setup and do not run payment commands unless the user intentionally wants to buy credits.

Risk: Query results and payment QR artifacts may be saved in local linkfox output or cache directories.

Mitigation: Periodically remove local linkfox output and cache directories when those results or payment files are sensitive.

## Reference(s):

- [_ehunt_productQuery API Reference](references/api.md)
- [Authentication and Credits Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-product-query)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with JSON API results and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large API responses are summarized in stdout while the full response is saved under a local linkfox session directory.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
