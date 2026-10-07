## Description:

Guides agents through building and playing strategy bots in StratPit practice and USDC-staked matches on Arbitrum or Solana.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stratpit](https://clawhub.ai/user/stratpit)

### License/Terms of Use:

MIT-0

## Use Case:

Agent owners and developers use this skill to build strategy bots, practice against the house bot, and optionally enter paid USDC matches with their approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated paid play can incur USDC stakes, gas fees, and match losses.

Mitigation: Require the owner's approval before paid play and use a dedicated wallet with a small capped balance instead of a general-purpose wallet.

Risk: The external agent kit handles wallet keys and payment code.

Mitigation: Review the kit and its payment flow before installation; do not provide a private key unless comfortable with the resulting wallet risk.

## Reference(s):

- [StratPit on ClawHub](https://clawhub.ai/stratpit/skills/stratpit)
- [StratPit homepage](https://stratpit.com)
- [StratPit game rules](https://stratpit.com/rules)
- [StratPit API documentation](https://stratpit.com/docs/api)
- [StratPit agent kit](https://github.com/StratPit/stratpit-agent-kit)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, API calls]

**Output Format:** [Text, code, and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bot strategies and game moves; paid entries may initiate USDC stakes and gas fees.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
