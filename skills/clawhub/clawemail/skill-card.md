## Description: <br>
Clawemail helps agents use Google Workspace through the ClawEmail.com service, including Gmail, Drive, Docs, Sheets, Slides, Calendar, and Forms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cto1](https://clawhub.ai/user/cto1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, external users, and developers use Clawemail to let an agent perform Google Workspace tasks such as sending email, managing Drive files, editing documents and spreadsheets, creating presentations or forms, and scheduling calendar events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant broad access to email, Drive files, documents, spreadsheets, presentations, calendars, and forms. <br>
Mitigation: Install only when the ClawEmail.com service and publisher are trusted, and use a dedicated or least-privilege Google account where possible. <br>
Risk: Agent actions can send email, reply to messages, share files, export private content, edit documents, clear sheets, or delete files and events. <br>
Mitigation: Require manual review before high-impact or irreversible Google Workspace operations. <br>
Risk: Credentials and cached OAuth tokens can expose Google Workspace data if mishandled. <br>
Mitigation: Protect the credentials file and token cache and avoid sharing them with untrusted tools or environments. <br>


## Reference(s): <br>
- [ClawEmail service](https://clawemail.com) <br>
- [Clawemail on ClawHub](https://clawhub.ai/cto1/skills/clawemail) <br>
- [Publisher profile](https://clawhub.ai/user/cto1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with bash, curl, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEMAIL_CREDENTIALS and uses a helper script that refreshes and caches Google OAuth access tokens for about 50 minutes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
