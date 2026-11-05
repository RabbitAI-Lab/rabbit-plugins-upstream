## Description:

Query and act on Evite events, guest lists, RSVPs, and messages from a shell using an Evite account session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to retrieve Evite event details, guest lists, RSVPs, and messages from a shell, and to make requested event or invitation changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated session cookie jar could expose a live Evite session if accessed by others.

Mitigation: Use a uniquely created private session file with restrictive permissions, avoid sharing it, and remove it after use.

Risk: An unchecked photo-upload or completion URL could send content to an unexpected destination.

Mitigation: Check upload and completion URLs against expected HTTPS destinations before uploading.

Risk: RSVP, event, invitation, message, broadcast, or photo operations can change or publish real Evite content.

Mitigation: Confirm the intended event, recipients, changes, and photos before sending or publishing.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [Evite](https://www.evite.com/)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands; Evite responses are JSON, with HTML used for template listings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and responses vary by the requested Evite operation.]

## Skill Version(s):

1.4.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
