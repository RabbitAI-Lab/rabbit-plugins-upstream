## Description: <br>
Assesses architecture designs across performance, availability, scalability, and security dimensions, then produces a quantified risk matrix with mitigation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architecture reviewers use this skill to review a proposed architecture, identify key risks, quantify probability and impact, and plan mitigations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Architecture descriptions may contain secrets or unnecessary proprietary details. <br>
Mitigation: Redact secrets and omit unnecessary proprietary details before asking an agent to analyze the architecture. <br>
Risk: Checklist-based risk ratings can be incomplete or misprioritized when the input architecture is incomplete. <br>
Mitigation: Review the report with system owners and validate high-impact findings against current architecture, operational data, and security requirements. <br>


## Reference(s): <br>
- [Architecture Risk Assessment on ClawHub](https://clawhub.ai/golngod/skills/architecture-risk-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown risk assessment report with risk matrices, mitigation plans, residual risks, and architecture improvement suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Checklist-guided assessment across performance bottlenecks, single points of failure, scalability bottlenecks, and security vulnerabilities] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
