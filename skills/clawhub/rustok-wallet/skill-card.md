## Description: <br>
Self-custody Ethereum agent wallet that runs locally in Docker or Podman, keeps private keys on the user's machine, reads balances and DeFi positions, previews and executes ETH sends, and signs plain messages and EIP-712 typed data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[temrjan](https://clawhub.ai/user/temrjan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to give an agent access to a local self-custody Ethereum wallet for reading wallet state, reviewing balances and DeFi positions, previewing transactions, executing ETH sends, and signing messages. It is intended only for users who intentionally want an agent-accessible wallet and accept the risk of real funds under agent control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real self-custody wallet funds and has no hard-coded spending limits. <br>
Mitigation: Use it only for wallets funded with amounts the user is prepared to risk, call get_wallet_context first, preview every send, show the amount, destination, cost, and risk level, and execute only after explicit user approval. <br>
Risk: The HTTP signing gateway can be exposed over a network if the operator opts in. <br>
Mitigation: Keep the gateway loopback-only unless every caller is fully trusted, and protect any exposed gateway with an operator-managed API key and network controls. <br>
Risk: The EIP-712 sign_typed_data endpoint is not gated by RUSTOK_MCP_CAPABILITIES and can authorize approvals, permits, orders, or other fund-moving actions. <br>
Mitigation: Treat EIP-712 signing requests with the same scrutiny as transaction execution and do not rely on restricted MCP capabilities as read-only isolation for callers that can reach the gateway. <br>
Risk: Loss or exposure of the recovery phrase, wallet volume, or keyring password can compromise funds. <br>
Mitigation: Back up the 12-word recovery phrase offline, never place the keyring password in MCP configuration or shell history, and use the documented secret or password-file approach. <br>


## Reference(s): <br>
- [Rustok MCP homepage](https://github.com/rustok-org/mcp) <br>
- [Rustok Wallet ClawHub listing](https://clawhub.ai/temrjan/skills/rustok-wallet) <br>
- [temrjan ClawHub publisher profile](https://clawhub.ai/user/temrjan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include wallet setup, MCP configuration, transaction preview and execution flow, signing guidance, and troubleshooting steps.] <br>

## Skill Version(s): <br>
0.4.9 (source: SKILL.md frontmatter, claw.json, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
