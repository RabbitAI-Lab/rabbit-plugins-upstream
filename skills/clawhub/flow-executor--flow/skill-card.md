## Description:

Provides agents with paid Base swap quotes, contract safety verdicts, and smart-wallet trading signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flow-executor](https://clawhub.ai/user/flow-executor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents evaluating Base trades can request swap quotes, contract safety assessments, and smart-wallet signals before acting; paid calls use USDC on Base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned external code that manages a local wallet and signs automatic payments.

Mitigation: Review the publisher and package provenance before installing; prefer a pinned version or verified source.

Risk: Automatic USDC payments can spend funds held in the local wallet within configured caps.

Mitigation: Fund the wallet with only a small amount you can afford to lose and inspect the wallet and spend ledger regularly.

## Reference(s):

- [Flow skill release](https://clawhub.ai/flow-executor/skills/flow)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured API responses with plain-language assessments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Swap quotes include a liquidity flag and expiry window; wallet signals flag stale data.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
