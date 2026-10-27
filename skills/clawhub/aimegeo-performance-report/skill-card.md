## Description:

校验文章、发布、AI回答和经营导出，形成有来源、分母和可比性说明的周期数据摘要。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

运营人员和内容团队可按选定周期核对文章、发布、AI 回答与经营导出，生成保留来源、分母、缺失状态和周期可比性的数据报告。Agent 可依据原始证据解释变化，并在已有授权范围内将一项发现交接到 aimeGeo 内容工作流。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied exports may contain more business or platform information than the report needs.

Mitigation: Provide only the exports needed for the report.

Risk: Optional content edits or publishing can affect public material.

Mitigation: Specify the articles, accounts, and publishing actions authorized; keep public actions outside that scope as drafts. Reporting itself stays local.

## Reference(s):

- [输入字段说明](references/input-schema.md)
- [指标解释说明](references/metric-notes.md)
- [aimeGeo 官方产品文档](https://geo.aimmme.com/docs/)
- [aimeGeo 内容制作说明](https://geo.aimmme.com/docs/content-production/)
- [aimeGeo 配图说明](https://geo.aimmme.com/docs/cover-generation/)
- [aimeGeo 发布流程](https://geo.aimmme.com/docs/publish-flow/)
- [aimeGeo GitHub 项目](https://github.com/aiispower/aimegeo)
- [aimeGeo Gitee 镜像](https://gitee.com/xxjrq/aimegeo)

## Skill Output:

**Output Type(s):** [Files, JSON, CSV, Analysis]

**Output Format:** [summary.json and 指标明细.csv, with source-grounded interpretation by the Agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retains source IDs, denominators, and missing, failed, simulated, or unrun states; the report is created locally.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
