## Description: <br>
Zoom API integration for meetings, calendar, chat, and user management. Use when the user asks to schedule meetings, check Zoom calendar, list recordings, send Zoom chat messages, manage contacts, or interact with any Zoom Workplace feature. Supports Server-to-Server OAuth and OAuth apps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tanchunsiong](https://clawhub.ai/user/tanchunsiong) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to automate Zoom Workplace tasks such as scheduling meetings, listing recordings, retrieving summaries, sending chat messages, and managing user or phone data through a configured Zoom OAuth app. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use high-privilege Zoom OAuth scopes to read or modify meetings, recordings, chat, users, summaries, and phone data. <br>
Mitigation: Use a dedicated Zoom OAuth app with only the minimum scopes needed and protect the .env credentials. <br>
Risk: The skill can delete meetings or recordings, send messages, start or stop RTMS, and download sensitive meeting content. <br>
Mitigation: Require explicit confirmation before destructive, messaging, RTMS, or export actions. <br>
Risk: The token cache is documented as /tmp/zoom_token.json, which may not provide strong per-user secrecy on shared systems. <br>
Mitigation: Use a private user-owned token cache with restrictive permissions or clear cached tokens after use. <br>


## Reference(s): <br>
- [Zoom Authentication Setup](references/AUTH.md) <br>
- [Zoom Marketplace](https://marketplace.zoom.us/) <br>
- [ClawHub Skill Page](https://clawhub.ai/tanchunsiong/skills/zoom-unofficial-community-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text output, downloaded meeting files, Markdown summaries, and setup guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Zoom OAuth credentials and feature-specific Zoom scopes.] <br>

## Skill Version(s): <br>
0.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
