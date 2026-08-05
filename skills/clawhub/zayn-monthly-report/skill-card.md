## Description: <br>
基于当月日报、周报、项目记录和业务结果，复盘月度目标达成、重点项目进展、结果密度、资源投入、等待阻塞、关闭能力和下月重点，并生成适合个人复盘或向管理者汇报的结构化月报。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, managers, and business operators use this skill to turn monthly work records, project updates, business outcomes, blockers, and next-month priorities into a structured monthly review or management report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monthly work records can include confidential metrics, customer details, or sensitive project status. <br>
Mitigation: Provide only business records approved for the agent environment and redact customer or confidential details when they are not needed for the review. <br>
Risk: Monthly conclusions can be misleading when source records lack reliable evidence or metric definitions. <br>
Mitigation: Use the skill's parameter checks, mark data gaps, and avoid ratios, trends, or business-state claims unless the underlying records support them. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Test Scenarios](artifact/tests.md) <br>
- [Changelog](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown report analysis and review guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return parameter gaps and follow-up questions when minimum monthly-report inputs are missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation lists v0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
