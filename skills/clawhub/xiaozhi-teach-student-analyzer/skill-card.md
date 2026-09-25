## Description:

将班级逐题成绩转化为知识点诊断、分层分析和可执行的教学调整建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学中高段及初中教师：分析班级逐题成绩、识别共性薄弱知识点与学生分层，并起草班级报告和教学调整建议，供教师审核后使用。

### Deployment Geography for Use:

Mainland China; localize consent and crisis-referral guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Student performance records and individual feedback can expose sensitive information if shared inappropriately.

Mitigation: Use student aliases unless real names are explicitly approved for internal use; check consent settings and have a teacher review parent-facing material before sharing.

Risk: Conclusions based on incomplete or limited assessment data may misrepresent student needs.

Mitigation: Limit total-score-only inputs to score-distribution analysis, avoid trend claims without repeated assessments, and have teachers review recommendations.

Risk: Consent and crisis-referral practices may not fit jurisdictions outside Mainland China.

Mitigation: Confirm localization with the school or operator before use elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](references/analysis-framework.md)
- [Class report template](references/class-report-template.md)
- [Student diagnosis card template](references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown reports, knowledge-point summaries, individual diagnosis cards and teaching recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Knowledge-point analysis requires item-level scores and an item-to-topic map; teacher review is required before sharing.]

## Skill Version(s):

2.4.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
