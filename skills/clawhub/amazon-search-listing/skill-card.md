## Description: <br>
Amazon search and category listing scraper that extracts product listings from Amazon search results, keyword search URLs, and category browse pages, returning per-item product cards and pagination state across regional Amazon domains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and marketplace operators use this skill to collect structured Amazon listing data from pages visible in their browser for price monitoring, competitive tracking, keyword ranking analysis, category audits, and ASIN list building. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes guidance for automating multiple Amazon pages and mentions stealth sessions, fingerprint variation, and proxy sharding. <br>
Mitigation: Use only when the activity is authorized and compliant with applicable site terms and policies; avoid anti-detection guidance unless it has been explicitly approved. <br>
Risk: The skill may create local page-level output files during batch extraction workflows. <br>
Mitigation: Review intended output paths before execution and avoid storing sensitive or unnecessary browsing-derived data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-search-listing) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON returned from browser-page extraction, with shell commands and procedural guidance for running pagination workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns product-card fields such as ASIN, title, URL, image, price, list price, rating, review count, badges, sponsorship flag, delivery text, social proof, position index, and pagination state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
