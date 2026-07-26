## Description: <br>
Walmart Product Reviews helps an agent navigate Walmart product review pages and extract paginated customer review data, including ratings, text, author details, dates, verification badges, helpfulness counts, variants, seller information, and photo metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to collect structured Walmart customer review data for user-directed review export, market research, competitor benchmarking, sentiment analysis, and review monitoring. The skill is intended for pages the user can access in their browser and returns review records page by page. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flagged the skill as suspicious because it may encourage anti-detection browsing for scraping workflows. <br>
Mitigation: Use only for user-directed, permitted review collection; respect Walmart's terms, robots and rate limits; avoid stealth or fingerprint-spreading tactics; and review generated scripts before execution. <br>
Risk: Batch scraping can trigger site rate limits or collect more customer review data than intended. <br>
Mitigation: Run a small 1-2 page test first, keep pagination serial with conservative delays, stop when the requested scope is complete, and store only the review data needed for the task. <br>
Risk: The extractor depends on Walmart page data structures that may change without notice. <br>
Mitigation: Validate the first page result before relying on a batch run and treat extraction errors or empty results as a signal to re-check the page structure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/walmart-product-reviews) <br>
- [Walmart reviews page pattern](https://www.walmart.com/reviews/product/{item-id}?page={page}) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, code, guidance] <br>
**Output Format:** [JSON review records with agent guidance and shell/browser automation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each page normally returns up to 10 reviews plus summary fields such as total review count, average rating, rating breakdown, lookup ID, and error messages when extraction fails.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
