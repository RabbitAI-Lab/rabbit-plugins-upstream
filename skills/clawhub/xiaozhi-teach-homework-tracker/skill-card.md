## Description:

帮助独立教师登记和追踪作业、归类错因，并根据作业表现生成下节课的教学预诊断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国 K12 独立教师，用于追踪作业提交与订正、汇总错因和生成下节课预诊断；顽固弱项由教师确认后才写入学员档案。

### Deployment Geography for Use:

中国大陆；在其他地区使用前须本地化危机转介和未成年人数据保护指引。

## Known Risks and Mitigations:

Risk: Student homework records may expose minors' personal or family information.

Mitigation: Confirm consent settings, use aliases, and do not store original answers, real names, or family details.

Risk: Incorrect error classification or inferred persistent weaknesses may misdirect teaching.

Mitigation: Review the underlying homework evidence and obtain teacher confirmation before updating a student's weaknesses.

Risk: Crisis or legal guidance intended for mainland China may not suit other regions.

Mitigation: Localize crisis referral and minors' data guidance before use outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [作业完成度追踪视图](artifact/references/completion-tracking-views.md)
- [错题回流清单模板](artifact/references/error-reflow-checklist-template.md)
- [下节课预诊断输出模板](artifact/references/pre-diagnosis-output-template.md)
- [错因与弱项词表](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reports and structured homework follow-up entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation required before recording persistent weaknesses; does not grade assignments or send messages.]

## Skill Version(s):

2.4.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
