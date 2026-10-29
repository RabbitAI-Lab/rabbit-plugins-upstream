## Description:

把独立教师散在文件夹、微信收藏和笔记本里的讲义、题目、讲评话术、错因案例收进一个可检索的库。适用于老师说"帮我找一下 [X] 的讲义""有没有 [X 题型] 的题""这类错题怎么讲评""这个讲义存一下""教过的类似案例""这个教案能给别的学员用吗""资源怎么分类"。流程：入库时打标签与版权状态 → 按知识点/难度检索 → 改编适配后复用 → 记录用过几次、效果如何。本 SKILL 不出题、不备课、不批改、不联系家长——只管资源的存、找、改；AI 生成的题必须老师验算后才算入库。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

独立教师可用此技能整理、标注和检索讲义、题目、讲评话术及脱敏错因案例，并在核对版权状态后改编复用。它侧重资源管理，不代替教师备课、出题、批改或联系家长。

### Deployment Geography for Use:

Global; confirm the learner's country or region before providing local crisis contacts or applying region-specific education guidance.

## Known Risks and Mitigations:

Risk: The resource schema requires more student information than the skill's stated field limits disclose.

Mitigation: Before using private student records, ask the publisher to align the schema with the advertised field limits and confirm the integration supplies only those fields.

Risk: Student records or generated exercises may be reused without adequate privacy review or accuracy checks.

Mitigation: Use anonymized cases, obtain explicit approval before sharing, and have a teacher verify AI-generated exercises before adding or recommending them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource entry examples](references/resource-entry-examples.md)
- [Resource categorization](references/resource-categorization.md)
- [Copyright annotation template](references/copyright-annotation-template.md)
- [Teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [AI-generated item check](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Concise Chinese-language resource guidance and structured resource-library entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resource entries use the documented workspace index fields; student cases should be anonymized, and AI-generated questions require teacher verification before learner use.]

## Skill Version(s):

2.12.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
