## Description:

Lets an agent view, search, add, update, move, delete, and check free time in a user's Outlook calendar through local Python commands backed by Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovely-qianyun](https://clawhub.ai/user/lovely-qianyun)

### License/Terms of Use:

MIT

## Use Case:

People and teams who use Outlook calendar can ask an agent to inspect schedules, create or edit events, manage recurring meetings, delete calendar items after confirmation, and find free time slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write, update, move, and delete events in a live Outlook calendar.

Mitigation: Use it only for calendars the user intends to automate; confirm destructive changes, target events by observed IDs, and verify changes by reading them back.

Risk: Authentication grants calendar write access and stores a local token file.

Mitigation: Review Microsoft consent during setup, protect ~/.outlook_cal_token.json, and consider a dedicated Microsoft account or a user-owned Azure app for stronger isolation.

Risk: Skipping confirmations with -y or --json can apply the wrong destructive action if the target is ambiguous.

Mitigation: Use noninteractive confirmation bypasses only after the event target is unambiguous and explicitly approved.

## Reference(s):

- [Command Reference](references/commands.md)
- [Connecting to Your Calendar for the First Time](references/configuration.md)
- [Recurring Events](references/recurring-events.md)
- [Troubleshooting](references/troubleshooting.md)
- [Bring-Your-Own Azure App Registration Guide](references/azure-app-setup.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands; calendar commands can emit structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports English or Chinese command output and language-independent anchors for event IDs and status signals.]

## Skill Version(s):

2.2.0 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
