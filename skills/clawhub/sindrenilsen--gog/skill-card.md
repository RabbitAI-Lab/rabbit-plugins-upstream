## Description: <br>
Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sindrenilsen](https://clawhub.ai/user/sindrenilsen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation agents use this skill to run Google Workspace CLI commands for Gmail, Calendar, Drive, Contacts, Sheets, and Docs after OAuth setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access or change sensitive Google Workspace data when broad OAuth permissions are granted. <br>
Mitigation: Install only when the gog CLI is trusted, grant only the services needed, and require explicit confirmation before sending email, exporting documents, listing contacts, or modifying Sheets data. <br>


## Reference(s): <br>
- [Gog homepage](https://gogcli.sh) <br>
- [ClawHub skill page](https://clawhub.ai/sindrenilsen/skills/gog) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return JSON when gog is used with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
