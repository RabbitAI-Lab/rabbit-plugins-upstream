## Description:

PayPal (paypal.com) skill for reading, creating, and updating PayPal data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an OOMOL-connected PayPal account use this skill to inspect live action schemas and run PayPal account, order, payment, refund, shipment tracking, balance, and transaction-history actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment-changing PayPal actions can create orders, capture funds, issue refunds, void authorizations, or update shipment tracking without sufficient confirmation.

Mitigation: Require explicit user confirmation of the exact action, target account or transaction, payload, and expected effect before every state-changing PayPal command.

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Independently verify the installer source and integrity before running remote install commands; prefer a reviewed installation path when available.

Risk: The skill depends on a PayPal account and OOMOL connection selected by the user.

Mitigation: Use only PayPal and OOMOL accounts the user intentionally trusts, and stop when authentication, scope, credential, or billing errors indicate the connection is not ready.

## Reference(s):

- [ClawHub PayPal skill page](https://clawhub.ai/oomol/skills/oo-paypal)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [PayPal homepage](https://www.paypal.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema inspection commands, connector run commands, and concise operational guidance.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
