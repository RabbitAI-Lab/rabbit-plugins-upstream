## Description: <br>
Applies CQRS and Event Sourcing for read/write separation and audit trails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architects use this skill to decide when CQRS and Event Sourcing fit a system, then outline aggregates, commands, events, projections, observability, and operational deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad architecture triggers may cause CQRS/Event Sourcing guidance to appear for simple CRUD or small projects where the pattern is unnecessary. <br>
Mitigation: Confirm the project needs read/write separation, durable event history, temporal queries, or audit trails before applying the pattern. <br>
Risk: CQRS/Event Sourcing can introduce operational overhead, eventual consistency concerns, and schema drift. <br>
Mitigation: Use explicit event schemas, versioning controls, projection monitoring, replay tooling, and documented read-model consistency expectations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-cqrs-es) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown architecture guidance with checklists and implementation vocabulary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only advisory output; no tool calls, shell commands, or code execution are defined by the skill.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
