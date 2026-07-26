## Description: <br>
Full Confluence Cloud REST API v2 skill for pages, spaces, folders, databases, whiteboards, comments, labels, tasks, properties, basic/OAuth authentication, pagination, and migration from confluence-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pangin](https://clawhub.ai/user/pangin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and manage Confluence Cloud content through REST API v2 helpers. It supports read, write, delete, administrative, and migration-oriented workflows when supplied with appropriate Confluence credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete Confluence data under the configured credentials. <br>
Mitigation: Use least-privilege OAuth scopes or tokens and require explicit human review before write, delete, redaction, invite, or administrative commands. <br>
Risk: Credentials may be stored locally in environment variables or a .env file. <br>
Mitigation: Keep .env files out of source control, restrict file permissions, and rotate tokens if exposure is suspected. <br>
Risk: Admin-key capabilities can broaden the impact of API calls in Premium or Enterprise Confluence environments. <br>
Mitigation: Enable the admin-key header only for approved administrative tasks and disable it for normal read or low-risk operations. <br>


## Reference(s): <br>
- [OpenAPI spec](refs/openapi-v2.v3.json) <br>
- [Endpoints list](refs/endpoints.md) <br>
- [OAuth scopes](refs/scopes.md) <br>
- [Usage tips](refs/usage.md) <br>
- [Test checklist](refs/tests.md) <br>
- [ClawHub skill page](https://clawhub.ai/pangin/skills/openclaw-confluence-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript command examples and JSON API responses from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may read local environment variables or .env credentials and call Confluence Cloud REST API v2 endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
