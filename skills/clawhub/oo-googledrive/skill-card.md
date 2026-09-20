## Description:

Provides agent guidance for reading, creating, updating, sharing, exporting, and deleting Google Drive content through an OOMOL-connected Google Drive account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Google Drive files, shared drives, permissions, labels, revisions, comments, replies, changes, approvals, and access proposals through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote oo CLI installation scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing and prefer a verified package or documented manual installation method.

Risk: The skill can guide write or destructive Google Drive actions that modify, delete, overwrite, or expose Drive content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action.

## Reference(s):

- [ClawHub Google Drive Skill](https://clawhub.ai/oomol/skills/oo-googledrive)
- [Google Drive](https://workspace.google.com/products/drive/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces connector schema inspection and action-running guidance for the oo CLI.]

## Skill Version(s):

1.0.7 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
