## Description:

PayPal (paypal.com) skill for reading, creating, and updating PayPal data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected PayPal account through OOMOL, including orders, authorizations, captures, refunds, tracking, balances, and transaction review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to change payment state in a connected PayPal account.

Mitigation: Require explicit user confirmation of the exact target, payload, and effect before order creation, authorization, capture, refund, void, or tracking updates.

Risk: The security guidance flags the pipe-to-shell installer path as unsafe.

Mitigation: Install the oo CLI through a verified, versioned, trusted channel where possible before using the skill.

Risk: Granting the agent access to a connected PayPal account can expose financial operations to unintended actions.

Mitigation: Review the skill before installation and use it only when the user is comfortable granting PayPal account access through the connected OOMOL account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-paypal)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [PayPal Homepage](https://www.paypal.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing PayPal actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
