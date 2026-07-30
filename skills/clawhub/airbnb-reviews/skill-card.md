## Description: <br>
Airbnb reviews helps agents read normalized Airbnb guest reviews for a listing while preserving native rating scales, powered by StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, travel operators, and developers use this skill to retrieve Airbnb guest feedback and native-scale ratings for a known listing through StayingAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a StayingAPI API key for requests. <br>
Mitigation: Use a sandbox key for evaluation and protect STAYINGAPI_KEY like any other API credential. <br>
Risk: Listing URLs or IDs queried through the skill are sent to StayingAPI. <br>
Mitigation: Install and use the skill only when third-party lodging review lookups through StayingAPI are acceptable. <br>
Risk: Live review lookups may require asynchronous polling and can hit rate limits if polled too aggressively. <br>
Mitigation: Honor Retry-After headers, back off between polling attempts, and cap the number of attempts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/airbnb-reviews) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Authentication setup guide](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request details and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY and internet access to api.stayingapi.com; may use the hosted MCP server with OAuth 2.1 + PKCE.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
