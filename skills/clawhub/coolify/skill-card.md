## Description: <br>
Manage Coolify deployments, applications, databases, and services via the Coolify API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visiongeist](https://clawhub.ai/user/visiongeist) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to inspect and manage Coolify-hosted applications, databases, services, deployments, projects, teams, environment variables, backups, and related infrastructure through the Coolify API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can deploy, stop, restart, delete, or otherwise modify real Coolify resources. <br>
Mitigation: Use a least-privilege Coolify token and require manual confirmation before deploy, stop, restart, delete, backup, or environment-variable changes. <br>
Risk: Commands may handle API tokens, environment variables, database passwords, SSH private keys, and GitHub App private keys. <br>
Mitigation: Provide secrets only through intended environment or configuration channels, and avoid passing private keys or secrets on the command line unless that exact action is explicitly intended. <br>
Risk: A command can target the wrong Coolify instance, project, server, application, database, or service UUID. <br>
Mitigation: Confirm COOLIFY_API_URL and list resources to verify UUIDs before running mutating commands. <br>


## Reference(s): <br>
- [ClawHub Coolify Skill](https://clawhub.ai/visiongeist/skills/coolify) <br>
- [Coolify](https://coolify.io) <br>
- [Coolify Documentation](https://coolify.io/docs/) <br>
- [Coolify GitHub Repository](https://github.com/coollabsio/coolify) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and structured JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires COOLIFY_TOKEN and can use COOLIFY_API_URL for Coolify Cloud or self-hosted instances.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
