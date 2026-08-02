## Description: <br>
Applies layered n-tier architecture with enforced boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and software architects use this skill when evaluating or adopting layered n-tier architecture for moderate systems that need clear presentation, domain, and persistence boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate during general architecture or domain-design conversations where layered architecture is not the best fit. <br>
Mitigation: Confirm that the task specifically benefits from layered n-tier guidance before applying the recommendations. <br>
Risk: Layered architecture guidance can introduce rigidity, pass-through code, or latency if applied to systems that need independent scaling or frequent cross-layer interaction. <br>
Mitigation: Review the proposed layering against project scalability, deployment, and business-logic constraints before adoption. <br>
Risk: Architecture recommendations may be incomplete or misleading if used without project-specific review. <br>
Mitigation: Have developers or architects review dependency rules, ADRs, diagrams, and enforcement checks before implementation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-layered) <br>
- [Claude Night Market archetypes homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with architecture steps, deliverables, tool suggestions, and risk notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No code execution, data access, persistence, or hidden behavior identified in server security evidence.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
