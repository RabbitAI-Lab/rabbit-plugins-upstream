## Description:

Guides developers through setting up vx projects and managing project tools, scripts, and environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this guide to initialize vx projects, configure vx.toml, manage tool versions and environments, and run project scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project setup and tool synchronization can change the development environment; vx sync --clean can remove unlisted tools.

Mitigation: Review the project configuration and proposed commands before running them, especially vx sync --clean and setup commands that install or update tools.

Risk: Configured hooks and scripts can run commands during project workflows.

Mitigation: Inspect hook and script definitions before enabling or running them in an existing project.

## Reference(s):

- [vx-project ClawHub release](https://clawhub.ai/loonghao/skills/vx-project)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash and TOML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and configuration examples should be reviewed for the target project before use.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
