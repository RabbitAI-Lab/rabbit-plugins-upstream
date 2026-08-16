## Description:

This skill helps agents search and filter Shopee product data across 11 marketplaces using LinkFox's YouYing service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce analysts, and developers use this skill to turn Shopee product-search requests into structured LinkFox API queries and inspect product, sales, price, rating, shop, and listing data across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox as a paid external service for Shopee product data.

Mitigation: Install and run it only after confirming the user accepts LinkFox service use and any credit consumption for each query.

Risk: Onboarding can send phone numbers, SMS codes, account or team details, and API credentials to LinkFox endpoints.

Mitigation: Ask for explicit confirmation before onboarding and avoid collecting or forwarding sensitive details unless they are required for the selected authentication path.

Risk: Order creation and payment QR commands can initiate paid actions.

Mitigation: Treat plan selection, order creation, payment method choice, and QR display as user-confirmed steps, and do not auto-run payment flows.

Risk: Gateway and login URL override environment variables can redirect credential-bearing requests.

Mitigation: Use the default LinkFox endpoints unless the destination is known and trusted.

Risk: Automatic feedback reporting may send user feedback or task details to a separate LinkFox feedback endpoint.

Mitigation: Avoid sending sensitive business or personal details through feedback reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-youying-shopee-get-product-infos)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox agent portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON API results saved to local files or summarized in stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shopee query results are cached for 24 hours for identical parameters; large responses are summarized while the complete JSON response is written under a linkfox session data directory.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
