## Description:

Email Assistant helps agents search, retrieve, summarize, prioritize, draft, and explicitly send email for user-authorized IMAP/SMTP accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bjwswang](https://clawhub.ai/user/bjwswang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage user-authorized mailbox workflows: find and summarize messages, triage next actions, draft replies, and send reviewed SMTP drafts only after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private mailbox data.

Mitigation: Install it only for an intended mailbox, prefer an app password or dedicated mailbox, and keep secrets out of chat and diagnostic output.

Risk: Outbound email is a real external side effect.

Mitigation: Keep EMAIL_SMTP_SEND_ENABLED=false until operationally ready, review the exact draft contents, and send only after explicit user confirmation.

Risk: Email bodies, subjects, links, and attachment names may contain untrusted instructions.

Mitigation: Treat mailbox content as data, cite factual summaries from returned source references, and do not execute links or attachments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bjwswang/skills/email-assistant)
- [IMAP and SMTP configuration](references/configuration.md)
- [Output contract](references/output-contract.md)
- [Email writing guide](references/writing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON files]

**Output Format:** [Markdown responses with inline shell commands and structured JSON artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox query, message, draft, and sent artifacts are UTF-8 JSON files; SMTP sends require explicit review confirmation and EMAIL_SMTP_SEND_ENABLED=true.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
