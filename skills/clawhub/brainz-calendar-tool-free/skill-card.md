## Description: <br>
Google 日历基础版 helps agents use gcalcli and CalDAV-style configuration to list, create, search, delete, and back up calendar events for personal scheduling workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage personal Google Calendar schedules through an agent, including listing date ranges, creating events, and reviewing matches before deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can interact with calendar accounts through command-line Google Calendar or CalDAV access, which may expose calendar data to external services depending on account configuration. <br>
Mitigation: Use only calendar accounts where command-line Google Calendar or CalDAV access is acceptable, and review credential and network configuration before installation. <br>
Risk: The skill supports searching for and deleting calendar events, and the security summary notes that destructive changes lack a clear confirmation requirement. <br>
Mitigation: Require the agent to show matched events and receive explicit user confirmation before deleting anything. <br>
Risk: The input schema includes an optional callback_url, which could send processing results to an untrusted destination. <br>
Mitigation: Avoid providing callback URLs unless the destination is trusted and expected for the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/brainz-calendar-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require command-line calendar credentials and explicit confirmation before destructive operations.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
