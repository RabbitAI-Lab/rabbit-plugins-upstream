## Description:

ClickMeeting lets an agent manage ClickMeeting meetings, webinars, sessions, registrations, recordings, chats, access tokens, phone gateways, and time zones through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect ClickMeeting schemas and run account-scoped ClickMeeting actions through the OOMOL connector. It supports room creation and updates, attendee and registration workflows, access-token management, recordings, chats, phone gateways, time zones, and API availability checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Prefer a verified or package-manager installation of the oo CLI, and run the remote installer only after reviewing and trusting OOMOL's installer endpoint.

Risk: Create, update, registration, and delete actions can change or remove ClickMeeting data.

Mitigation: Confirm the exact action, payload, target room or participant, and expected effect with the user before running state-changing or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickmeeting)
- [ClickMeeting homepage](https://clickmeeting.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected ClickMeeting account before connector actions can succeed.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
