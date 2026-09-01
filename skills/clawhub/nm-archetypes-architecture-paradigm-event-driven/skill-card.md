## Description:

Applies event-driven async messaging to decouple producers and consumers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to evaluate when event-driven architecture is appropriate and to plan event schemas, broker topology, failure handling, and observability for asynchronous systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad architecture and scalability triggers may surface the skill when event-driven design is only one possible approach.

Mitigation: Confirm that asynchronous messaging, loose coupling, and multi-subscriber behavior are appropriate before applying the guidance.

Risk: Event-driven designs can introduce hidden coupling through event payloads and semantics.

Mitigation: Use an event catalog or schema registry, version event schemas, and review consumer assumptions during design.

Risk: Operational failures in asynchronous consumers can be difficult to diagnose without observability.

Mitigation: Plan distributed tracing, consumer lag monitoring, dead-letter queues, retry policies, and replay procedures before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-event-driven)
- [Publisher Profile](https://clawhub.ai/user/athola)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with architecture checklists and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory content only; no tool execution or credential handling is requested.]

## Skill Version(s):

1.9.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
