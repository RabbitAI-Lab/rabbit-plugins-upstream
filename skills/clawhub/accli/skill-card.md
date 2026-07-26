## Description: <br>
This skill helps agents interact with Apple Calendar on macOS to list calendars, view events, manage calendar events, and check free/busy availability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joargp](https://clawhub.ai/user/joargp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users on macOS use this skill to inspect Apple Calendar schedules, find availability, and create, update, or delete events through the accli command-line tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change sensitive Apple Calendar data through a third-party CLI on macOS. <br>
Mitigation: Install only if the external @joargp/accli npm package is trusted and the user is comfortable granting Apple Calendar access. <br>
Risk: Calendar create, update, and delete commands can make unintended schedule changes. <br>
Mitigation: Confirm event details with the user before executing create, update, or delete actions. <br>
Risk: Broad calendar queries can expose more calendar data than needed or target the wrong calendar. <br>
Mitigation: Use explicit calendars or persistent calendar IDs and keep date ranges narrow. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and JSON-output recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces accli command patterns; recommends --json for parsing and confirmation before create, update, or delete actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
