## Description:

Helps middle-school physics teachers plan and review laboratory instruction across experiment goals, design, implementation, data processing, conclusions, reports, safety levels, grouping, and equipment arrangements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 physics teachers use this skill to draft experiment teaching plans, organize lab groups and equipment, guide data processing, and prepare lab-report feedback while keeping teacher review and school safety rules in control.

### Deployment Geography for Use:

Global; content is designed for Mainland China Chinese K12 settings and should be localized for other regions before classroom use.

## Known Risks and Mitigations:

Risk: Unsafe experiment guidance could be used without local lab supervision or school-specific safety rules.

Mitigation: Install as a teacher-facing aid only; require teacher review, apply the skill's safetyLevel rules, and follow the school laboratory policy before students act on any experiment plan.

Risk: High-risk or unclear physics experiments may be misclassified for student group work or at-home replication.

Mitigation: Use the bundled lab-safety definitions and physics experiment type reference; high safetyLevel experiments are demonstration-only and should not be recommended for home use.

Risk: The skill is designed around Mainland China Chinese K12 assumptions, which may not match other curricula, emergency guidance, or privacy expectations.

Mitigation: Localize terminology, curriculum alignment, emergency guidance, consent, and privacy handling before using it outside that setting.

Risk: Generated experiment questions, procedures, or report feedback could contain mistakes or overstep teacher judgment.

Mitigation: Keep outputs as drafts, retain required AI-generated labels where applicable, and have the teacher verify calculations, safety, and report feedback before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-experiment-coach)
- [初中物理实验类型详解](references/experiment-types.md)
- [实验安全约定（理化生通用）](shared/lab-safety.md)
- [实验设计样板（探究电流与电压、电阻的关系）](references/experiment-design-sample.md)
- [数据记录样板（数据表格 + 数据图像）](references/data-record-samples.md)
- [初中物理实验数据处理评分](references/data-processing-rubric.md)
- [实验报告模板与评分细则（8 段）](references/lab-report-template.md)
- [班级实验能力档案模板](references/student-lab-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [平台能力约定与降级路径（全库共享）](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Analysis]

**Output Format:** [Markdown prose, tables, checklists, templates, and structured classroom-planning fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing Chinese-language outputs; generated experiment plans and items require teacher review before classroom use.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
