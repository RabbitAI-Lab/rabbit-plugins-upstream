## Description:

Less common Hyperliquid actions and their rules - dead-man's switch (scheduleCancel), TWAP orders, spot orders, expiresAfter and nonces, API wallet approval from code, sub-account and vault addressing, HIP-3 dexs, and what the desk deliberately does not do (transfers, withdrawals, builder fees, staking). Write actions are Execution Trader only, on an approved ticket. Use when a ticket asks for one of these or when a user asks whether the desk can.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents through advanced Hyperliquid trading workflows that require explicit approved execution tickets, including TWAPs, spot orders, dead-man's switches, sub-account or vault addressing, and related operational limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed Hyperliquid actions can have direct financial impact.

Mitigation: Require an approved execution ticket for every write action and verify each ticket before signing.

Risk: Main-wallet keys could be exposed if placed in the agent environment.

Mitigation: Keep main-wallet keys out of the agent environment and use the Hyperliquid app path for normal API wallet approval.

Risk: A triggered dead-man's switch cancels stops as well as open orders.

Mitigation: Re-arm protective stops after a dead-man's switch fires.

Risk: Parallel signing with one API wallet can cause nonce collisions and rejected actions.

Mitigation: Use one Execution Trader process per API wallet at a time.

## Reference(s):

- [HyperGrok Hyperliquid Advanced](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-advanced)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration]

**Output Format:** [Markdown with inline Python and TypeScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces trading workflow guidance only; write actions remain limited to approved execution tickets.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
