## Description:

查询上市公司股权激励计划与股份回购信息，并分析方案要素、实施效果、同行对比和市场趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

企业薪酬与人力团队、投资者和分析师可用它查询上市公司公开披露的股权激励与回购信息，比较方案要素并评估单家公司方案。技能文档描述的股权激励数据覆盖沪深北上市公司，不适用于未公开披露的非上市公司员工股权安排。

### Deployment Geography for Use:

Global (data coverage described by the skill: A-share companies listed in Shanghai, Shenzhen, and Beijing)

## Known Risks and Mitigations:

Risk: API keys may be exposed if shared in chat.

Mitigation: Enter the key privately, restrict access to configuration files, and rotate any key pasted into chat.

Risk: Original questions may be sent to Cue before the privacy confirmation is shown.

Mitigation: Use public, non-sensitive questions unless you accept sending the original text to Cue before redaction confirmation.

Risk: The external runner and Cue server behavior were not covered by the security review.

Mitigation: Inspect and pin the external runner before execution; review credential setup before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue platform](https://cuecue.cn)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Equity incentive MCP](https://mcp.cuecue.cn/api/esop/mcp/)
- [Share buyback MCP](https://mcp.cuecue.cn/api/buyback/mcp/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured data for direct lookups and Markdown research reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response may be a concise data result or a longer report, depending on the request.]

## Skill Version(s):

1.1.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
