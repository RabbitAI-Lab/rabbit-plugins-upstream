## Description:

Helps users check easyTable restaurant availability and create, change, or cancel reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People booking restaurants through easyTable can check available areas, dates, and times, then create, change, or cancel a reservation with their approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The booking flow depends on the ContextMint Bridge browser extension and uses guest details such as name and mobile number in the open booking tab.

Mitigation: Install the extension only if trusted and confirm the guest details and restaurant before proceeding.

Risk: Creating, modifying, or cancelling a booking could change the wrong reservation.

Mitigation: Review each reservation preview and approve only changes that match the user's intent.

Risk: Retrying after an uncertain booking response could create a duplicate reservation.

Mitigation: Look up bookings using the guest's mobile number before retrying.

Risk: Modifying a booking can clear existing email, comments, or company details.

Mitigation: Ask the user for existing details to retain and review any fields marked for clearing in the preview.

## Reference(s):

- [easytable skill listing](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability results and reservation previews; booking changes require user confirmation.]

## Skill Version(s):

1.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
