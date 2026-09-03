## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows, including parallel reviews, pipeline workflows, and divide-and-conquer work with subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering leads use this skill to coordinate multi-agent code reviews, research waves, implementation pipelines, and divide-and-conquer workflows while maintaining ownership, validation, and handoff discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debugging examples may read local team config, task, and inbox files that contain prompts, messages, or operational context.

Mitigation: Inspect only teams you are authorized to inspect, limit disclosure of local team-state contents, and redact sensitive prompt or message data before sharing.

Risk: Persistent or background agents may remain active after a multi-agent workflow finishes.

Mitigation: Request shutdown or cleanup for finished teammates and verify that no stale team resources remain.

Risk: Parallel implementation agents working in the same checkout can overwrite files or race on shared state.

Mitigation: Use separate worktrees for parallel implementation, or serialize implementation work and assign one owner per file.

## Reference(s):

- [Skill source](SKILL.md)
- [Skill specification](SPEC.md)
- [Agent Types](references/agent-types.md)
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md)
- [Codex collaboration quick reference](references/codex-quick-reference.md)
- [Context Carry-Forward Strategies](references/context-carry-forward.md)
- [Cross-Run Coordination](references/cross-run-coordination.md)
- [Dispatch Anti-Patterns](references/dispatch-anti-patterns.md)
- [Environment Variables and Team Config](references/environment-config.md)
- [Handoff Templates](references/handoff-templates.md)
- [Message Formats](references/message-formats.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Orchestration Primitives](references/primitives.md)
- [Swarm Resilience Patterns](references/resilience-patterns.md)
- [Spawn Backends](references/spawn-backends.md)
- [Task System Integration](references/task-system.md)
- [Preset Team Compositions](references/team-compositions.md)
- [TeammateTool Operations](references/teammate-operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces orchestration prompts, task briefs, handoff templates, checklists, and validation guidance; it does not directly execute spawned agents by itself.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
