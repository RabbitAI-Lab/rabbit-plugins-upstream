## Description:

Discover, issue, and manage an x402card wallet-owned virtual card through Base-USDC x402 payments, including capability checks, wallet authentication, idempotent card issuance, card status, balance, and secure credential reveal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elvismusli](https://clawhub.ai/user/elvismusli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to safely discover, issue, and manage wallet-owned virtual cards through x402 while preserving owner-controlled signing and credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent through wallet-authenticated payment and virtual-card issuance, including a 25 USDC payment with platform fees.

Mitigation: Confirm the payment amount, fees, and card economics before signing, and treat unknown settlement state as pending or operator review instead of initiating another payment.

Risk: The public installation path uses a remote install script.

Mitigation: Review the installer before running it, or prefer a source checkout or verified signed release when available.

Risk: Card credentials and wallet signing authority are sensitive if exposed through agent outputs or tools.

Mitigation: Use only a signer command controlled by the wallet owner, never request or store private keys or seed phrases, and reveal card credentials only to the controlling TTY or explicit clipboard flow.

## Reference(s):

- [x402card install](https://x402card.org/install)
- [x402card agent API](https://api.x402card.org/api/agent)
- [ClawHub skill page](https://clawhub.ai/elvismusli/skills/x402card-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment status, card status, balance checks, and credential-handling guidance; should not expose private keys, seed phrases, or card credentials in chat, logs, stdout, MCP, or files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
