## Description:

Helps an agent order user-requested physical products through Axiom and check saved payment methods, order status, and receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[axiom-wallet](https://clawhub.ai/user/axiom-wallet)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can request a specific physical product from a known merchant, check their saved Axiom payment method, or review their orders and receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clear purchase request can initiate a real order using the user's saved payment method, potentially without another chat confirmation when within approval limits.

Mitigation: Confirm the merchant, exact product, and required options before ordering; review Axiom spending rules, approval limits, and saved payment method before use.

Risk: Order access permits purchases and viewing order details.

Mitigation: Review requested account permissions before authorizing access, and relay approval requests for the user to decide in Axiom.

## Reference(s):

- [Axiom skill listing](https://clawhub.ai/axiom-wallet/skills/axiom)
- [Axiom homepage in skill metadata](https://clawhub.ai/axiom-wallet/axiom)
- [Authentication](references/authentication.md)
- [Tool reference](references/tool-reference.md)
- [Worked examples](references/examples.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown text with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include order updates, approval links, and receipt links returned by Axiom.]

## Skill Version(s):

0.3.1 (source: VERSION, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
