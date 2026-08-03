## Description: <br>
向采购、工程、财务、物流等内部角色提出背景充分、问题具体、截止时间明确的可执行请求。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees use this skill to prepare complete internal requests for procurement, engineering, finance, logistics, or similar teams. It helps structure the background, specific question, evidence, expected output, deadline, and risk notes before sending the request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Internal business requests may include unnecessary confidential details. <br>
Mitigation: Provide only the information needed for the request and avoid entering unnecessary confidential details. <br>
Risk: A generated request may overstate unverified facts, conflicting inputs, or responsibility assignments. <br>
Mitigation: Keep the parameter status visible, mark missing or conflicting information, and verify facts before sending the request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-request) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Usage template](artifact/examples.md) <br>
- [Test criteria](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with a parameter status table and structured request sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the user to provide the request target, business context, specific question, deadline, and at least one reliable evidence item before producing a formal request.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
