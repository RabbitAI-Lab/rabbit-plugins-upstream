## Description:

Guides an agent through purchasing products in the Pinduoduo Android app using USB ADB, including product selection, payment, and group-buy completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to shop on Pinduoduo can follow this workflow to find and verify a product, confirm an order, complete payment with user participation, and finish the group-buy flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect listing, quantity, price, shop, or payment method could lead to an unintended purchase.

Mitigation: Require the user's explicit purchase request and confirm the product, specification, quantity, price, shop, and payment method before submitting the order.

Risk: Wallet payment exposes sensitive authentication steps.

Mitigation: Request the PIN only at payment time, use it only for that payment, and leave fingerprint or face verification to the user.

Risk: Cached screenshots may contain personal or payment-related information.

Mitigation: Review and clear the companion skill's OCR screenshot cache when sensitive screens may have been captured.

## Reference(s):

- [Pdd Android Adb on ClawHub](https://clawhub.ai/openlittlebear/skills/pdd-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the separately installed appium-android-adb base skill and a connected Android device.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
