## Description:

学情分析（元镜）—— 把成绩 / 答题表与题目-知识点映射，变成可复算、可追溯的诊断报告：数据质量闸门、逐题统计、按分值加权的知识点掌握率、A/B/C 分层与临界生识别、薄弱点诊断（低样本自动降级为人工复核），支持阈值配置、学生标识匿名化与 CI 闸门；零依赖本地运行，不联网、不调用模型，不用于学生评价或排名。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Teachers and school teams use the skill to analyze structured class score or answer sheets, identify knowledge gaps and borderline cases, and prepare evidence-based reports for teaching improvement. It does not provide student rankings or evaluations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student identities may be exposed in shared reports or error logs even when --anonymize is used.

Mitigation: Replace student identifiers with independently assigned random codes before analysis; keep reports and error logs private.

Risk: Low-sample conclusions may be unreliable.

Mitigation: Review low-sample conclusions manually.

Risk: Future npm downloads are outside the current inspection.

Mitigation: Use a pinned, reviewed release.

## Reference(s):

- [Project repository](https://github.com/YottaMeta/yotta-mirror)
- [Input data format](references/data-format.md)
- [Report format](references/report-format.md)
- [Privacy guidance](references/privacy.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown or JSON diagnostic reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic; conclusions include item IDs, sample sizes, rates, and thresholds. Low-sample findings are flagged for human review.]

## Skill Version(s):

0.1.2 (source: frontmatter, CHANGELOG released 2026-11-01, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
