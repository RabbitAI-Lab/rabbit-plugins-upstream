## Description:

Guides an Execution Trader through approved Hyperliquid order, cancel, modify, leverage, and close actions with pre-send checks, single-send discipline, unknown-result handling, reconciliation, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External trading-desk operators and agent developers use this skill to turn a risk-approved, user-approved ticket into one Hyperliquid exchange action, then reconcile and report the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact exchange actions can place, modify, cancel, or close positions on an account.

Mitigation: Use only in a trading-desk setup where ticket, risk approval, user approval, and wallet-key handling processes are already in place.

Risk: Unknown send results can lead to duplicate or inconsistent exchange actions if retried.

Mitigation: Do not retry a send with an unknown result; reconcile by client order id, open orders, fills, and account state before any fresh approval.

Risk: Network, account, wallet, or formatting mistakes can send an action to the wrong target or create an invalid order.

Mitigation: Confirm network, account address, API wallet authority, live market data, order formatting, and rehearsal requirements before sending.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-execution-protocol)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, execution notes, and report instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approved ticket, risk approval, user approval, account checks, and wallet-key handling controls before high-impact exchange actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
