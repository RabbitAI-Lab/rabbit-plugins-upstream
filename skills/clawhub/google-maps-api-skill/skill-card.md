## Description: <br>
This skill helps agents collect structured Google Maps business data through BrowserAct using search keywords, language, and country parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, sales, operations, and market research users can use this skill to gather local business listings, contact details, ratings, websites, and operating status from Google Maps for lead generation, competitor research, directory building, or local market analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The BrowserAct API key and search parameters are sent to BrowserAct when the skill runs. <br>
Mitigation: Keep the API key in environment configuration, avoid pasting it into chat, and install the skill only when BrowserAct-based Google Maps data collection is intended. <br>
Risk: Broad or recurring searches may collect phone numbers or other business contact data. <br>
Mitigation: Confirm the scope before lead-generation searches and review applicable privacy, compliance, and site-term obligations before using the collected data. <br>
Risk: Automated BrowserAct tasks can take several minutes and may fail or return empty results. <br>
Mitigation: Monitor status output, retry only once for non-authorization failures, and stop for invalid authorization errors until the API key is corrected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phheng/skills/google-maps-api-skill) <br>
- [Publisher profile](https://clawhub.ai/user/phheng) <br>
- [BrowserAct API key setup](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct workflow API endpoint](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Console text and structured JSON-like business listing data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; accepts keywords, language, and country inputs.] <br>

## Skill Version(s): <br>
0.1.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
