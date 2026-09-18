## Description:

Enables an agent to read, create, update, and delete monday.com data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate monday.com work management resources from an agent after their OOMOL account and monday connection are configured. It supports board, item, workspace, dashboard, document, form, user, team, department, asset, audit log, and activity log workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer scripts that may be run directly in a shell.

Mitigation: Review the installer path before installation and prefer manual or otherwise verified oo CLI installation.

Risk: Write and destructive monday actions can change, remove, or overwrite workspace data.

Mitigation: Confirm the exact payload, action, and board, item, workspace, or user targets before executing any tagged write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-monday)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [monday.com](https://monday.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally return JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
