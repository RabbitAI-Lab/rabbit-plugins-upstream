## Description: <br>
Extracts structured product details from an open Amazon product detail page, including title, brand, price, ratings, stock, delivery, attributes, variants, seller information, images, bestseller ranks, and sample reviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to turn an already open Amazon product page into normalized product data for catalog audits, competitive research, per-ASIN enrichment, and price or stock monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags the skill as suspicious because its operating instructions discuss scaled scraping, proxy use, stealth sessions, and CAPTCHA retry behavior. <br>
Mitigation: Review before installation, confirm the intended use complies with applicable site terms and internal policy, and restrict use to approved browsing sessions and volumes. <br>
Risk: Amazon page structure, localization, anti-bot interstitials, and session location can affect extracted fields such as price, stock, delivery, variants, reviews, and bestseller ranks. <br>
Mitigation: Validate with a small sample before batch use, inspect errors, and treat results as page-derived observations from the active browsing session. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-product-detail) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands and JSON product records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns page-derived product fields and clear JSON error messages when the page is not a supported Amazon product detail page.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
