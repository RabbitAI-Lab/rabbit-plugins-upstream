## Description: <br>
ClickMeeting (clickmeeting.com). Use this skill for ANY ClickMeeting request: reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate ClickMeeting through an OOMOL-connected account, including room management, sessions, attendees, registrations, recordings, chats, access tokens, phone gateways, and time zones. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete ClickMeeting data, including conference rooms, registrations, access tokens, and conference settings. <br>
Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval before destructive actions such as deleting a conference. <br>
Risk: The skill depends on OOMOL as an intermediary for the connected ClickMeeting account. <br>
Mitigation: Install and use the skill only when OOMOL is an approved intermediary for the account and review connection or credential-expiration errors before retrying. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClickMeeting homepage](https://clickmeeting.com/) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickmeeting) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
