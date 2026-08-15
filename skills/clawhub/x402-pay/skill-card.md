## Description:

Enables agents to discover x402-protected services, preview prices, fund a Base wallet, and make confirmed USDC micropayments for HTTP 402 resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pivortex](https://clawhub.ai/user/pivortex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an agent access paid x402 APIs while checking price, balance, wallet configuration, and transaction results. It is intended for workflows where human approval and wallet-level controls govern payment and funding actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend real USDC for paid API calls and wallet funding.

Mitigation: Use explicit command approvals, wallet-level spend limits, and preferably a dedicated low-balance wallet before approving payment or funding actions.

Risk: Payment or funding actions can target the wrong service, price, deposit address, refund destination, or transaction result if reviewed carelessly.

Mitigation: Review the service URL, decoded price, max-price cap, deposit address, refund destination, and transaction result before approving execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pivortex/skills/x402-pay)
- [Project homepage](https://github.com/NearDeFi/agent-payments-skill)
- [Detecting wallets](references/detecting-wallets.md)
- [Wallet flows](references/wallet-flows.md)
- [NEAR Intents funding](references/near-intents-funding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include decoded prices, wallet balances, payment commands, funding instructions, response bodies, and transaction hashes.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
