## Description: <br>
Google Calendar integration for viewing, creating, and managing events through natural language, including schedule lookup, availability checks, event changes, and morning briefs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bilalmohamed187-cpu](https://clawhub.ai/user/bilalmohamed187-cpu) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
External users and Clawdbot operators use this skill to view Google Calendar events, find availability, and, with Pro access, create, update, delete events and generate morning briefs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Google Calendar events without reliably enforcing user confirmation. <br>
Mitigation: Require an explicit preview and user confirmation before any create, quick-add, update, or delete action, and prefer read-only use unless write access is needed. <br>
Risk: Calendar OAuth credentials and tokens stored under ~/.config/gcal-pro could expose private calendar access if shared or mishandled. <br>
Mitigation: Protect ~/.config/gcal-pro, do not share or display credential files, and install only if granting Google Calendar access is acceptable. <br>
Risk: Morning briefs sent through cron or messaging can expose private schedule details. <br>
Mitigation: Enable scheduled briefs only for private destinations the user trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bilalmohamed187-cpu/skills/gcal-pro-calendar) <br>
- [Google Cloud Project Setup Guide](docs/GOOGLE_CLOUD_SETUP.md) <br>
- [Google Calendar API Quick Reference](references/api-quickref.md) <br>
- [Google Calendar API](https://www.googleapis.com/calendar/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, Python snippets, and calendar summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Google OAuth credentials, local token storage, and a Pro license for write operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
