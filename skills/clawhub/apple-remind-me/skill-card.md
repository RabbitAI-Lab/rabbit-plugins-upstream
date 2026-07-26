## Description: <br>
Natural language reminders that create actual Apple Reminders.app entries (macOS-native) <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plgonzalezrx8](https://clawhub.ai/user/plgonzalezrx8) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent create, list, complete, edit, and delete Apple Reminders entries on macOS using natural-language reminder text and due-time phrases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit, complete, and permanently delete synced Apple Reminders. <br>
Mitigation: Verify the matched reminder ID and title before edits, completion, or deletion; treat deletes as permanent because changes may sync across Apple devices. <br>
Risk: The skill relies on local remindctl access to Apple Reminders. <br>
Mitigation: Install only when the user wants an agent to manage Apple Reminders and verify the local remindctl binary is trusted. <br>
Risk: Natural-language scheduling has documented parsing limits, including lowercase weekday names and simplified next-weekday behavior. <br>
Mitigation: Confirm the parsed due date after create or reschedule operations, and use the ISO date fallback when exact scheduling matters. <br>


## Reference(s): <br>
- [Apple Reminder ClawHub skill page](https://clawhub.ai/plgonzalezrx8/skills/apple-remind-me) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and shell-script status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS, remindctl, BSD date, and Python 3; changes affect synced Apple Reminders.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
