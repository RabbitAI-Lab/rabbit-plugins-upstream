## Description: <br>
Read SignUpGenius sign-up sheets, slot reports, groups, and public slot availability, and add group members or RSVP when explicitly requested. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill through an agent to inspect their SignUpGenius profile, groups, created and invited sign-ups, public slot availability, and owner-scoped reports. The skill also supports limited write actions for RSVPs and adding members to groups when the user explicitly requests them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser-cookie authentication can expose an active SignUpGenius session to the MCP. <br>
Mitigation: Use the Pro API key or email/password mode when appropriate, or set SIGNUPGENIUS_DISABLE_FETCHPROXY=1 to avoid browser-cookie lifting. <br>
Risk: The skill includes write actions for RSVPs and adding group members. <br>
Mitigation: Confirm any RSVP or group-member add request before allowing the tool call. <br>
Risk: Automated SignUpGenius access may be inappropriate for accounts the user does not own or for scaled use. <br>
Mitigation: Limit use to personal-account, personal-scale workflows and review SignUpGenius terms before broader deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius) <br>
- [SignUpGenius](https://www.signupgenius.com) <br>
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require a SignUpGenius session, a Pro API key for owner-scoped reports, or browser-cookie access through fetchproxy; write actions should be confirmed by the user.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
