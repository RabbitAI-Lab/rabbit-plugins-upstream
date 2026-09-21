## Description:

Operate OneDrive through an OOMOL-connected account to read, create, update, delete, upload, download, and search OneDrive content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workspace agents use this skill to operate OneDrive files and folders via an OOMOL-connected account, including browsing, metadata lookup, file transfers, and guarded write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a remote installer script on the user's machine.

Mitigation: Install the oo CLI through a trusted, manually reviewed method; do not let an agent automatically run the remote installer command.

Risk: Write and destructive OneDrive actions can rename, move, overwrite, or delete files and folders.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub OneDrive Skill](https://clawhub.ai/oomol/skills/oo-one-drive)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OneDrive](https://www.microsoft.com/microsoft-365/onedrive/online-cloud-storage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed, signed-in oo CLI and a connected OneDrive account.]

## Skill Version(s):

1.0.4 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
