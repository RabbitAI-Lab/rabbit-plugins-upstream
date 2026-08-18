## Description:

亚马逊店铺商品定价 skill that helps agents call Amazon SP-API Product Pricing operations through LinkFox, including pricing, competitive pricing, listing and item offers, batch offers, featured offer expected price, and competitive summary workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to retrieve Amazon store pricing and offer data for ASIN and SKU workflows, including single-item, batch, FOEP, and competitive-summary queries. It is intended for authorized LinkFox and Amazon store contexts where the user understands account, billing, and local data persistence implications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence marks the package suspicious because a pricing-focused skill includes account login and payment helpers.

Mitigation: Install only when LinkFox is trusted for the related Amazon account, store, and billing workflows, and prefer API-key setup through the dedicated auth skill or the official LinkFox site.

Risk: SMS-code login and payment-order flows can affect account access or billing if invoked unintentionally.

Mitigation: Do not enter SMS codes or initiate payment orders from this skill unless the user explicitly intended that onboarding or billing flow.

Risk: Configurable LinkFox endpoint environment variables can redirect requests to non-default services.

Mitigation: Do not set custom LinkFox endpoint variables unless the endpoint is controlled and trusted.

Risk: Full pricing responses are saved locally by the scripts.

Mitigation: Treat saved response files as sensitive store data and review the local linkfox session data directory before sharing or retaining outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-pricing)
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai)
- [Artifact API Reference](artifact/references/api.md)
- [Artifact Onboarding Reference](artifact/references/onboarding.md)
- [Amazon SP-API getPricing](https://developer-docs.amazon.com/sp-api/reference/getpricing)
- [Amazon SP-API getCompetitivePricing](https://developer-docs.amazon.com/sp-api/reference/getcompetitivepricing)
- [Amazon SP-API getListingOffers](https://developer-docs.amazon.com/sp-api/reference/getlistingoffers)
- [Amazon SP-API getItemOffers](https://developer-docs.amazon.com/sp-api/reference/getitemoffers)
- [Amazon SP-API getItemOffersBatch](https://developer-docs.amazon.com/sp-api/reference/getitemoffersbatch)
- [Amazon SP-API getListingOffersBatch](https://developer-docs.amazon.com/sp-api/reference/getlistingoffersbatch)
- [Amazon SP-API getFeaturedOfferExpectedPriceBatch](https://developer-docs.amazon.com/sp-api/reference/getfeaturedofferexpectedpricebatch)
- [Amazon SP-API getCompetitiveSummary](https://developer-docs.amazon.com/sp-api/reference/getcompetitivesummary)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full pricing responses under a local linkfox session data directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.7 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
