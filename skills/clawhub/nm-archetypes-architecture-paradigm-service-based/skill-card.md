## Description: <br>
Applies coarse-grained service architecture for deployment independence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architecture teams use this skill to evaluate and describe service-based architectures for systems that need independently deployable components while retaining coarse-grained services or shared data constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may appear in broad architecture or modularity conversations because of its activation keywords. <br>
Mitigation: Use the guidance when service-based architecture is relevant, and review recommendations before applying them to a system design. <br>
Risk: Service-based guidance can still influence architecture decisions even though the skill has no executable behavior. <br>
Mitigation: Validate service boundaries, data ownership, contracts, deployment plans, and rollback plans with the responsible architecture and engineering teams. <br>
Risk: Shared databases can couple services and degrade the architecture into a distributed monolith. <br>
Mitigation: Assign schema ownership, control breaking changes through review, track coupling, and use views, replication, or schema deprecation schedules where appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-service-based) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown prose with architecture checklists and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable behavior, data access, or persistence.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
