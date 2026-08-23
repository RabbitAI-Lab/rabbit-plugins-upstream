## Description:

Bind a buyer-owned response contract to an agent payment decision and validate the settled output before accepting delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[epistemedeus](https://clawhub.ai/user/epistemedeus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when evaluating paid API, HTTP 402, x402, MPP, MCP, or machine-commerce responses that must satisfy a buyer-owned output contract before acceptance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid delivery may be mistaken for valid output.

Mitigation: Keep settlement and output validation as separate receipt fields, and release the paid body downstream only after it passes the buyer-owned schema.

Risk: A changed or mutable schema could weaken the authorized buyer contract.

Mitigation: Bind the canonical schema digest into the authorization and require reauthorization whenever the local schema digest changes.

Risk: Wallet credentials, raw receipts, transaction bodies, signatures, or paid output could be exposed during reconciliation.

Mitigation: Pass only controlled match states into receipt-completeness checks and keep wallet credentials and transaction secrets outside this workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/epistemedeus/skills/agent-payment-policy)
- [ClawHub publisher profile](https://clawhub.ai/user/epistemedeus)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline JSON, JavaScript, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces buyer-contract validation guidance and local package commands; it does not create wallets, sign payments, choose facilitators, authorize spend, or handle credentials.]

## Skill Version(s):

0.15.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
