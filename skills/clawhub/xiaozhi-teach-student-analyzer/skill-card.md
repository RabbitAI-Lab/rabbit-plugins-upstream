## Description:

把班级成绩表变成可执行的教学调整：导入逐题分数后生成班级画像、知识点热力图、分层结果和教学调整建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 teachers use this skill to analyze class assessment data, identify shared and individual weak points, and turn score tables into practical teaching adjustments and parent-facing draft materials. It is intended for teacher-reviewed analysis rather than automated student evaluation.

### Deployment Geography for Use:

Global, with Chinese-language K12 defaults and China Mainland safety-channel guidance that should be localized for other regions.

## Known Risks and Mitigations:

Risk: The skill handles sensitive student assessment records and may reference related teaching records beyond the raw score table.

Mitigation: Use pseudonyms or seat numbers, honor delete/export/share controls, and require consent checks before parent-facing output or cross-skill sharing.

Risk: Score analysis may become misleading when inputs are incomplete, sample sizes are small, or historical evidence is insufficient.

Mitigation: Label total-score-only analysis, suppress unsupported trend claims, and mark conclusions as evidence-insufficient or sample-insufficient when thresholds are not met.

Risk: Parent-facing or safety-related summaries could expose sensitive student details or soften crisis signals.

Mitigation: Require teacher review before sharing, remove names and rankings from public reports, and follow the crisis referral protocol instead of producing ordinary analysis when crisis signals appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [学情分析框架与模板](artifact/references/analysis-framework.md)
- [班级学情报告模板](artifact/references/class-report-template.md)
- [学生个体诊断卡模板](artifact/references/student-diagnosis-card-template.md)
- [班级教学工作区 JSON Schema](artifact/shared/class-teaching-workspace.schema.json)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports, structured teaching recommendations, draft parent-facing text, and workspace field updates requiring teacher confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces aggregate class analysis, knowledge-point heatmaps, individual diagnosis cards, student tiers, and pending workspace updates; parent-facing and stored outputs require consent or teacher review.]

## Skill Version(s):

2.2.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
