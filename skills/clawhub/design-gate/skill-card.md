## Description: <br>
A design gate checker for architecture validation, feasibility analysis, and impact scope assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terr123123](https://clawhub.ai/user/terr123123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill during design review to check architecture completeness, technical feasibility, and impact scope before implementation proceeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill produces checklist-style pass/fail scores that may be incomplete for sensitive or complex designs. <br>
Mitigation: Treat results as advisory and require human architecture review before implementation decisions. <br>
Risk: A design may pass the local gate while still missing security, compliance, or domain-specific review requirements. <br>
Mitigation: Use the gate as an early completeness check and pair it with project-specific security and risk review. <br>


## Reference(s): <br>
- [Design Gate Skill on ClawHub](https://clawhub.ai/terr123123/skills/design-gate) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, guidance] <br>
**Output Format:** [Python objects and JSON-serializable gate results with pass/fail status, scores, messages, and issue details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configurable score thresholds; outputs are advisory design review signals, not authoritative security or architecture decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
