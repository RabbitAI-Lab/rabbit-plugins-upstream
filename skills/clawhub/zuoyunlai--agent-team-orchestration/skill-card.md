## Description:

Orchestrate multi-agent teams with defined roles, task lifecycles, handoff protocols, and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to structure sustained multi-agent workflows, define team roles, route tasks through review, and standardize handoffs and artifact sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared task comments and artifacts can expose sensitive project information if teams use broad shared directories or paste secrets into coordination notes.

Mitigation: Keep shared directories scoped to the project and avoid placing secrets in task comments or artifacts.

Risk: Scheduled ops workflows can dispatch or summarize work without appropriate oversight if enabled too broadly.

Mitigation: Review scheduled ops setup before enabling it and keep orchestrator ownership over task routing and state transitions.

Risk: Agent handoffs can produce misleading or incomplete work if outputs are accepted without review.

Mitigation: Require review gates and verification steps before marking work done.

## Reference(s):

- [Agent Team Orchestration on ClawHub](https://clawhub.ai/zuoyunlai/skills/agent-team-orchestration)
- [Team Setup](references/team-setup.md)
- [Task Lifecycle](references/task-lifecycle.md)
- [Communication](references/communication.md)
- [Patterns](references/patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with templates, workflow steps, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-readable operating patterns and handoff templates; it does not include executable scripts or install hooks.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
