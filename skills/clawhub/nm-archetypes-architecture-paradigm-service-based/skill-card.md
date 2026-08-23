## Description:

Applies coarse-grained service architecture for deployment independence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to evaluate when a service-based architecture fits systems that need independent component deployment while shared databases or ERP constraints make full microservices impractical. It helps outline adoption steps, service contracts, database ownership, delivery artifacts, and architecture risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words may cause the skill to appear in more conversations than intended.

Mitigation: Use or enable it for architecture discussions where service-based architecture, SOA, modular systems, or shared-database constraints are relevant.

Risk: The artifact references a separate Claude Code plugin for the full experience.

Mitigation: Evaluate that plugin separately before installing it.

Risk: Shared-database coupling can make changes cascade across services.

Mitigation: Use database views, replication, or a formal schema deprecation schedule, and assign explicit schema or table ownership.

Risk: Weak governance can let a service-based architecture degrade into a distributed monolith.

Mitigation: Track coupling metrics and enforce clear service and data ownership.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-service-based)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only advisory prompt; no code execution, data access, persistence, or hidden behavior according to ClawHub security evidence.]

## Skill Version(s):

1.9.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
