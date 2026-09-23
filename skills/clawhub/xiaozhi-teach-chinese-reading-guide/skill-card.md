## Description:

面向语文老师的现代文阅读教学设计工具。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 language teachers use this skill to design modern-text reading lessons, reading strategy practice, group reading activities, discussion questions, and teacher-reviewed class reading records.

### Deployment Geography for Use:

Global, with localization required outside mainland China Chinese K12 contexts.

## Known Risks and Mitigations:

Risk: Student classroom records or parent-facing outputs may expose minor data without proper consent.

Mitigation: Store records only in approved school systems, prefer aliases, and require explicit consent for parent sharing and student writeback.

Risk: The skill assumes mainland China Chinese K12 curriculum, consent rules, language, and crisis contacts.

Mitigation: Localize curriculum assumptions, language, data-consent rules, and crisis referral contacts before deployment in other contexts.

Risk: Generated reading questions, discussion prompts, or teaching tasks may be inaccurate or misaligned with the source text.

Mitigation: Require teacher review and the AI item self-check before classroom use, homework assignment, or resource-library storage.

Risk: Copyrighted textbook, teaching-aid, or literary text could be reproduced beyond permitted use.

Mitigation: Use index-only references for copyrighted material and output outlines, guide questions, or tasks rather than full source text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-reading-guide)
- [文本三解模板](references/text-three-solve.md)
- [阅读 6 大策略卡片](references/six-strategies-card.md)
- [群文阅读设计模板](references/group-text-design.md)
- [群文阅读设计样板](references/group-text-sample-childhood.md)
- [学员阅读力档案模板](references/reading-ability-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [ClassTeachingWorkspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured teaching plans, discussion prompts, reading tasks, and pending class-record entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed drafts; student records, parent-facing content, and writeback actions require explicit consent and confirmation.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
