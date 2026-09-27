## Description:

Manage Google Calendar events using `gcalcli`. Create, list, and delete calendar events from the CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xejrax](https://clawhub.ai/user/xejrax)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to list, create, and delete Google Calendar events from the command line through gcalcli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar credentials or event details may be exposed through careless handling or command output.

Mitigation: Protect API keys and CalDAV passwords, avoid printing sensitive event details, and run the tool in an isolated environment when possible.

Risk: Delete commands may remove unintended calendar events if a search term matches the wrong event.

Mitigation: Require review of matched events before running any delete command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xejrax/skills/brainz-calendar)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires gcalcli and calendar credentials such as GOOGLE_CALENDAR_API_KEY or CalDAV credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
