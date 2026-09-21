## Description:

Outlook Calendar (microsoft.com). Use this skill for ANY Outlook Calendar request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to manage Outlook Calendar through an OOMOL-connected Microsoft account, including reading calendars and events, creating or updating events, responding to invitations, and finding meeting times.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback may ask an agent to install the oo CLI from a remote script without independent verification.

Mitigation: Prefer manual installation from OOMOL's official install guide, verify the source before running installers, and require user approval before setup commands.

Risk: Calendar write and destructive actions can change, cancel, or delete Outlook events.

Mitigation: Confirm the exact target, payload, and expected effect with the user before create, update, cancel, delete, or invitation-response actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-outlook-calendar)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Outlook Calendar Homepage](https://www.microsoft.com/microsoft-365/outlook/outlook-calendar)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are expected to be JSON objects with data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
