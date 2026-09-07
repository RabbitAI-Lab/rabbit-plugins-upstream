## Description:

Deploys a self-rollback workflow that helps an AI agent snapshot, verify, list, and restore its own memory files and selected project files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to add local snapshot and rollback practices around persistent agent memory, agent rules, and selected project files. It is intended for assistants that can read and write local files and need a practical recovery path after accidental edits or corruption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The rollback workflow creates long-lived local copies of agent memory and selected project files, which may contain sensitive information.

Mitigation: Store snapshots outside shared repositories or synced folders, restrict filesystem permissions, and avoid snapshotting secrets or unrelated personal files.

Risk: Broad local copying and weak snapshot containment can make the snapshot directory a secondary exposure point.

Mitigation: Configure the snapshot directory deliberately, review its retention and access controls, and keep it separate from public project artifacts.

Risk: Extra-path snapshots are backup-only unless restore and verify behavior is extended for those paths.

Mitigation: Treat extra-path snapshots as manual recovery material and validate restore coverage before relying on them operationally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mowenqwq/skills/agent-self-rollback)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with PowerShell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a portable PowerShell rollback script for snapshot, list, restore, and verify actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
