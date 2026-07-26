## Description: <br>
Manage Apple Calendar events via icalBuddy and AppleScript CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rainbat](https://clawhub.ai/user/rainbat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to list Apple Calendar calendars and events, search upcoming events, and create calendar events from command-line workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent Apple Calendar events. <br>
Mitigation: Confirm the title, date, time, notes, and target calendar before creating events. <br>
Risk: The skill depends on the local calctl command available on PATH. <br>
Mitigation: Use the skill only when the calctl command on PATH is trusted. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may include calendar names, dates, times, event titles, notes, and target calendar options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
