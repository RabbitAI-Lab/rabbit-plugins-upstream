## Description: <br>
Search and extract Google data through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to turn Google research, discovery, local, visual, vertical, and webpage extraction requests into KeyAPI REST workflows backed by current official KeyAPI documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A KeyAPI token may be exposed if configured in a shared shell, pasted into chat, printed, logged, or committed. <br>
Mitigation: Configure credentials in a private local terminal, avoid the --token argument on shared systems, never print KEYAPI_TOKEN, and rotate the token if exposure is suspected. <br>
Risk: User queries, URLs, files, or image inputs may be sent to KeyAPI during live Google data retrieval. <br>
Mitigation: Do not submit sensitive content unless the user intends to send it to KeyAPI, and confirm scope before broad or multi-endpoint workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xyzzero/skills/keyapi-google) <br>
- [KeyAPI docs index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Google docs](https://docs.keyapi.ai/en/google/) <br>
- [Authentication docs](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global Rules](references/global-rules.md) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, REST request guidance, and optional JSON results from KeyAPI calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call live KeyAPI endpoints and may save complete helper responses only when requested or needed for analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
