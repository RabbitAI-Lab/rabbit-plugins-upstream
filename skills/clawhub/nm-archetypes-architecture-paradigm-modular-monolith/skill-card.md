## Description: <br>
Applies modular monolith guidance with enforced internal boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architecture teams use this skill to decide when a modular monolith fits a codebase and to plan module boundaries, public contracts, and enforcement checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may appear during broad architecture prompts even when a modular monolith is not the right fit. <br>
Mitigation: Confirm the application needs bounded modules and service-like autonomy without distributed-system overhead before applying the guidance. <br>
Risk: Architecture recommendations can become misleading if module boundaries and contracts are not enforced. <br>
Mitigation: Review proposed boundaries with project owners and back them with dependency checks, contract documentation, or CI enforcement before relying on the pattern. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-modular-monolith) <br>
- [Claude Night Market archetypes](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with bullet lists and architecture recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no tools, secrets, code execution, data access, or persistence are required.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
