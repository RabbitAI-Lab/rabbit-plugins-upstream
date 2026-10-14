## Description:

Guides an agent through user-authorized purchases in the Pinduoduo Android app on a connected phone, from product search and selection through payment and order completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

People who explicitly ask an agent to buy an item on Pinduoduo can use this skill to navigate the Android app, verify product details, and complete an approved purchase with user-provided payment authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could select the wrong product, shop, quantity, or price, or submit an unwanted purchase.

Mitigation: Use only for an explicit purchase request and obtain confirmation of product, shop, quantity, and price before submitting the order.

Risk: Payment authentication could be used without the buyer's intent.

Mitigation: Request payment credentials only when the buyer intends to pay; use the wallet PIN only for that payment and leave biometric verification to the buyer.

Risk: Cached screenshots may expose personal or payment information.

Mitigation: Review and clear cached screenshots when they may contain sensitive information.

## Reference(s):

- [Pdd Android Adb on ClawHub](https://clawhub.ai/openlittlebear/skills/pdd-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell command examples and purchase summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Purchase submission requires explicit user confirmation; biometric verification remains with the user.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
