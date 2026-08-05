## Description: <br>
Applies hexagonal architecture isolating domain from infrastructure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architects use this skill to apply hexagonal, ports-and-adapters architecture when they need domain logic isolated from infrastructure and adapter dependencies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may appear during broad architecture or testability conversations where explicit ports-and-adapters guidance was not requested. <br>
Mitigation: Narrow invocation triggers when deployment should be limited to explicit hexagonal architecture or ports-and-adapters design work. <br>
Risk: Architecture advice may introduce unnecessary abstraction for small utilities or short-lived prototypes. <br>
Mitigation: Apply the skill when external dependencies, adapter swaps, or contract-testable boundaries justify the added structure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-hexagonal) <br>
- [Clawdis metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown prose with architecture steps, deliverables, risks, and mitigations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory guidance only; no code execution, tool calls, or sensitive access.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
