## Description:

Mailtrap (mailtrap.io). Use this skill for ANY Mailtrap request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Mailtrap inboxes, messages, contacts, lists, templates, domains, suppressions, billing usage, permissions, and sending analytics through OOMOL-connected Mailtrap actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that execute directly in a shell.

Mitigation: Review the oo CLI installer source or use official installation steps with checksum or signature verification before installation.

Risk: Several Mailtrap actions create, update, delete, reset, import, export, or clean account data.

Mitigation: Confirm exact targets, payloads, and intended effects before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailtrap)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Mailtrap Homepage](https://mailtrap.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and typically return JSON responses from Mailtrap connector actions.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
