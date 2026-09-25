## Description:

OneDrive (microsoft.com). Use this skill for OneDrive requests to read, create, update, and delete data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent browse OneDrive metadata, list and search items, inspect permissions, and transfer files. With explicit confirmation, the skill can also create folders, upload files, replace file content, delete items, and update OneDrive item metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify, overwrite, or delete connected OneDrive data.

Mitigation: Require explicit user confirmation for write and destructive actions, including the exact target and payload, before running the connector command.

Risk: First-time setup includes remote installer script commands for the oo CLI.

Mitigation: Install the oo CLI from a verified, pinned package or inspect the installer before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-one-drive)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OneDrive homepage](https://www.microsoft.com/microsoft-365/onedrive/online-cloud-storage)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return OneDrive metadata, permission details, file transfer results, and connector execution IDs.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
