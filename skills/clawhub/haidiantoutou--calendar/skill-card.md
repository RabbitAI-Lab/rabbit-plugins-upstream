## Description:

Calendar management and scheduling. Create events, manage meetings, and sync across calendar providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haidiantoutou](https://clawhub.ai/user/haidiantoutou)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to coordinate calendar work such as creating events, scheduling meetings, setting reminders, checking availability, and syncing across supported providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar reads, event creation, reminders, or sync actions can expose private scheduling data or change a user's calendar.

Mitigation: Confirm provider access with the user and ask for review before creating or editing events, reminders, or sync actions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown or plain text with optional shell commands for calendar-provider coordination]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq when shell-based provider interactions are used.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
