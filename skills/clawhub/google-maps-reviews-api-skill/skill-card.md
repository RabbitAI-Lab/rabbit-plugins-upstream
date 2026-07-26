## Description: <br>
This skill helps an agent collect structured Google Maps review data for local businesses, brands, venues, and competitors through BrowserAct's Google Maps Reviews API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to gather Google Maps reviews for local business research, reputation monitoring, competitive benchmarking, sentiment analysis, and service-quality audits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Maps review results can include reviewer-identifying fields such as profile URLs and avatar URLs. <br>
Mitigation: Keep collection user-directed, avoid unnecessary bulk collection of identifying fields, and apply appropriate privacy controls before sharing or storing results. <br>
Risk: Use of BrowserAct to retrieve Google Maps reviews may carry platform terms, privacy, and consent obligations. <br>
Mitigation: Confirm the intended collection and analysis comply with applicable platform terms and privacy expectations before running broad or repeated jobs. <br>
Risk: The skill depends on a BrowserAct API key and an external workflow service. <br>
Mitigation: Use the BROWSERACT_API_KEY environment variable, avoid exposing the key in prompts or logs, and stop on invalid authorization rather than retrying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phheng/skills/google-maps-reviews-api-skill) <br>
- [BrowserAct Console](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct Workflow API endpoint](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Terminal status logs followed by structured review data as text or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY and accepts keywords, language, and country arguments; polls BrowserAct task status until completion.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
