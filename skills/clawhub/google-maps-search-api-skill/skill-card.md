## Description: <br>
Extracts structured business listings from Google Maps search results through BrowserAct for local discovery, lead generation, competitor mapping, and market research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to run Google Maps business searches with keyword, language, country, and result-count inputs, then collect structured place data for prospecting, market research, competitor mapping, and CRM preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Maps search terms, location filters, and BrowserAct API usage are sent to BrowserAct. <br>
Mitigation: Review sensitive competitor, prospecting, or location-based searches before running the skill. <br>
Risk: The skill requires a BrowserAct API key. <br>
Mitigation: Keep BROWSERACT_API_KEY in an environment variable and avoid pasting it into shared logs or chats. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phheng/skills/google-maps-search-api-skill) <br>
- [BrowserAct Console integrations](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct workflow API endpoint](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal status logs followed by structured business search results as text or JSON fallback.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; polls BrowserAct task status before returning results.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
