## Description:

数学教案设计帮助数学教师将概念建构、例题示范、变式训练、课堂小结和错例档案组织成可审阅的中文 K12 数学教案草稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External math teachers and teaching teams use this skill to draft Chinese K12 math lesson plans that connect concept introduction, worked examples, variation practice, summaries, and error-file follow-up. It is intended as teacher-facing planning support, not as a replacement for teacher judgment or direct student evaluation.

### Deployment Geography for Use:

China (mainland) K12 math-teaching context; localize curriculum alignment, consent requirements, and crisis-resource guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Persistent student or class records may contain sensitive education data.

Mitigation: Confirm consent settings before writeback, keep student identities pseudonymized, and keep unapproved entries in the teacher workspace.

Risk: The skill is designed for a Chinese K12 math-teaching context and may give unsuitable curriculum or safety guidance elsewhere.

Mitigation: Localize curriculum assumptions, consent rules, and crisis-resource guidance before deployment outside mainland China.

Risk: AI-generated math items or lesson examples may be incorrect or unsuitable for the grade band.

Mitigation: Run the skill's item self-check, label teacher-side generated items as AI-generated, and require teacher verification before reuse or storage.

Risk: Copied textbook, workbook, or exam content may have uncertain reuse rights.

Mitigation: Use the skill's copyright-status categories and avoid storing unauthorized source problems beyond permitted indexing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-lesson-planner)
- [数学概念建构四步模板](references/concept-build-template.md)
- [变式训练设计模板](references/variation-design.md)
- [数学错因分类表（教案层）](references/error-pattern-rubric.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [班级教学工作空间 Schema](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese Markdown lesson-plan drafts, structured classWorkspace entries, and teacher-reviewed handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher review is required before student-facing, parent-facing, resource-library, or persistent-record use.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
