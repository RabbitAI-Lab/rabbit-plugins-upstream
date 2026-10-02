## Description:

Helps users place specific physical-product orders through Axiom and check saved payment methods, order status, and receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[axiom-wallet](https://clawhub.ai/user/axiom-wallet)

### License/Terms of Use:

MIT-0

## Use Case:

People use Axiom to order clearly specified physical products through their saved Axiom payment method, check their payment method, and review order progress and receipts. The agent asks for missing product details before starting an order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can start real purchases using the user's saved payment method.

Mitigation: Start only clearly requested orders with a known merchant, exact product, and required options; use low spending limits and Axiom approval rules.

Risk: The OAuth troubleshooting fallback intercepts browser-opening commands and can capture authorization URLs.

Mitigation: Avoid the PATH-interception fallback unless its capture behavior is understood; prefer the standard authentication flow.

## Reference(s):

- [Axiom on ClawHub](https://clawhub.ai/axiom-wallet/axiom)
- [Authentication](references/authentication.md)
- [Worked examples](references/examples.md)
- [Axiom tool reference](references/tool-reference.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown text with purchase updates, approval links, and receipt details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only report an order as complete after Axiom confirms completion.]

## Skill Version(s):

0.2.2 (source: release metadata, VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
