## Description:

Instructs an agent to call HyperNatt's remote MCP liquidation-radar market-data tool before sizing crypto perpetual positions, without local execution, filesystem access, custody, or trade execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dialloube-research](https://clawhub.ai/user/dialloube-research)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent check HyperNatt liquidation-radar market data before evaluating crypto perpetual trade sizing. It is limited to market-data guidance and MCP call ordering, not trade advice, custody, swaps, or order execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote get_liq_radar MCP call can cost $0.001 USDC per request after any free allowance.

Mitigation: Configure the agent to ask before paid calls when payment approval or spend control matters.

Risk: Requests to the external MCP service can reveal the requested symbol or trading context.

Mitigation: Use the skill only when sharing that market-data request context with HyperNatt is acceptable.

Risk: Liquidation-radar data can be mistaken for trade advice or an execution signal.

Mitigation: Treat the output as market-data context only and execute trades through a separate reviewed venue skill or workflow.

## Reference(s):

- [HyperNatt homepage](https://hypernatt.com)
- [HyperNatt MCP protocol](https://hypernatt.com/mcp/protocol)
- [HyperNatt MCP server card](https://hypernatt.com/.well-known/mcp/server-card.json)
- [HyperNatt terminal source](https://github.com/DIALLOUBE-RESEARCH/hypernatt-terminal)
- [HyperNatt terminal security policy](https://github.com/DIALLOUBE-RESEARCH/hypernatt-terminal/blob/main/SECURITY.md)
- [ClawHub skill page](https://clawhub.ai/dialloube-research/skills/hypernatt-liq-radar)

## Skill Output:

**Output Type(s):** [guidance, API Calls, configuration]

**Output Format:** [Markdown instructions with MCP tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces call-order guidance for a remote paid MCP market-data service and does not produce local files or shell commands.]

## Skill Version(s):

1.0.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
