## Description:

MENTAT guides agents through token swaps using Base escrow, signed CoW orders, and Wagyu-routed XMR trades, with settlement evidence for each path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agora0x](https://clawhub.ai/user/agora0x)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use MENTAT to request token-swap quotes, prepare or submit trades, and track settlement across Base escrow, CoW Protocol, and an XMR route.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid quotes and trade execution can incur fees or move funds.

Mitigation: Check addresses, amounts, fees, and payment terms before authorizing a quote, signature, deposit, or trade.

Risk: CoW orders require a signature from the trader's wallet.

Mitigation: Review the full order and signed data before signing with your own wallet.

Risk: The XMR route relies on Wagyu as a settlement counterparty and is not trustless.

Mitigation: Assess counterparty risk and use the created order's exact deposit address, amount, and expiry rather than a quote to fund it.

## Reference(s):

- [MENTAT homepage](https://mentat.market)
- [MENTAT agent card](https://api.mentat.market/.well-known/agent.json)
- [ClawHub skill listing](https://clawhub.ai/agora0x/skills/mentat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON responses]

**Output Format:** [Markdown with curl examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes and orders describe settlement paths, route legs, and available transaction proofs.]

## Skill Version(s):

1.4.5 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
