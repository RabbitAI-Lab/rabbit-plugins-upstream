## Description:

A finance research toolkit for market analysis, strategy backtesting, factor and options analysis, trade-journal review, and multi-agent research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[warren618](https://clawhub.ai/user/warren618)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, researchers, and developers use this skill to analyze market data, test investment strategies, review trading behavior, and produce research reports across equity and crypto markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External MCP servers can expose arbitrary tools when wildcard access is enabled.

Mitigation: Enable only trusted MCP servers and explicitly allowlist the tools the agent needs.

Risk: Broker and OAuth connections can grant higher-risk trading access.

Mitigation: Keep credentials limited to read-only or paper profiles unless live trading is intentionally authorized.

## Reference(s):

- [Vibe-Trading on ClawHub](https://clawhub.ai/warren618/skills/vibe-trading)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Text and structured tool results, with optional HTML or PDF research reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some data providers, multi-agent research, and broker connectors require separate credentials.]

## Skill Version(s):

0.1.16 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
