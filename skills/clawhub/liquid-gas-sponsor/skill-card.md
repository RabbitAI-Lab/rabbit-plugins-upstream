## Description:

Send any transaction on Base with a wallet that holds USDC but no ETH. Pay the gas per operation in USDC over x402 (from $0.03) through an ERC-4337 paymaster; one endpoint for smart-wallet SDKs and plain wallets. No account, no API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leftychris13](https://clawhub.ai/user/leftychris13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route Base transactions through a USDC-paid gas sponsorship flow when a wallet has USDC but no ETH. It guides plain wallets and ERC-4337 smart-wallet SDKs through quoting, payment, signing, and submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet or client signatures may approve an unintended destination contract call, x402 USDC payment amount, paymaster or delegate address, expiry, or EIP-7702 authorization.

Mitigation: Review the transaction, payment, paymaster or delegate, expiry, and any EIP-7702 authorization before signing; simulate higher-value transactions first.

Risk: The sponsorship fee is taken at sponsorship time, so an on-chain operation that later fails can still consume the quoted USDC payment.

Mitigation: Build and simulate calls before requesting sponsorship, especially for higher-value or complex contract interactions.

Risk: Quotes and sponsorships expire after a short validity window.

Mitigation: Submit signed operations before the returned validity deadline or request a fresh quote.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/leftychris13/skills/liquid-gas-sponsor)
- [Liquid Agent gas sponsor API](https://api.liquidagent.ai/v1/gas)
- [Liquid Agent gas sponsor stats](https://api.liquidagent.ai/v1/gas/stats)
- [Gasless Base transaction example](https://github.com/LiquidAgent/liquidagentx402/blob/main/examples/gasless.js)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for command examples; no API key is described.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
