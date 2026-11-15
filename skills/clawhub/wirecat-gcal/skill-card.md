## Description:

Use gcal, a Google Calendar CLI from WireCat, from an agent — check the owner's Google sign-in, find a command, run it with the owner's profile, read JSON answers. Use when a task needs the owner's Google Calendar — sync the calendars, then list, show and search events, their people and Drive files offline, prepare a meeting brief or a daily or weekly digest from the local store, create, change or delete an event, answer an invitation, or call any Calendar API method through gcal api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with access to gcal can check the owner's calendar, prepare meeting briefs and schedule digests, and carry out calendar changes the owner requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan did not fully evaluate all instruction text and references, and reported medium confidence.

Mitigation: Review the command and timer guidance before installation; only the owner should install or remove scheduled commands.

Risk: The skill can make changes to the owner's calendar when granted write access.

Mitigation: Make calendar changes only when the owner requested them and follow the skill's permission and notification guidance.

## Reference(s):

- [Remote access guide](https://github.com/WireCatLabs/gcal-cli/blob/main/docs/remote.md)
- [Gcal Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-gcal)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language responses, JSON results, meeting briefs and digests, and shell commands when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses draw on the owner's selected Google Calendar profile and locally synced data when applicable.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
