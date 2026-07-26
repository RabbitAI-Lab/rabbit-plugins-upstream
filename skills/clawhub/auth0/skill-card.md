## Description: <br>
Auth0 helps agents add, fix, migrate, and troubleshoot authentication workflows across common web, mobile, API, and backend frameworks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[auth0](https://clawhub.ai/user/auth0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to integrate Auth0 authentication, protect APIs, configure tenant settings, troubleshoot auth errors, and migrate applications from other identity providers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can broadly activate for authentication work and may propose Auth0 tenant-resource changes. <br>
Mitigation: Require explicit approval before running Auth0 CLI commands, raw Management API calls, or changes to tenant resources, users, roles, actions, or applications. <br>
Risk: Authentication setup can expose bearer tokens, client secrets, or sensitive environment values in chat, shell history, or config files. <br>
Mitigation: Do not paste live secrets into chat or shell history; prefer manual secret entry or a secret manager and review any env or config file writes. <br>
Risk: The skill may recommend installing Auth0 tooling or using remote installer workflows. <br>
Mitigation: Approve package installs explicitly, verify the requested Auth0 CLI source, and install tooling only when it is needed for the task. <br>


## Reference(s): <br>
- [Auth0 Agent Skills homepage](https://github.com/auth0/agent-skills) <br>
- [Auth0 CLI reference](references/tooling-cli.md) <br>
- [Auth0 security best practices](references/pattern-security.md) <br>
- [Token handling patterns](references/pattern-token-handling.md) <br>
- [Auth0 CLI documentation](https://auth0.github.io/auth0-cli/) <br>
- [Auth0 Management API v2](https://auth0.com/docs/api/management/v2) <br>
- [Auth0 documentation](https://auth0.com/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Auth0 CLI commands, tenant configuration changes, and local config edits that require review before execution.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
