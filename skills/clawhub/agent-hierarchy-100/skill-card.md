## Description:

A system for designing and managing multi-level subagent hierarchies in OpenClaw with explicit upgrade paths, quality gates, and capability unlocks across escalating agent levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when they explicitly want to design, scale, or upgrade a structured hierarchy of subagents. It maps tasks to levels, proposes subagent creation or activation, supervises quality, and preserves operator approval gates for creation, escalation, and tool grants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subagent creation, escalation, or tool grants can expand the scope of agent activity beyond the original task.

Mitigation: Require explicit operator approval for each creation, reactivation, escalation, and tool allocation, and keep the skill inactive for ordinary single-agent tasks.

Risk: Large hierarchies can consume context, tools, or concurrent-agent capacity quickly.

Mitigation: Apply the documented hierarchy limits, including the 100-level depth cap, concurrent-agent limits, context budgets, quality gates, and graceful degradation when overloaded.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/agent-hierarchy-100)
- [README](artifact/README.md)
- [Master skill definition](artifact/SKILL.md)
- [Hierarchy orchestrator](artifact/orchestrator/SKILL.md)
- [Hierarchy tests](artifact/tests/hierarchy-tests.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown instructions with configuration templates and example commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit operator confirmation before creating, reactivating, escalating, or granting tools to subagents.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
