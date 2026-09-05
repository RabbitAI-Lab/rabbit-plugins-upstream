## Description:

Guides an agent through buying products in the Pinduoduo Android app over USB ADB using uiautomator2, OCR, and accessibility-tree checks for search, specification selection, payment handoff, and post-payment group-buy completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate the Pinduoduo Android app for a user-requested purchase while preserving explicit checkout confirmation and user participation in payment verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent control of a shopping app can place orders or select the wrong product, specification, quantity, shop, or price if used without review.

Mitigation: Use only after an explicit purchase request and confirm product, specification, quantity, shop, and price before order submission.

Risk: Payment requires sensitive wallet credentials and biometric verification.

Mitigation: Request the wallet PIN only at payment time, use it only to tap the on-screen keypad, and leave fingerprint or face verification to the user.

Risk: OCR screenshots may contain personal data.

Mitigation: Store screenshots only in the private cache path described by the skill and clear the cache periodically when it may contain personal data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/openlittlebear/skills/pdd-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational checkpoints for user consent, payment handoff, and OCR/accessibility-tree verification.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
