## Description:

Operates PayPal through an OOMOL-connected account for reading account data, creating orders, authorizing or capturing payments, issuing refunds, voiding authorizations, and managing shipment tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform PayPal account, order, payment, refund, authorization, transaction, and shipment-tracking workflows through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Money-moving or state-changing PayPal actions may be under-labeled, including captures, refunds, voids, order creation, and tracking changes.

Mitigation: Require explicit user confirmation of the exact action, target, amount, and payload before running any PayPal command that can move funds or change account state.

Risk: Untagged actions may be treated as safe reads even when the security summary indicates some write behavior is not consistently labeled.

Mitigation: Treat untagged PayPal actions as not automatically safe until the action list is corrected and reviewed.

## Reference(s):

- [ClawHub PayPal skill page](https://clawhub.ai/oomol/skills/oo-paypal)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [PayPal homepage](https://www.paypal.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PayPal action results as JSON returned by the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
