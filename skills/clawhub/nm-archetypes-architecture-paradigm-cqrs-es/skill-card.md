## Description: <br>
Applies CQRS and Event Sourcing for read/write separation and audit trails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architects use this skill to evaluate and apply CQRS and Event Sourcing when systems need separated read/write models, complex domain behavior, durable event history, or audit trails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may appear in broad architecture or scalability discussions where CQRS and Event Sourcing are not actually warranted. <br>
Mitigation: Use it only when the system needs complex domain logic, separate read/write scaling, or full state-change history; avoid it for simple CRUD applications. <br>
Risk: CQRS and Event Sourcing can add operational overhead, eventual consistency, and event schema drift risks. <br>
Mitigation: Plan observability, replay and recovery tooling, read-model update expectations, schema versioning, and validation gates before adopting the paradigm. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-cqrs-es) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with architecture steps, deliverables, risks, and component vocabulary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Text-only architecture guidance; no tools, credentials, or privileged actions are requested.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
