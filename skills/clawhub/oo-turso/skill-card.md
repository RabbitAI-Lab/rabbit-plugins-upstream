## Description:

Turso (turso.tech). Use this skill for ANY Turso request -- reading, creating, updating, and deleting data. Whenever a task involves Turso, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Turso databases, groups, organizations, and locations through an OOMOL-connected account. It supports read operations plus confirmed create and delete actions for Turso resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup points to online shell and PowerShell installer commands for the oo CLI.

Mitigation: Review the installer path before installation, prefer a pinned and verifiable oo CLI install method when available, and do not let an agent run installer scripts automatically.

Risk: The skill can create groups and databases and can delete databases.

Mitigation: Require explicit user confirmation for write and destructive actions, including the exact organization, group, database, and payload before execution.

Risk: Connector calls may expose sensitive database or organization information in prompts or logs.

Mitigation: Send only the minimum Turso identifiers and payload fields needed for the requested action.

## Reference(s):

- [ClawHub Turso skill page](https://clawhub.ai/oomol/skills/oo-turso)
- [Turso homepage](https://turso.tech)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action payloads are constructed.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
