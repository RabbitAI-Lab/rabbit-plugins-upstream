## Description:

Coordinates multi-agent swarms for parallel reviews, pipeline workflows, and divide-and-conquer work with subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering leads use this workflow to coordinate multiple agents for code review, research, implementation pipelines, and divide-and-conquer tasks while preserving file ownership and handoff discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background or persistent agents can continue affecting shared work if their scope is not managed.

Mitigation: Use explicit owned files or isolated worktrees, keep implementation scopes narrow, and clean up persistent teams after use.

Risk: Parallel implementation agents can overwrite each other's changes in a shared worktree.

Mitigation: Assign exclusive owned files, run a pre-dispatch file-intersection check, or isolate implementation agents in separate worktrees.

Risk: Coordination workflows may expose unrelated local team or profile data if agents inspect broader state than needed.

Mitigation: Avoid inspecting unrelated ~/.claude profile or session data and keep agent prompts bound to the relevant repository, files, and task artifacts.

## Reference(s):

- [Skill specification](SPEC.md)
- [Team compositions](references/team-compositions.md)
- [Agent types](references/agent-types.md)
- [Teammate operations](references/teammate-operations.md)
- [Task system integration](references/task-system.md)
- [Codex collaboration quick reference](references/codex-quick-reference.md)
- [Message formats](references/message-formats.md)
- [Orchestration patterns](references/orchestration-patterns.md)
- [Spawn backends](references/spawn-backends.md)
- [Environment variables and team config](references/environment-config.md)
- [Handoff templates](references/handoff-templates.md)
- [Context carry-forward strategies](references/context-carry-forward.md)
- [Anti-sycophancy patterns](references/anti-sycophancy.md)
- [Swarm resilience patterns](references/resilience-patterns.md)
- [Orchestration primitives](references/primitives.md)
- [Orchestrating swarms quick reference](references/quick-reference.md)
- [Dispatch anti-patterns](references/dispatch-anti-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code blocks and structured task/message templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes users to bundled references for the active harness and workflow pattern.]

## Skill Version(s):

4.4.2 (source: server release evidence; changelog v4.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
