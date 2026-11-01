## Description:

用 Cue 查询和分析上市公司股权激励计划与股份回购——基于市面上最全的股权激励数据库（2015年至今10年+历史覆盖），独家特有数据源。查单个计划或要素、或一次多家公司的同类要素，可直连 Cue 数据接口秒级返回；单家公司的方案设计、实施效果、同行对比，以及全市场方案盘点与趋势分析，则生成深度报告（后者走自由式深研），用真实数据评估激励方案的竞争力与合理性。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as company executives, HR teams, investors, analysts, and consultants use the skill to query public equity incentive and share buyback disclosures, compare plans, and prepare company or market analyses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questions may be sent to Cue before the skill presents its redaction confirmation.

Mitigation: Use public or locally sanitized questions, since the original text is received before confirmation.

Risk: Credential-storage instructions conflict with the skill's safety guidance.

Mitigation: Protect the stored API key with restricted file permissions or supported secret storage, and review runner and MCP configuration changes before installation.

## Reference(s):

- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Equity incentive MCP](https://mcp.cuecue.cn/api/esop/mcp/)
- [Share buyback MCP](https://mcp.cuecue.cn/api/buyback/mcp/)
- [Example Cue report](https://cuecue.cn/share/TIxQDFYs)

## Skill Output:

**Output Type(s):** [Structured data, Analysis, Markdown reports]

**Output Format:** [Structured query results and Markdown reports with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Direct queries return structured data; deeper analyses return reports. Coverage is based on public disclosures.]

## Skill Version(s):

1.1.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
