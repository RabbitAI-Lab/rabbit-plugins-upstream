## Description: <br>
Extracts full item detail from an open eBay item URL and returns structured JSON fields including title, price, seller, condition, images, availability, shipping, and item specifics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, catalog operators, and product researchers use this skill to extract structured data from individual eBay listings already open in the browser for enrichment, monitoring, comparison, and catalog audit workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports scraping-oriented eBay item extraction and includes guidance that could encourage high-throughput or rate-limit-avoidance workflows. <br>
Mitigation: Use it only for authorized, user-directed listing extraction, keep runs small or serial, and respect eBay's rules and rate limits. <br>
Risk: Collected listing details may be written to disk during batch workflows. <br>
Mitigation: Confirm the storage location and retention need before persisting item data, and avoid storing unnecessary seller or listing fields. <br>
Risk: DOM-based extraction can return incomplete or stale values when eBay redirects, blocks access, changes selectors, or lazily loads page data. <br>
Mitigation: Validate the returned item number, title, and key fields before using the JSON in downstream catalog, pricing, or monitoring decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/ebay-item-detail) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [json, shell commands, guidance] <br>
**Output Format:** [JSON emitted by a browser DOM extraction command, with Markdown guidance in the skill instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns nullable fields for listing attributes that are absent or unavailable on the current eBay item page.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
