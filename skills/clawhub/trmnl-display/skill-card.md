## Description: <br>
Send concise text, notifications, or updates with optional Markdown and images to a TRMNL e-ink terminal display via webhook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peetzweg](https://clawhub.ai/user/peetzweg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to send short display-ready reminders, status updates, Markdown text, and public image URLs to a TRMNL e-ink display via webhook. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages are sent to a fixed TRMNL webhook whose ownership is not established. <br>
Mitigation: Install only if the webhook is the intended display, and avoid sending private reminders, credentials, internal status, or sensitive image links until the destination can be configured or confirmed. <br>
Risk: Public image URLs included in display content may expose sensitive or internal media links. <br>
Mitigation: Use only public, non-sensitive image URLs and review message content before sending it to the display. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/peetzweg/skills/trmnl-display) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Posts concise title, text, and optional public image URL fields to a TRMNL webhook.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
