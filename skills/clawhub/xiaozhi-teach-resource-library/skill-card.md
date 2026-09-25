## Description:

帮助独立教师分类保存、检索和改编讲义、题目、讲评话术及匿名错因案例，并记录资源的使用效果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师可建立带知识点、难度和版权状态的教学资源索引，查找适合当前教学需求的材料，并在人工审核后复用或改编。

### Deployment Geography for Use:

Mainland China; adapt language, legal, and crisis-support guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Student cases or shared resource records may reveal identifying information.

Mitigation: Remove identifying details before saving cases and require consent before sharing across skills.

Risk: Storing third-party exercises or scans may infringe copyright.

Mitigation: Record copyright status; keep textbook and past-exam questions as references to source and page rather than copied text.

Risk: Unverified AI-generated or adapted questions may contain errors.

Mitigation: Label them pending verification and require the teacher to solve and check each item before student use.

Risk: Saving or deleting resources without teacher approval may cause unwanted or irreversible changes.

Mitigation: Confirm changes with the teacher before saving or deleting resource records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization and retrieval](artifact/references/resource-categorization.md)
- [Resource entry examples](artifact/references/resource-entry-examples.md)
- [Copyright annotation template](artifact/references/copyright-annotation-template.md)
- [AI-generated item review](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown recommendations and structured resource-index entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results explain their relevance; AI-generated items remain marked pending teacher verification.]

## Skill Version(s):

2.4.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
