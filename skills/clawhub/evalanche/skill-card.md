## Description:

Helps agents manage multi-chain EVM wallets, interact with contracts, and perform payments, swaps, bridging, trading, and Avalanche administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ijaack](https://clawhub.ai/user/ijaack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Evalanche to connect autonomous agents to EVM wallets and on-chain services, including transfers, DeFi operations, market orders, and Avalanche network management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous wallet access can move funds through transfers, swaps, bridges, market orders, and leveraged trades.

Mitigation: Start with a fresh low-balance wallet and testnets or small limits; require manual approval for value-bearing actions.

Risk: Persistent wallet keys and external command execution can expose signing authority.

Mitigation: Isolate the runtime, protect or avoid persistent keystores, and pin external CLI paths.

Risk: Proxy upgrades and validator or subnet administration can make lasting changes.

Mitigation: Require manual approval before any upgrade or network administration action.

## Reference(s):

- [Evalanche on ClawHub](https://clawhub.ai/ijaack/skills/evalanche)
- [Project homepage listed in skill metadata](https://github.com/iJaack/evalanche)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown, with code and commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or initiate wallet and blockchain actions when granted access.]

## Skill Version(s):

1.14.0 (source: server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
