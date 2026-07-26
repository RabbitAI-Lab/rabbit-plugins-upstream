## Description: <br>
Manage Google Calendar events using `gcalcli`. Create, list, and delete calendar events from the CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and calendar users use this skill to manage Google Calendar events from an agent workflow through gcalcli commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar commands can access or change real calendar events. <br>
Mitigation: Confirm the target calendar, event title, date, and time before creating or deleting events. <br>
Risk: Calendar credentials or API keys could be exposed through prompts, logs, or shell history. <br>
Mitigation: Keep credentials out of prompts, logs, and shared shell history, and use credentials only for the intended calendar account. <br>


## Reference(s): <br>
- [Calendar Skill on ClawHub](https://clawhub.ai/xejrax/skills/brainz-calendar) <br>
- [Publisher Profile](https://clawhub.ai/user/xejrax) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires gcalcli and calendar credentials for the intended account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
