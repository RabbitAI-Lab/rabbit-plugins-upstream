## Description:

ProjectManager helps an agent search and read ProjectManager projects and tasks through OOMOL's ProjectManager connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve ProjectManager project records and query tasks without handling raw ProjectManager API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes mutable remote installer scripts run directly in a shell.

Mitigation: Prefer the official installation guide, inspect installer contents, and verify the source before running Bash or PowerShell install commands.

Risk: Connector commands depend on live ProjectManager action schemas and server-side credentials.

Mitigation: Inspect the action schema before each action and run first-time setup or connection recovery only after an auth or connection failure.

## Reference(s):

- [ProjectManager homepage](https://www.projectmanager.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ProjectManager skill page](https://clawhub.ai/oomol/skills/oo-projectmanager)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions require live schema inspection before building command payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
