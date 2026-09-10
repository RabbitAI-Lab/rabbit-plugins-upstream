## Description:

Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules through Maton CLI or gateway calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Google Calendar through managed OAuth, including reading calendars and events, checking free/busy availability, and preparing calendar changes for explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar writes, deletes, connection creation, and connection deletion can change schedules, notify participants, revoke access, or disrupt automations.

Mitigation: Default to read and list operations, verify identifiers and account context first, and require explicit user confirmation for every write, delete, or new connection.

Risk: Long-lived API keys and provider-issued tokens can be exposed through environment variables, logs, command lines, or copied output.

Mitigation: Prefer OAuth through the Maton CLI, do not print or persist credentials, send keys only to api.maton.ai, and minimize returned calendar data to the fields needed for the task.

Risk: The maton api passthrough can reach endpoints beyond the documented examples when the connected account authorizes them.

Mitigation: Treat the documented endpoints as the intended operating surface, use least-privilege scopes, and apply the same confirmation rules to any passthrough POST, PUT, PATCH, or DELETE call.

Risk: The release evidence notes an unpinned third-party install path for Maton packages.

Mitigation: Verify the Maton package publisher before installation and use the expected Maton NPM, Homebrew, CLI, or SDK source for the environment.

## Reference(s):

- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference)
- [Google Calendar Events: List](https://developers.google.com/workspace/calendar/api/v3/reference/events/list)
- [Google Calendar Events: Insert](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)
- [Google Calendar FreeBusy: Query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce read/list commands by default and write/delete commands only after explicit user confirmation.]

## Skill Version(s):

1.2.1 (source: server release evidence; artifact frontmatter metadata reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
