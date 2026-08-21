## Description:

Applies event-driven async messaging to decouple producers and consumers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to decide when event-driven architecture is appropriate and to plan event schemas, broker topology, failure handling, observability, and deliverables for loosely coupled asynchronous systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad architecture triggers may surface this skill in general architecture conversations where a more specific pattern is preferable.

Mitigation: Confirm that the system actually needs asynchronous, loosely coupled, or multi-subscriber behavior before applying the event-driven recommendations.

Risk: Event-driven designs can create hidden coupling through undocumented event meanings or fields.

Mitigation: Use an event catalog or schema registry with clear ownership, versioning, and consumer-driven contract checks.

Risk: Operational complexity can make failed or lagging consumers difficult to diagnose.

Mitigation: Plan observability, dead-letter queues, retry behavior, idempotent consumers, and replay procedures before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-event-driven)
- [Night Market archetypes source](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown prose with architecture recommendations, checklists, and risk mitigations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no code execution, data access, persistence, or privileged authority requested.]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
