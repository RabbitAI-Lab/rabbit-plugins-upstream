## Description:

This skill guides an agent through 163.com mailbox management, including IMAP/SMTP setup, sending mail, reading and searching messages, folder operations, attachment handling, and read/delete/move actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation operators use this skill to manage a 163.com mailbox through agent-generated email, search, folder, attachment, and message-operation commands. It is intended for mailboxes the user controls, especially workflows that need Chinese-language interaction and IMAP ID guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad mailbox actions, including sending, reading, moving, attachment download, and bulk delete operations.

Mitigation: Use only with a 163.com mailbox the user controls and require explicit confirmation before any send, move, attachment download, or bulk delete operation.

Risk: Mailbox authorization codes and configuration files can expose account access if mishandled.

Mitigation: Store the 163.com client authorization code carefully, restrict configuration-file permissions, and avoid placing credentials in version control or unrelated API-key settings.

Risk: The security verdict is suspicious because destructive and generic messaging actions are weakly scoped.

Mitigation: Review before installing, constrain use to the documented 163.com email-management workflow, and avoid using the skill for unrelated messaging or spam-like bulk sending.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/email-163-com)
- [Publisher Profile](https://clawhub.ai/user/thcjp)
- [SkillHub Skill Page](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing operational guidance; message send, move, attachment download, and bulk delete steps should require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
