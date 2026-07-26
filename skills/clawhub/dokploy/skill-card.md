## Description: <br>
Manage Dokploy deployments, projects, applications, and domains via the Dokploy API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joshuarileydev](https://clawhub.ai/user/joshuarileydev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to manage Dokploy projects, applications, deployments, domains, and application environment variables from an agent-assisted command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Dokploy API key can carry deployment-management authority. <br>
Mitigation: Use the narrowest key available and review deploy, update, and delete commands before execution. <br>
Risk: Configuration can store the Dokploy API key in a plaintext shell file. <br>
Mitigation: Prefer environment injection from a secret manager, or restrict local file permissions before using the config command on production systems. <br>
Risk: Command output from config show, environment-variable listing, or deployment logs may expose secrets. <br>
Mitigation: Redact terminal output before sharing it and avoid running secret-revealing commands in shared sessions. <br>
Risk: The security guidance flags an env-delete bug as a production concern. <br>
Mitigation: Review and fix the environment-variable delete behavior before using the skill against production applications. <br>


## Reference(s): <br>
- [ClawHub Dokploy skill page](https://clawhub.ai/joshuarileydev/skills/dokploy) <br>
- [Publisher profile](https://clawhub.ai/user/joshuarileydev) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; commands use DOKPLOY_API_URL and DOKPLOY_API_KEY to call the Dokploy API.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact package metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
