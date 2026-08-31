## Description:

monday (monday.com). Use this skill for ANY monday request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to let an agent work with monday.com boards, items, workspaces, dashboards, docs, forms, teams, users, updates, and departments through an OOMOL-connected account. It supports read workflows and state-changing workflows, with explicit confirmation expected before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a user's monday.com account and includes actions that write, archive, delete, deactivate, or change memberships and account structures.

Mitigation: Review proposed payloads carefully and approve only actions whose target and effect are clear, especially for delete, archive, deactivate, membership, workspace, board, item, and department changes.

Risk: Incorrect payloads or misunderstood targets could modify the wrong monday.com data.

Mitigation: Fetch the live connector schema before constructing a payload and confirm the exact payload and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-monday)
- [monday homepage](https://monday.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector execution results as JSON with data and metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
