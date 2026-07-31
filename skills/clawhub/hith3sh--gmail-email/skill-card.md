## Description: <br>
Read, search, draft, reply to, and organize Gmail from chat via the Gmail API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hith3sh](https://clawhub.ai/user/hith3sh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill as an inbox copilot for Gmail: searching and reading messages, managing labels and threads, creating drafts, sending replies, forwarding mail, retrieving attachments, and troubleshooting account connections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a full Gmail mailbox OAuth grant and can read or change mailbox data. <br>
Mitigation: Install only when that access is acceptable, use the connected Google account intentionally, and revoke the grant from Google account permissions when the skill is no longer needed. <br>
Risk: Write operations can send mail, modify labels, move messages to trash, or permanently delete messages. <br>
Mitigation: Preview write actions and require explicit user confirmation before execution, with extra review for recipients, subjects, message bodies, labels, and destructive operations. <br>
Risk: Bulk operations can affect many messages at once. <br>
Mitigation: Use clear search criteria or message IDs, confirm the intended scope before execution, and avoid permanent deletion unless the user explicitly approves it. <br>


## Reference(s): <br>
- [ClawHub Gmail skill page](https://clawhub.ai/hith3sh/skills/gmail-email) <br>
- [Gmail API Documentation](https://developers.google.com/gmail/api) <br>
- [Gmail API Reference](https://developers.google.com/gmail/api/reference/rest) <br>
- [Gmail Search Operators](https://support.google.com/mail/answer/7190) <br>
- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=gmail-email) <br>
- [ClawLink OpenClaw Docs](https://docs.claw-link.dev/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON tool parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Gmail tool names, search queries, preview steps, confirmation prompts, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
