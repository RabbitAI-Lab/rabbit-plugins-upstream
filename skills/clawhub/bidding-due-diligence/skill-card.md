## Description:

基于招投标记录生成单家公司或双公司对比的经营实态尽调报告，涵盖合同走势、客户关系、竞争格局与有来源的公开风险信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

投资、并购或合作前需要初步核查企业的用户，可用它分析公开招投标记录中的经营活动、客户结构和竞争态势，并查看附有来源的公开风险信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account setup may store an API key locally and use Zhiliaobiaoxun's service.

Mitigation: Confirm the service and obtain user consent before account registration; keep the API key private.

Risk: HTML reports may expose business-sensitive findings through shareable signed links.

Mitigation: Review reports and recipients before sharing; treat signed links as sensitive.

Risk: Incomplete public records or unverified allegations could mislead due-diligence decisions.

Mitigation: Check source links, distinguish facts from interpretations, and avoid treating the report as investment or legal advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bidding-due-diligence)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [企业情报工作流](artifact/references/workflow.md)
- [报告模板](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML report]

**Output Format:** [Markdown report in conversation and shareable HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links; HTML reports may contain signed links and business-sensitive findings.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
