## Description:

Databricks helps agents read, create, update, and delete Databricks workspace resources through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Databricks action schemas, run read-only workspace queries, and perform confirmed write or destructive Databricks actions through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad Databricks write and delete actions in the connected workspace.

Mitigation: Require explicit confirmation for every write or destructive Databricks action, including the exact target and payload.

Risk: The skill documentation includes remote installer commands that pipe downloaded scripts into a shell or PowerShell.

Mitigation: Prefer a verified package, pinned release, or separately downloaded installer that can be inspected before execution.

## Reference(s):

- [ClawHub Databricks Skill](https://clawhub.ai/oomol/skills/oo-databricks)
- [Databricks Homepage](https://www.databricks.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions that change or delete Databricks resources require explicit user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
