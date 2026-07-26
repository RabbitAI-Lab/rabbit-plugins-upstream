## Description: <br>
Execute native cross-chain cryptocurrency swaps via Chainflip Broker as a Service for supported assets including BTC, ETH, SOL, DOT, TRX, USDC, USDT, and FLIP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baas](https://clawhub.ai/user/baas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to quote, start, and monitor native cross-chain cryptocurrency swaps through the Chainflip BaaS MCP server. It guides asset discovery, quote review, deposit-address handling, refund-address use, optional partner-key commission attribution, and swap status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help initiate real cryptocurrency swaps where transfers may be irreversible. <br>
Mitigation: Review quotes, destination addresses, refund addresses, slippage settings, and deposit addresses before sending funds. <br>
Risk: The skill connects agents to a remote MCP server for swap quotes, swap starts, and status checks. <br>
Mitigation: Install only when the agent is intended to assist with real cryptocurrency swaps through Chainflip BaaS. <br>
Risk: An optional API key can attribute swaps for broker commission. <br>
Mitigation: Provide an API key only when the operator understands and accepts the commission attribution behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/baas/skills/chainflip) <br>
- [Chainflip BaaS Documentation](https://chainflip-broker.io/ai) <br>
- [Chainflip BaaS Homepage](https://chainflip-broker.io) <br>
- [Chainflip BaaS MCP Endpoint](https://chainflip-broker.io/mcp) <br>
- [Broker as a Service Issue Tracker](https://github.com/CumpsD/broker-as-a-service/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with MCP tool call names, parameters, shell commands, and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include real-funds swap IDs, deposit addresses, destination addresses, refund addresses, quotes, fees, rates, and status updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
