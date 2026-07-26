## Description: <br>
Bitcoin L1 wallet for agents - check balances, send BTC, manage UTXOs. Extends to Stacks L2 (STX, DeFi) and Pillar smart wallets (sBTC yield). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whoabuddy](https://clawhub.ai/user/whoabuddy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to guide LLM agents through Bitcoin wallet balance checks, UTXO review, fee lookup, BTC transfer workflows, and optional Stacks, Pillar, inscription, identity, and paid API flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents broad authority over crypto funds, wallet keys, DeFi actions, paid APIs, and persistent identity flows. <br>
Mitigation: Use only when intentionally deploying an agent-controlled crypto wallet; start on testnet or with a dedicated low-balance wallet, keep wallets locked by default, and require explicit approval for every transfer, DeFi action, contract write or deploy, inscription, identity registration, and paid API call. <br>
Risk: Secrets such as imported seed phrases and PILLAR_API_KEY can authorize wallet or Pillar smart-wallet actions. <br>
Mitigation: Avoid importing valuable seed phrases, protect PILLAR_API_KEY as signing authority, and pin and audit the MCP server package before use. <br>


## Reference(s): <br>
- [AIBTC Bitcoin Wallet on ClawHub](https://clawhub.ai/whoabuddy/skills/aibtc-bitcoin-wallet) <br>
- [npm Package](https://www.npmjs.com/package/@aibtc/mcp-server) <br>
- [GitHub Repository](https://github.com/aibtcdev/aibtc-mcp-server) <br>
- [Agent Skills Specification](https://agentskills.io) <br>
- [Genesis Agent Lifecycle](references/genesis-lifecycle.md) <br>
- [Bitcoin Inscription Workflow](references/inscription-workflow.md) <br>
- [Pillar Smart Wallet](references/pillar-wallet.md) <br>
- [Stacks L2 DeFi](references/stacks-defi.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [x402 Inbox Flow](references/x402-inbox.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline examples, tool names, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require wallet credentials, network selection, and explicit approval for value-moving actions.] <br>

## Skill Version(s): <br>
1.26.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
