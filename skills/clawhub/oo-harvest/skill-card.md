## Description:

Harvest enables agents to read, create, update, and delete Harvest data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Harvest clients, projects, tasks, task assignments, users, and time entries from an agent session through the OOMOL Harvest connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell installer commands for the oo CLI.

Mitigation: Verify the installer through OOMOL's official documentation before running it, instead of blindly piping a remote script into a shell.

Risk: Write and destructive Harvest actions can create, update, stop, restart, or delete time entries.

Mitigation: Review the exact payload, target, and expected effect with the user and get explicit approval before running those actions.

## Reference(s):

- [ClawHub Harvest skill page](https://clawhub.ai/oomol/skills/oo-harvest)
- [Harvest homepage](https://www.getharvest.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; write and destructive Harvest actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
