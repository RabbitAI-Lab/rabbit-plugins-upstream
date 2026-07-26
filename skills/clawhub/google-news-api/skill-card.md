## Description: <br>
Scrape structured news data from Google News automatically for topic searches, industry trend tracking, and PR monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to retrieve structured Google News results for topics, companies, industry trends, and PR monitoring through BrowserAct. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a BrowserAct API key and sends news queries to BrowserAct's external API. <br>
Mitigation: Store BROWSERACT_API_KEY in an environment variable or secrets manager and avoid pasting credentials into chat. <br>
Risk: The skill retrieves current news from an external service, so results may be incomplete, stale, or affected by upstream service availability. <br>
Mitigation: Review returned article metadata before relying on it and retry only within the documented one-retry limit. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phheng/skills/google-news-api) <br>
- [BrowserAct Console](https://www.browseract.com/reception/integrations) <br>
- [BrowserAct Workflow API](https://api.browseract.com/v2/workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Structured text or JSON-like news results printed by a Python command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns headline, source, link, published time, and author when available.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
