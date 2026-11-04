## Description:

Use gcal, a Google Calendar CLI from WireCat, from an agent — check the owner's Google sign-in, find a command, run it with the owner's profile, read JSON answers. Use when a task needs the owner's Google Calendar — sync the calendars, then list, show and search events, their people and Drive files offline, prepare a meeting brief or a daily or weekly digest from the local store, create, change or delete an event, answer an invitation, or call any Calendar API method through gcal api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and calendar users use this skill to read, search, summarize, and manage the owner's Google Calendar through gcal, including preparing meeting briefs and daily or weekly digests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting briefs may include private communications already stored by other WireCat tools.

Mitigation: Choose the intended profile and include only information needed for the requested brief.

Risk: MCP changes may run without another confirmation.

Mitigation: Make each change request identify the exact calendar action and target event.

Risk: The separately installed gcal CLI was not covered by this security review.

Mitigation: Assess the installed CLI separately before relying on it for sensitive calendar data or changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wirecat/skills/wirecat-gcal)
- [Remote MCP guide](https://github.com/WireCatLabs/gcal-cli/blob/main/docs/remote.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [JSON command results, Markdown meeting briefs and digests, and gcal shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses reflect the selected account and locally stored calendar data; a brief may include communications already stored by other WireCat tools.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
