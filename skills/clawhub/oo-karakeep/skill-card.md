## Description:

This skill lets an agent manage Karakeep data through the OOMOL oo CLI, including bookmarks, assets, backups, feeds, tags, lists, highlights, and admin workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users with a connected OOMOL and Karakeep account use this skill to inspect action schemas and run Karakeep connector actions for reading, creating, updating, deleting, backing up, and administering Karakeep data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to run remote oo CLI installer scripts directly in a shell.

Mitigation: Download and verify the installer before running it, and install the skill only when the user trusts OOMOL.

Risk: The connector can perform broad write, destructive, backup, signed-URL, and admin actions against a connected Karakeep account.

Mitigation: Use a least-privileged Karakeep API key where possible and require explicit review before approving state-changing, destructive, backup-download, signed-URL, or admin actions.

Risk: Some actions can expose or transfer Karakeep assets and backups through temporary file or signed URLs.

Mitigation: Treat returned URLs as sensitive, share them only with intended recipients, and avoid requesting asset or backup downloads unless needed for the task.

## Reference(s):

- [Karakeep homepage](https://karakeep.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-karakeep)
- [Karakeep icon](https://static.oomol.com/logo/third-party/karakeep.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return temporary connector file URLs for downloaded assets or backups.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
