## Description: <br>
Audits agent ADC accounts, passwords, roles, and workspace configurations for default passwords, role assignment issues, configuration drift, and health reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit agent account credentials, ADC role assignments, workspace files, and configuration drift before acting on agent health or access-control issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports live credentials, root SSH use, a hard-coded database password, and role-changing database instructions. <br>
Mitigation: Use only with an operator authorized for the target host, credential files, and database; replace embedded credentials with scoped runtime-supplied credentials before normal use. <br>
Risk: Login checks and documented SQL updates can trigger live authentication attempts or privileged role changes. <br>
Mitigation: Run login checks only when live authentication attempts are acceptable, and use the SQL update path only through a separately approved admin change process. <br>


## Reference(s): <br>
- [Role manifest](references/role-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Human-readable terminal report with shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The audit script writes a timestamped report directory under /tmp when run.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
