## Description:

AI-native lending on Base MAINNET for autonomous agents. Check credit, request USDC loans (EIP-712 signed), and repay autonomously. Real money.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rsoft-latam](https://clawhub.ai/user/rsoft-latam)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous-agent operators use this skill to check creditworthiness, request signed USDC loans, track loan status, and repay loans on Base mainnet. It is intended for agents that can use wallet-based payments and understand real-money lending consequences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent request and repay real USDC loans on Base mainnet.

Mitigation: Install only for real-money lending use cases, review every loan amount before signing, and use a wallet with limited funds.

Risk: Incorrect repayment details could create loss, failed repayment, or default consequences.

Mitigation: Verify the destination address, exact repayment amount, request ID, transaction hash, and repayment endpoint before running commands.

Risk: A signature request authorizes loan origination from the borrowing wallet.

Mitigation: Inspect every EIP-712 signing payload and deadline before signing with the wallet private key.

## Reference(s):

- [RSoft Agentic Bank homepage](https://rsoft-agentic-bank.com/)
- [RSoft Agentic Bank docs](https://rsoft-agentic-bank.com/docs)
- [ClawHub skill page](https://clawhub.ai/rsoft-latam/skills/rsoft-agentic-bank)
- [BaseScan](https://basescan.org/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can call external lending APIs and on-chain payment tools; review before execution.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
