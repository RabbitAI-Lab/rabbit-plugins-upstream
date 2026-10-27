## Description:

Query and manage Evite events, guest lists, RSVPs, and messages from the shell using authenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Evite users can use the skill to retrieve event details, guest lists, RSVPs, and messages, or perform event-related actions from shell-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event actions can send messages, invitations, or cancellations to real recipients.

Mitigation: Confirm recipients and intended changes before sending messages, invitations, or cancellations.

Risk: Photo-upload instructions give server responses excessive control over local file access and network destinations.

Mitigation: Before using photo uploads, validate storage and finalization destinations and handle server-provided form values literally.

Risk: Session cookies can expose an authenticated Evite session if stored insecurely or left behind.

Mitigation: Store session cookies in a uniquely created private file and remove it afterward.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [Evite](https://www.evite.com/)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/evite-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Evite API data summarized in text, with shell commands for queries and actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an authenticated Evite session; some actions change events or send communications to guests.]

## Skill Version(s):

1.3.7

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
