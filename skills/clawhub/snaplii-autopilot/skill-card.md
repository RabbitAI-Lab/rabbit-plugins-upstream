## Description:

Helps an agent buy a Snaplii gift card, redeem it through a browser, and complete a merchant or delivery order.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers use this skill to have an agent purchase a prepaid Snaplii gift card, redeem it at a merchant or delivery site, and prepare or place their order using browser automation.

### Deployment Geography for Use:

United States and Canada (subject to account and merchant availability)

## Known Risks and Mitigations:

Risk: The skill may spend prepaid funds on gift cards without fresh per-transaction confirmation, before final merchant checkout approval.

Mitigation: Review this behavior before installation; use a narrowly scoped Snaplii API key with a low daily spending limit and monitor purchases.

Risk: The skill handles Snaplii credentials and gift-card redemption codes while automating checkout.

Mitigation: Use secure credential entry, avoid sharing redemption codes in chat, and confirm the order summary before final checkout.

## Reference(s):

- [Snaplii Autopilot on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-autopilot)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Conversational text with order summaries and redemption guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report purchased gift-card details and merchant order confirmation.]

## Skill Version(s):

1.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
