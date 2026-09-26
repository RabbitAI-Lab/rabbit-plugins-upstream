## Description:

Add liquidity, remove liquidity, or collect fees on Uniswap V2/V3/V4 pools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wpank](https://clawhub.ai/user/wpank)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to manage Uniswap liquidity positions, including adding liquidity, removing or partially removing positions, and collecting accrued fees with pool selection and safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger high-impact wallet transactions and the security evidence notes unclear final confirmation for adding liquidity.

Mitigation: Require the agent to show the exact pool, token amounts, approvals, range, gas estimate, and expected effects, then wait for explicit user confirmation before any transaction.

Risk: The security evidence warns against placing a high-value wallet private key in a project .env file.

Mitigation: Use a hardware wallet, managed signer, or dedicated low-balance wallet instead of storing a high-value private key in project configuration.

Risk: Mutable installation commands can change over time.

Mitigation: Install and review a pinned version before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wpank/skills/manage-liquidity)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transaction details, pool selection rationale, token amounts, range information, warnings, and explorer links.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
