## Description:

Guides AI agents in using vx to manage development tools and run project workflows across platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to select vx-managed commands for tool setup, coding tasks, CI, and MCP configurations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to post outcomes to an issue or task tracker without requiring user approval.

Mitigation: Require explicit approval before posting to external trackers.

Risk: Suggested commands can install tools or change project, global, CI, or MCP configuration.

Mitigation: Start with read-only status and check commands; approve changes explicitly and pin versions where reproducibility matters.

## Reference(s):

- [ClawHub vx-usage release](https://clawhub.ai/loonghao/skills/vx-usage)
- [Managed command shim guide](https://github.com/loonghao/vx/blob/main/docs/guide/managed-command-shims.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations for vx-managed development workflows.]

## Skill Version(s):

1.0.11 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
