## Description:

Guides agents through booking train tickets in the 12306 Android app using USB ADB and screen-reading workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can navigate the 12306 Android app to find trains, select passengers, and prepare or submit a ticket order after the user confirms the itinerary. The user logs in and completes payment on the phone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a logged-in 12306 session gives the agent control of the phone app.

Mitigation: Use only for an explicit booking request; keep login and device access under the user's control.

Risk: The agent can submit an order with the wrong train, date, route, seat, price, or passenger.

Mitigation: Show the complete itinerary and passenger to the user, and wait for confirmation before submitting; leave payment to the user.

Risk: Screenshots, UI dumps, or clipboard contents may expose personal information or secrets.

Mitigation: Do not paste secrets or store captures in shared locations; keep captures private and remove them when no longer needed.

## Reference(s):

- [12306 Android Adb on ClawHub](https://clawhub.ai/openlittlebear/skills/12306-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for confirming an order before submission; payment remains manual.]

## Skill Version(s):

2.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
