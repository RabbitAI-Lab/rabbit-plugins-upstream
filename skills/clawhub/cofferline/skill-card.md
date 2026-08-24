## Description:

Cofferline helps agents manage on-chain treasury operations and Polymarket prediction-market risk through a non-custodial REST API with policy limits, delegated execution, payment handling, and ledger reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guscoffer](https://clawhub.ai/user/guscoffer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building autonomous agents use this skill to discover Cofferline endpoints, authenticate with a wallet, set spend and market-risk policies, manage funding and gas, submit policy-gated Polymarket limit orders, and produce audit statements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through high-impact wallet treasury and prediction-market operations.

Mitigation: Use dedicated wallets or funder accounts, set tight spend and market policies, and review each operation before granting or using delegated authority.

Risk: Cofferline may hold platform fee balances, pre-signed auto-topup authorizations, and optional venue credentials as enumerated exceptions to wallet non-custody.

Mitigation: Review the custody matrix and pricing manifest before use, keep prepaid balances limited, and revoke API keys, delegations, auto-topup authorizations, and venue credentials when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guscoffer/skills/cofferline)
- [Cofferline manifest](https://cofferline.com/.well-known/cofferline.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline HTTP examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses machine-readable discovery documents and live API endpoints; does not directly handle private wallet keys.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
