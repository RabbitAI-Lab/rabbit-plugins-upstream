## Description:

Fetches crypto Fear & Greed and market sentiment data through a paid x402 API call so agents can factor sentiment into trading-timing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading automation agents use this skill to request crypto sentiment data before considering entries or filtering FOMO-driven trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each sentiment request is a paid x402 call.

Mitigation: Run the skill only when a fresh sentiment check is needed and confirm expected x402/USDC costs before use.

Risk: The configured X402_API_KEY is sent to the selected sentiment endpoint.

Mitigation: Use only endpoints you control or trust, keep the key in the environment, and avoid committing or logging it.

Risk: Allowing HTTP can expose a payment-capable API key outside a secure local test environment.

Mitigation: Keep X402_BASE on HTTPS and enable X402_ALLOW_HTTP only for intentional local testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/crypto-sentiment-pulse)
- [Publisher profile](https://clawhub.ai/user/mohamedabdisamed)
- [x402 API reference](https://github.com/MohamedAbdisamed/x402-api)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration guidance]

**Output Format:** [JSON printed to stdout with a brief paid-call warning.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, network access, X402_API_KEY, and optionally X402_BASE; each run may incur x402/USDC charges.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
