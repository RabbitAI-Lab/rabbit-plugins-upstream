## Description:

Operate Google Calendar through OOMOL's googlecalendar connector for reading, creating, updating, and deleting calendar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users use this skill to manage Google Calendar through an OOMOL-connected account, including event workflows, calendar management, availability checks, ACLs, colors, and settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar reads can expose event details, attendee information, calendar settings, ACLs, and availability data.

Mitigation: Install only when the user trusts OOMOL and intends to let the agent access Google Calendar through that service.

Risk: Write actions can create, update, move, import, or sync calendar data.

Mitigation: Confirm the exact payload and expected effect with the user before approving state-changing actions.

Risk: Destructive actions can remove or clear events, calendars, attendees, calendar-list entries, or ACL rules.

Mitigation: Require explicit approval for the target and action before running destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-googlecalendar)
- [Google Calendar](https://workspace.google.com/products/calendar/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
