## Description: <br>
This skill helps users automatically extract structured news data from Google News via BrowserAct API for topic research, trend tracking, media monitoring, competitor updates, market research, and breaking-news collection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run BrowserAct-powered Google News searches and collect structured news results for monitoring, research, and reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms may be shared with BrowserAct and used to run Google News searches, which can expose sensitive or confidential queries. <br>
Mitigation: Use the skill only when that third-party data sharing is acceptable and avoid sensitive or confidential search terms. <br>
Risk: Unsafe API-key handling could expose the BrowserAct credential. <br>
Mitigation: Configure BROWSERACT_API_KEY through an environment variable or secret manager instead of pasting the key into chat. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/phheng/skills/google-news-api-skill) <br>
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct Workflow API Endpoint](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; runtime output is plain text or JSON-like structured news results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; sends configured search keywords, date range, and item limit to BrowserAct.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
