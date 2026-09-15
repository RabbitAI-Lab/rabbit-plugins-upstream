## Description:

This skill helps agents handle monday.com requests, including reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to read and manage monday.com boards, items, workspaces, dashboards, docs, forms, users, teams, and related account data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute remote installer scripts directly.

Mitigation: Review the installer path before use and prefer a verified package or downloaded file with checksum or signature validation.

Risk: The skill can perform high-impact monday.com write and delete actions.

Mitigation: Approve write or destructive actions only after checking the exact target, payload, and expected effect.

## Reference(s):

- [monday homepage](https://monday.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-monday)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide calls that return JSON data from monday connector actions.]

## Skill Version(s):

1.0.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
