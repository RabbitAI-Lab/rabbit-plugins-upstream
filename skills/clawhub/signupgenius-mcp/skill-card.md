## Description: <br>
Read SignUpGenius sign-up sheets, slot reports, profiles, and groups, and add group members or RSVP to public slots through a connected SignUpGenius account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can connect a SignUpGenius account to inspect their profile, groups, created or invited sign-ups, and Pro slot reports. The skill also supports limited account-changing actions for adding group members and RSVPing to public sign-up slots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change SignUpGenius account data by adding group members or RSVPing to public slots. <br>
Mitigation: Require explicit user confirmation before any RSVP or group-member change and review proposed writes before execution. <br>
Risk: The skill connects to personal SignUpGenius credentials, cookies, or API keys. <br>
Mitigation: Use only accounts the user is comfortable connecting, keep credentials scoped, and verify the referenced npm package and fetchproxy extension before installation. <br>
Risk: Broad trigger phrases may route general sign-up requests to this integration unexpectedly. <br>
Mitigation: Ask the agent to confirm intent before invoking SignUpGenius tools, especially before actions that modify account data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/signupgenius-mcp) <br>
- [npm package](https://www.npmjs.com/package/signupgenius-mcp) <br>
- [SignUpGenius](https://www.signupgenius.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON configuration examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include account data returned by SignUpGenius MCP tools and proposed write actions that should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.1.6 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
