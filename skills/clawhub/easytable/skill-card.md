## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to find easyTable restaurant availability and create, modify, or cancel reservations through their own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an unpinned browser extension that can act through the user's live easyTable browser tab.

Mitigation: Review the fetchproxy extension source, release, and browser permissions before installing it, and use a dedicated browser profile with only the easyTable tab open.

Risk: Reservation write actions can create, modify, or cancel bookings from the user's browser session.

Mitigation: Review the dry-run preview before rerunning write actions with confirm: true, and remove or disable the extension when the workflow is finished.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [easyTable booking widget](https://book.easytable.com/book/?id=<restaurantId>)
- [ClawHub easytable skill page](https://clawhub.ai/chrischall/skills/easytable)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [Markdown or plain text with reservation details, dry-run previews, and confirmation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are confirm-gated before creating, modifying, or canceling reservations.]

## Skill Version(s):

0.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
