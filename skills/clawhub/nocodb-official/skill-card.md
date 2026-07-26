## Description: <br>
Access and manage NocoDB databases via REST APIs across free-plan resources such as bases, tables, fields, records, links, filters, sorts, and attachments, with additional enterprise-plan coverage for workspaces, views, scripts, teams, and collaboration features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darkphoenix2704](https://clawhub.ai/user/darkphoenix2704) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to configure NocoDB API access and operate workspaces, bases, tables, fields, views, records, filters, sorts, attachments, scripts, teams, and API tokens from a shell-backed CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use the configured NOCODB_TOKEN to modify or delete live NocoDB data and administrative resources. <br>
Mitigation: Use a least-privilege token and require explicit human approval before delete, bulk update, member or team management, script, file upload, action trigger, token:create, or token:delete commands. <br>
Risk: Testing against production data can cause unintended changes because the CLI sends REST API calls directly to the configured NOCODB_URL. <br>
Mitigation: Test with a non-production workspace or base before using the skill with production data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/darkphoenix2704/skills/nocodb-official) <br>
- [Publisher profile](https://clawhub.ai/user/darkphoenix2704) <br>
- [Agent Skills Open Standard](https://agentskills.io) <br>
- [NocoDB Cloud endpoint](https://app.nocodb.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and a NOCODB_TOKEN; NOCODB_URL and NOCODB_VERBOSE are optional environment variables.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
