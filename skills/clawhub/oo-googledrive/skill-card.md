## Description:

Google Drive (workspace.google.com) skill for reading, creating, updating, and deleting Google Drive data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agent operators use this skill to inspect and manage Google Drive files, folders, shared drives, permissions, comments, replies, labels, revisions, and change tracking through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute code from an installer endpoint.

Mitigation: Use a trusted, pinned, signed, or checksum-verified installer before running setup commands.

Risk: Google Drive write and destructive actions can change or remove Drive data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-googledrive)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Google Drive Homepage](https://workspace.google.com/products/drive/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
