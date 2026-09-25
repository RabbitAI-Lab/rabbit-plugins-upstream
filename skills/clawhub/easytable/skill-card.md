## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check easyTable restaurant availability, find existing bookings by mobile number, and create, modify, or cancel table reservations through the user's browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, modify, and cancel actions can change real restaurant reservations.

Mitigation: Require user confirmation and show the reservation preview before submitting any write action.

Risk: Modifying a booking can clear email, comment, or company fields if the user does not provide them.

Mitigation: Ask the user for the current email, comment, and company values, pass them through unchanged when appropriate, and only clear a field intentionally.

Risk: The skill depends on the user's browser session through the fetchproxy extension and an open easyTable booking tab.

Mitigation: Use only with a loaded easyTable booking tab and install the extension only when the user accepts that browser-session dependency.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [guidance, configuration]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup guidance, tool-use flow, and confirmation requirements for reservation write actions.]

## Skill Version(s):

1.2.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
