## Description:

Provides pay-per-call crypto trading signals with entry, stop-loss, take-profit, and risk-reward data for automated AI trading via USDC payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect an agent to a paid x402-style crypto signals API that returns trading direction, entry, stop-loss, take-profit, and risk-reward fields. It is intended for automated workflows that can explicitly approve payment and handle financial-risk disclosures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says this is a financial workflow that routes payment and API-key use over plain HTTP.

Mitigation: Use only with explicit user approval for payment, avoid sending API keys or transaction details over unsecured HTTP, and prefer a secure transport before production use.

Risk: The security guidance says advertised crypto-trading results should be treated as unverified financial claims rather than guarantees.

Mitigation: Present signal results as unverified inputs, require user review before trading action, and avoid representing past performance as expected profit.

Risk: The artifact describes paid per-call access and API-key issuance after payment.

Mitigation: Require clear spend limits, transaction confirmation, and key-handling controls before an agent attempts purchase or retrieval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/northcap-x402-api)
- [Publisher profile](https://clawhub.ai/user/mohamedabdisamed)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with HTTP endpoint descriptions and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit payment approval and an issued API key before fetching paid signal data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
