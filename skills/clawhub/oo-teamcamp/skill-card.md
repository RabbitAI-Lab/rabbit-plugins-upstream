## Description:

Teamcamp (teamcamp.app) helps agents read, create, and update Teamcamp data through the OOMOL-connected oo CLI instead of calling the Teamcamp API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operational users use this skill to inspect Teamcamp action schemas, retrieve projects, tasks, workspace users, and customers, and post task comments after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the installation path manually, use a version-pinned and verifiable oo CLI source, and do not let an agent run remote installer commands automatically.

Risk: The skill can post comments to Teamcamp tasks.

Mitigation: Confirm the exact Teamcamp write payload and intended effect with the user before running write actions.

## Reference(s):

- [Teamcamp Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-teamcamp)
- [Teamcamp Homepage](https://www.teamcamp.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Teamcamp connector schemas before constructing requests; write actions require confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
