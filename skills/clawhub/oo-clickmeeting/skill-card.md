## Description:

Operates ClickMeeting through an OOMOL-connected account using the oo CLI for reading, creating, updating, and deleting ClickMeeting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage ClickMeeting rooms, sessions, attendees, registrations, access tokens, recordings, chats, phone gateways, time zones, and API availability through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute arbitrary local code.

Mitigation: Review and trust the OOMOL installer source or use safer verified installation options before running installer commands.

Risk: Create, update, delete, registration, and token-generation actions can change ClickMeeting state or access controls.

Mitigation: Confirm the exact action target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClickMeeting ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickmeeting)
- [ClickMeeting homepage](https://clickmeeting.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when commands are run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
