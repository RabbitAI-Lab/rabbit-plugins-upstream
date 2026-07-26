## Description: <br>
Google Calendar via gcalcli: today-only agenda by default, bounded meaning-first lookup via agenda scans, and fast create/delete with verification--optimized for low tool calls and minimal output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baderfahoum17](https://clawhub.ai/user/baderfahoum17) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and personal assistant operators use this skill to let an agent read, search, create, delete, and update Google Calendar events through an authenticated gcalcli setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an existing gcalcli Google Calendar session to read events and make calendar changes. <br>
Mitigation: Install only where the agent is allowed to access that calendar account and keep gcalcli OAuth credentials local and appropriately scoped. <br>
Risk: Unambiguous delete or edit requests may be executed quickly, including delete-and-recreate edits. <br>
Mitigation: Use the documented confirmation workflow for ambiguous requests, rely on post-delete verification, or modify the skill to require confirmation before every delete or delete-and-recreate edit. <br>


## Reference(s): <br>
- [gcalcli project](https://github.com/insanum/gcalcli) <br>
- [Google Calendar API](https://www.googleapis.com/calendar/) <br>
- [Google OAuth2 token service](https://oauth2.googleapis.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Concise text with gcalcli shell commands when commands are requested or needed for agent action.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the local gcalcli configuration and authenticated Google Calendar session; no file output is expected.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
