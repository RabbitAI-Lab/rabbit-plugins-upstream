## Description: <br>
Daily news and hot topics via the 6551 API. Supports news categories, hot news articles, and trending tweets by category. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[infra403](https://clawhub.ai/user/infra403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch public daily news categories, hot news articles, and trending-topic data from the 6551 API through agent-proposed curl requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes network requests to ai.6551.io to retrieve public news and trending-topic data. <br>
Mitigation: Install and use it only in environments where outbound requests to ai.6551.io are acceptable. <br>
Risk: Returned news and trending-topic data may be cached, periodically updated, or temporarily unavailable while data is generated. <br>
Mitigation: Treat responses as time-sensitive public data and handle 503 responses or stale results in downstream workflows. <br>


## Reference(s): <br>
- [Daily News ClawHub page](https://clawhub.ai/infra403/6551-daily-news) <br>
- [6551 API base URL](https://ai.6551.io) <br>
- [News categories endpoint](https://ai.6551.io/open/free_categories) <br>
- [Hot news endpoint](https://ai.6551.io/open/free_hot?category=macro) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-invoked curl requests and interpretable public news or trending-topic API responses; no authentication is documented.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
