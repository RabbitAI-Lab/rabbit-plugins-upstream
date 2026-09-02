## Description:

Applies coarse-grained service architecture guidance for deployment independence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and software architects use this skill to decide when a service-based architecture is appropriate and to plan service boundaries, contracts, shared data ownership, and deployment coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Architecture reference guidance can be applied to a system where the assumptions do not fit.

Mitigation: Review the guidance with project architects before adopting service boundaries, shared data ownership rules, or deployment procedures.

Risk: Shared database coupling can create cascading changes across services.

Mitigation: Use explicit schema ownership, database views, replication, or a formal schema deprecation schedule to manage change.

Risk: Weak governance can let a service-based architecture degrade into a distributed monolith.

Mitigation: Track coupling metrics and enforce clear ownership of services and data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-service-based)
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [guidance, markdown, text]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static advisory content; no executable behavior or special access is indicated by the security evidence.]

## Skill Version(s):

1.9.19 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
