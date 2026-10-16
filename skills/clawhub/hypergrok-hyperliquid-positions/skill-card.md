## Description:

Helps a trading desk inspect Hyperliquid perpetual positions and margin, assess protection and liquidation risk, and perform ticket-approved leverage, margin, and closing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk staff use this skill to review Hyperliquid positions, margin, liquidation distance, and protective orders. Authorized Execution Traders can change leverage or isolated margin and close positions on approved tickets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trading actions could be taken without the intended authorization.

Mitigation: Restrict write actions to the Execution Trader role and require an approved ticket.

Risk: An action on the wrong network or with incorrect leverage or margin could cause financial loss.

Mitigation: Verify the selected network and live position details before changing leverage, isolated margin, or closing a position.

Risk: Order cleanup after a partial close could remove protection from the remaining position.

Mitigation: Confirm whether the position is fully closed before canceling orders; maintain a protective stop for any remainder.

## Reference(s):

- [HyperGrok Hyperliquid Positions on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-positions)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with Bash and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only assessments and ticket-gated trading actions.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata; bundled skill frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
