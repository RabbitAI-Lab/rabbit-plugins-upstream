## Description: <br>
Google Workspace CLI helps agents operate Google Workspace through the gws CLI for Gmail, Drive, Calendar, Sheets, Docs, and Admin SDK workflows, including search, send, upload, export, sharing, and administration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, developers, and workspace administrators use this skill to compose safe gws CLI workflows for Google Workspace tasks such as mailbox triage, Drive sharing and export, calendar management, editor automation, audit reporting, and tenant administration. It is also used to expose selected Workspace operations as MCP tools with scoped services and change-control gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward Google Workspace write operations such as sending mail, sharing files, deleting records, or performing admin actions. <br>
Mitigation: Keep write_policy at dry-run-first, require explicit confirmation for send/share/delete/admin actions, and verify affected accounts, tenants, targets, and side effects before applying changes. <br>
Risk: Overly broad OAuth scopes or unclear account selection can expand the workspace data an agent can access or mutate. <br>
Mitigation: Use narrow OAuth scopes, explicit account selection, and read-only scope variants for investigation workflows whenever possible. <br>
Risk: Local workspace configuration and migration files may contain account, tenant, or operational context. <br>
Mitigation: Review any migration from old skill folders before moving files, keep local configuration under the documented paths, and avoid exposing credentials or secrets in chat or shared workspaces. <br>
Risk: Workspace content fetched from Gmail, Docs, Chat, or Drive can contain untrusted text that may influence downstream agent behavior. <br>
Mitigation: Use the skill's sanitize guidance for fetched content and require human review before unsanitized external content is used in autonomous write workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/google-workspace-cli) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic skill page](https://clawic.com/skills/google-workspace-cli) <br>
- [Google API discovery endpoint](https://www.googleapis.com/discovery/v1/apis) <br>
- [Google OAuth authorization](https://accounts.google.com) <br>
- [Google OAuth token service](https://oauth2.googleapis.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON parameters, configuration snippets, and change-control notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should favor JSON-oriented gws commands, explicit account selection, dry-run-first write posture, bounded pagination, and human confirmation for send, share, delete, and admin actions.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
