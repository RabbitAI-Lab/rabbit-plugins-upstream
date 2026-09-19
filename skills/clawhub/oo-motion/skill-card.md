## Description:

Motion (usemotion.com). Use this skill for ANY Motion request: reading, creating, updating, and deleting Motion data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and teams using Motion use this skill to list workspaces, users, schedules, statuses, projects, and tasks, and to create or update Motion projects and tasks through the OOMOL connector. Agents should confirm write payloads and destructive targets before changing Motion data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer source and prefer an official signed or checksum-verified installation path before running it.

Risk: The skill can create, update, and delete Motion data.

Mitigation: Confirm the exact JSON payload and intended effect with the user before write actions, and require explicit approval before destructive actions.

Risk: The OOMOL connector requires access to Motion account data.

Mitigation: Install only when the user accepts OOMOL as the Motion connector and grants the minimum account access needed for the task.

## Reference(s):

- [Motion homepage](https://www.usemotion.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Motion skill page](https://clawhub.ai/oomol/skills/oo-motion)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Motion connector schemas to shape JSON inputs and returns connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
