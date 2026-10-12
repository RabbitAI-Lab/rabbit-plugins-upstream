## Description:

Guides a HyperGrok trading desk through bot roles, evidence standards, user approvals, and handoffs across research, testnet, and mainnet workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Trading desk operators and their agents use this skill to assign responsibilities, document market evidence, and coordinate risk review and user-approved trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exchange write could bypass chat-based approval and expose real funds.

Mitigation: Verify native user approval covers every exchange write route before enabling testnet or mainnet; otherwise remain research-only.

Risk: An overprivileged API wallet could permit withdrawals or transfers beyond trading.

Mitigation: Use trade-only API permissions; never grant withdrawal, transfer, or broad account authority.

## Reference(s):

- [HyperGrok Desk Operating Model on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-operating-model)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown and short text handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes proposal IDs, cited evidence, UTC timestamps, and next-owner handoffs when relevant.]

## Skill Version(s):

1.5.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
