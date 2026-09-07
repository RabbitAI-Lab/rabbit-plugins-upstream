## Description:

Helps middle-school physics teachers organize experiment teaching from goals, design, implementation, data processing, conclusions, and lab reports through safety levels, grouping, and equipment planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to plan and facilitate middle-school physics lab lessons, including experiment classification, variable control, data-recording scaffolds, safety handling, group roles, and report guidance. It is scoped to experiment teaching rather than full concept lesson planning, individual problem explanations, or assessment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Experiment archives may contain student information or classroom records.

Mitigation: Use platforms that enforce teacher confirmation, consent, pseudonymization, and sharing controls; teachers should avoid entering real student names, contact details, or family information.

Risk: Lab guidance can create physical safety issues if high-risk activities are assigned to students or homes.

Mitigation: Require a safetyLevel for every experiment, keep high safetyLevel activities as teacher demonstrations only, and avoid recommending high-risk activities for home use.

Risk: Generated experiment plans or items may contain calculation, safety, or equipment-range errors.

Mitigation: Mark AI-generated material for human verification and require teacher checks before classroom use or item-bank storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-experiment-coach)
- [初中物理实验类型详解](references/experiment-types.md)
- [实验设计样板（探究电流与电压、电阻的关系）](references/experiment-design-sample.md)
- [数据记录样板（数据表格 + 数据图像）](references/data-record-samples.md)
- [初中物理实验数据处理评分](references/data-processing-rubric.md)
- [实验结论样板](references/conclusion-sample.md)
- [实验报告模板与评分细则（8 段）](references/lab-report-template.md)
- [实验报告样板（八段完整示例）](references/lab-report-sample.md)
- [班级实验能力档案模板](references/student-lab-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured sections, tables, checklists, and classroom profile fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes safetyLevel labels and teacher-review prompts; does not perform experiments or replace teacher grading.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
