## Description:

Coordinates 16 specialized agent roles for research, coding, writing, review, and other workflows using shared communication tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaneflorin](https://clawhub.ai/user/zaneflorin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users coordinate specialist workers for staged or parallel research, implementation, documentation, and review tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated agents can run commands and write files without clearly defined user-control boundaries.

Mitigation: Use a constrained workspace with permission controls and review worker tasks before execution.

Risk: Web browsing and scraping can expose sensitive repositories or credentials if agents are given broad access.

Mitigation: Avoid providing sensitive repositories or credentials unless the environment enforces access restrictions.

Risk: Persistent shared state may retain task information across agent restarts.

Mitigation: Limit sensitive information shared with workers and review retained state.

## Reference(s):

- [Multi-Agent Orchestrator on ClawHub](https://clawhub.ai/zaneflorin/skills/multi-agent-orchestrator)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown and task-specific files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include specialist findings, deliverables, and shared coordination state.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
