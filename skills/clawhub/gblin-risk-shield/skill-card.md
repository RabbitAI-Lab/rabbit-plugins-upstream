## Description: <br>
On-chain BTC/ETH market-risk check for agents on Base that reads the live Crash Shield risk regime, can mint a 10-minute EIP-712 Risk Attestation via x402, verifies peer attestations, and can optionally guide surplus USDC into an oracle-priced index treasury. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gblinproject](https://clawhub.ai/user/gblinproject) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents, developers, and treasury operators use this skill before trades, rebalances, or treasury moves to check BTC/ETH market-risk posture and record or verify short-lived proof-of-diligence attestations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a third-party financial risk service and paid x402 endpoints. <br>
Mitigation: Install only if the operator accepts the third-party service dependency and small USDC charges; review each payment requirement before signing. <br>
Risk: Wallet tooling may be used to sign x402 payments. <br>
Mitigation: Do not provide private keys to the skill; use existing wallet tooling and review every wallet transaction before signing. <br>
Risk: The market-risk signal may be mistaken for financial advice. <br>
Mitigation: Treat the signal as advisory input to the operator's own trading or treasury policy. <br>
Risk: Risk attestations are short-lived and can become stale. <br>
Mitigation: Verify peer attestations and re-mint or re-check them for each decision cycle when freshness matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gblinproject/skills/gblin-risk-shield) <br>
- [GBLIN agent docs](https://gblin.digital/agents) <br>
- [Live usage stats](https://gblin.digital/api/agent-stats) <br>
- [Base contract](https://basescan.org/address/0x36C81d7E1966310F305eA637e761Cf77F90852f0) <br>
- [MCP server package](https://www.npmjs.com/package/@gblin-protocol/mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API response expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require curl, x402-capable payment tooling, a wallet with USDC on Base, and optional Node.js for the MCP server.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
