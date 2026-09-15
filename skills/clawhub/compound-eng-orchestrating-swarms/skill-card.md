## Description:

Coordinates multi-agent swarms for parallel reviews, pipeline workflows, and divide-and-conquer subagent work while preserving explicit ownership and verification boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this workflow to coordinate parallel agents, independent reviews, pipeline handoffs, and shared-workspace implementation while keeping ownership, trust boundaries, and verification explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unnecessary agent fan-out can add coordination overhead without improving delivery.

Mitigation: Use the workflow only when concurrent work, independent review, or isolated context justifies coordination; otherwise work inline.

Risk: Parallel or shared-workspace work can create ownership overlaps, conflicting edits, or incomplete verification.

Mitigation: Assign one owner per file and one owner for aggregate checks; use worktrees or the documented shared-tree wave conditions before parallel implementation.

Risk: Worker prompts can blur authority, scope, or trust boundaries if they omit constraints.

Mitigation: Review worker prompts before dispatch and include objective, owned files, interface contracts, acceptance criteria, out-of-scope limits, validation assignment, and trust boundary.

Risk: Background teammates or optional tooling can introduce unmanaged operational exposure.

Mitigation: Monitor terminal states, shut down background teammates when work closes, and approve optional installs such as it2 only after checking package source and version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Skill specification](artifact/SPEC.md)
- [Dispatch contract](artifact/references/dispatch-contract.md)
- [Wave contract and QA escalation](artifact/references/wave-contract.md)
- [Worker lifecycle](artifact/references/worker-lifecycle.md)
- [Review and delivery](artifact/references/review-and-delivery.md)
- [Session coordination](artifact/references/session-coordination.md)
- [Orchestration patterns](artifact/references/orchestration-patterns.md)
- [Anti-sycophancy patterns](artifact/references/anti-sycophancy.md)
- [Swarm resilience patterns](artifact/references/resilience-patterns.md)
- [Spawn backends](artifact/references/spawn-backends.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown instructions with optional shell command snippets and structured handoff templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill itself produces orchestration guidance; downstream agents may produce code, patches, tests, configuration, or review findings.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
