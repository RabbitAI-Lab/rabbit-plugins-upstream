## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this workflow to coordinate multiple agents for parallel reviews, pipeline workflows, and divide-and-conquer implementation while preserving ownership, trust boundaries, and verification discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting guidance can expose local agent session messages or task records.

Mitigation: Inspect only the active team or task scope and avoid printing raw inboxes or complete team/task files unless explicitly approved.

Risk: The workflow can coordinate background agents and persistent team state.

Mitigation: Use explicit ownership, bounded objectives, authorized safe defaults, and verified terminal statuses before reporting completion.

Risk: Third-party it2 installation is referenced by the security guidance.

Mitigation: Pin or verify any third-party it2 installation before use.

## Reference(s):

- [Runtime Skill Instructions](SKILL.md)
- [Skill Specification](SPEC.md)
- [Dispatch Contract](references/dispatch-contract.md)
- [Wave Contract](references/wave-contract.md)
- [Worker Lifecycle](references/worker-lifecycle.md)
- [Review and Delivery](references/review-and-delivery.md)
- [Session Coordination](references/session-coordination.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Resilience Patterns](references/resilience-patterns.md)
- [Spawn Backends](references/spawn-backends.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with structured task briefs, status labels, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May coordinate background agents and local team or task state when supported by the active runtime.]

## Skill Version(s):

4.5.2 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
