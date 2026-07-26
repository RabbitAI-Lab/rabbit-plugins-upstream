## Description: <br>
Read, search, draft, reply to, and organize Gmail from chat via the Gmail API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thejanethmina](https://clawhub.ai/user/thejanethmina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill as a Gmail inbox copilot to search messages, read threads, manage labels, draft and send email, and handle attachments through ClawLink-mediated Gmail access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires sensitive Gmail mailbox access through OAuth. <br>
Mitigation: Install only after reviewing Google consent scopes and use it from a trusted OpenClaw environment. <br>
Risk: Send, reply, label, archive, trash, and delete actions can change mailbox state. <br>
Mitigation: Preview each write action and confirm recipients, subject, body, labels, and target messages before execution. <br>
Risk: Trash, permanent delete, and bulk modification actions can affect many messages or remove data. <br>
Mitigation: Use explicit confirmation for destructive actions and verify message or thread targets before allowing the call. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thejanethmina/skills/gmail-email) <br>
- [Gmail API Documentation](https://developers.google.com/gmail/api) <br>
- [Gmail API Reference](https://developers.google.com/gmail/api/reference/rest) <br>
- [Gmail Search Query Syntax](https://support.google.com/mail/answer/7190) <br>
- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=gmail-email) <br>
- [ClawLink Docs](https://docs.claw-link.dev/openclaw) <br>
- [ClawLink Verification](https://claw-link.dev/verify) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ClawLink Gmail OAuth connection; write actions require preview and explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
