## Description:

帮助独立教师依据单名学员的真实学习记录起草阶段报告、学习计划和非强迫式续课建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师根据指定学员的课后记录、作业跟进和课时信息，起草有据可查的阶段报告及供教师审定的续课沟通话术。报告由教师自行决定是否发送给家长。

### Deployment Geography for Use:

Mainland China; localize language, curriculum, consent requirements and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: A report could disclose a minor's longitudinal learning records to a parent without the required consent.

Mitigation: Confirm the named student's consent fields before drafting parent-facing content; otherwise prepare only a teacher-facing report, and have the teacher review and send it manually.

Risk: Chinese K12 curriculum assumptions and mainland-China crisis contacts may be inappropriate in other regions.

Mitigation: Localize language, curriculum and crisis-contact guidance before use outside the intended setting; confirm location before providing local help contacts.

Risk: Unsupported learning statistics or renewal claims could mislead families.

Mitigation: Tie figures and progress statements to recorded evidence, use qualitative descriptions when scores are unavailable, and require teacher review before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [阶段报告模板](artifact/references/stage-report-templates.md)
- [续课沟通话术](artifact/references/renewal-communication-scripts.md)
- [平台能力与地域约定](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language report drafts and renewal conversation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-linked observations; qualitative assessments where scores are unavailable; teacher review and manual sending.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
