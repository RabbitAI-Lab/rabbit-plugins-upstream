## Description:

Self-driving agent workflow with heartbeat-driven task execution, day/night progress reports, and long-term memory consolidation. Integrates with todo-management for task tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers configuring OpenClaw agents use this skill to initialize a project workspace and set up heartbeat-driven task execution, progress reporting, and memory-maintenance guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow makes service routing mandatory and persistent.

Mitigation: Before enabling heartbeats, replace the routing with providers you approve and define what project content they may receive.

Risk: Autonomous task execution may exceed the intended project scope or spending limits.

Mitigation: Limit the agent to the intended project and set explicit spending and stopping limits.

Risk: Heartbeat and memory instructions, including automatic commits, may persist or publish project changes.

Mitigation: Review MEMORY.md and HEARTBEAT.md, including the automatic-commit behavior, before enabling the workflow.

## Reference(s):

- [ClawHub release](https://clawhub.ai/seairteng/skills/agent-autopilot)
- [Publisher profile](https://clawhub.ai/user/seairteng)
- [Example setup](references/example-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance and templates with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the todo-management skill for task tracking.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
