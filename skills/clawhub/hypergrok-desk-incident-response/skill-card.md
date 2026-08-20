## Description:

Provides a trading-desk incident response checklist for Hyperliquid issues such as unknown send results, unexpected fills or positions, unprotected positions, stuck orders, API outages, rate limiting, and suspected API wallet compromise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External trading-desk operators and agents use this skill to contain and reconcile Hyperliquid trading incidents, pause new risk, require approved tickets for corrective actions, and close incidents with review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live trading incident guidance can lead to financial harm if used outside a controlled desk process.

Mitigation: Use only with trade-only API wallets, secure secret storage, and the stated ticket approval and containment rules.

Risk: Operators may act on incomplete exchange state during outages, unknown send results, or rate limiting.

Mitigation: Pause new proposals, reconcile against the exchange record, and require fresh approval before any new send or containment action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-incident-response)
- [Hyperliquid info API endpoint](https://api.hyperliquid.xyz/info)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown checklist and incident-response playbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes containment steps, approval requirements, reconciliation checks, and incident review guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
