## Description: <br>
Google Calendar integration for viewing, creating, and managing events through natural-language schedule, availability, event-editing, and morning-brief requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bilalmohamed187-cpu](https://clawhub.ai/user/bilalmohamed187-cpu) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
External users and Clawdbot operators use this skill to check schedules, search calendars, find free time, and, with Pro access, create, update, or delete Google Calendar events and generate morning briefs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pro commands can create, edit, or delete real Google Calendar events without an enforced confirmation barrier. <br>
Mitigation: Require the agent to show the exact event, time, calendar, and action, then obtain explicit user confirmation before any create, update, or delete operation. <br>
Risk: The skill requires Google Calendar OAuth credentials and stores local client_secret.json and token.json files. <br>
Mitigation: Use only an OAuth project the user personally created and recognizes, keep credential and token files private, and do not proceed through Google's unverified-app warning for an unknown OAuth project. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bilalmohamed187-cpu/skills/gcal-pro) <br>
- [Google Cloud setup guide](docs/GOOGLE_CLOUD_SETUP.md) <br>
- [Google Calendar API quick reference](references/api-quickref.md) <br>
- [Google Calendar API](https://www.googleapis.com/calendar/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown/text responses with calendar summaries, confirmations, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read Google Calendar data and, for Pro users, create, update, or delete calendar events after OAuth authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
