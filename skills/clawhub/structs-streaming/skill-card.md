## Description:

Connects to the GRASS real-time event system via NATS WebSocket for real-time Structs game updates, event monitoring, and event-driven tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to subscribe to GRASS event streams, discover subject patterns, build Node.js or Python listeners, and monitor raids, fleets, player creation, combat, inventory, and grid events. It is intended for event-driven Structs tooling instead of repeated polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad wildcard subscriptions can expose unrelated player or tenant event data during discovery.

Mitigation: Use wildcard subscriptions briefly, then narrow subscriptions to authorized subjects and avoid logging unrelated data.

Risk: Automated reactions to streamed events can perform unintended game actions if keys or permissions are too broad.

Mitigation: Use separate scoped keys, grant minimal object-specific permissions, require approval for high-impact actions, and keep an audit log.

Risk: Long-running listeners can overwhelm clients or leave idle connections open.

Mitigation: Limit subscriptions per connection, implement reconnection with backoff, parse payloads defensively, and close unused connections.

## Reference(s):

- [Structs skill page](https://clawhub.ai/abstrct/skills/structs-streaming)
- [Publisher profile](https://clawhub.ai/user/abstrct)
- [GRASS/NATS protocol specification](https://structs.ai/protocols/streaming)
- [Streaming event type catalog](https://structs.ai/api/streaming/event-types)
- [Streaming event schemas](https://structs.ai/api/streaming/event-schemas)
- [Subscription patterns and examples](https://structs.ai/api/streaming/subscription-patterns)
- [Struct attack event detail schema](https://structs.ai/api/integration-notes#struct_attack-event-detail-schema)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JavaScript, Python, Bash, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to create listener scripts, subscribe to NATS subjects, filter event noise, and apply safe automation boundaries.]

## Skill Version(s):

1.25.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
