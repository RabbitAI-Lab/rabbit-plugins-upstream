## Description:

把独立教师散在文件夹、微信收藏和笔记本里的讲义、题目、讲评话术、错因案例收进一个可检索的库。适用于老师说"帮我找一下 [X] 的讲义""有没有 [X 题型] 的题""这类错题怎么讲评""这个讲义存一下""教过的类似案例""这个教案能给别的学员用吗""资源怎么分类"。流程：入库时打标签与版权状态 → 按知识点/难度检索 → 改编适配后复用 → 记录用过几次、效果如何。本 SKILL 不出题、不备课、不批改、不联系家长——只管资源的存、找、改；AI 生成的题必须老师验算后才算入库。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to store, tag, retrieve, adapt, and reuse Chinese K12 teaching resources such as handouts, item references, feedback scripts, anonymized error cases, and lesson-plan materials. It supports resource matching by knowledge point and difficulty while keeping teacher review, copyright status, and student-data controls visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student cases or learning records could expose personal information if stored without anonymization.

Mitigation: Store only fully anonymized cases, remove names, schools, contact details, and family identifiers, and use the documented deletion and export controls when a learner or guardian requests data handling changes.

Risk: Copyrighted question text, unauthorized scans, or exam-confidential material could be copied into the resource library.

Mitigation: Keep textbook-support and past-exam items as source indexes only, do not store question text or scans, require copyrightStatus on every resource, and avoid entering pre-release exam material.

Risk: AI-generated or adapted items may contain incorrect, ambiguous, out-of-scope, or unverified educational content.

Mitigation: Mark AI-generated items, keep verifiedByTeacher false until a teacher has solved and checked them, and exclude unverified items from learner-facing recommendations.

Risk: Cross-skill sharing can broaden access to resource metadata and limited student-learning records.

Mitigation: Use the provided pause, sharing, and consent controls, and confirm cross-skill sharing consent before another skill reads resource-library data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [资源标签、检索与脱敏](references/resource-categorization.md)
- [资源五大类：用途、入库要求与示例](references/resource-entry-examples.md)
- [版权标注模板](references/copyright-annotation-template.md)
- [全库统一词表（单一事实源）](shared/vocab.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [SoloTeacherWorkspace schema](https://xiaozhi-skills.openclaw.dev/schemas/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese-language Markdown guidance with structured resource metadata fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces retrieval results, tagging guidance, resource-library entries, copyright annotations, anonymization checks, and teacher-review warnings; no executable install behavior.]

## Skill Version(s):

2.3.0 (source: ClawHub release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
