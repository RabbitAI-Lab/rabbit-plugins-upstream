## Description:

MailBluster helps agents operate a connected MailBluster account through the OOMOL oo CLI for reading, creating, updating, and deleting lead data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage MailBluster leads, custom fields, tags, metadata, subscription state, and double opt-in settings from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts directly in a shell without verification.

Mitigation: Review the installer through a safer channel, prefer a pinned package or verified checksum/signature, and avoid executing installer commands automatically.

Risk: The skill can create, update, or delete MailBluster lead data.

Mitigation: For write or destructive actions, inspect the live action schema and confirm the exact payload, effect, and target with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailbluster)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MailBluster Homepage](https://mailbluster.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI schema-inspection and connector-run commands; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
