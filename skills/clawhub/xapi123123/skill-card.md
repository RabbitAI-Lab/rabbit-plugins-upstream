## Description: <br>
Use the xapi CLI to access real-time external data from Twitter/X, crypto, web search, news, AI text processing, and third-party API services through JSON-oriented CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glacier-luo](https://clawhub.ai/user/glacier-luo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to discover xapi actions, inspect their schemas, and run JSON-based CLI calls for real-time social, crypto, web, news, AI text, and third-party API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route agent requests through a broad external API gateway, including services that retrieve, post, or transform data. <br>
Mitigation: Install and use it only when the user trusts xapi.to and the xapi-to package, and confirm the selected action schema before each call. <br>
Risk: OAuth binding, posting, write methods, and payment or top-up flows can affect user accounts or incur cost. <br>
Mitigation: Require explicit human approval before OAuth binding, POST/PUT/PATCH/DELETE calls, balance checks, top-ups, or payment flows. <br>
Risk: The XAPI_API_KEY and generated payment URLs can expose credentials or account access if logged or shared. <br>
Mitigation: Keep the API key and local xapi config private, avoid sending confidential content through the gateway, and do not log or share top-up URLs. <br>


## Reference(s): <br>
- [xAPI homepage](https://xapi.to) <br>
- [ClawHub skill page](https://clawhub.ai/glacier-luo/skills/xapi123123) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI calls return JSON by default; some actions require XAPI_API_KEY, OAuth authorization, or account balance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
