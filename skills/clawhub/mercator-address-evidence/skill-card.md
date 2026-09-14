## Description:

MERCATOR Address Evidence helps an agent verify whether an entity's own published source and an independent chain source support a candidate contract address and chain before transaction use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arzuo](https://clawhub.ai/user/arzuo)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to check a candidate crypto contract address against the entity's published source and an independent chain source before sending a transaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls send inputs to an external MERCATOR API and can spend $0.25 USDC through the user's x402 setup.

Mitigation: Use the free validate route first, confirm the 402 payee, asset, chain, and price, and only provide X_PAYMENT when MERCATOR_BASE_URL is the intended trusted endpoint.

Risk: A PASS result confirms provenance for an intended target, not that the contract is safe, audited, or unable to take funds.

Mitigation: Treat the result as address provenance only and perform separate contract, deployer, upgradeability, and transaction-risk review before use.

Risk: The skill can return UNRESOLVED when the entity has no reachable published address source or when sources disagree.

Mitigation: Do not guess or transact from an unresolved result; require accessible entity-published evidence and independent support for important actions.

Risk: Self-published-only evidence can be weaker because a compromised project page may publish a malicious address.

Mitigation: Inspect confidence and self_published_only fields and require independent corroboration for high-value or irreversible transactions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arzuo/skills/mercator-address-evidence)
- [MERCATOR Address Evidence API](https://mercator-entity-evidence.fly.dev)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with curl examples and JSON response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use MERCATOR_BASE_URL and X_PAYMENT; the paid route is $0.25 USDC on Base and a free validate route is available.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
