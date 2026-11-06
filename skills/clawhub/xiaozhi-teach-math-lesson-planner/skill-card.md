## Description:

为初中和高中数学教师设计概念建构、例题讲解、变式训练、复习与讲评课的教学方案框架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆初高中数学教师，生成概念教学路径、例题与变式练习框架，并组织复习课、讲评课和错例记录，供教师审核后用于备课。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: 课堂记录可能包含未成年学生的个人或成绩信息。

Mitigation: 使用化名；将原始个人分数留在此技能访问范围之外；保存或分享前由教师审核，并确认宿主平台落实同意与存储控制。

Risk: 输入尚未启用的统考试题或未经核验的生成题，可能泄露考试内容或将错误练习带入课堂。

Mitigation: 不要输入尚未启用的考试题；对 AI 生成题按要求标注，并由教师验算后再写入资源库或试卷。

Risk: 引用原题或教辅内容可能超出授权范围。

Mitigation: 注明历年真题或教辅原题出处，不整卷复制，并遵守技能规定的题目版权状态。

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-lesson-planner)
- [高中数学课程地图](artifact/references/math-hs-curriculum-map.md)
- [概念建构四步模板](artifact/references/concept-build-template.md)
- [变式训练设计](artifact/references/variation-design.md)
- [错因分类与教案预防](artifact/references/error-pattern-rubric.md)
- [班级教学工作空间数据契约](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [中文教案框架、教学说明、例题与变式练习，以及结构化班级工作空间字段]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [输出为教师审阅的草稿；AI 生成的数学题需标注并由教师验算后才能保存或使用。]

## Skill Version(s):

2.12.6 (source: server-resolved release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
