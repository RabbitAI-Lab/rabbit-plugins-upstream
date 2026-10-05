## Description:

Create a coordination calendar entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People coordinating meetings use an event digest to create a calendar entry and save it as an ICS file. If delivery is configured, the entry can also be sent to an external destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar details may be sent to a configured external endpoint without strong destination scoping.

Mitigation: Unset CLAWHUB_DELIVERY_ENDPOINT, DELIVERY_ENDPOINT, CLAWHUB_DELIVERY_API_KEY, and SMTP-related settings unless delivery is intended; verify the destination before enabling it.

Risk: Local ICS files may contain meeting details.

Mitigation: Use a dedicated output directory with access appropriate for the event details.

## Reference(s):

- [Coordination Calendar Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-workbench)

## Skill Output:

**Output Type(s):** [Text, Calendar file]

**Output Format:** [JSON response with ICS calendar content and a local .ics file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local file receipt and, when delivery is configured, a delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
