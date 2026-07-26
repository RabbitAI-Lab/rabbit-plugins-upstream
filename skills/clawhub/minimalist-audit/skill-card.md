## Description: <br>
Audit a codebase or directory for deletion candidates: dead code, unused dependencies, single-use abstractions, config that never varies, and duplicated helpers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[divyeshjayswal](https://clawhub.ai/user/divyeshjayswal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit a project for low-risk deletion candidates and prioritize cleanup work with evidence, estimated removable lines, and risk ratings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may identify code for removal that is still needed, especially around tests, authentication, validation, or error handling. <br>
Mitigation: Review each recommendation manually and require proven zero references before applying cleanup in sensitive paths. <br>
Risk: The skill guides an agent to inspect project files and produce cleanup recommendations. <br>
Mitigation: Run it only on code the user is authorized to inspect, and treat results as review guidance rather than automatic edits. <br>


## Reference(s): <br>
- [Minimalist Audit on ClawHub](https://clawhub.ai/divyeshjayswal/skills/minimalist-audit) <br>
- [Publisher profile](https://clawhub.ai/user/divyeshjayswal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown deletion audit with ranked findings and a summary paragraph] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each deletion candidate includes path, estimated removable LOC, evidence, and low/medium/high risk.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
