## Description:

为单家公司或两家公司生成基于招中标记录的企业画像、中标业绩和竞争格局分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

企业采购、销售及市场分析人员可查询公司的中标履历、客户与供应商关系，并比较投标重叠形成的竞争格局。支持单公司背调和双公司对比。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages an API key and can register a trial account using a device fingerprint.

Mitigation: Provide ZLBX_API_KEY through a secure environment mechanism; obtain consent before registration and avoid use on shared machines.

Risk: Generated reports may expose signed access links and business or contact data.

Mitigation: Review and restrict access to reports before sharing or storing them.

Risk: Incomplete records or unverified public allegations could mislead business decisions.

Mitigation: Cite sources, state data coverage and gaps, and distinguish documented facts from interpretation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/bid-award-competitive-analysis)
- [API quick reference](references/api-quick.md)
- [Analysis workflow](references/workflow.md)
- [Report templates](references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML report]

**Output Format:** [Markdown response and optional shareable HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include cited bidding records, signed access links, and business or contact data.]

## Skill Version(s):

1.0.4 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
