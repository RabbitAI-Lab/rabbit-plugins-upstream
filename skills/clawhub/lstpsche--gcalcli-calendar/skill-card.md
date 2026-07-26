## Description: <br>
Uses gcalcli to let an agent read, search, create, and delete Google Calendar events with bounded lookups and post-action verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lstpsche](https://clawhub.ai/user/lstpsche) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
People using an authenticated gcalcli setup can have an agent handle calendar agenda checks, event lookup, event creation, and event deletion with concise conversational responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can use the user's authenticated gcalcli setup to read and change Google Calendar events, including deletion. <br>
Mitigation: Install only for agents and environments trusted to manage the calendar account, and review the documented action policy before use. <br>
Risk: Clearly matched delete or edit requests may be executed without a second confirmation. <br>
Mitigation: Change the skill's action policy to always ask before destructive actions if stricter control is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lstpsche/skills/gcalcli-calendar) <br>
- [gcalcli project](https://github.com/insanum/gcalcli) <br>
- [Google Calendar API](https://www.googleapis.com/calendar/) <br>
- [Google OAuth2 token endpoint](https://oauth2.googleapis.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an authenticated gcalcli installation and local OAuth2 credentials managed by gcalcli.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata, released 2026-02-12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
