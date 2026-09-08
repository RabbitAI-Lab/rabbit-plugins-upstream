## Description:

Analyzes Hyperliquid perpetual futures markets, account state, strategy sizing, and user-signed execution or cancellation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to research Hyperliquid perpetual futures markets, inspect account risk, size strategy proposals, and prepare user-approved signed execution or cancellation requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place or cancel real leveraged Hyperliquid futures trades while the top-level description says orders are preview-only.

Mitigation: Treat execution and cancellation as live financial actions; require fresh explicit user confirmation for every request and present trade details, leverage, fees, exposure, and cancellation impact before signing.

Risk: Persisted workflow ledger data may expose sensitive trading state without clear retention limits.

Mitigation: Keep workflow state isolated and short-lived unless a clear retention policy, access controls, and user expectations are in place.

Risk: Wallet or account setup could lead users to share private key material.

Mitigation: Never request, store, or transmit private keys, seed phrases, mnemonics, wallet exports, OAuth tokens, or raw wallet secrets; rely on per-request EIP-712 signing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical FarmDash Futures Strategist skill manual](https://www.farmdash.one/openclaw-skills/farmdash-futures-strategist/SKILL.md)
- [FarmDash OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash security and authority boundaries](https://www.farmdash.one/security)
- [FarmDash fees and commercial terms](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured JSON strategy objects and API request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include market analysis, account-risk summaries, position sizing, no-trade reasons, and user-confirmation prompts before signed execution or cancellation.]

## Skill Version(s):

1.0.23 (source: server release metadata; artifact metadata reports 3.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
