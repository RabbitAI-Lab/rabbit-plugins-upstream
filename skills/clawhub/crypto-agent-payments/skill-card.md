## Description: <br>
Create and manage ERC20-compatible wallets, transfer and swap tokens across supported chains, enable agent payments, and configure optional referrer fees. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nicofains1](https://clawhub.ai/user/nicofains1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to connect agents to the OnlySwaps MCP server for wallet creation, portfolio checks, token transfers, swaps, and agent-to-agent payments. It is suited to low-value operational payment workflows such as rewards, bug bounties, and automated payouts where users can review transactions before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects agents to an unpinned external payment tool that can access raw crypto private keys and execute fund-moving actions. <br>
Mitigation: Install only if the OnlySwaps MCP server is trusted; use a new low-balance wallet, avoid main or high-value private keys, and consider pinning and reviewing the MCP package before use. <br>
Risk: Transfers, swaps, approvals, slippage settings, chain selections, and referral fees can move funds or increase transaction costs if configured incorrectly. <br>
Mitigation: Verify every recipient, chain, amount, approval, slippage value, and referral fee before execution, and start with small test transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nicofains1/skills/crypto-agent-payments) <br>
- [@onlyswaps/mcp-server on npm](https://www.npmjs.com/package/@onlyswaps/mcp-server) <br>
- [OnlySwaps documentation](https://onlyswaps.fyi) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet setup, quote, portfolio, transfer, swap, and referrer fee examples; wallet operations require an agent-accessible private key.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
