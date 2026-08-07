## Description:

DeFi Diligence screens Base and Solana tokens by symbol or contract address and returns PASS/WATCH/FLAG risk verdicts with scored checkpoints and an x402 payment path for the full report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trdyqs6bsr-lksnf](https://clawhub.ai/user/trdyqs6bsr-lksnf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to perform pre-buy token risk checks on Base or Solana assets using a symbol or contract address. It is intended to provide risk verdicts and checkpoint data, not price targets or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An x402-enabled agent could sign or send a real USDC payment without enough explicit user approval.

Mitigation: Require the agent to show the chain, amount, recipient or challenge, and request details, then obtain explicit user approval before any payment is signed or sent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trdyqs6bsr-lksnf/skills/defi-diligence)
- [Service homepage](https://crypto-api-blush.vercel.app)
- [OpenAPI schema](https://crypto-api-blush.vercel.app/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [JSON API responses and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PASS/WATCH/FLAG verdicts and scored token-risk reports; full reports require an x402 USDC payment flow.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
