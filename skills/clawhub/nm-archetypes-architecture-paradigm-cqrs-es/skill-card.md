## Description:

Applies CQRS and Event Sourcing for read/write separation and audit trails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to decide when CQRS and Event Sourcing fit a system and to plan aggregates, commands, events, projections, observability, and operational tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked during broad architecture or scalability discussions where CQRS and Event Sourcing are not appropriate.

Mitigation: Review the skill's fit against the stated non-use cases before applying its guidance to simple CRUD applications or small projects.

Risk: CQRS and Event Sourcing can add operational overhead through event ordering, replay, projection, and failure-handling concerns.

Mitigation: Plan automation, dead-letter handling, replay procedures, observability, and integration tests before adopting the architecture.

Risk: Eventual consistency and event schema drift can confuse users or break consumers.

Mitigation: Document read-model update expectations, use schema versioning, and validate event versions through release controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-cqrs-es)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only advisory output; no executable behavior is included.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
