## Description: <br>
Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl by using email/password session login to obtain JWT and session cookies for direct v3 API and legacy dispatcher calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical operators use this skill to inspect SignUpGenius account data, groups, sign-up listings, public slot availability, and RSVP flows from scripts or shell sessions without running the MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles SignUpGenius credentials, JWTs, cookies, and raw curl commands that could leak through logs, shell history, or temporary files. <br>
Mitigation: Use a secret manager or protected environment variables, keep cookie and header files permission-restricted, avoid printing tokens, and delete temporary credential, header, and output files after use. <br>
Risk: The skill can guide agents to read account data and public sign-up slot data, and includes write-capable RSVP and group-member examples. <br>
Mitigation: Use it only for accounts and sign-ups the user owns or is authorized to inspect, avoid bulk collection of public slot data, and require explicit user confirmation before write operations. <br>
Risk: Session-mode authentication is not suitable for SSO or 2FA accounts and can fail when JWT or ColdFusion sessions expire. <br>
Mitigation: Check for documented login-failure, 401, HTML login-page, and legacy-session expiry signals; reauthenticate only for expiry and treat 403 responses as permission failures. <br>


## Reference(s): <br>
- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces direct API request patterns and operational cautions; does not run requests by itself.] <br>

## Skill Version(s): <br>
1.3.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
