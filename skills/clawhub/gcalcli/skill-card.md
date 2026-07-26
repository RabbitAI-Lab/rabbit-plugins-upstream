## Description: <br>
Interact with Google Calendar via gcalcli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gargravish](https://clawhub.ai/user/gargravish) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and calendar-aware agents use this skill to view, search, and export Google Calendar events, including event attachments and Gemini meeting notes, through gcalcli command workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to run a custom gcalcli fork and a local gcmd checkout. <br>
Mitigation: Install and run it only after confirming the fork and local checkout are trusted for the environment. <br>
Risk: The documented workflows can bulk export sensitive meeting notes and attachment links to local files. <br>
Mitigation: Limit exports to the minimum needed scope, use a secure non-shared output directory, and avoid bulk exports unless explicitly required. <br>
Risk: The examples include hard-coded calendar addresses and local paths. <br>
Mitigation: Replace them with the intended calendar targets and local directories before execution. <br>
Risk: Google OAuth credentials are cached for future use. <br>
Mitigation: Clear or revoke cached Google credentials on shared or less trusted machines. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gargravish/skills/gcalcli) <br>
- [Official gcalcli documentation](https://github.com/insanum/gcalcli) <br>
- [Custom gcalcli fork with attachment support](https://github.com/shanemcd/gcalcli/tree/attachments-in-tsv-and-json) <br>
- [Google Calendar API v3](https://developers.google.com/calendar/api/v3/reference) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON, TSV, or human-readable command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may authenticate with Google OAuth, read calendar data, and export meeting-note attachments to local files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
