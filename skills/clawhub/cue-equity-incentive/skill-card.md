## Description:

用 Cue 查询和分析上市公司股权激励计划与股份回购，支持单项要素直查、批量公司取数、单家公司方案深研，以及全市场盘点和趋势分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, consultants, investors, and listed-company operations teams use this skill to retrieve public A-share equity-incentive and buyback data, compare company plans, and generate Cue-backed research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to persistently modify local MCP client configuration with a Cue bearer token.

Mitigation: Review MCP configuration edits before accepting them, store only a user-provided Cue key, avoid exposing the key in prompts or logs, and rotate the key if it was disclosed.

Risk: The skill depends on a remote Cue runner checkout without a pinned revision.

Mitigation: Pin or review the runner checkout before execution and re-review changes before updating it.

Risk: Cue services receive equity-incentive queries and may process sensitive research interests.

Mitigation: Use the skill only when sending those queries to Cue is acceptable for the user or organization.

Risk: The high-net-worth person lookup can raise compliance and appropriate-use concerns.

Mitigation: Avoid that lookup unless there is a legitimate, compliance-approved use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Cue equity-incentive MCP endpoint](https://mcp.cuecue.cn/api/esop/mcp/)
- [Cue buyback MCP endpoint](https://mcp.cuecue.cn/api/buyback/mcp/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, JSON MCP configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Cue report links, local report paths, MCP-derived data tables, and configuration guidance for Cue API key usage.]

## Skill Version(s):

1.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
