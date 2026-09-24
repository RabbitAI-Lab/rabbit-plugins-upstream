## Description:

英语听力教学设计：把“放一遍录音对答案”变成有目标、有策略、有微技能训练的听力课。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and teaching teams use this skill to design Chinese K-12 English listening lessons, select and label listening materials, build pre-listening, while-listening, and post-listening activities, and plan micro-skill training for upper-primary and middle-school learners.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student or class records may contain personal or sensitive educational information.

Mitigation: Use student aliases, keep teacher confirmation in the workflow, and require teacherWritebackConsent before any personal-profile handoff.

Risk: Listening materials and exam items may include unauthorized audio or protected pre-release exam content.

Mitigation: Require copyrightStatus for every material, store only indexes for restricted sources, avoid pre-release exam content, and keep AI-generated items out of formal use until a teacher verifies them.

Risk: Safety guidance and data rules are written for a Chinese K-12 context and may not fit other regions.

Mitigation: Localize emergency contacts, school-stage assumptions, and minor-data consent rules before deployment outside Mainland China.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-listening-designer)
- [英语听力材料来源清单](references/listening-material-sources.md)
- [听力微技能训练法](references/micro-skill-training.md)
- [英语听力评估评分细则](references/listening-rubric.md)
- [听前预测样板](references/pre-listening-prediction-sample.md)
- [听中任务设计样板](references/while-listening-task-sample.md)
- [学员听力档案模板](references/student-listening-profile-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured teaching-plan text with optional class-workspace field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teacher-reviewed drafts, listening-task structures, rubrics, material-source labels, and consent-gated record handoff guidance; it does not produce audio when platform speech synthesis is unavailable.]

## Skill Version(s):

2.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
