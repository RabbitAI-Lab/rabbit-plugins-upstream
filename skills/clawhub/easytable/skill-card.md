## Description:

Checks restaurant availability and helps users create, change, or cancel reservations at restaurants that book through easyTable widgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to check easyTable restaurant availability and manage reservations through their own browser session. It supports listing booking areas, dates, and times, finding bookings by mobile number, and confirm-gated create, modify, and cancel actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's browser session and depends on the fetchproxy browser extension.

Mitigation: Verify that the extension is trusted before installation and approve pairing only for intended easyTable actions.

Risk: Creating, modifying, or cancelling reservations can affect real restaurant bookings.

Mitigation: Review each dry-run preview and provide confirmation only for actions the user intends to take.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable)

## Skill Output:

**Output Type(s):** [guidance, configuration, text]

**Output Format:** [Markdown guidance with tool-use parameters and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are dry-run previews until the user confirms creation, modification, or cancellation.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
