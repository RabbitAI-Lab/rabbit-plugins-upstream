## Description:

Helps agents buy Snaplii gift cards, redeem them through a browser, and place merchant or delivery orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

People use this skill to have an agent purchase a prepaid Snaplii gift card, redeem it on a merchant or delivery site, and complete an order with browser automation. It requires Snaplii access and a browser-control tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend a user's prepaid balance on gift cards without transaction-specific confirmation.

Mitigation: Use a narrowly scoped API key with a low spending limit and require explicit confirmation before every gift-card purchase.

Risk: An automated merchant order can incur additional charges or go to the wrong address.

Mitigation: Verify the delivery address and full order total, then obtain explicit confirmation before placing the final order.

## Reference(s):

- [Snaplii Autopilot on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-autopilot)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with order summaries and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report purchase, order, and cashback details; gift-card redemption codes and PINs are sensitive.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
