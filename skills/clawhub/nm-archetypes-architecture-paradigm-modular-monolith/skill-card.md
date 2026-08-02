## Description: <br>
Applies modular monolith guidance with enforced internal boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and software architecture teams use this skill to decide when a modular monolith is appropriate and to plan internal module boundaries, contracts, dependency checks, and evolution paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms such as "architecture" and "monolith" may activate the skill in unrelated design discussions. <br>
Mitigation: Use narrower activation terms or confirm that modular monolith guidance is relevant before applying the skill output. <br>
Risk: Architecture guidance can be misapplied to systems that are already distributed or too small to benefit from formal module boundaries. <br>
Mitigation: Check the system context before adopting the pattern and avoid using the guidance where the artifact's stated non-use cases apply. <br>
Risk: Module boundaries may erode over time if teams do not enforce dependency rules. <br>
Mitigation: Pair the guidance with code review discipline and automated dependency checks that fail when forbidden module references are introduced. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-modular-monolith) <br>
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with architecture recommendations, adoption steps, deliverables, troubleshooting notes, and risk mitigations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no executable tools, credential use, or API calls are indicated by the evidence.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
