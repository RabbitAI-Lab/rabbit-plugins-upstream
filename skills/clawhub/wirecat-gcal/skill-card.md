## Description:

Use gcal, a Google Calendar CLI from WireCat, from an agent — check the owner's Google sign-in, find a command, run it with the owner's profile, read JSON answers. Use when a task needs the owner's Google Calendar — sync the calendars, then list, show and search events, their people and Drive files offline, prepare a meeting brief or a daily or weekly digest from the local store, create, change or delete an event, answer an invitation, or call any Calendar API method through gcal api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this agent skill to work with the owner's Google Calendar through gcal. It guides calendar sync and search, event and attendee review, meeting briefs and digests, and owner-requested calendar changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting briefs can contain private messages, mail, and transcripts from WireCat’s local store.

Mitigation: Choose the intended account and review the brief for sensitive details before sharing it.

Risk: The security assessment does not audit the separately installed CLI or verify its runtime safeguards.

Mitigation: Review the CLI's permissions and configuration, and grant write or sharing access only when needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-gcal)
- [Remote setup guide](https://github.com/WireCatLabs/gcal-cli/blob/main/docs/remote.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Markdown]

**Output Format:** [Markdown guidance with shell command examples and JSON or human-readable calendar summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calendar task dependent; summaries and meeting briefs use the owner's available synced data and may be incomplete when sync or stored context is incomplete.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
