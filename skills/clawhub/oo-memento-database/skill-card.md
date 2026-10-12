## Description:

Helps an agent inspect, search, create, update, and delete entries in a connected Memento Database account through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with a connected Memento Database account use this skill to browse libraries and entries, search records, and make approved changes to entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating, updating, or deleting entries may change or remove account data.

Mitigation: Review the exact payload and effect before writes; confirm the target and obtain explicit approval before deletion.

Risk: The optional CLI setup uses a downloaded installer executed by a shell.

Mitigation: Verify the installer against official OOMOL documentation before running it.

Risk: Connecting the skill grants agent access to the connected Memento Database account.

Mitigation: Install only when that account access is intended and review changes before approval.

## Reference(s):

- [Memento Database skill on ClawHub](https://clawhub.ai/oomol/skills/oo-memento-database)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Memento Database](https://mementodatabase.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown, with optional JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write and delete operations require user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
