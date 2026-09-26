## Description:

Coordinates multiple resident OpenClaw agents by delegating subtasks, tracking progress, retrying failures, and combining attributed results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use this skill to divide work among their resident agents, monitor delegated tasks, and receive a sourced summary of the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuration changes could expand which agents can communicate.

Mitigation: Review and approve any proposed configuration patch before it is applied.

Risk: Delegated task details and results may be visible to target agents and their sessions.

Mitigation: Delegate only information appropriate for those agents and review their results before sharing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-agent-orchestrator)
- [Agent-to-agent configuration guide](references/agent_to_agent.md)
- [Session messaging guide](references/sessions_send.md)
- [Safe configuration changes](references/config_patch.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown report with agent-attributed results and optional configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report to a user-selected location; retries failures up to three times by default.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
