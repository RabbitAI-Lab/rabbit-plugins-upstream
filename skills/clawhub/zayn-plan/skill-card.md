## Description: <br>
把模糊目标拆解为有顺序、依赖、时间、资源、责任和完成标准的可执行计划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users can use this prompt-only planning skill to turn a goal, current state, deadline, scope, constraints, dependencies, owners, and completion criteria into an actionable plan after required inputs are checked. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incomplete, conflicting, or unverified inputs could lead to an overconfident plan. <br>
Mitigation: The skill requires a parameter status table and instructs the agent to ask for missing critical inputs or mark preliminary analysis before formal planning. <br>
Risk: A generated plan could assume resources, dependencies, owners, or completion criteria that the user did not provide. <br>
Mitigation: The skill explicitly checks resources, constraints, dependencies, responsible parties, and completion standards, and forbids treating assumptions as confirmed facts. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with a parameter status table and structured planning sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only; no tools or execution authority indicated.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation lists v0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
