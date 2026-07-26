## Description: <br>
Create and manage USDC escrows for agent-to-agent payments on Base Sepolia with batch operations and dispute resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[droppingbeans](https://clawhub.ai/user/droppingbeans) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to create, inspect, release, cancel, dispute, and batch-manage USDC escrows for agent-to-agent services on Base Sepolia. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet keys, contract calls, and USDC approvals can expose funds if used in an untrusted agent environment. <br>
Mitigation: Use a dedicated Base Sepolia test wallet, keep allowances minimal, and never paste a valuable private key into shared code or an untrusted agent environment. <br>
Risk: Incorrect contract or token addresses, receivers, amounts, deadlines, or escrow IDs can create unintended transactions. <br>
Mitigation: Verify contract and token addresses, simulate or review transactions before signing, and confirm escrow parameters before execution. <br>


## Reference(s): <br>
- [Trust Escrow ClawHub page](https://clawhub.ai/droppingbeans/skills/trust-escrow) <br>
- [Trust Escrow web app](https://trust-escrow-web.vercel.app) <br>
- [Agent docs](https://trust-escrow-web.vercel.app/agent-info) <br>
- [Integration guide](https://trust-escrow-web.vercel.app/skill.md) <br>
- [Base Sepolia contract](https://sepolia.basescan.org/address/0x6354869F9B79B2Ca0820E171dc489217fC22AD64) <br>
- [llms.txt](https://trust-escrow-web.vercel.app/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with TypeScript code examples and contract configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Base Sepolia contract, USDC, RPC, and workflow details for escrow transactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
