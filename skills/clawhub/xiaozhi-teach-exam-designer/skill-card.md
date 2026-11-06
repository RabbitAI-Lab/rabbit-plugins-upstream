## Description:

帮助教师按双向细目表设计测评，编制或改编试题、控制难度并制定评分标准。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学至高中教师，用于围绕测评目标设计试卷与练习、编制双向细目表、完善评分标准，并依据已有题目统计提出返修建议。高中数学、英语和历史命题应转交相应学科技能；教师应审核面向学生或家长的内容后再使用。

### Deployment Geography for Use:

China (guidance is tailored to mainland Chinese primary and secondary education)

## Known Risks and Mitigations:

Risk: Generated questions or scoring criteria may contain errors and affect assessment quality.

Mitigation: Have a teacher solve each generated question and check its answer and points before marking it verified or using it in a formal assessment.

Risk: Confidential exam content or identifiable classroom information could be exposed through prompts or saved records.

Mitigation: Use anonymized classroom details and do not enter confidential exam materials; review retention, deletion, and sharing controls on the platform.

Risk: Draft assessment content may be used with students before it is reviewed for accuracy and suitability.

Mitigation: A teacher should review and approve student- or family-facing content before use.

## Reference(s):

- [试卷蓝图与双向细目表](references/exam-blueprint.md)
- [高中学科标准](references/hs-subject-standards.md)
- [ClawHub release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Markdown and structured class workspace records (JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assessment blueprints, candidate questions, answer and scoring criteria, and item-revision guidance. AI-generated questions require teacher verification before formal use; the skill does not automatically grade students.]

## Skill Version(s):

2.12.6 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
