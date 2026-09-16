## Description:

Motion (usemotion.com). Use this skill for ANY Motion request: reading, creating, updating, and deleting data through an OOMOL-connected Motion account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to manage Motion workspaces, users, projects, tasks, schedules, and statuses through the OOMOL oo CLI. It supports read operations and confirmed write or destructive task and project actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review installation instructions first, prefer a trusted versioned oo CLI source with checksum or signature verification, and run remote installer commands only after accepting the remote-code execution risk.

Risk: Motion write and destructive actions can create, update, or delete workspace data.

Mitigation: Inspect the live connector schema, confirm the exact payload and intended effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-motion)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Motion Homepage](https://www.usemotion.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal outputs include Motion connector command guidance and JSON-shaped action payloads or results.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
