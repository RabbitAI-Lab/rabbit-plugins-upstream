## Description:

面向语文老师的文言文与古诗词教学设计工具，支持诵读正音、训诂、串讲、主题讨论、文化联结和班级古文积累记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language teachers use this skill to plan classical Chinese and poetry lessons for upper-primary and middle-school classes. It produces teacher-reviewed reading, exegesis, discussion, cultural-connection, homework, and draft class progress-record materials.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Class or student records may be used without the right consent or teacher review.

Mitigation: Verify platform consent settings before using records and keep lesson plans, progress entries, writebacks, and parent-facing materials in teacher-confirmed draft form.

Risk: Generated lesson items, examples, or explanations may be inaccurate or unsuitable for the declared grade band.

Mitigation: Run generated items through the AI item self-check, label teacher-facing generated items for manual verification, and require teacher confirmation before classroom or resource-library use.

Risk: Modern textbook annotations, translations, or teaching aids may be copyrighted even when the classical source text is public-domain.

Mitigation: Use public-domain source text, avoid copying protected editions, label citation copyright status, and provide frameworks or partial translation guidance rather than full modern translations.

Risk: Student distress or safety signals could be softened or mishandled in learning or parent-feedback workflows.

Mitigation: Apply the crisis referral protocol first, avoid diagnostic labels and sensitive detail storage, and provide location-appropriate emergency or trusted-adult referral guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-classical-guide)
- [文言常用实词虚词速查](references/classical-vocab-quick-ref.md)
- [文言文诵读三阶与节奏训练指南](references/recitation-rhythm-guide.md)
- [文言文训诂四法速查卡](references/exegesis-method-card.md)
- [诗词意象速查](references/poetry-image-catalog.md)
- [串讲样板模板](references/serial-explain-sample-template.md)
- [主题讨论问题设计题库](references/theme-discussion-question-bank.md)
- [学员古文积累档案模板](references/classical-accumulation-profile-template.md)
- [ClassTeachingWorkspace schema](shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown teaching plans, discussion prompts, and JSON-compatible draft classWorkspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-confirmed drafts; student record writeback and parent-facing materials require consent checks.]

## Skill Version(s):

2.1.10 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
