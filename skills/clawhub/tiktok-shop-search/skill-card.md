## Description: <br>
Extracts TikTok Shop product search results by keyword and country region, returning product identifiers, titles, prices, seller and shop details, ratings, review and sold counts, images, SKU variants, brand data, and product URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and commerce operators use this skill to collect publicly visible TikTok Shop search listing data for market research, competitor tracking, product discovery, and pricing analysis. <br>

### Deployment Geography for Use: <br>
Global, subject to TikTok Shop regional availability and applicable local requirements. <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation that collects TikTok Shop listing data may be subject to TikTok Shop rules and applicable law. <br>
Mitigation: Use the skill only when the intended collection is permitted, and review site terms, legal requirements, and organizational policy before execution. <br>
Risk: The artifact includes guidance involving stealth browsers, proxies, multi-session collection, and CAPTCHA handling. <br>
Mitigation: Avoid those tactics unless they have been specifically reviewed and approved for compliance with TikTok Shop rules and applicable law. <br>
Risk: The skill may read or append operational notes in a local memory file when unexpected execution conditions occur. <br>
Mitigation: Review the memory-file behavior before use if local working-directory notes are not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/tiktok-shop-search) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>
- [TikTok Shop search URL pattern](https://shop.tiktok.com/{country_code_lower}/s?q={keyword}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON extraction output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces paginated product search records with product, seller, pricing, rating, image, SKU, and URL fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
