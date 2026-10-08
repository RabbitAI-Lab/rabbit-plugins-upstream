## Description:

Coordinates authorized OpenClaw agents by dividing work, dispatching tasks, tracking progress, retrying failures, and compiling attributed results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers delegate parallel research, reviews, or routine checks to authorized agents and receive a progress-aware summary with results attributed to each agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated prompts and results are visible to authorized agents.

Mitigation: Review the agent-to-agent allowlist and session visibility before sending tasks; limit access to intended agents.

Risk: Changing agent authorization can grant unintended access.

Mitigation: Approve configuration patches only after checking which agents they authorize.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-agent-orchestrator)
- [Agent-to-agent configuration guide](references/agent_to_agent.md)
- [Session dispatch guide](references/sessions_send.md)
- [Safe configuration changes](references/config_patch.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown reports or conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries attribute results to each agent; reports may be written to a user-selected location.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
