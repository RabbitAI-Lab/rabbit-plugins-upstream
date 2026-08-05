## Description: <br>
Applies event-driven async messaging to decouple producers and consumers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architects use this skill to decide when event-driven architecture fits a system and to plan async messaging, event schemas, broker topology, failure handling, and observability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate in broad architecture, scalability, or resilience conversations and steer the agent toward event-driven patterns. <br>
Mitigation: Verify that loose coupling, asynchronous processing, and multi-subscriber event flow fit the project before adopting the recommendations. <br>
Risk: Event-driven designs can add operational complexity around ordering, retries, dead-letter queues, schema changes, and observability. <br>
Mitigation: Require explicit event schemas, ownership, broker topology, idempotent consumers, failure handling, and monitoring before treating the guidance as implementation-ready. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-event-driven) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with structured sections and bullet lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Non-executable architecture guidance; no tools, API keys, or shell commands required.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
