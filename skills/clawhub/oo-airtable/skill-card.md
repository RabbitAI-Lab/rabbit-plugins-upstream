## Description:

Airtable (airtable.com). Use this skill for ANY Airtable request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and operations teams use this skill to let an agent inspect Airtable schemas and records, then create, update, or delete Airtable bases, tables, fields, and records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Airtable data through the connected account.

Mitigation: Review write and delete payloads carefully before approving them, and require explicit confirmation for destructive actions.

Risk: The first-time oo CLI setup may run a remote installer if the CLI is not already installed.

Mitigation: Install only when you trust OOMOL and need the Airtable connector; review the installer source or use an approved installation path when required.

Risk: Commands operate with the permissions granted to the connected Airtable credential.

Mitigation: Use an account or connection scoped to the Airtable bases and actions needed for the task.

## Reference(s):

- [Airtable homepage](https://airtable.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-airtable)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include Airtable read results, schema summaries, proposed write payloads, and confirmation requests for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
