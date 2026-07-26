## Description: <br>
Manage Yandex Calendar over CalDAV with vdirsyncer and khal to view, add, search, and sync calendar events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gbroccoli](https://clawhub.ai/user/gbroccoli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and agents with an existing Yandex Calendar CalDAV setup use this skill to inspect upcoming events, add events, search calendar entries, and keep local calendar data synchronized through vdirsyncer and khal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar reads and syncs can expose private event details from configured calendars. <br>
Mitigation: Install only when the user wants agent access to the existing khal/vdirsyncer calendar setup, and limit configured calendars to those the user is comfortable letting the agent read and sync. <br>
Risk: Ambiguous dates, times, durations, or titles can cause unintended calendar event additions. <br>
Mitigation: Before allowing event additions, review ambiguous event details with the user and confirm the target date, time, duration, and title. <br>
Risk: Sync errors can leave calendar state stale or prevent changes from reaching the remote calendar. <br>
Mitigation: If vdirsyncer reports an error, inspect the sync issue before retrying and use khal-only reads only when stale local data is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gbroccoli/skills/yandex-calendar) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/gbroccoli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands assume an existing khal and vdirsyncer configuration for the user's Yandex Calendar.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, released 2026-02-08) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
