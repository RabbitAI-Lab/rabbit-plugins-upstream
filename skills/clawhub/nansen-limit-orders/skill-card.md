## Description:

Guides price-triggered trading with native Solana limit orders and settlement alerts for other chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and their agents use this skill to create, review, update, and cancel Solana limit orders, or set up best-effort settlement alerts for orders placed on other chains.

### Deployment Geography for Use:

Global, subject to applicable sanctions and geographic restrictions.

## Known Risks and Mitigations:

Risk: Trading commands can place, modify, or cancel real orders and require wallet signing.

Mitigation: Review the wallet, tokens, amount, trigger price, slippage, and expiry before approving commands or signatures.

Risk: Settlement alerts can miss fills or match unrelated transfers, and notifications may reach an unintended destination.

Mitigation: Verify the alert filters and notification destination, and check order status on the trading venue.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-limit-orders)
- [Nansen CLI package](https://www.npmjs.com/package/nansen-cli)
- [Nansen CLI repository (linked in skill)](https://github.com/nansen-ai/nansen-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Order details and settlement-alert guidance; alerts are not authoritative fill tracking.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
