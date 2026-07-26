## Description: <br>
Automates BambooHR employee, time-off, benefits, dependents, and employee update workflows through Rube MCP with current tool schema lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
HR operators, managers, and agent developers use this skill to find BambooHR employees, track employee changes, manage time-off requests, update employee records, and review dependents or benefit coverage through Rube MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live BambooHR changes, including employee updates and time-off create, approve, deny, or cancel actions, without built-in final confirmation steps. <br>
Mitigation: Require human review before employee update or time-off mutation actions. <br>
Risk: The skill can expose sensitive HR data through broad employee or dependent queries. <br>
Mitigation: Use the least-privileged BambooHR account available and avoid broad employee or dependent queries unless needed. <br>


## Reference(s): <br>
- [Rube MCP](https://rube.app/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/bamboohr-automation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with MCP tool sequences and parameter notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an active Rube MCP BambooHR connection and current tool schema lookup before workflows.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
