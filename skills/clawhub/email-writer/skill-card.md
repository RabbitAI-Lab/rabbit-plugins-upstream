## Description: <br>
Draft and send emails via browser automation. Supports Gmail, Outlook, QQ Mail, 163 Mail. Requires OpenClaw v2026.3.22+ with browser access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People who use supported webmail services use this skill to draft, review, and send individual emails or replies through a logged-in browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send email through a logged-in webmail session, including content and attachments to the selected provider. <br>
Mitigation: Confirm recipient, subject, body, attachments, and send intent before browser action. <br>
Risk: Sensitive email content can leave the user's environment once sent through Gmail, Outlook, QQ Mail, 163 Mail, or 126 Mail. <br>
Mitigation: Avoid sensitive content unless the user trusts the selected mail provider and account context, and review content before sending. <br>
Risk: The artifact describes local processing while also sending messages through provider servers, which can confuse privacy expectations. <br>
Mitigation: Distinguish local drafting from provider transmission and tell users that sending email is a network operation. <br>
Risk: Provider UI changes, login state, or verification prompts can cause browser automation to fail. <br>
Mitigation: Ask the user to log in before use, avoid handling verification codes, and prompt for manual sending if automation fails. <br>


## Reference(s): <br>
- [ClawHub Skill: Email Writer](https://clawhub.ai/tobewin/skills/email-writer) <br>
- [Publisher Profile: tobewin](https://clawhub.ai/user/tobewin) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, guidance] <br>
**Output Format:** [Markdown guidance with browser automation code snippets and drafted email text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a logged-in webmail browser session; recipient, subject, content, tone, and login status should be confirmed before browser action.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
