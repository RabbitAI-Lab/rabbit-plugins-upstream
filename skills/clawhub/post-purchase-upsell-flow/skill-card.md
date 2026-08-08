## Description:

Design and implement one-click post-purchase upsells and downsells that raise average order value without hurting the main conversion rate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonnel](https://clawhub.ai/user/autonnel)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to design, measure, and implement one-click post-purchase upsell, cross-sell, and downsell flows after checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The implementation guidance touches Docker setup and payment-provider flows that involve saved payment methods, off-session charges, and refund handling.

Mitigation: Review the referenced project's docker-compose.yml, run it in an appropriate local environment, and validate payment accept, decline, authentication, and refund paths before sending traffic.

## Reference(s):

- [Post-Purchase Upsell Flow on ClawHub](https://clawhub.ai/autonnel/skills/post-purchase-upsell-flow)
- [Autonnel repository](https://github.com/autonnel/autonnel)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with explanatory tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes implementation guidance for payment, order, refund, and measurement workflows.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
