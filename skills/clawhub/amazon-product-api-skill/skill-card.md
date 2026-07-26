## Description: <br>
This skill helps users extract structured Amazon product listings, including titles, ASINs, prices, ratings, and specifications, through BrowserAct's Amazon Product API template. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and market researchers use this skill to search Amazon by keyword, brand, page count, and language, then collect structured product data for market research, competitor monitoring, catalog enrichment, rating analysis, and price tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BrowserAct receives Amazon search terms, brand filters, page counts, language choices, and account usage associated with the API key. <br>
Mitigation: Use the skill only when this data sharing is acceptable for the task and account. <br>
Risk: The BrowserAct API key is a secret that could authorize account usage if exposed. <br>
Mitigation: Provide BROWSERACT_API_KEY through an environment variable or secret manager, use a dedicated revocable key, and avoid placing it in chat or source files. <br>
Risk: Automated browser workflow runs can fail, return empty output, or require retry handling. <br>
Mitigation: Monitor timestamped status logs, retry failed non-authorization errors once, and stop on invalid authorization errors so the key can be checked. <br>


## Reference(s): <br>
- [Amazon Product Api Skill on ClawHub](https://clawhub.ai/phheng/skills/amazon-product-api-skill) <br>
- [BrowserAct Console](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct Workflow API](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Terminal logs followed by structured product listing text or JSON from the BrowserAct API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; sends search terms, brand filters, page counts, and language choices to BrowserAct.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
