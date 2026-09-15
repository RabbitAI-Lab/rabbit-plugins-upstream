## Description:

Google Drive lets agents read, create, update, delete, and manage Google Drive files, folders, permissions, comments, labels, revisions, shared drives, and change tracking through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill when an agent needs to inspect or operate Google Drive content through the OOMOL-connected oo CLI. It supports read workflows, file and folder creation or updates, permission management, comments, labels, revisions, shared drives, exports, downloads, and deletion workflows with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line shell and PowerShell installers fetched from remote URLs.

Mitigation: Review the installer path before installing and prefer a verified package, pinned release, checksum, or manual inspection before running installer commands.

Risk: The skill can perform write or destructive Google Drive actions, including deleting files, shared drives, comments, permissions, replies, and revisions.

Mitigation: Require explicit approval for destructive actions and confirm exact payloads and expected effects before running state-changing connector commands.

Risk: Google Drive actions are routed through OOMOL-connected infrastructure.

Mitigation: Confirm that the deployment is comfortable routing Google Drive operations through OOMOL before enabling the skill.

## Reference(s):

- [ClawHub Google Drive skill page](https://clawhub.ai/oomol/skills/oo-googledrive)
- [OOMOL oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Drive product page](https://workspace.google.com/products/drive/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action schemas should be inspected before submitting JSON payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
