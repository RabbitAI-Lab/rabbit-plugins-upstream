## Description: <br>
Extracts product listings from public eBay search or category pages, returning item cards with pricing, seller, image, review, and pagination fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and developers use this skill to extract visible listing data from public eBay search and category pages for price comparison, competitive monitoring, brand keyword tracking, and catalog audits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be used at scale against eBay pages where anti-bot friction, captcha pages, or site access restrictions appear. <br>
Mitigation: Use only where permitted, avoid stealth or captcha-bypass workflows, keep explicit item and page caps, and stop when eBay presents access challenges. <br>
Risk: Saved extraction results or memory files may retain marketplace data beyond the immediate task. <br>
Mitigation: Store only the fields needed for the task and clean up saved result or memory files when they are no longer required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/ebay-search-listing) <br>
- [Skill instructions](SKILL.md) <br>
- [Listing extractor script](scripts/extract-listing.py) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON result objects with optional Markdown progress or troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Per-page item arrays plus pagination fields; supports item caps through --max-items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
