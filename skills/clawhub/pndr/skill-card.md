## Description: <br>
Personal productivity app with Ideas/Tasks, Journal, Habits, Package tracking, Lists, and more via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dgershman](https://clawhub.ai/user/dgershman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External Pndr users connect an MCP-capable AI assistant to their Pndr account to manage tasks, habits, journal entries, package tracking, lists, comments, attachments, and productivity analytics through natural language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing this skill can let an AI assistant read, change, download, and delete data in the user's Pndr account. <br>
Mitigation: Use a dedicated, revocable token and require confirmation before delete, archive, bulk edit, or attachment download actions. <br>
Risk: OAuth client secrets and bearer tokens can grant access to the connected Pndr account if exposed. <br>
Mitigation: Keep the client secret and bearer token out of chats, screenshots, shared config files, and other places where an assistant or collaborator could reveal them. <br>


## Reference(s): <br>
- [Pndr](https://pndr.io) <br>
- [Pndr Documentation](https://pndr.io/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/dgershman/skills/pndr) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown with JSON configuration examples and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Pndr account, OAuth client credentials, a bearer token, an MCP-capable assistant, and mcporter for manual setup.] <br>

## Skill Version(s): <br>
1.0.20260202 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
