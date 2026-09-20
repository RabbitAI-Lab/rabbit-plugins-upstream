## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows. Use when coordinating multiple agents, running parallel reviews, building pipeline workflows, or implementing divide-and-conquer patterns with subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this workflow to coordinate multi-agent reviews, parallel analysis, pipeline work, and divide-and-conquer implementation while preserving explicit ownership, trust boundaries, and completion accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prompt the agent to spawn background workers or inspect team/task state, expanding activity beyond a single-threaded interaction.

Mitigation: Install it only when multi-agent orchestration is intended, keep worker prompts tightly scoped, and verify active tool schemas and user authority before dispatch.

Risk: Parallel implementation in a shared workspace can create ownership conflicts or overwrite work if write surfaces are not assigned clearly.

Mitigation: Use worktrees or enforce the wave contract: committed baseline, exclusive file ownership, no worker git operations, orchestrator-owned aggregate verification, and rollback limited to attributable paths.

Risk: Parallel reviewers or evaluators can converge on the same mistaken premise if their prompts share unverified claims or prior verdicts.

Mitigation: Use cold-start isolation, pass claims as items to verify, withhold prior verdicts until synthesis, and inspect returned evidence directly.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [SPEC.md](SPEC.md)
- [Agent Types](references/agent-types.md)
- [Dispatch Contract](references/dispatch-contract.md)
- [Wave Contract and QA Escalation](references/wave-contract.md)
- [Worker Lifecycle](references/worker-lifecycle.md)
- [Review and Delivery](references/review-and-delivery.md)
- [Session Coordination](references/session-coordination.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md)
- [Swarm Resilience Patterns](references/resilience-patterns.md)
- [Claude Code agent teams documentation](https://code.claude.com/docs/en/agent-teams)
- [Claude Code tools reference](https://code.claude.com/docs/en/tools-reference)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with task briefs, status conventions, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces orchestration instructions for agent workflows rather than standalone executable artifacts.]

## Skill Version(s):

4.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
