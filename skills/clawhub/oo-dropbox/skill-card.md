## Description:

Dropbox (dropbox.com). Use this skill for any Dropbox request, including reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Dropbox through the OOMOL-connected oo CLI for file, folder, sharing, revision, metadata, and search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute downloaded shell or PowerShell content during setup.

Mitigation: Use a trusted installer channel and prefer pinned, signed, or checksum-verified installers before running setup commands.

Risk: Write and destructive Dropbox actions can change, revoke, restore, or delete user data and sharing links.

Mitigation: Review payloads carefully and require explicit approval before write, sharing, restore, revoke, or delete operations.

## Reference(s):

- [ClawHub Dropbox skill page](https://clawhub.ai/oomol/skills/oo-dropbox)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Dropbox homepage](https://www.dropbox.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live oo connector schemas before running Dropbox actions and may return JSON responses with execution IDs.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
