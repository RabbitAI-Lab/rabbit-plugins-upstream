## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows, including parallel reviews, pipeline workflows, and divide-and-conquer subagent work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this workflow skill to decide when and how to coordinate multiple agents, assign isolated work, manage handoffs, and integrate results from parallel or pipeline agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parallel implementation agents can overwrite shared files or race on repository state when ownership and isolation are unclear.

Mitigation: Keep file ownership explicit, use isolated worktrees for parallel writers, and run integration checks after agents return.

Risk: Long-lived or reused spawned agents can carry stale assumptions into later work.

Mitigation: Retire agents after their assigned unit, use fresh agents for new implementation or review rounds, and verify spawned agents are shut down and cleaned up afterward.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Skill runtime instructions](artifact/SKILL.md)
- [Skill specification](artifact/SPEC.md)
- [Agent Types](artifact/references/agent-types.md)
- [Anti-Sycophancy Patterns](artifact/references/anti-sycophancy.md)
- [Codex Collaboration Quick Reference](artifact/references/codex-quick-reference.md)
- [Context Carry-Forward Strategies](artifact/references/context-carry-forward.md)
- [Dispatch Anti-Patterns](artifact/references/dispatch-anti-patterns.md)
- [Environment Variables and Team Config](artifact/references/environment-config.md)
- [Handoff Templates](artifact/references/handoff-templates.md)
- [Message Formats](artifact/references/message-formats.md)
- [Orchestration Patterns](artifact/references/orchestration-patterns.md)
- [Orchestration Primitives](artifact/references/primitives.md)
- [Orchestrating Swarms Quick Reference](artifact/references/quick-reference.md)
- [Swarm Resilience Patterns](artifact/references/resilience-patterns.md)
- [Spawn Backends](artifact/references/spawn-backends.md)
- [Task System Integration](artifact/references/task-system.md)
- [Preset Team Compositions](artifact/references/team-compositions.md)
- [TeammateTool Operations](artifact/references/teammate-operations.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with structured task prompts, command examples, code snippets, and configuration patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-orchestration instructions and handoff structures for the active harness; it does not install executable runtime components.]

## Skill Version(s):

4.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
