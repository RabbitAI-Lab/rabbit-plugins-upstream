## Description: <br>
Extracts paginated public product listings from Etsy category and subcategory pages, returning listing IDs, shop IDs, titles, URLs, images, prices, ratings, review counts, shop names, ad markers, shipping badges, and pagination state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers, ecommerce operators, and developers use this skill to collect Etsy category listing data for trend research, competitor benchmarking, seasonal monitoring, supplier discovery, and category export workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags instructions for stealth sessions, proxy or fingerprint changes, and multi-session scraping when Etsy blocks automation. <br>
Mitigation: Keep use within Etsy's rules and applicable laws; if Etsy presents an anti-bot challenge, stop rather than attempting stealth, proxy, fingerprint rotation, or similar bypasses. <br>
Risk: Scraped marketplace listing data may be saved to files during batch collection. <br>
Mitigation: Review and control any files created from scraped results, and retain only data the user is authorized to collect and use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/etsy-category-listing) <br>
- [Etsy category page example](https://www.etsy.com/c/jewelry) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [JSON object emitted by browser DOM extraction, with markdown instructions for navigation and error handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes one page of listings at a time plus current page, count, nextPageUrl, and error fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
