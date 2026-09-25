## Description: <br>
Describes an Outlook calendar reminder workflow that scans tomorrow's events each evening, schedules Feishu reminders by time of day, and reports scan results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent workers, and teams use this skill to configure daily Outlook calendar scans and Feishu reminders for upcoming meetings, cross-time-zone schedules, and shared team visibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release appears to be documentation-only or unfinished while describing a workflow that depends on an external calendar_reminder.py script. <br>
Mitigation: Inspect and test the actual calendar_reminder.py implementation before enabling the cron job or relying on the documented reminder behavior. <br>
Risk: The workflow can send potentially sensitive Outlook calendar details to Feishu users or groups. <br>
Mitigation: Limit which calendar fields are sent, confirm all recipients are authorized to see the events, and prefer the smallest appropriate Feishu target. <br>
Risk: The workflow registers a persistent scheduled task that may continue sending messages after setup. <br>
Mitigation: Verify how to pause, resume, update, and remove the skill-platform cron task before activating scheduled scans. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar-reminder) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes setup, cron registration, validation, troubleshooting, and reminder-output structure.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter states 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
