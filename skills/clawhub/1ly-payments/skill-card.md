## Description: <br>
Agent-native payments via 1ly MCP for x402 payment handling, USDC API and service payments, store and paid-link creation, marketplace search, key management, and Bags.fm token launch, trade, and fee-claim workflows on Solana and Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1lystore](https://clawhub.ai/user/1lystore) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to configure and operate the 1ly MCP server for buying paid APIs, selling services through paid links, accepting USDC, and running Solana/Base token and payment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform real-money crypto actions, including payments, token trades, token launches, and fee claims that may be irreversible. <br>
Mitigation: Use low-balance wallets, set explicit spend budgets, and review every payment or token action before approval. <br>
Risk: Payment credentials and seller API keys may be stored locally for later use. <br>
Mitigation: Understand the configured local storage paths, store credentials securely, and remove or revoke seller credentials when they are no longer needed. <br>
Risk: Autonomous spend can proceed without per-call confirmation when the user opts in and budgets are configured. <br>
Mitigation: Set ONELY_BUDGET_PER_CALL and ONELY_BUDGET_DAILY explicitly, or set ONELY_BUDGET_PER_CALL=0 to disable auto-spend. <br>


## Reference(s): <br>
- [1ly Homepage](https://1ly.store) <br>
- [1ly Docs](https://docs.1ly.store/) <br>
- [1ly MCP npm Package](https://www.npmjs.com/package/@1ly/mcp-server) <br>
- [ClawHub Skill Page](https://clawhub.ai/1lystore/skills/1ly-payments) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to use the 1ly MCP server for payment, seller, and token workflows; paid actions require explicit budgets and wallet credentials.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
