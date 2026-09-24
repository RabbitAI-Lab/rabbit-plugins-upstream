## Description:

Helps agents check easyTable restaurant availability and guide users through creating, modifying, finding, or cancelling reservations through an open book.easytable.com booking widget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents assisting them use this skill to inspect easyTable availability and manage restaurant reservations in the user's own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed create, modify, or cancel actions can change a real restaurant reservation.

Mitigation: Review the dry-run preview before confirming and act only on reservations the user is authorized to manage.

Risk: A create or modify attempt can have an unknown outcome after a timeout or unclear easyTable response.

Mitigation: Search for the booking by the guest mobile number before retrying the write action.

Risk: Modifying a booking replaces the whole booking, while easyTable does not expose the existing email, comment, or company values.

Mitigation: Ask the user for current values to pass through unchanged, or intentionally pass an empty value when the user wants a field cleared.

Risk: The workflow depends on the fetchproxy browser extension and an open easyTable booking tab.

Mitigation: Install and pair the extension only if the user accepts that browser-based workflow, and provide booking details only for reservations they are authorized to manage.

## Reference(s):

- [ClawHub easytable skill page](https://clawhub.ai/chrischall/skills/easytable)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation write actions require dry-run review and explicit confirmation; create and modify actions also require an open, loaded easyTable browser tab through fetchproxy.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
