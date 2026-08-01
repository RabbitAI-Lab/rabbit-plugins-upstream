## Description: <br>
User-driven conversation archiving for AI agents. Archive by topic or time, free context, recall on demand. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to archive long agent conversations by topic or time range into structured Markdown summaries, list saved archives, and recall selected summaries into the current context when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected conversation summaries are saved as persistent Markdown files in the workspace and may retain sensitive or proprietary details. <br>
Mitigation: Avoid archiving secrets, credentials, personal data, or proprietary information unless retention is intended, and periodically review or delete old files in archives/. <br>


## Reference(s): <br>
- [Context Archive Skill on ClawHub](https://clawhub.ai/thomaszhou22/skills/context-archive) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown archive summaries and concise conversational status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or reads Markdown files under archives/ in the workspace when the user invokes archive, list, or recall flows.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
