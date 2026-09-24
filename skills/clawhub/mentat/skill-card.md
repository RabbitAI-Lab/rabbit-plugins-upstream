## Description:

MENTAT is an agent-native OTC trading venue that offers Base escrow, CoW Protocol relay, and an XMR route via Wagyu, with quote and order responses carrying settlement paths, route legs, and proofs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agora0x](https://clawhub.ai/user/agora0x)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use MENTAT to request OTC token quotes, create or relay trades, and check settlement status across escrow, CoW relay, and XMR routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DeFi trades can lose funds if an agent uses the wrong amount, address, fee, signature, or funding instruction.

Mitigation: Verify token amounts, destination addresses, fees, signatures, and deposit instructions before funding or submitting any order.

Risk: The XMR route is explicitly not trustless and depends on Wagyu as the settlement counterparty.

Mitigation: Use the XMR route only when that counterparty risk is acceptable, and review the returned route legs and proofs for each order.

## Reference(s):

- [MENTAT homepage](https://mentat.market)
- [MENTAT ClawHub skill page](https://clawhub.ai/agora0x/skills/mentat)
- [MENTAT agent card](https://floor-a2a-production.up.railway.app/.well-known/agent.json)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include settlement_path, route_legs, proofs, fees, order status, and route-specific funding or signing guidance.]

## Skill Version(s):

1.4.1 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
