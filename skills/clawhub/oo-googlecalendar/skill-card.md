## Description:

Google Calendar lets an agent read, create, update, and delete Google Calendar data through the OOMOL oo CLI and a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Google Calendar from an agent workflow, including reading calendars and events, finding free/busy data, and managing calendars, events, attendees, ACLs, and sync.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote oo CLI installer scripts.

Mitigation: Install only after reviewing or verifying the installer, and avoid elevated shells unless clearly required.

Risk: The skill can change or remove Google Calendar data through write and destructive actions.

Mitigation: Require explicit user confirmation for the exact target, payload, and effect before any write or destructive calendar operation.

## Reference(s):

- [ClawHub Google Calendar skill page](https://clawhub.ai/oomol/skills/oo-googlecalendar)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Calendar](https://workspace.google.com/products/calendar/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected Google Calendar account before calendar actions can run.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
