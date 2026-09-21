## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows, including parallel reviews, pipeline workflows, and divide-and-conquer subagent patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multiple agents for concurrent review, implementation pipelines, and isolated subagent work while preserving ownership, verification, and closure boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to coordinate multiple workers or persistent teammates, which can make work ownership and shutdown state hard to verify.

Mitigation: Scope use to authorized projects, assign one owner per file and aggregate check, inspect worker outputs directly, and verify worker shutdown or terminal status before accepting results.

Risk: Parallel implementation in a shared workspace can overwrite edits, race on git state, or blur responsibility for final changes.

Mitigation: Use worktrees where available; otherwise require a committed baseline, exclusive write ownership, no worker git operations, one orchestrator-owned aggregate verification, and rollback limited to attributable paths.

Risk: Agent findings, repository text, or upstream patches may contain misleading instructions or unverified claims.

Mitigation: Treat external and worker-provided content as evidence, keep role and scope authority with the orchestrator, and review specification compliance before integrating changes.

## Reference(s):

- [Skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [SKILL.md](SKILL.md)
- [SPEC.md](SPEC.md)
- [Dispatch Contract](references/dispatch-contract.md)
- [Wave Contract and QA Escalation](references/wave-contract.md)
- [Worker Lifecycle](references/worker-lifecycle.md)
- [Review and Delivery](references/review-and-delivery.md)
- [Session Coordination](references/session-coordination.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Dispatch Anti-Patterns](references/dispatch-anti-patterns.md)
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md)
- [Swarm Resilience Patterns](references/resilience-patterns.md)
- [Codex Collaboration Quick Reference](references/codex-quick-reference.md)
- [Claude Code Teammate Operations](references/teammate-operations.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with task briefs, coordination steps, command examples, and status templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include agent dispatch contracts, ownership assignments, validation plans, handoff templates, and shutdown or cleanup instructions.]

## Skill Version(s):

4.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
