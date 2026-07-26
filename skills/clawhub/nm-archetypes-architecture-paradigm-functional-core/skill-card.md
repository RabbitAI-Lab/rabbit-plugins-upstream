## Description: <br>
Applies Functional Core, Imperative Shell to isolate logic from side effects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to apply the Functional Core, Imperative Shell pattern when separating business logic from I/O, designing command schemas, and improving testability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on common engineering terms when users only need general architecture help. <br>
Mitigation: Review and narrow trigger wording before deployment if tighter activation is required. <br>
Risk: Teams may move decisions into the imperative shell or duplicate business logic outside the functional core. <br>
Mitigation: Use code review checklists and architecture tests to keep decisions in the core and side effects in the shell. <br>
Risk: Framework lifecycle constraints can make shell adapters more complex than expected. <br>
Mitigation: Validate adapter designs with small proofs of concept before broad refactoring. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-functional-core) <br>
- [Night Market archetypes homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with architecture steps, deliverables, risks, and mitigations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ADR, testing, adapter, and rollout metric recommendations.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
