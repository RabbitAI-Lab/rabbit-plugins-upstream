## Description:

Coordinates multi-agent swarms for parallel reviews, pipeline workflows, and divide-and-conquer work with subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this workflow skill to coordinate multi-agent code reviews, parallel implementation waves, pipeline handoffs, and failure recovery while preserving explicit ownership and verification boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional tool installation and team-state inspection examples can introduce supply-chain or local-data exposure when copied broadly.

Mitigation: Install the skill only when multi-agent orchestration is needed, pin or independently verify optional tools such as it2, and limit ~/.claude reads to current team and task files.

Risk: Parallel implementation agents can conflict in a shared workspace if ownership, isolation, and aggregate verification are not enforced.

Mitigation: Use worktrees or the documented wave contract, assign one owner per write surface and aggregate check, and perform post-integration verification before accepting results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Agent Types](references/agent-types.md)
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md)
- [Codex Collaboration Quick Reference](references/codex-quick-reference.md)
- [Context Carry-Forward Strategies](references/context-carry-forward.md)
- [Cross-Run Coordination](references/cross-run-coordination.md)
- [Dispatch Anti-Patterns](references/dispatch-anti-patterns.md)
- [Environment Variables & Team Config](references/environment-config.md)
- [Handoff Templates](references/handoff-templates.md)
- [Message Formats](references/message-formats.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Orchestration Primitives](references/primitives.md)
- [Orchestrating Swarms Quick Reference](references/quick-reference.md)
- [Swarm Resilience Patterns](references/resilience-patterns.md)
- [Spawn Backends](references/spawn-backends.md)
- [Task System Integration](references/task-system.md)
- [Preset Team Compositions](references/team-compositions.md)
- [TeammateTool Operations](references/teammate-operations.md)
- [Wave Contract and QA Escalation](references/wave-contract.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, shell command examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses harness-specific orchestration primitives and routes to reference documents based on task context; no structured machine output is guaranteed.]

## Skill Version(s):

4.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
