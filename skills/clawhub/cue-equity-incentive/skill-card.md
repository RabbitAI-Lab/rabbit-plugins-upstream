## Description:

用 Cue 查询和分析上市公司股权激励计划与股份回购，支持单计划或要素直查、批量多公司要素查询，以及方案设计、实施效果和同行竞品对比的深度报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve and analyze public equity incentive and share buyback information for listed companies, especially A-share companies. It supports quick factual lookups through Cue MCP endpoints and longer-form Markdown reports for evaluation, comparison, and scheme design questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist a Cue API key into local AI-client configuration.

Mitigation: Use a scoped or throwaway Cue API key where possible, keep it out of chat and logs, review MCP configuration changes before use, and rotate the key if it has been exposed.

Risk: The skill runs code pulled from a remote runner repository.

Mitigation: Install only after deciding to trust Cue and the sensedeal runner repository, and review runner changes before setup or updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Equity incentive MCP endpoint](https://mcp.cuecue.cn/api/esop/mcp/)
- [Share buyback MCP endpoint](https://mcp.cuecue.cn/api/buyback/mcp/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, JSON-like MCP configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cue report links for deep research outputs; factual MCP lookups return structured data without a report link.]

## Skill Version(s):

1.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
