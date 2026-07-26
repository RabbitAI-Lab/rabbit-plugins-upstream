## Description: <br>
Earn yield on any Ethereum wallet on Base, Arbitrum, and Plasma using either a simple Base USDC Vault or a Zyfai Smart Wallet with automated yield optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldefi](https://clawhub.ai/user/pauldefi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect Ethereum wallets to Zyfai, compare Vault and Smart Wallet modes, and perform DeFi yield actions such as deposits, withdrawals, session-key setup, and profile updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent high-impact wallet and transaction authority for DeFi deposits, withdrawals, smart-wallet deployment, session keys, profile changes, cross-chain settings, and identity-registry actions. <br>
Mitigation: Require explicit user approval for each high-impact action and use only funds the user is willing to expose to DeFi risk. <br>
Risk: Wallet keys and Zyfai API keys could be exposed if handled directly by an agent or stored insecurely. <br>
Mitigation: Avoid raw private keys, prefer KMS or wallet-as-a-service controls, store API keys securely, and never print secrets in logs or generated output. <br>
Risk: Unpinned SDK or dependency versions can change transaction behavior or introduce supply-chain risk. <br>
Mitigation: Pin and verify package versions before installation and review generated transaction parameters before signing. <br>


## Reference(s): <br>
- [Zyfai SDK](https://sdk.zyf.ai) <br>
- [Zyfai Documentation](https://docs.zyf.ai) <br>
- [Zyfai SDK Demo](https://github.com/ondefy/zyfai-sdk-demo) <br>
- [Zyfai MCP Server](https://mcp.zyf.ai/mcp) <br>
- [Zyfai Agent Registration](https://www.zyf.ai/.well-known/agent-registration.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with TypeScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet setup, SDK method examples, API-key handling notes, DeFi transaction flows, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
