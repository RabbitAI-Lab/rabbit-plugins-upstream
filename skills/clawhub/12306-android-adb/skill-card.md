## Description:

Guides agents through booking train tickets in the 12306 Android app using USB ADB and OCR-assisted navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and their authorized agents use this skill to navigate the 12306 Android app, select a train and passenger, and submit a ticket order after user confirmation. The traveler completes payment manually.

### Deployment Geography for Use:

Global (for train travel in China)

## Known Risks and Mitigations:

Risk: ADB grants the agent control of a connected phone during a live ticket-booking flow.

Mitigation: Use only with the traveler's explicit request and confirm the train, route, date, seat, passenger, and price before submitting the order; keep payment manual.

Risk: Clipboard-based Chinese input may expose copied contents to other apps.

Mitigation: Do not put passwords, payment details, or other secrets on the clipboard.

## Reference(s):

- [12306 Android Adb on ClawHub](https://clawhub.ai/openlittlebear/skills/12306-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the separately installed appium-android-adb skill, a connected Android phone, and a logged-in 12306 app.]

## Skill Version(s):

2.2.4 (source: server-resolved release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
