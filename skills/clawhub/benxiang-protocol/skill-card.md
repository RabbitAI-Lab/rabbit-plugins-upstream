## Description:

Benxiang Protocol helps agents maintain persistent project state in .origin packages through object records, semantic transactions, deterministic gates, and provenance-backed explanations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to represent durable project state as objects, constraints, facts, decisions, tasks, and risks that agents can query, update, and audit across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security review flags an unrelated third-party executable installer promoted in the skill documentation.

Mitigation: Install the skill only for local .origin state package workflows, and do not download or run the unrelated installer unless its publisher, provenance, and need are independently verified.

Risk: The skill is designed around durable local state changes.

Mitigation: Review proposed transactions before committing them and keep backups or versioned copies of important .origin packages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/benxiang-protocol)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents toward local .origin state package operations and MCP server usage.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
