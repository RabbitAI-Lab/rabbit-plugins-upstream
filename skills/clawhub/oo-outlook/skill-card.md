## Description:

Outlook (microsoft.com). Use this skill for ANY Outlook request: reading, creating, and updating data through the OOMOL-connected Outlook connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate a connected Outlook mailbox from an agent, including reading messages and folders, creating or updating drafts, sending mail, replying to mail, and managing mailbox settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands for remote scripts.

Mitigation: Review and independently verify installer source and permissions before running the documented installer commands.

Risk: Write actions can send emails, change drafts, reply to messages, or update mailbox settings.

Mitigation: Confirm the exact payload and intended effect with the user before allowing email-sending, draft-changing, reply, or mailbox-settings updates.

Risk: The skill requires trust in OOMOL with Outlook mailbox access.

Mitigation: Install and use the skill only when the publisher and Outlook connection are trusted for the mailbox involved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-outlook)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Outlook](https://www.microsoft.com/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON data and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
