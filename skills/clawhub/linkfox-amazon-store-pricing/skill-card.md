## Description:

Enables agents to retrieve Amazon store Product Pricing data through LinkFox, including getPricing, competitive pricing, listing/item offers, featured offer expected price, and competitive summary operations for single-item and batch workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query Amazon Product Pricing data for pricing checks, competitive offer review, featured-offer analysis, and batch pricing workflows from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes account login, API-key generation, and billing or payment-order flows.

Mitigation: Provide phone numbers, SMS codes, API keys, plan selections, or payment choices only when intentionally resolving LinkFox authentication or billing, and review each payment step before proceeding.

Risk: Credential-bearing LinkFox endpoints can be configured through environment variables.

Mitigation: Keep endpoint override variables unset unless you control and trust the destination.

Risk: Saved response files may contain sensitive Amazon seller, pricing, or business data.

Mitigation: Run the skill in a trusted workspace and review local linkfox session files before sharing logs or project directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-pricing)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Amazon Product Pricing API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Amazon SP-API getPricing](https://developer-docs.amazon.com/sp-api/reference/getpricing)
- [Amazon SP-API getCompetitivePricing](https://developer-docs.amazon.com/sp-api/reference/getcompetitivepricing)
- [Amazon SP-API getListingOffers](https://developer-docs.amazon.com/sp-api/reference/getlistingoffers)
- [Amazon SP-API getItemOffers](https://developer-docs.amazon.com/sp-api/reference/getitemoffers)
- [Amazon SP-API getItemOffersBatch](https://developer-docs.amazon.com/sp-api/reference/getitemoffersbatch)
- [Amazon SP-API getListingOffersBatch](https://developer-docs.amazon.com/sp-api/reference/getlistingoffersbatch)
- [Amazon SP-API getFeaturedOfferExpectedPriceBatch](https://developer-docs.amazon.com/sp-api/reference/getfeaturedofferexpectedpricebatch)
- [Amazon SP-API getCompetitiveSummary](https://developer-docs.amazon.com/sp-api/reference/getcompetitivesummary)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses saved as local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are written under a local linkfox session data directory; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
