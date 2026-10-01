## Description:

Helps agents read, search, organize, and send Fastmail email and manage mailboxes, contacts, and masked addresses through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Fastmail users and their agents can search and read messages, organize mail, draft and send email, manage contacts and aliases, and set up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mail, contacts, and aliases contain sensitive personal information accessible through the connected account.

Mitigation: Authorize only the intended account, use the narrowest available scopes, and disclose only information needed for the task.

Risk: Sending, deleting, or moving mail can have irreversible or unintended effects.

Mitigation: Start with read-only actions and obtain explicit user approval before sending, deleting, moving, or creating automations.

Risk: Raw API keys or persistent trigger destinations can expose account access or forward future events.

Mitigation: Prefer managed sign-in over raw keys, and review and approve each trigger destination and its event fields.

## Reference(s):

- [Fastmail skill release](https://clawhub.ai/byungkyu/skills/fastmail)
- [Maton homepage](https://maton.ai)
- [Fastmail developer documentation](https://www.fastmail.com/dev/)
- [JMAP core and mail specifications](https://jmap.io/)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples, plus requested Fastmail results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected Fastmail account and network access; actions are limited by granted permissions.]

## Skill Version(s):

1.2.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
