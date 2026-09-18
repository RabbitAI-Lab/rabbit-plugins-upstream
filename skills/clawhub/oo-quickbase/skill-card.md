## Description:

Quickbase (quickbase.com). Use this skill for ANY Quickbase request: reading, creating, updating, and deleting data through the OOMOL-connected Quickbase connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Quickbase app and table metadata, query records, and perform guarded record writes or deletes through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upsert or delete Quickbase records when write or destructive actions are requested.

Mitigation: Confirm the exact payload, target table, record ids, and expected effect with the user before running write or destructive commands.

Risk: First-time setup may require running shell or PowerShell installer commands for the oo CLI.

Mitigation: Review the OOMOL installer or official install guide before running installer commands.

Risk: Quickbase access is mediated by OOMOL-connected credentials.

Mitigation: Install and use the skill only when the user accepts OOMOL as the intermediary for Quickbase operations.

## Reference(s):

- [ClawHub Quickbase Skill](https://clawhub.ai/oomol/skills/oo-quickbase)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Quickbase Homepage](https://www.quickbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
