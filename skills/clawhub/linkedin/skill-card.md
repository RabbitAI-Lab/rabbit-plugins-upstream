## Description: <br>
LinkedIn automation via browser relay or cookies for messaging, profile viewing, and network actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[biostartechnology](https://clawhub.ai/user/biostartechnology) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to operate LinkedIn in a browser session for messaging, profile viewing, search, notifications, and network actions with explicit user confirmation for account-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a LinkedIn li_at cookie that acts like a login token if exposed. <br>
Mitigation: Prefer browser relay or manual browser login, keep any cookie in a proper secret store, avoid sharing it in chats or logs, and revoke sessions if exposure is suspected. <br>
Risk: The skill can send messages, connection requests, accept requests, or otherwise change the LinkedIn account state. <br>
Mitigation: Require explicit user confirmation before every message, connection request, acceptance, or other account-changing action. <br>
Risk: Rapid automated LinkedIn actions may trigger rate limits or account challenges. <br>
Mitigation: Rate-limit activity, pause after limits or CAPTCHA challenges, and resume only after manual user intervention. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/biostartechnology/skills/linkedin) <br>
- [LinkedIn](https://linkedin.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline browser commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an authenticated browser session or securely stored LinkedIn session cookie.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
