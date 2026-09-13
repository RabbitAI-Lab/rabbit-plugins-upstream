## Description:

英语听力教学设计：把"放一遍录音对答案"变成有目标、有策略、有微技能训练的听力课。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External English teachers use this skill to design listening lessons and practice sequences for upper-primary and junior-secondary learners. It helps select and document listening materials, plan pre-listening, while-listening, and post-listening activities, train micro-skills, and prepare teacher-reviewed classroom records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom scores, exam items, or student records could be written back outside the intended listening-only scope.

Mitigation: Install only where the platform enforces the listening-only scope and requires active teacher confirmation and consent controls before any writeback.

Risk: AI-generated listening materials or questions could be used in a resource library or exam before review.

Mitigation: Keep the skill's required AI-generated label and require teacher verification before storing generated items or adding them to formal tests.

Risk: Listening materials could include unauthorized copied audio or unclear source rights.

Mitigation: Require a copyrightStatus value for each material and store only indexes for教辅原题, past exam questions, or sources without confirmed redistribution rights.

Risk: Student micro-skill profiles could overstate evidence when only total scores or too few observations are available.

Mitigation: Use item-level scores as the source for micro-skill strengths and weaknesses, leave micro-skill fields empty when only total scores exist, and keep low-sample conclusions out of long-term records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-listening-designer)
- [英语听力材料来源清单](references/listening-material-sources.md)
- [英语听力评估评分细则](references/listening-rubric.md)
- [听力微技能训练法](references/micro-skill-training.md)
- [听前预测样板](references/pre-listening-prediction-sample.md)
- [听中任务设计样板](references/while-listening-task-sample.md)
- [学员听力档案模板](references/student-listening-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [班级教学工作空间 schema](shared/class-teaching-workspace.schema.json)
- [危机例外](shared/crisis-exception.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured classroom workspace fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listening lesson plans, material-selection checklists, AI-generated item labels, micro-skill training suggestions, and teacher-confirmed writeback fields.]

## Skill Version(s):

2.1.12 (source: evidence.json release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
