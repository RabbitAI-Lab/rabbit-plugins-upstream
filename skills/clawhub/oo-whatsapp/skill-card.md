## Description:

WhatsApp (whatsapp.com). Use this skill for WhatsApp requests that read, create, update, or delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate WhatsApp Business through the oo CLI, including profile and media reads, template management, and sending messages. It is intended for accounts already connected through OOMOL, with confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run an internet installer directly in a shell without verification.

Mitigation: Review the install command first and prefer a verified, versioned, signed, or package-manager installation source for the oo CLI.

Risk: WhatsApp write actions can send messages, upload media, or create templates, and the destructive action can delete message templates.

Mitigation: Confirm the exact action, payload, target account, and recipient or template name before running write or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-whatsapp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WhatsApp](https://www.whatsapp.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
