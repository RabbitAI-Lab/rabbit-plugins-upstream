## Description:

Guides agents in using vx to manage development tools and run project workflows across local environments, MCP integrations, and CI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and their agents use this skill to choose vx-managed commands, configure project tool versions, and prepare MCP, GitHub Actions, and container workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global skill setup can change guidance for other agent sessions.

Mitigation: Review changes before running vx ai setup globally; prefer project-local setup when appropriate.

Risk: MCP integrations and GitHub operations can access sensitive files or credentials and publish comments.

Mitigation: Limit MCP paths and token permissions, and review GitHub comments before posting.

Risk: CI and container examples using latest or main can pull changing dependencies.

Mitigation: Pin action, image, and tool versions where practical.

## Reference(s):

- [vx-usage on ClawHub](https://clawhub.ai/loonghao/skills/vx-usage)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover vx.toml, MCP, CI, and containers.]

## Skill Version(s):

1.0.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
