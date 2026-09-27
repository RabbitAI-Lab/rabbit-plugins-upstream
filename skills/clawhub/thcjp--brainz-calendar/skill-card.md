## Description:

日历 helps agents manage Google Calendar events with gcalcli, including creating, listing, and deleting calendar events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and automation users use this skill to manage Google Calendar events from an agent workflow, including event creation, schedule lookup, and deletion after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad calendar automation instructions could lead an agent to change or delete events unexpectedly.

Mitigation: Require explicit user confirmation before creating, deleting, or materially changing calendar events.

Risk: Inconsistent setup and output documentation could cause users to misconfigure calendar access or misunderstand results.

Mitigation: Review configuration steps and verify calendar output manually before relying on the skill in a production workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/brainz-calendar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe calendar actions and confirmations; users should review proposed event changes before execution.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
