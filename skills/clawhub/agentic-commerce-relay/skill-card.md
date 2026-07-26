## Description: <br>
Run the CCTP relay to burn USDC on a source chain and mint on a destination chain, returning verifiable receipts for multichain agent-to-agent settlement with optional Moltbook discovery and integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nativ3ai](https://clawhub.ai/user/nativ3ai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to prepare and run a CCTP-based USDC bridge workflow across supported chains, including required RPC, wallet, token, messenger, transmitter, domain, and amount configuration. It is intended for multichain agent-to-agent settlement workflows that need machine-readable burn, message, mint, and recipient receipt fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses a raw wallet private key that can authorize movement of real USDC. <br>
Mitigation: Inspect and pin the relay source, use a dedicated low-balance wallet, and require explicit approval for source chain, destination chain, recipient, amount, and fees before any transaction is signed. <br>
Risk: Incorrect contract addresses or CCTP domain IDs can route transactions incorrectly or fail settlement. <br>
Mitigation: Verify CCTP contract addresses and domain IDs against trusted sources for each chain before running the relay. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nativ3ai/skills/agentic-commerce-relay) <br>
- [Moltbook](https://www.moltbook.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON receipt fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied environment variables for RPC endpoints, wallet key, chain contracts, destination domain, and optional discovery settings.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
