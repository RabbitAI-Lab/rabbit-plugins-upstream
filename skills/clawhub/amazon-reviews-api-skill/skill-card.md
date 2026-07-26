## Description: <br>
This skill helps users automatically extract Amazon product reviews via the Amazon Reviews API for product feedback, competitive analysis, sentiment monitoring, and review data collection by ASIN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to fetch structured Amazon product review data for a supplied ASIN. Typical uses include product feedback review, competitor analysis, market research, sentiment monitoring, verified-purchase comparison, and quality-assurance insight gathering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a BrowserAct API key and sends the provided Amazon ASIN to BrowserAct for review extraction. <br>
Mitigation: Confirm the user intends to use BrowserAct before execution, use BROWSERACT_API_KEY from the environment, and do not expose or echo the key in responses or logs. <br>
Risk: Returned review data can include reviewer names, profile links, countries, ratings, and review text that may be personal or profile-related information. <br>
Mitigation: Handle extracted review results according to applicable privacy and platform policies, and avoid unnecessary retention or redistribution of profile-related fields. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/phheng/skills/amazon-reviews-api-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/phheng) <br>
- [BrowserAct Integrations Console](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct Workflow API Endpoint](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text with status logs and structured Amazon review data, often returned as JSON or a structured string.] <br>
**Output Parameters:** [1D; ASIN string input.] <br>
**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; polls BrowserAct until completion and retries once on non-authorization failure.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
