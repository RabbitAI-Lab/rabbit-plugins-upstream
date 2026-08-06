## Description: <br>
Analyze read-only multichain EVM portfolios, wallet balances, idle stablecoins, capital efficiency, allocation drift, and rebalance proposals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External DeFi users and agent developers use this skill to inspect public EVM wallet portfolio data, identify candidate liquid reserves, evaluate allocation drift, and draft non-custodial rebalance discussion points without executing transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses and optional API credentials are sent to FarmDash for portfolio analysis and tier identification. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and provide FARMDASH_API_KEY only when the higher tier limits or position depth are needed. <br>
Risk: The optional onboarding POST registers the public agent or wallet address and skill identifier for tier, capability, and telemetry purposes. <br>
Mitigation: Run the onboarding POST only after explicit informed consent; do not trigger it automatically or by default. <br>
Risk: Portfolio recommendations are based on read-only snapshots and may be incomplete when coverage, pricing, liquidity, liabilities, or off-wallet exposures are unavailable. <br>
Mitigation: Present recommendations as reviewable analysis, label missing coverage clearly, and require a separate execution flow for any transaction. <br>


## Reference(s): <br>
- [FarmDash Agent Hub](https://www.farmdash.one/agents) <br>
- [FarmDash OpenAPI Spec](https://www.farmdash.one/agents/openapi.yaml) <br>
- [FarmDash MCP Configuration](https://www.farmdash.one/.well-known/mcp.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-wagon-steward) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-derived portfolio summaries and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only portfolio analysis; wallet calls require a public EVM address and may use optional FARMDASH_API_KEY for tier limits.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata; artifact frontmatter lists 0.7.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
