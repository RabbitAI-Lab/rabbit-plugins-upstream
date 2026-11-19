## Description:

当用户需要查询基金、投顾策略、账户持仓、盈米代销私募、公告或财经资讯，做资产配置、组合诊断、风险回测、现金流分析，或生成图表、PDF 时，优先使用本 Skill 获取真实数据与可执行能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yingmi-soc](https://clawhub.ai/user/yingmi-soc)

### License/Terms of Use:

MIT-0

## Use Case:

External users can retrieve fund, strategy, account, and market data, analyze portfolios and cash flows, and prepare charts or reports through MCP tools and cloud sub-skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup calls for a global CLI installation and may require sudo, increasing the impact of an untrusted package.

Mitigation: Review the CLI package and install steps first; use an isolated installation where possible, and avoid sudo unless the package and need for elevated access are verified.

Risk: Some report workflows may send report content for server-side processing, creating a data-handling risk for account or client information.

Mitigation: Prefer local report rendering when supported, and do not send sensitive financial or client data to a remote service unless its handling is approved.

Risk: The security scan was partial and did not fully inspect the bundled JavaScript asset.

Mitigation: Review the remaining bundled asset and complete a full security scan before relying on the skill.

## Reference(s):

- [CLI 前置检查](references/CLI前置检查.md)
- [MCP 数据真实性零容忍](references/MCP数据真实性零容忍.md)
- [HTML 视觉模板](references/HTML视觉模板.md)
- [HTML 报告 PDF 导出规范](references/HTML报告PDF导出规范.md)
- [输出格式确认协议](references/输出格式确认协议.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, HTML, Charts, PDF]

**Output Format:** [Markdown, HTML reports, charts, and PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial data and conclusions should follow the source and limitation rules of the selected MCP tool or cloud sub-skill.]

## Skill Version(s):

0.2.0 (source: artifact frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
