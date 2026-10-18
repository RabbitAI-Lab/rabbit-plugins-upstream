## Description:

Guides an agent through buying a Snaplii gift card, redeeming it in a merchant browser session, and placing an order with user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers use this skill to purchase a Snaplii gift card with cashback, redeem it on a merchant or delivery site, and complete an order through browser automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication instructions hidden in a Markdown comment can initiate account connection and access payment capabilities.

Mitigation: Review the hidden Auth section before connecting and use a Snaplii API key with minimal permissions and an appropriate spending limit.

Risk: Buying a gift card charges the user's prepaid balance before the merchant order is placed.

Mitigation: Check the brand, quoted amount, available balance, and user's approval before purchase; never repeat a purchase with an unclear outcome without checking card history.

Risk: Browser ordering can expose redemption credentials or place an order with the wrong delivery details.

Mitigation: Keep redemption codes private, verify the delivery address and full order summary, and require explicit confirmation before the final pay button.

## Reference(s):

- [Snaplii Autopilot on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-autopilot)
- [Publisher profile](https://clawhub.ai/user/snapliiai)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown with order summaries and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report a redemption code to the user only when requested or when browser ordering cannot continue.]

## Skill Version(s):

1.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
