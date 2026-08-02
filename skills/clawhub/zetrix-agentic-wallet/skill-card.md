## Description: <br>
Gives an AI agent a Zetrix wallet to prove identity (x401), pay for resources (x402), obtain verifiable credentials, and set up a wallet holder account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zetrix](https://clawhub.ai/user/zetrix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent work with a Zetrix wallet for identity proofs, gated-resource payments, and verifiable credential issuance. It is intended for provisioned deployments where wallet secrets and spend limits are configured outside the chat session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a real wallet and spend real funds when configured on mainnet. <br>
Mitigation: Use testnet unless mainnet is intended, keep MAX_PAYMENT_AMOUNT low, and require explicit user intent before any paid action. <br>
Risk: The onboarding path may cause a sensitive HSM wallet password to pass through the agent. <br>
Mitigation: Provision accounts and HSM passwords through an out-of-band setup flow or secret store; do not paste passwords or private keys into chat. <br>
Risk: Wallet actions depend on a correctly provisioned external MCP server and tenant secrets. <br>
Mitigation: Install only after reviewing provisioning, pinned package version, required environment variables, and fail-closed spend-cap configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zetrix/skills/zetrix-agentic-wallet) <br>
- [Publisher profile](https://clawhub.ai/user/zetrix) <br>
- [Project homepage](https://github.com/Zetrix-Chain/zetrix-agentic-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API Calls, configuration, text] <br>
**Output Format:** [Markdown text with wallet, payment, identity-proof, and credential guidance; tool calls return structured data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include wallet addresses, DIDs, proof response headers, transaction hashes, credential IDs, payment amounts, and fetched resource bodies when returned by wallet tools.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
