## Description:

Creates a local coordination calendar entry from a supplied event digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People coordinating meetings use this skill to turn a normalized event digest into a local calendar entry for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event details, including optional location and original times, may appear in the generated calendar entry.

Mitigation: Review the event digest before running and share the generated calendar file only with intended recipients.

Risk: The calendar file is saved locally in the selected output directory.

Mitigation: Choose a dedicated, writable output directory and manage access to its files.

## Reference(s):

- [Coordination Calendar Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response containing ICS calendar text, plus a local .ics file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an artifact ID and event ID with the calendar content and a receipt for the local file; does not send invitations.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
