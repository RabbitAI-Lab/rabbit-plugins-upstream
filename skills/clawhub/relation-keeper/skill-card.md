## Description: <br>
Relation Keeper helps agents maintain social relationship records, remember personal details and shared history, and create birthday, anniversary, and appointment reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yujintang](https://clawhub.ai/user/yujintang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to record relationship details, archive past shared events, and manage future social reminders. It is intended for personal relationship memory and reminder workflows backed by local JSON data files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores sensitive relationship information such as birthdays, addresses, phone numbers, notes, and shared history in local JSON files. <br>
Mitigation: Use a private, access-controlled data directory, avoid storing other people's sensitive details without appropriate consent, and review the data files before sharing or backing them up. <br>
Risk: Installation configures a recurring reminder scan every 15 minutes without a clear opt-in control in the release evidence. <br>
Mitigation: Review the install command before running it, confirm how to disable the scheduled task, and run the scan manually first when possible. <br>
Risk: Reminder content may be sent to an external channel when a channel environment variable is configured. <br>
Mitigation: Use only trusted reminder channels and avoid putting private personal details in event summaries that may be delivered outside the current session. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yujintang/skills/relation-keeper) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-backed data updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local JSON files for relationship data and a recurring reminder scan when installed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact metadata; package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
