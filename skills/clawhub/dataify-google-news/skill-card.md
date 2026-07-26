## Description: <br>
When the user requests "call Google News" or "news search/information", or explicitly mentions the news search field, the dataify-google-news skill is triggered. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to convert Google News search requests into confirmed Dataify Scraper API calls and return the API response body. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google News queries and selected parameters are sent to Dataify during live API calls. <br>
Mitigation: Install only if this data sharing is acceptable for the intended use case, and review the confirmation table before approving each call. <br>
Risk: The Dataify API token could be exposed if handled carelessly. <br>
Mitigation: Store DATAIFY_API_TOKEN securely and avoid passing tokens on the command line when possible. <br>


## Reference(s): <br>
- [Dataify Google News API Reference](references/google_news_api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-news) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API Calls, JSON, Text] <br>
**Output Format:** [Markdown confirmation table, shell command invocation, and raw API response body in the requested output mode.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN for live calls, confirms parameters before outbound requests, and returns the API response body without summarizing.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
