## Description: <br>
检查工作汇报中的目标、进展、证据、风险、下一步和所需支持，并整理为结构清晰的汇报。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and teams use this skill to check whether a work report has a clear goal, progress, evidence, risks, next steps, requested support, and audience. When required information is missing or conflicting, the skill should ask for clarification or clearly mark any preliminary analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may paste sensitive business details into a work-report review. <br>
Mitigation: Use only information appropriate for the workspace and avoid sharing sensitive details unless permitted. <br>
Risk: Incomplete, conflicting, or unverified inputs could be presented as stronger conclusions than the evidence supports. <br>
Mitigation: Require the parameter status table, ask for missing key inputs, preserve conflicts for verification, and mark preliminary analysis when the formal trigger conditions are not met. <br>
Risk: The artifact is marked as a draft and its evidence-priority rules are still incomplete. <br>
Mitigation: Treat human-confirmed facts and real business records as authoritative, and review outputs before using them in operational reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-report) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown report with a parameter status table and structured report sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a background goal, current progress, next-step plan, and at least one reliable evidence item before formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact changelog lists v0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
