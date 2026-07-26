## Description: <br>
Walmart Keyword Search extracts structured product listing data from Walmart search result pages by keyword, page, and sort order. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect Walmart search result listings for price comparison research, product URL discovery, ranking monitoring, and catalog data extraction. It returns the product fields visible in Walmart search results, including item IDs, URLs, titles, prices, ratings, availability, seller information, and fulfillment data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes guidance for stealth browser sessions and fingerprint splitting that could support bulk scraping or attempts to work around access limits. <br>
Mitigation: Remove or ignore stealth-session and fingerprint-splitting guidance, keep collection runs modest, and respect Walmart access limits and terms. <br>
Risk: The skill may read or append local experience notes, which can persist observations across tasks. <br>
Mitigation: Review the local memory file behavior before use and avoid recording sensitive task details or product search outputs in experience notes. <br>
Risk: Walmart page structure, pagination caps, or anti-scraping behavior can make extraction incomplete or fail unexpectedly. <br>
Mitigation: Test one or two pages before batching, check error responses and item counts, and stop or revise the run when page behavior changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/walmart-keyword-search) <br>
- [Walmart search page](https://www.walmart.com/search) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, JSON] <br>
**Output Format:** [Markdown guidance with browser navigation steps, shell commands, and JSON extraction output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Extraction returns paginated Walmart product listing objects. Keep runs modest, respect Walmart access limits and terms, and validate a small sample before batching.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
