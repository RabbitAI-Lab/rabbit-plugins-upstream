## Description:

Helps agents book Shanghai hospital appointments through a WeChat service account using a connected Android phone, with a confirmation step before submission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

People requesting appointments at Shanghai hospitals can use an agent to navigate the booking flow, select a visit slot, and confirm the details before submitting a real appointment.

### Deployment Geography for Use:

Shanghai, China

## Known Risks and Mitigations:

Risk: ADB control can interact with the connected phone and submit a real medical appointment.

Mitigation: Use only for a user-requested booking; show the hospital, department, date, visit card, and fee, and obtain explicit confirmation before submission.

Risk: Booking screens, screenshots, and SMS codes may expose patient information.

Mitigation: Get the SMS code from the user and avoid retaining screenshots or logs containing patient details or codes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/openlittlebear/skills/hospital-android-adb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appointment details and booking status depend on the live hospital booking page.]

## Skill Version(s):

2.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
