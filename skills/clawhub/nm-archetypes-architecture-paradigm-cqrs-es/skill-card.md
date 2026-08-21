## Description:

Applies CQRS and Event Sourcing for read/write separation and audit trails

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to evaluate when CQRS and Event Sourcing fit a system, then outline aggregates, commands, events, projections, audit trails, and operational safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad architecture trigger may activate the skill during general design conversations where CQRS or Event Sourcing guidance is not needed.

Mitigation: Review whether the trigger set should be narrowed before deployment, and apply the skill only when the user is designing systems with complex domain logic, audit history, or separate read/write scaling needs.

Risk: CQRS and Event Sourcing can add operational overhead, eventual consistency concerns, and event schema drift if applied to simple CRUD systems.

Mitigation: Use the skill's own fit criteria before adopting the pattern, and require clear event versioning, projection monitoring, replay procedures, and user-facing consistency expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-cqrs-es)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with architecture recommendations, deliverables, and implementation considerations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no executable tools, commands, or environment variables are declared.]

## Skill Version(s):

1.9.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
