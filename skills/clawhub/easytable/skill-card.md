## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check easyTable restaurant availability and create, modify, or cancel reservations through the user's own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, modify, and cancel actions affect real restaurant reservations.

Mitigation: Review the dry-run preview and only confirm the action when the reservation details are correct.

Risk: Confirmed create and modify actions may submit the user's name and mobile number to easyTable.

Mitigation: Confirm only with user-approved contact details and avoid entering unnecessary personal data.

Risk: The workflow depends on a fetchproxy browser extension and an open easyTable booking tab.

Mitigation: Install and pair the extension intentionally, keep the intended booking tab loaded, and confirm actions only in the expected browser session.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Markdown or plain text with reservation availability, dry-run previews, and confirmation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are confirm-gated; create and modify actions may submit a name and mobile number to easyTable after user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
