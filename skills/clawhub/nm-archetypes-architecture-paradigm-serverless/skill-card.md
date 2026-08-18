## Description:

Applies serverless FaaS patterns for event-driven workloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to evaluate serverless architecture for event-driven, bursty workloads, including function decomposition, externalized state, cold-start planning, observability, security, deployment automation, and cost controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may steer broad architecture discussions toward serverless patterns even when long-running processing, persistent connections, or local state are required.

Mitigation: Review workload requirements against the skill's stated non-use cases before adopting serverless recommendations.

Risk: Serverless designs can create provider dependency, distributed debugging complexity, and resource-limit constraints.

Mitigation: Use portable interfaces where feasible, standardize tracing and structured logging, and monitor provider quotas, concurrency, duration, memory, and cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-serverless)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance with architecture recommendations and deliverable outlines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces documentation-oriented serverless architecture guidance; no code execution or credential access is described in the security evidence.]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
