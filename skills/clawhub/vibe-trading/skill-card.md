## Description:

Provides finance research tools for market analysis, strategy backtesting, factor analysis, options pricing, and trade-journal review across supported markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[warren618](https://clawhub.ai/user/warren618)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and financial researchers use the tools to analyze market data, test strategies, price options, and review trade journals across supported markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broker authorization can expose financial account information.

Mitigation: Start with research or paper/read-only profiles and authorize only the access needed.

Risk: Swarm research sends supplied context to the configured model provider.

Mitigation: Avoid including sensitive context unless the provider is approved to receive it.

Risk: The eToro execute-write integration can grant direct trading authority.

Mitigation: Keep execute-write excluded unless direct trading is intentional and explicitly authorized.

Risk: Session-level MCP server overrides can introduce untrusted tool servers.

Mitigation: Leave session server overrides disabled unless callers are trusted.

## Reference(s):

- [Interactive Brokers public MCP endpoint](https://api.ibkr.com/v1/api/mcp-public)
- [eToro MCP skill documentation](https://mcp.public-api.etoro.com/skill)

## Skill Output:

**Output Type(s):** [Financial analysis, Backtest results, Strategy guidance, HTML/PDF reports, Configuration instructions]

**Output Format:** [Structured tool results and Markdown analysis; Shadow Account reports can be HTML or PDF.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected market, data sources, strategy, and analysis period.]

## Skill Version(s):

0.1.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
