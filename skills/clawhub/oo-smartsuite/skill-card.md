## Description:

This skill helps agents manage SmartSuite data through OOMOL's oo CLI connector, including reading, creating, updating, and deleting records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers with a connected OOMOL account use this skill to operate SmartSuite workspaces through guided CLI actions for listing solutions and tables, retrieving records, and making confirmed record changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update SmartSuite records in a connected workspace.

Mitigation: Confirm the exact table, record fields, and payload with the user before running write actions.

Risk: The skill can delete SmartSuite records.

Mitigation: Require explicit approval for the target record before running destructive actions.

Risk: Setup commands may install or authenticate the oo CLI.

Mitigation: Use the disclosed OOMOL setup path only when commands fail due to missing CLI, authentication, connection, or billing issues.

## Reference(s):

- [SmartSuite homepage](https://www.smartsuite.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed, signed-in oo CLI and a connected SmartSuite account; write and delete actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
