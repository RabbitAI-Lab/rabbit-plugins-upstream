## Description:

把班级成绩表变成可执行的教学调整：导入逐题分数，生成班级画像、知识点热力图、学生分层和教学调整建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn class assessment data into a practical learning diagnosis: score distributions, weak knowledge points, student tiers, individual diagnosis cards, parent-facing communication material, and short- or medium-term teaching adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Class assessment records and student-level diagnosis can expose sensitive education data if entered with identifying details or shared too broadly.

Mitigation: Use student aliases or seat numbers, confirm comfort with storing class assessment records before installation, and narrow read access to reviewPlans when field-level scoping is available.

Risk: Parent-facing or student-profile outputs may disclose information without the required consent.

Mitigation: Check parentSharingConsent, emotionSharingWithParent, and teacherWritebackConsent before generating parent material or writing student-profile outputs.

Risk: Safety-relevant crisis signals may appear during education conversations and should not be handled as ordinary learning analytics.

Mitigation: Stop the normal analysis flow when crisis indicators appear and follow the bundled crisis referral guidance before returning to academic tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [学情分析框架与模板](artifact/references/analysis-framework.md)
- [班级学情报告模板](artifact/references/class-report-template.md)
- [学生个体诊断卡模板](artifact/references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown reports and structured classroom workspace updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses student aliases or seat numbers, consent checks for parent-facing and student-profile outputs, and conservative labels when sample size or data completeness is insufficient.]

## Skill Version(s):

2.1.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
