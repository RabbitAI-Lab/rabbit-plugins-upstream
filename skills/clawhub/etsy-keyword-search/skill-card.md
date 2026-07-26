## Description: <br>
Etsy Keyword Search helps an agent collect paginated product listing data from public Etsy keyword search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and marketplace operators use this skill to gather Etsy search listings for keyword research, competitor review, price monitoring, and product discovery. It is intended for public search-result pages and stops when anti-bot verification blocks automated extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags anti-bot evasion guidance and persistent bulk-scraping workflows. <br>
Mitigation: Use the skill only for intentional browser-based Etsy scraping, respect platform terms and rate limits, and stop if Etsy presents verification instead of escalating automation. <br>
Risk: The skill can write local result files during resumed or batch collection. <br>
Mitigation: Review output paths before execution and avoid storing sensitive or unnecessary data in local scrape results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/etsy-keyword-search) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON listing records with agent-facing execution guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returned listing fields include listingId, shopId, title, url, image, salePrice, originalPrice, currency, rating, reviewCount, shopName, isAd, freeShipping, badge, and positionIndex.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
