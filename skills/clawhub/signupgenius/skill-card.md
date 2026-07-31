## Description: <br>
Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect their own SignUpGenius profile, groups, sign-ups, public sign-up pages, and slot reports, and to perform limited write actions such as adding group members or submitting RSVPs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP may access a SignUpGenius account through cookies, credentials, or an API key. <br>
Mitigation: Install only for accounts you control, protect credentials and API keys, and review the external npm package and fetchproxy extension before use. <br>
Risk: The skill includes write actions that can add group members or submit RSVPs. <br>
Mitigation: Review prompts and tool arguments before allowing group membership changes or RSVP submissions. <br>
Risk: Automated SignUpGenius access may be inappropriate for accounts or usage patterns outside the user's own personal-scale use. <br>
Mitigation: Use the skill only within the user's own account context and review SignUpGenius terms and account expectations before broader or repeated use. <br>


## Reference(s): <br>
- [SignUpGenius](https://www.signupgenius.com) <br>
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets and tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require SignUpGenius cookies, direct-login credentials, or a Pro API key depending on the selected authentication mode and requested tool.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
