## Description: <br>
根据成交证据、时间紧迫度、项目价值、当前卡点和所需投入，安排今日优先推进的客户与动作。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer-management users use this skill to rank which customer opportunities to advance today based on evidence, urgency, value, blockers, and required effort. It supports a Chinese-language workflow that asks for missing or conflicting inputs before producing a formal priority list. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may process customer status, project value, and deal signals. <br>
Mitigation: Provide only information appropriate for the agent context and verify final priorities before acting on them. <br>
Risk: Incomplete, conflicting, or unverified inputs could lead to premature prioritization. <br>
Mitigation: Use the skill's parameter-status and minimum-running-condition checks to request clarification or mark analysis as preliminary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-priority) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with tables and prioritized action lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stop for clarification or label the result as preliminary when required customer-prioritization inputs are missing, conflicting, or unverified.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
