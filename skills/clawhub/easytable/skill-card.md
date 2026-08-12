## Description:

This skill helps users check availability and make, change, or cancel table reservations through easyTable booking widgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and reservation managers use this skill to inspect easyTable availability, find existing bookings by phone number, and create, modify, or cancel intended restaurant reservations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit reservation create, modify, or cancellation actions using the user's active browser session.

Mitigation: Review the dry-run preview and only confirm actions for restaurants and bookings the user intends to manage.

Risk: Confirmed create or modify actions depend on an open, loaded easyTable booking tab and a short-lived Turnstile token.

Mitigation: Keep the intended booking widget tab open when confirming; reload the tab and retry if token submission fails.

Risk: Finding, modifying, or cancelling bookings uses the phone number associated with an existing reservation.

Mitigation: Use only phone numbers and booking records the user is authorized to access or manage.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Text with structured reservation-tool results and dry-run previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes are confirm-gated before create, modify, or cancel actions are applied.]

## Skill Version(s):

0.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
