## Description: <br>
为寻求融资的初创或成长期项目做初步筛选诊断，同时对照 VC/PE 分阶段 BP 标准与政府引导/产投基金落地要求，输出结构化达标度、红旗清单与整改建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhuiwensm99](https://clawhub.ai/user/zhuiwensm99) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External founders, fundraising advisers, investment teams, and project-screening users use this skill to assess whether a startup or growth project is ready for VC/PE review and Chinese government or industrial fund landing requirements. It helps compare investor fit, identify BP gaps, flag return-investment or local-landing risks, and produce remediation suggestions before fundraising. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Project inputs and generated reports may contain sensitive business, fundraising, or financing information. <br>
Mitigation: Use an appropriate local workspace and control access to input JSON files and generated Markdown or JSON reports. <br>
Risk: Government-fund policy details and city-level landing rules can change after the evidence date. <br>
Mitigation: Verify current local rules and official application guidance before using the report for a financing or legal decision. <br>
Risk: The diagnostic output can be mistaken for formal investment, legal, or compliance advice. <br>
Mitigation: Use the report as preliminary screening support and have qualified reviewers confirm investment, legal, and policy conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhuiwensm99/skills/project-fund-screening) <br>
- [筛选标准细则（参考知识库）](references/standards.md) <br>
- [评分卡与权重（Rubric）](references/scorecards.md) <br>
- [项目筛选诊断 — 输入模板与输出骨架](assets/diagnosis-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON input templates, JSON summaries, and shell commands for running the local diagnosis script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language output by default; missing project fields are marked as pending verification instead of being invented.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
