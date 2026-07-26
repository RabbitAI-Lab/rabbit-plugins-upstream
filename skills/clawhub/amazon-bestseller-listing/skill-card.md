## Description: <br>
Extracts ranked product listings and category pagination details from Amazon Best Sellers pages that the user can access in a browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and ecommerce operators use this skill to collect visible Amazon Best Sellers rankings, ASINs, titles, prices, ratings, image links, and pagination metadata for competitive intelligence, niche research, and rank tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a scraping workflow for Amazon pages and the security evidence flags stealth sessions, fingerprint changes, and proxies as suspicious for higher-throughput use. <br>
Mitigation: Use it conservatively only on pages accessible in a normal browser session; avoid stealth, fingerprint rotation, proxy scaling, or batch use that conflicts with Amazon terms or organizational policy. <br>
Risk: Amazon may show interstitials, gates, or changed page structures that cause missing or misleading extraction results. <br>
Mitigation: Check the browser page state, test one or two categories before larger runs, and treat extracted rankings, prices, ratings, and review counts as point-in-time page snapshots. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-bestseller-listing) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>
- [Amazon Best Sellers page pattern](https://www.amazon.com/gp/bestsellers/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON returned from browser-act evaluation, with concise Markdown guidance for setup and pagination.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes category metadata, pagination state, item count, and product fields such as rank, ASIN, title, URL, image, price, stars, review count, and raw rating text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
