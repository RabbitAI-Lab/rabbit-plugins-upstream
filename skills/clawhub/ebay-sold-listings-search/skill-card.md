## Description: <br>
Searches eBay sold listings across eight marketplaces with filters and returns paginated sale records with prices, sale dates, listing type, shipping, images, and seller information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to collect eBay sold-listing comparables for resale valuation, price benchmarking, appraisal, and market research across supported regional marketplaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to continue scraping after eBay blocks access by using stealth browsers, proxies, IP switching, or distributed scraping. <br>
Mitigation: Do not use those bypass techniques; stop collection when eBay presents challenges, rate limits, regional refusal pages, or other blocking responses. <br>
Risk: The skill browses eBay, collects sold-listing data, and may write local result files. <br>
Mitigation: Install and run it only when local file output and automated collection of visible eBay sold-listing data are acceptable for the environment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/browseract-cli/skills/ebay-sold-listings-search) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or JSONL listing records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces paginated eBay sold-listing records and may write local JSONL result files for batch runs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
