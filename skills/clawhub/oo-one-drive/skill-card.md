## Description:

Use OneDrive through the OOMOL one_drive connector and oo CLI to read, create, update, and delete files and folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a user's connected OneDrive account through OOMOL for file and folder reads, listing, search, uploads, content replacement, metadata updates, folder creation, and recycle-bin deletes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes internet installer scripts for the oo CLI.

Mitigation: Review the installation path first and prefer a verified package or pinned release before installing.

Risk: The skill can upload files, replace file content, change item metadata, create folders, and move deleted items to the recycle bin.

Mitigation: Require clear user confirmation of the exact target, payload, and effect before any write, overwrite, delete, or metadata-changing action.

Risk: OneDrive access depends on OOMOL as an intermediary for connected account credentials.

Mitigation: Install and use the skill only when the user is comfortable with OOMOL mediating OneDrive actions for the connected account.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OneDrive](https://www.microsoft.com/microsoft-365/onedrive/online-cloud-storage)
- [ClawHub OneDrive Skill](https://clawhub.ai/oomol/skills/oo-one-drive)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive OneDrive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
