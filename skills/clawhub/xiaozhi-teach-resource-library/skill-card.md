## Description:

教学资源复用库帮助独立教师把讲义、题目、讲评话术和错因案例整理成可检索、可复用、带版权状态和验算标记的资源库。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师用它整理、检索和复用教学资源，包括讲义、题目、讲评话术、错因案例、教案和课件。它支持资源入库、标签管理、版权状态记录、学员情境匹配、改编说明和使用效果记录，并保留教师审核环节。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student-data sharing consent is not represented in the packaged schema according to the server security summary.

Mitigation: Install only where the platform enforces cross-skill sharing consent outside this schema or treats missing consent as denial; add an explicit consent.crossSkillSharing or equivalent field before real learner use.

Risk: Resource matching can touch learner records and case examples.

Mitigation: Keep case entries anonymized, avoid identifiable learner details, and use deletion, pause, and sharing controls when requested.

Risk: Unauthorized teaching material could be copied into the resource library.

Mitigation: Require copyrightStatus on every resource, store tutoring-book originals and past exam papers as index-only references, and do not store pirated scans or unauthorized reposts.

Risk: AI-generated exercises can be incorrect or unsuitable if reused before review.

Mitigation: Mark AI-generated items, keep verifiedByTeacher false until a teacher verifies each item, and exclude unverified items from student-facing recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization](references/resource-categorization.md)
- [Resource entry examples](references/resource-entry-examples.md)
- [Copyright annotation template](references/copyright-annotation-template.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Shared vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured resource-library entries and status labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference workspace resource-library fields such as resourceId, title, resourceType, copyrightStatus, aiGenerated, verifiedByTeacher, and usageNotes.]

## Skill Version(s):

2.1.12 (source: server release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
