## Description:

Guides Chinese middle-school physics teachers through lab teaching workflows, including goals, design, implementation, data handling, conclusions, reports, safety levels, grouping, and equipment planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators use this skill to draft and review Chinese middle-school physics lab lessons, plan safe grouping and equipment use, scaffold data processing and lab reports, and maintain teacher-confirmed student lab records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Physics lab plans may involve equipment, heat, electricity, glassware, lasers, or other classroom hazards.

Mitigation: Require every experiment to carry a safetyLevel; high-risk experiments are demonstration-only or replaced by video or simulation, and medium-risk experiments require teacher presence and first-use apparatus checks.

Risk: Student lab records may contain personal or classroom learning information.

Mitigation: Use pseudonyms or minimized records where appropriate, require teacher-confirmed updates, and ensure consent, sharing controls, export, correction, and deletion controls are enforced by the deployment platform.

Risk: AI-generated questions, experiment plans, or lab-report guidance could be used without sufficient human review.

Mitigation: Label AI-generated materials for teacher verification and keep classroom-facing or parent-facing content subject to teacher approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-experiment-coach)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [初中物理实验类型详解](artifact/references/experiment-types.md)
- [实验设计样板](artifact/references/experiment-design-sample.md)
- [数据记录样板](artifact/references/data-record-samples.md)
- [数据处理评价量规](artifact/references/data-processing-rubric.md)
- [实验报告模板](artifact/references/lab-report-template.md)
- [学生实验档案模板](artifact/references/student-lab-profile-template.md)
- [实验安全约定](artifact/shared/lab-safety.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [班级教学工作区 Schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured tables, rubrics, templates, and JSON-compatible class record fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing Chinese educational guidance; record updates are proposed for teacher confirmation rather than applied automatically.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
