## Description: <br>
Searches Bing Shopping product results through Dataify after mapping a user's request to API fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Bing Shopping product searches through Dataify, preview request parameters before the call, and receive the raw API response for downstream use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed searches send the shopping query and Dataify API token to Dataify. <br>
Mitigation: Review the parameter table before confirming, use a scoped or temporary token when available, and avoid sharing tokens in chats or persistent shell profiles unless intended. <br>
Risk: The skill returns the Dataify API response directly, including HTML when that output format is requested. <br>
Mitigation: Prefer JSON-only responses unless HTML is needed, and review returned HTML before rendering or reusing it. <br>


## Reference(s): <br>
- [Dataify Bing Shopping API Reference](references/api.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, text] <br>
**Output Format:** [Markdown parameter table followed by raw Dataify API response text, usually JSON and optionally HTML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN for confirmed live calls and asks for user confirmation before sending the request.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
