## Description: <br>
Sync and query CalDAV calendars (iCloud, Google, Fastmail, Nextcloud, etc.) using vdirsyncer + khal. Works on Linux. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bigdonuts0](https://clawhub.ai/user/bigdonuts0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and calendar power users use this skill to configure vdirsyncer and khal, sync CalDAV calendars, query events, and prepare create, edit, or delete calendar commands on Linux. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help access sensitive calendar data and local calendar credentials. <br>
Mitigation: Use provider app passwords or limited-scope credentials and protect the local password file. <br>
Risk: Create, edit, and delete commands can change calendar state after syncing. <br>
Mitigation: Review proposed calendar changes before running them and sync only after confirming the intended action. <br>
Risk: Deleting the khal cache can remove local cached event data used for troubleshooting. <br>
Mitigation: Use the cache deletion command only as a troubleshooting step when synced data appears stale. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bigdonuts0/skills/caldav-calendar-1-0-1) <br>
- [iCloud CalDAV endpoint](https://caldav.icloud.com/) <br>
- [Fastmail CalDAV endpoint example](https://caldav.fastmail.com/dav/calendars/user/EMAIL/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux with vdirsyncer and khal installed; calendar writes should be reviewed before syncing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
