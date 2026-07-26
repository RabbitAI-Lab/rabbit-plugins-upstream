## Description: <br>
Route natural-language TikTok commerce intelligence requests into authenticated EchoTik API workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn business-language TikTok commerce intelligence requests into EchoTik API workflows for creator discovery, product research, seller analysis, video intelligence, live lookup, search, and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow stores reusable EchoTik username and password values as plaintext exports in the user's shell profile. <br>
Mitigation: Use a dedicated low-privilege EchoTik API credential, review the generated shell profile block after setup, and prefer a secret manager or session-only environment variables when possible. <br>
Risk: EchoTik API queries and request parameters are sent to EchoTik during live workflows. <br>
Mitigation: Install and use the skill only when sending the relevant commerce intelligence queries to EchoTik is acceptable for the user's data-handling requirements. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xyzzero/skills/echotik-api-assistant) <br>
- [Publisher Profile](https://clawhub.ai/user/xyzzero) <br>
- [EchoTik Official Docs Index](https://opendocs.echotik.live/llms.txt) <br>
- [EchoTik Authentication](https://opendocs.echotik.live/authentication) <br>
- [Scenario Rules](references/scenarios.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with shell command snippets and JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute local Node.js scripts that call EchoTik APIs when credentials are configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
