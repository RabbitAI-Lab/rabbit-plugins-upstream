## Description:

OpenClaw Agent Orchestrator helps an agent split multi-agent work into subtasks, dispatch those tasks to resident OpenClaw agents, track progress, aggregate sourced results, and retry failed subtasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to coordinate multiple resident agents for parallel research, batch audits, multi-perspective reviews, daily digests, and sourced result aggregation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate cross-agent messaging and may propose persistent OpenClaw configuration changes for agent visibility or allowlists.

Mitigation: Approve config.patch changes only after checking which agents are being added to visibility or allowlists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-agent-orchestrator)
- [sessions_send reference](references/sessions_send.md)
- [agentToAgent configuration guide](references/agent_to_agent.md)
- [config.patch safety guide](references/config_patch.md)
- [Task prompt template](templates/task_prompt.md)
- [Design document](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce sourced aggregation reports and proposed OpenClaw config.patch changes after user approval.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
