## Description: <br>
ClawEmail helps agents work with Google Workspace services including Gmail, Drive, Docs, Sheets, Slides, Calendar, and Forms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cto1](https://clawhub.ai/user/cto1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use ClawEmail to have an agent search, read, send, and organize email; manage Drive files; create and edit Docs, Sheets, Slides, Forms; and view or change Calendar events through Google APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through broad Google Workspace actions, including sends, shares, deletes, calendar changes, and bulk edits. <br>
Mitigation: Require an explicit preview and confirmation before allowing sends, shares, deletes, calendar changes, or bulk edits. <br>
Risk: ClawEmail credentials and cached OAuth access tokens can expose email, files, calendars, and documents if mishandled. <br>
Mitigation: Use a dedicated or least-privileged Google account and protect both the credentials file and local token cache. <br>
Risk: The security review found broad power over Google Workspace without strong built-in guardrails. <br>
Mitigation: Install only when the publisher and ClawEmail service are trusted, and review OAuth scopes before connecting an account. <br>


## Reference(s): <br>
- [ClawEmail skill page](https://clawhub.ai/cto1/skills/claw) <br>
- [ClawEmail setup](https://clawemail.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with bash, curl, and inline Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEMAIL_CREDENTIALS pointing to ClawEmail credentials; the token helper caches OAuth access tokens for 50 minutes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
