## Description:

ClickHouse (clickhouse.com). Use this skill for ANY ClickHouse request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect ClickHouse databases, inspect table schemas, and run SQL through an OOMOL-connected ClickHouse account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts for the oo CLI.

Mitigation: Review the OOMOL installation path before use, prefer an installer from OOMOL, verify source or checksum/signature when available, and require explicit approval before installation.

Risk: The execute_query action can change or delete ClickHouse data.

Mitigation: Treat non-read SQL as potentially destructive and require clear user confirmation of the exact query, target, and expected effect before execution.

## Reference(s):

- [ClickHouse homepage](https://clickhouse.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickhouse)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing ClickHouse action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
