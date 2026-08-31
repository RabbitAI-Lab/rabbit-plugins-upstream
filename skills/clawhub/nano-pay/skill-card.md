## Description:

nano-pay helps agents pay x402-priced HTTP APIs with feeless Nano micropayments from a self-custodied local wallet, including quote, payment, transfer, top-up, faucet-claim, and merchant endpoint workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[glennquinting](https://clawhub.ai/user/glennquinting)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill when an agent needs to quote, fund, send, receive, or pay for HTTP 402 API access using Nano. It also supports small-wallet merchant workflows for agents that expose paid endpoints to other agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment, transfer, and swap commands can trigger real financial actions.

Mitigation: Quote before paying or topping up, review prices and destinations, and keep only limited working funds in the wallet.

Risk: Wallet seeds and NanSwap API keys are sensitive credentials.

Mitigation: Protect ~/.nano-pay/wallet.json and any NANSWAP_API_KEY, avoid printing or committing secrets, and restrict wallet contents to small operational balances.

Risk: Nano payments and swap activity can be irreversible.

Mitigation: Treat balance and ledger state as authoritative, verify command results before retrying, and avoid relying on protocol-level refunds.

## Reference(s):

- [ClawHub nano-pay skill page](https://clawhub.ai/glennquinting/skills/nano-pay)
- [feeless402 reference endpoint](https://feeless402.com)
- [x402nano facilitator](https://www.x402nano.org/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command-output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are expected to print JSON; payment commands can perform real Nano transfers or swap orders when executed.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
