## Description:

Instructs an agent to use the remote HyperNatt MCP market-data tools, especially get_liq_radar, before sizing crypto perpetual trades while avoiding local execution, custody, swaps, and order placement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dialloube-research](https://clawhub.ai/user/dialloube-research)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading-agent operators use this skill to add a read-only liquidation-map check to crypto perpetual workflows. It guides agents to call HyperNatt MCP market-data tools and interpret liquidation structure without treating the result as trade advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects agents to a remote MCP service and can trigger small paid x402 market-data calls.

Mitigation: Verify the HyperNatt MCP connection before installation, configure wallet or payment limits in the MCP runtime, and approve paid data calls only when they match the user's intent.

Risk: The same MCP host exposes swap functionality outside this skill's market-data scope.

Mitigation: Use this skill only for get_agent_manifest and get_liq_radar; use a separate explicit trading or funding skill before placing orders, swapping, bridging, or moving funds.

Risk: Liquidation-map data can be misread as trading advice or a performance guarantee.

Mitigation: Treat the output as market-data context only, avoid inventing signals, and require separate strategy and venue logic for any trade decision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dialloube-research/skills/hypernatt-liq-radar)
- [Server-resolved GitHub Import](https://github.com/DIALLOUBE-RESEARCH/hypernatt-terminal/tree/main/skills/hypernatt-liq-radar)
- [HyperNatt](https://hypernatt.com)
- [HyperNatt MCP Protocol](https://hypernatt.com/mcp/protocol)
- [HyperNatt MCP Server Card](https://hypernatt.com/.well-known/mcp/server-card.json)

## Skill Output:

**Output Type(s):** [guidance, API calls, configuration]

**Output Format:** [Markdown instructions with MCP tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No local shell, filesystem, or environment variables; paid get_liq_radar calls use x402 payment through the MCP runtime.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
