## Description:

帮助独立教师登记作业、追踪提交状态与错因，并根据作业表现准备下一节课的教学重点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文 K12 场景的独立教师：记录学员作业与提交状态，整理错因和反复出现的弱项，生成完成度视图及下节课预诊断，供教师核对和使用。

### Deployment Geography for Use:

Mainland China by default; localize curriculum, consent requirements, and help channels for other regions.

## Known Risks and Mitigations:

Risk: Homework follow-up records and student summaries could be stored or shared without appropriate consent.

Mitigation: Confirm profile, cross-skill sharing, and parent-summary consent; use aliases and limit stored information to low-sensitivity follow-up details.

Risk: Mainland China-specific help channels may be inappropriate elsewhere.

Mitigation: Confirm the user's region and localize crisis and help-channel text before deployment outside Mainland China.

## Reference(s):

- [ClawHub release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [作业完成度视图模板](references/completion-tracking-views.md)
- [错题回流清单模板](references/error-reflow-checklist-template.md)
- [顽固弱项档案模板](references/persistent-weakness-file-template.md)
- [下节课预诊断模板](references/pre-diagnosis-output-template.md)
- [学员作业画像模板](references/student-homework-profile-template.md)
- [错因与弱项分类规范](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text and Markdown summaries, checklists, and teacher-facing drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update consented homework follow-up and progress records in the platform workspace; teacher reviews assessments and outward-facing text.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
