## Description:

Operates monday.com through OOMOL's oo CLI connector for reading, creating, updating, and deleting monday data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users with an OOMOL-connected monday account use this skill to inspect action schemas and run monday connector actions for boards, items, workspaces, docs, forms, dashboards, users, teams, and departments. It supports read workflows and user-confirmed write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installing and prefer a verified or package-manager installation of the oo CLI.

Risk: A connected monday account can be used for write or destructive actions.

Mitigation: Allow write or destructive monday actions only after checking the exact board, item, workspace, and payload the agent will send.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-monday)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [monday.com](https://monday.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector responses containing data and meta.executionId.]

## Skill Version(s):

1.0.7 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
