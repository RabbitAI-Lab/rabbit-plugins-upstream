## Description:

Earning and trading in Structs — selling energy via providers, buying capacity via agreements, allocations, reactor staking economics, the guild Central Bank (mint/redeem/convert), and token transfers. Use when you want to monetize surplus energy, shop for an energy agreement, set provider pricing, stake Alpha into a reactor for capacity, mint/redeem/convert guild tokens, or send tokens. For just keeping your own structs powered, see structs-energy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and agent operators use this skill to plan and execute commerce workflows for selling or buying energy, managing provider agreements, staking Alpha into reactors, using guild Central Bank conversions, and transferring tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed commerce transactions can spend, stake, transfer, lock, or convert in-game assets irreversibly or with cooldowns and penalties.

Mitigation: Use interactive signing and verify provider rates, denominations, validator addresses, destination addresses, slippage limits, agreement duration, and capacity before broadcast.

Risk: Agreement costs are paid upfront in the provider's rate denomination, and users with only ualpha may fail broadcasts when a guild token is required.

Mitigation: Check the provider rateDenom and acquire the required token before opening an agreement.

Risk: Token transfers and reactor migrations depend on exact recipient or validator addresses, with no practical undo after signing.

Mitigation: Confirm addresses from trusted queries and treat transfers to new addresses or validator migrations as high-review actions.

## Reference(s):

- [Structs commerce skill page](https://clawhub.ai/abstrct/skills/structs-commerce)
- [Structs energy skill](https://structs.ai/skills/structs-energy/SKILL)
- [Structs conventions](https://structs.ai/skills/conventions)
- [Energy mechanics](https://structs.ai/knowledge/mechanics/energy)
- [Energy market](https://structs.ai/knowledge/economy/energy-market)
- [Guild banking](https://structs.ai/knowledge/economy/guild-banking)
- [Structs guild skill](https://structs.ai/skills/structs-guild/SKILL)
- [Structsd install skill](https://structs.ai/skills/structsd-install/SKILL)
- [Economy valuation](https://structs.ai/knowledge/economy/valuation)
- [Trading](https://structs.ai/knowledge/economy/trading)
- [Late-game playbook](https://structs.ai/playbooks/phases/late-game)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and command tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require structsd on PATH, TX_FLAGS conventions, and an interactive signing key.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
