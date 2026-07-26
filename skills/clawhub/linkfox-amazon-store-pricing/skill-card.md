## Description: <br>
Helps agents query Amazon store Product Pricing data through LinkFox, including single-item and batch pricing, listing offers, item offers, featured offer expected price, and competitive summary results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketplace operators, sellers, and developers use this skill to retrieve Amazon store pricing and offer data by ASIN or SKU, compare competitive pricing, and inspect batch Product Pricing results. It requires LinkFox and Amazon store authorization and should be used only with seller data the user is authorized to access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles LinkFox API credentials, Amazon store access tokens, and seller pricing data. <br>
Mitigation: Install only if you trust linkfox-ai and LinkFox with that access; verify the configured API key and gateway environment variables before use. <br>
Risk: Full API responses may be saved locally and may contain sensitive business pricing information. <br>
Mitigation: Review the LinkFox session data directory, restrict access to saved files, and delete response files after use when they contain sensitive data. <br>


## Reference(s): <br>
- [Amazon Store Product Pricing API Reference](references/api.md) <br>
- [Amazon SP-API getPricing](https://developer-docs.amazon.com/sp-api/reference/getpricing) <br>
- [Amazon SP-API getCompetitivePricing](https://developer-docs.amazon.com/sp-api/reference/getcompetitivepricing) <br>
- [Amazon SP-API getListingOffers](https://developer-docs.amazon.com/sp-api/reference/getlistingoffers) <br>
- [Amazon SP-API getItemOffers](https://developer-docs.amazon.com/sp-api/reference/getitemoffers) <br>
- [Amazon SP-API getItemOffersBatch](https://developer-docs.amazon.com/sp-api/reference/getitemoffersbatch) <br>
- [Amazon SP-API getListingOffersBatch](https://developer-docs.amazon.com/sp-api/reference/getlistingoffersbatch) <br>
- [Amazon SP-API getFeaturedOfferExpectedPriceBatch](https://developer-docs.amazon.com/sp-api/reference/getfeaturedofferexpectedpricebatch) <br>
- [Amazon SP-API getCompetitiveSummary](https://developer-docs.amazon.com/sp-api/reference/getcompetitivesummary) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses saved as local files or printed to stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under a LinkFox session data directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
