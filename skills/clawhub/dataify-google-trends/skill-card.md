## Description: <br>
Turns a user's Google Trends request into a confirmed Dataify Scraper API form submission and returns the raw API response. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert Google Trends requests into confirmed Dataify Scraper API calls for trend data retrieval. The skill is useful when an agent needs to map natural-language trend analysis requests to Dataify parameters and return the service response directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Trends query parameters and the Dataify API token are sent to Dataify when a call is confirmed. <br>
Mitigation: Review the confirmation table before approving each call and prefer DATAIFY_API_TOKEN from the environment instead of pasting tokens into chat. <br>
Risk: Incorrect inferred parameters could produce an unintended Dataify request. <br>
Mitigation: The skill requires a complete Markdown parameter table and explicit user confirmation before each API call, and regenerates the table when parameters change. <br>


## Reference(s): <br>
- [Dataify Google Trends API Reference](references/google_trends_api.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-trends) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Text] <br>
**Output Format:** [Markdown confirmation table plus raw Dataify API response body] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The response body is returned directly without summarizing, extracting, cleaning, translating, or reshaping.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
