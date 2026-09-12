## Description:

Hyperliquid perps strategist: market scans, funding rates, position sizing, and user-signed EIP-712 order execution and cancellation with drawdown guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Hyperliquid perpetual futures markets, compare funding and technical signals, size positions, and prepare user-approved EIP-712 order or cancellation requests. It is intended for zero-custody workflows where every state-changing action requires current market evidence and explicit manual confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help submit real leveraged futures trades or cancellations.

Mitigation: Require fresh EIP-712 user signatures and immediate explicit confirmation for every state-changing request.

Risk: Leveraged futures trading can cause financial loss.

Mitigation: Verify order details, sizing, leverage metadata, stop levels, and builder fee terms before signing.

Risk: Credential confusion could lead users to expose sensitive wallet material.

Mitigation: Use FARMDASH_API_KEY only for FarmDash access tier and rate limits; never request or provide private keys, seed phrases, mnemonics, or wallet exports.

Risk: Stale analysis or mismatched delegated accounts can make execution unsafe.

Mitigation: Refresh analysis before execution and verify signer, account owner, nonce, expiry, and intent hash against the current request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical FarmDash Futures Strategist skill manual](https://www.farmdash.one/openclaw-skills/farmdash-futures-strategist/SKILL.md)
- [Agent integration documentation](https://www.farmdash.one/docs)
- [OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)
- [Live agent capability status](https://www.farmdash.one/api/v1/agent/status)
- [Fees and commercial terms](https://www.farmdash.one/fees)
- [Security and authority boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured JSON-compatible tool parameters and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce trading analysis, no-trade outcomes, EIP-712 signing instructions, and user-confirmed execution or cancellation request parameters; private keys and seed phrases are never required.]

## Skill Version(s):

1.0.25 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
