## Description:

monday (monday.com) lets an agent read, create, update, and delete monday.com data through the OOMOL monday connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill when they want an agent to operate monday.com boards, items, workspaces, docs, dashboards, forms, users, teams, departments, updates, assets, audit logs, and activity logs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform powerful write and delete actions against monday.com data.

Mitigation: Review every proposed write or delete payload carefully and require explicit confirmation before changing boards, workspaces, items, docs, departments, or related records.

Risk: Connector action schemas or required scopes may differ from assumptions in a prompt.

Mitigation: Inspect the live action schema before building a payload and resolve connection or scope errors before retrying.

Risk: The skill operates through the oo CLI and OOMOL connection path.

Mitigation: Install only when the user intends to operate a monday.com account through OOMOL and trusts that connection path.

## Reference(s):

- [monday homepage](https://monday.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
