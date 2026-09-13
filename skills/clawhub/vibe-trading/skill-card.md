## Description:

Vibe-Trading is a finance research skill for backtesting, factor analysis, options analysis, market-data retrieval, trade-journal analysis, shadow-account reports, and multi-agent investment research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[warren618](https://clawhub.ai/user/warren618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run finance research workflows across equities, crypto, futures, forex, options, broker journals, and multi-agent investment teams. It helps agents produce strategy analysis, backtest outputs, market research, configuration, and reports for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs an unpinned finance trading package.

Mitigation: Install it in an isolated environment and pin and review the vibe-trading-ai package version before deployment.

Risk: External MCP access may expose broker credentials or trade-related actions.

Mitigation: Use read-only or paper-trading broker credentials by default and avoid wildcard enabledTools entries for external MCP servers.

Risk: Optional write-enabled broker or public API tools can trigger live state-changing trading actions.

Mitigation: Do not enable execute-write unless live trading actions are intentional and separately approved.

## Reference(s):

- [Vibe-Trading ClawHub Skill Page](https://clawhub.ai/warren618/skills/vibe-trading)
- [Interactive Brokers Public MCP Endpoint](https://api.ibkr.com/v1/api/mcp-public)
- [eToro Public API MCP](https://mcp.public-api.etoro.com)
- [eToro MCP Skill](https://mcp.public-api.etoro.com/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML/PDF reports, code snippets, shell commands, and configuration fragments.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include research summaries, backtest metrics, factor results, market-data responses, strategy files, and report artifacts for human review.]

## Skill Version(s):

0.1.15 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
