## Description: <br>
Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tionghieng](https://clawhub.ai/user/tionghieng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use Gog to run Google Workspace workflows from an agent or terminal, including Gmail, Calendar, Drive, Contacts, Sheets, and Docs tasks that can be scripted with JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth setup can grant access to selected Google Workspace services and account data. <br>
Mitigation: Install only when this access is intended, review the OAuth account and service scopes, and use the least service access needed for the task. <br>
Risk: Commands can send mail, create calendar items, and modify or clear Sheets data. <br>
Mitigation: Review each command before execution, confirm mutating actions, and prefer JSON or no-input modes for scripted workflows. <br>


## Reference(s): <br>
- [Gog homepage](https://gogcli.sh) <br>
- [ClawHub skill page](https://clawhub.ai/tionghieng/skills/gog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may access or modify Google Workspace data through the gog CLI after OAuth setup.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
