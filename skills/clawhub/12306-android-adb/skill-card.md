## Description:

Guides agents through booking train tickets in the 12306 Android app using a user-connected Android phone, OCR-based verification, and USB ADB interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide an agent through supervised 12306 train-ticket booking on an Android phone that is already installed and logged in. It covers station and date entry, train-list navigation, passenger selection, submit-order confirmation, and recovery from stale ticket data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ADB automation can control the connected Android phone and may expose personal travel or passenger information.

Mitigation: Use only after an explicit booking request, watch the phone during automation, and clean temporary screenshots or clipboard contents that may contain personal data.

Risk: Submitting an order can reserve a real ticket and move the user into a payment flow.

Mitigation: Require user confirmation of train, date, route, seat, price, and passenger before submit-order actions, and leave payment to the user on the phone.

Risk: OCR, WebView behavior, or stale ticket data can lead to wrong selections or expired-order errors.

Mitigation: Verify each critical screen with OCR before proceeding and re-query ticket data before rebooking after stale-data errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/openlittlebear/skills/12306-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline bash and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human supervision for login, submit-order confirmation, and payment.]

## Skill Version(s):

2.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
